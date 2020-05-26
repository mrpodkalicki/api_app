import pickle
import pandas as pd

from pobieranie_dziennych_meczy import aktualne_mecze_dzienne
from stworzenie_modelu import lista_srednich_i_odchylen_standardowych, roznice_wartosci_z
from dostepne_statystyki import dostepne_statystyki
from pobieranie_statystyk import pobieranie_statystyk_dla_druzyny
from zmiana_folderu import zmiana_folderu_roboczego


# Pobieranie listy gier i statystyk oraz standaryzacja
def dane_meczy_dziennych(mecze, slownik_srednia, slownik_odchylenie, data_startowa, data_koncowa, sezon):

    dane_meczy = []

    for gospodarz, gosc in mecze.items():

        gospodarz_statystyki = pobieranie_statystyk_dla_druzyny(
            gospodarz, data_startowa, data_koncowa, sezon)
        gosc_statystyki = pobieranie_statystyk_dla_druzyny(
            gosc, data_startowa, data_koncowa, sezon)

        aktualny_mecz = [gospodarz, gosc]

        for stat, statType in dostepne_statystyki.items():
            zScoreDif = roznice_wartosci_z(
                gospodarz_statystyki[stat], gosc_statystyki[stat], slownik_srednia[stat], slownik_odchylenie[stat])
            aktualny_mecz.append(zScoreDif)

        dane_meczy.append(aktualny_mecz)

    return(dane_meczy)


# Zwraca liste z danymi
# Index 0 - słownik z meczami
# Index 1 - lista z prawdopodobieństwem [[lossProb, winProb]]
def predykacja_meczy_dziennych(data, sezon='2019-20', start_sezonu='10/22/19'):

    mecze = aktualne_mecze_dzienne(data)
    slownik_srednich, slownik_odchylen = lista_srednich_i_odchylen_standardowych(
        start_sezonu, data, sezon)
    lista_meczy_dziennych = dane_meczy_dziennych(
        mecze, slownik_srednich, slownik_odchylen, start_sezonu, data, sezon)
    dane_meczy_ze_standaryzacja = pd.DataFrame(
        lista_meczy_dziennych,
        columns=['Home', 'Away', 'W_PCT', 'REB', 'TOV',
                 'PLUS_MINUS', 'OFF_RATING', 'DEF_RATING', 'TS_PCT']
    )

    wartosci_z = dane_meczy_ze_standaryzacja.loc[:, 'W_PCT':'TS_PCT']

    with open('model.pkl', 'rb') as file:
        model = pickle.load(file)

    predykcje = model.predict_proba(wartosci_z)

    mecze_z_predykcjami = [mecze, predykcje]
    #print(mecze_z_predykcjami)
    return mecze_z_predykcjami


# Zwraca prawdopodobieństwo wygranej druzyny ktora jest gospodarzem
def interpretacja_predykcji(mecze_z_predykcjami):

    mecze = mecze_z_predykcjami[0]
    prawdopodobienstwo = mecze_z_predykcjami[1]
    data_do_json = []

    for gameNum in range(len(prawdopodobienstwo)):
        prawdopodobienstwo_wygranej = prawdopodobienstwo[gameNum][1]
        zaokraglenie_prawdopodobienstwa_wygranej = round(
            prawdopodobienstwo_wygranej, 4)
        prawdopodobienstwo_wygranej_procent = "{:.2%}".format(
            zaokraglenie_prawdopodobienstwa_wygranej)

        gospodarz = list(mecze.keys())[gameNum]
        gosc = list(mecze.values())[gameNum]
        #print(gospodarz)
        #print(gosc)
        #print(prawdopodobienstwo_wygranej_procent)
        d = {'HOME': gospodarz, 'AWAY': gosc, 'WIN': prawdopodobienstwo_wygranej_procent}
        data_do_json.append(d)
        #print(type(d))
        #print(data_do_json)
        
    
        print('Jest ' + prawdopodobienstwo_wygranej_procent +
              ' szans na to że ' + gospodarz + ' pokona ' + gosc + '.')
        
    json_df = pd.DataFrame.from_dict(data_do_json)
    json = json_df.to_json(orient='index')
    return(data_do_json)

        
def predykacja_meczy_wynik(data, sezon='2019-20', start_sezonu='10/22/19'):

    zmiana_folderu_roboczego('Modele')

    print('Predykcje dla ' + data + ':')
    predykcje = predykacja_meczy_dziennych(data, sezon, start_sezonu)
    
    return(interpretacja_predykcji(predykcje))

