from nba_api.stats.endpoints import leaguegamelog, scoreboard
from id_druzyn import druzyny
from headers import headers

# Funkcja zwraca pary meczowe z podanego dnia w formacie (Gospodarz - Gość) dla poprzednich sezonów
# Index 0 to pary meczowe, Index 1 to wyniki meczy
# Data w formacie 'mm/dd/yyyy'
# Sezon w formacie 'yyyy-yy'


def rozegrane_mecze_dzienne(data, sezon):

    # Pobieranie listy meczy dla podanej daty
    mecze_dzienne = leaguegamelog.LeagueGameLog(season=sezon, league_id='00', season_type_all_star='Regular Season',
                                                date_from_nullable=data, date_to_nullable=data, headers=headers, timeout=60)
    mecze_dzienne_slownik = mecze_dzienne.get_normalized_dict()
    mecze_dzienne_lista = mecze_dzienne_slownik['LeagueGameLog']

    wyniki_meczy_lista = []
    # Zwraca pary meczowe dla podanego dnia w formacie Gospodarz - Gość, oraz wynik danego meczu
    # @ oznacza drużyne gości
    mecze_dla_gospodarzy_slownik = {}
    for i in range(0, len(mecze_dzienne_lista), 2):
        if '@' in mecze_dzienne_lista[i]['MATCHUP']:
            nazwa_goscia = mecze_dzienne_lista[i]['TEAM_NAME']
            nazwa_gospodarza = mecze_dzienne_lista[i+1]['TEAM_NAME']

            wyniki_meczy_lista.append(mecze_dzienne_lista[i+1]['WL'])

        else:
            nazwa_goscia = mecze_dzienne_lista[i+1]['TEAM_NAME']
            nazwa_gospodarza = mecze_dzienne_lista[i]['TEAM_NAME']

            wyniki_meczy_lista.append(mecze_dzienne_lista[i]['WL'])

        mecze_dla_gospodarzy_slownik.update({nazwa_gospodarza: nazwa_goscia})

    wyniki_meczy = [mecze_dla_gospodarzy_slownik, wyniki_meczy_lista]
    return(wyniki_meczy)


# Funkcja zwraca pary meczowe z podanego dnia w formacie (Gospodarz - Gość) dla aktualnego sezonu
# Index 0 zawiera pary meczowe
def aktualne_mecze_dzienne(data):

    # Pobieranie listy meczy dla podanej daty
    mecze_dzienne = scoreboard.Scoreboard(
        league_id='00', game_date=data, headers=headers, timeout=120)
    mecze_dzienne_slownik = mecze_dzienne.get_normalized_dict()
    mecze_dzienne_lista = mecze_dzienne_slownik['GameHeader']

    mecze_dla_gospodarzy_slownik = {}

    for game in mecze_dzienne_lista:

        id_gospodarza = game['HOME_TEAM_ID']

        for druzyna, id_druzyny in druzyny.items():
            if id_druzyny == id_gospodarza:
                nazwa_gospodarza = druzyna

        id_goscia = game['VISITOR_TEAM_ID']

        for druzyna, id_druzyny in druzyny.items():
            if id_druzyny == id_goscia:
                nazwa_goscia = druzyna

        mecze_dla_gospodarzy_slownik.update({nazwa_gospodarza: nazwa_goscia})
        # mecze_dla_gospodarzy_slownik

    return mecze_dla_gospodarzy_slownik