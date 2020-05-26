from standaryzacja_statystyk import standaryzacja_z, odchylenie_standardowe_dla_statystyk, srednia_dla_statystyk
from pobieranie_dziennych_meczy import rozegrane_mecze_dzienne
from pobieranie_statystyk import pobieranie_statystyk_dla_druzyny
from dostepne_statystyki import dostepne_statystyki
from zmiana_folderu import zmiana_folderu_roboczego

from sklearn.model_selection import train_test_split
from xgboost import XGBClassifier
from sklearn import metrics
import pandas as pd
import pickle
import os


from datetime import timedelta, date


# Obliczanie różnicy wartości z dla statystyk pary meczowej
def roznice_wartosci_z(statystyka_gospodarza, statystyka_goscia, srednia, odchylenie_standardowe):

    wartosc_z_gospodarza = standaryzacja_z(
        statystyka_gospodarza, srednia, odchylenie_standardowe)
    wartosc_z_goscia = standaryzacja_z(
        statystyka_goscia, srednia, odchylenie_standardowe)

    roznica_wartosci_z_dla_pary_meczowej = wartosc_z_gospodarza - wartosc_z_goscia
    return roznica_wartosci_z_dla_pary_meczowej


# Pobieranie danych dla par meczowych - zwraca dataframe z parami meczowymi i róźnicami wartości z
# index 0 - roznice wartości z, index 1 - rezultat
def dane_dla_par_meczowych(dzienne_mecze, srednia_slownik, odchylenie_standardowe_slownik, data_startowa, data_koncowa, sezon):

    dane_meczowe = []
    numer_meczu = 0
    wyniki_dzienne = dzienne_mecze[1]

    for nazwa_gospodarza, nazwa_goscia in dzienne_mecze[0].items():

        statystyki_gospodarza = pobieranie_statystyk_dla_druzyny(
            nazwa_gospodarza, data_startowa, data_koncowa, sezon)
        statystyki_goscia = pobieranie_statystyk_dla_druzyny(
            nazwa_goscia, data_startowa, data_koncowa, sezon)

        aktualny_mecz = [nazwa_gospodarza, nazwa_goscia]

        for statystyka, typ_statystyki in dostepne_statystyki.items():
            roznica_z = roznice_wartosci_z(
                statystyki_gospodarza[statystyka], statystyki_goscia[statystyka], srednia_slownik[statystyka], odchylenie_standardowe_slownik[statystyka])
            aktualny_mecz.append(roznica_z)

        if wyniki_dzienne[numer_meczu] == 'W':
            rezultat = 1
        else:
            rezultat = 0

        aktualny_mecz.append(rezultat)
        numer_meczu += 1

        dane_meczowe.append(aktualny_mecz)

    return(dane_meczowe)


# Funkcja pomocnicza do dat
def daty(data_startowa, data_koncowa):

    for n in range(int((data_koncowa - data_startowa).days)):
        yield data_startowa + timedelta(n)


# Zwraca liste ze srednią oraz odchyleniem standardowym
# Index 0 - słownik ze średnią dla statystyk, Index 1- słownik z odchyleniem standardowym dla statystyk
def lista_srednich_i_odchylen_standardowych(data_startowa, data_koncowa, sezon):

    slownik_srednich = {}
    slownik_odchylen = {}

    for statystyka, typ_statystyki in dostepne_statystyki.items():
        statystyka_srednia = srednia_dla_statystyk(
            data_startowa, data_koncowa, statystyka, typ_statystyki, sezon)
        slownik_srednich.update({statystyka: statystyka_srednia})

        statystyka_odchylenie = odchylenie_standardowe_dla_statystyk(
            data_startowa, data_koncowa, statystyka, typ_statystyki, sezon)
        slownik_odchylen.update({statystyka: statystyka_odchylenie})

    lista_srednich_i_odchylen = []
    lista_srednich_i_odchylen.append(slownik_srednich)
    lista_srednich_i_odchylen.append(slownik_odchylen)

    return lista_srednich_i_odchylen


