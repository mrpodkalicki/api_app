from nba_api.stats.endpoints import leaguedashteamstats
import statistics
from pobieranie_statystyk import pobieranie_statystyk_dla_druzyny
import time
from headers import headers

# Znajduje średnią ligową dla statystyk (typ_statystyki = "Base" lub "Advanced")


def srednia_dla_statystyk(data_startowa, data_koncowa, statystyka, typ_statystyki='Base', sezon='2018-19'):

    time.sleep(.2)
    # Pobieranie listy słowników ze statystykami każdej drużyny w celu wyliczenia średniej
    statystyki_wszystkich_druzyn = leaguedashteamstats.LeagueDashTeamStats(per_mode_detailed='Per100Possessions',
                                                                           measure_type_detailed_defense=typ_statystyki,
                                                                           date_from_nullable=data_startowa,
                                                                           date_to_nullable=data_koncowa,
                                                                           season=sezon,
                                                                           headers=headers,
                                                                           timeout=120)
    statystyki_wszystkich_druzyn_slownik = statystyki_wszystkich_druzyn.get_normalized_dict()
    statystyki_wszystkich_druzyn_tablica = statystyki_wszystkich_druzyn_slownik[
        'LeagueDashTeamStats']

    # Rozdzielenie tablicy wszystkich statystyk na pojedyńcze
    rozdzielone_statystyki_druzyn = []
    for i in range(len(statystyki_wszystkich_druzyn_tablica)):
        rozdzielone_statystyki_druzyn.append(
            statystyki_wszystkich_druzyn_tablica[i][statystyka])

    srednie_statystyki = statistics.mean(rozdzielone_statystyki_druzyn)
    return srednie_statystyki


# Znajduje ligowe odchylenie standardowe dla statystyk (typ_statystyki = "Base" lub "Advanced")
def odchylenie_standardowe_dla_statystyk(data_startowa, data_koncowa, statystyka, typ_statystyki='Base', sezon='2018-19'):

    time.sleep(.2)
    # Pobieranie listy słowników ze statystykami każdej drużyny w celu wyliczenia odchylenia standardowego
    statystyki_wszystkich_druzyn = leaguedashteamstats.LeagueDashTeamStats(per_mode_detailed='Per100Possessions',
                                                                           measure_type_detailed_defense=typ_statystyki,
                                                                           date_from_nullable=data_startowa,
                                                                           date_to_nullable=data_koncowa,
                                                                           season=sezon,
                                                                           headers=headers,
                                                                           timeout=120
                                                                           )
    statystyki_wszystkich_druzyn_slownik = statystyki_wszystkich_druzyn.get_normalized_dict()
    statystyki_wszystkich_druzyn_tablica = statystyki_wszystkich_druzyn_slownik[
        'LeagueDashTeamStats']

    rozdzielone_statystyki_druzyn = []
    for i in range(len(statystyki_wszystkich_druzyn_tablica)):
        rozdzielone_statystyki_druzyn.append(
            statystyki_wszystkich_druzyn_tablica[i][statystyka])

    odchylenie_standardowe = statistics.stdev(rozdzielone_statystyki_druzyn)
    return odchylenie_standardowe


# Zwraca wartości po zastasowaniu standaryzacji Z
def standaryzacja_z(wartosc_obserwowana, wartosc_srednia, odchylenie_standardowe):

    wartosc_z = (wartosc_obserwowana - wartosc_srednia) / \
        odchylenie_standardowe  # Calculation for z-score

    return(wartosc_z)