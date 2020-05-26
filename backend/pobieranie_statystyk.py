from id_druzyn import druzyny
from nba_api.stats.endpoints import teamdashboardbygeneralsplits, leaguedashteamstats
import time
from headers import headers


def pobieranie_statystyk_dla_druzyny(druzyna, data_startowa, data_koncowa, sezon='2019-20'):

    time.sleep(1)
    # Pobieranie bazowych statystyk dla 100 posiadań.
    bazowe_statystyki_druzyny = teamdashboardbygeneralsplits.TeamDashboardByGeneralSplits(
        team_id=druzyny[druzyna], per_mode_detailed='Per100Possessions', date_from_nullable=data_startowa, date_to_nullable=data_koncowa, season=sezon, headers=headers, timeout=120)
    bazowe_statystyki_druzyny_slownik = bazowe_statystyki_druzyny.get_normalized_dict()
    bazowe_statystyki_druzyny_tablica = bazowe_statystyki_druzyny_slownik[
        'OverallTeamDashboard'][0]

    # Rozbicie tablicy z bazowymi statystykami na pojedyńcze statystyki.
    procent_wygranych = bazowe_statystyki_druzyny_tablica['W_PCT']
    zbiorki = bazowe_statystyki_druzyny_tablica['REB']
    straty = bazowe_statystyki_druzyny_tablica['TOV']
    plus_minus = bazowe_statystyki_druzyny_tablica['PLUS_MINUS']

    # Pobieranie zaawansowanych statystyk dla 100 posiadań.
    zaawansowane_statystyki_druzyny = teamdashboardbygeneralsplits.TeamDashboardByGeneralSplits(
        team_id=druzyny[druzyna], measure_type_detailed_defense='Advanced', date_from_nullable=data_startowa, date_to_nullable=data_koncowa, season=sezon, headers=headers, timeout=120)
    zaawansowane_statystyki_druzyny_slownik = zaawansowane_statystyki_druzyny.get_normalized_dict()
    zaawansowane_statystyki_druzyny_tablica = zaawansowane_statystyki_druzyny_slownik[
        'OverallTeamDashboard'][0]

    # Rozbicie tablicy z zaawansowanymi statystykami na pojedyńcze statystyki.
    rating_ofensywny = zaawansowane_statystyki_druzyny_tablica['OFF_RATING']
    rating_defensywny = zaawansowane_statystyki_druzyny_tablica['DEF_RATING']
    wskaznik_tsp = zaawansowane_statystyki_druzyny_tablica['TS_PCT']

    # wrzucenie bazowych i zaawansowanych statystyk do jednego słownika
    wszystkie_statystyki = {
        'W_PCT': procent_wygranych,
        'REB': zbiorki,
        'TOV': straty,
        'PLUS_MINUS': plus_minus,
        'OFF_RATING': rating_ofensywny,
        'DEF_RATING': rating_defensywny,
        'TS_PCT': wskaznik_tsp,
    }

    return wszystkie_statystyki