# Pobierania danych treningowych dla każdego dnia pomiędzy podanymi datami
# Sezon -  'yyyy-yy' Daty  - 'mm/dd/yyyy'
def pobieranie_danych_treningowych(rok_startowy, miesiac_startowy, dzien_startowy, rok_koncowy, miesiac_koncowy, dzien_koncowy, sezon, start_sezonu):

    data_startowa = date(rok_startowy, miesiac_startowy, dzien_startowy)
    data_koncowa = date(rok_koncowy, miesiac_koncowy, dzien_koncowy)

    wszystkie_mecze = []

    for dzien_meczowy in daty(data_startowa, data_koncowa):
        aktualna_data = dzien_meczowy.strftime("%m/%d/%Y")
        #print(aktualna_data)

        dzien_poprzedni = dzien_meczowy - timedelta(days=1)
        dzien_poprzedni_format = dzien_poprzedni.strftime("%m/%d/%Y")

        slowniki_srednich_i_odchylen = lista_srednich_i_odchylen_standardowych(
            start_sezonu, dzien_poprzedni_format, sezon)
        slownik_srednich = slowniki_srednich_i_odchylen[0]
        slownik_odchylen = slowniki_srednich_i_odchylen[1]

        mecze_aktualnej_daty = rozegrane_mecze_dzienne(aktualna_data, sezon)
        # Formats Z Score difs for games on current date in loop
        statystyki_meczy_aktualnej_daty = dane_dla_par_meczowych(
            mecze_aktualnej_daty, slownik_srednich, slownik_odchylen, start_sezonu, dzien_poprzedni_format, sezon)

        for game in statystyki_meczy_aktualnej_daty:
            game.append(aktualna_data)
            wszystkie_mecze.append(game)

    return(wszystkie_mecze)


# Zwraca dane z lsisty gier i statystykami po standaryzacji
def dane_meczy_z_roznicami_wartosci_z(lista_meczy):

    mecze = pd.DataFrame(
        lista_meczy,
        columns=['Home', 'Away', 'W_PCT', 'REB', 'TOV', 'PLUS_MINUS',
                 'OFF_RATING', 'DEF_RATING', 'TS_PCT', 'Result', 'Date']
    )

    return(mecze)


# Stworzenie modelu klasyfikacji przy użyciu biblioteki XGBoost
def uczenie_modelu(dane_treningowe, dane_testowe):

    statystyki = ['W_PCT', 'REB', 'TOV', 'PLUS_MINUS',
                  'OFF_RATING', 'DEF_RATING', 'TS_PCT']

    X = dane_treningowe[statystyki]
    Y = dane_treningowe.Result

    X_train = X
    Y_train = Y

    X_test = dane_testowe[statystyki]
    Y_test = dane_testowe.Result

    # Dzielenie danych na treningowe i testowe z jednego zbioru
    #X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.25, shuffle=True)

    # ustawienie klasyfikatora
    klasyfikator = XGBClassifier(n_estimators=100, gamma=0.5, max_depth=3, learning_rate=0.02,
                                 min_child_weight=1, subsample=1, colsample_bytree=1, scale_pos_weight=1)

    klasyfikator.fit(X_train, Y_train)

    Y_pred = klasyfikator.predict(X_test)

    macierz_bledow = metrics.confusion_matrix(Y_test, Y_pred)

    # Przedstawienie wyników uczenia
    print('--------------------------------')
    print('------------XGBoost-------------')
    print('Precision : ', metrics.precision_score(Y_test, Y_pred))
    print('Accuracy : ', metrics.accuracy_score(Y_test, Y_pred))
    print('Recall : ', metrics.recall_score(Y_test, Y_pred))
    print('Confusion Matrix :')
    print(macierz_bledow)
    print('--------------------------------')
    print('--------------------------------')

    return klasyfikator


# Zapisywanie modelu przy użyciu biblioteki pickle, dla późniejszych predykcji
def zapisywanie_modelu(model, nazwa_pliku):

    zmiana_folderu_roboczego('Modele')

    with open(nazwa_pliku, 'wb') as file:
        pickle.dump(model, file)


# Tworzenie nowego modelu
def stworzenie_modelu(rok_startowy=None, miesiac_startowy=None, dzien_startowy=None, rok_koncowy=None, miesiac_koncowy=None, dzien_koncowy=None, sezon='2018-19', start_sezonu='10/16/2018', nazwa_pliku='model.pkl'):

    # dane = pobieranie_danych_treningowych(rok_koncowy, miesiac_startowy, dzien_startowy, rok_koncowy, miesiac_koncowy, dzien_koncowy, sezon, start_sezonu)  # Unnecessary if using data from CSV file
    import os
    #dane_treningowe = dane_meczy_z_roznicami_wartosci_z(dane)
    zmiana_folderu_roboczego('Modele')
    os.remove("model.pkl")
    zmiana_folderu_roboczego('Dane')
    # Should be commented out if needing to obtain data on different range of games
    dane_testowe = pd.read_csv('sezony2015-2019.csv')
    dane_treningowe = pd.read_csv('sezon2020_test.csv')
    model = uczenie_modelu(dane_testowe, dane_treningowe)

    zapisywanie_modelu(model, nazwa_pliku)