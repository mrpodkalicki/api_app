import os

def zmiana_folderu_roboczego(nazwa_folderu):

    aktualny_folder_roboczy = os.path.dirname(os.path.abspath(__file__))
    nowy_folder_roboczy = os.path.join(aktualny_folder_roboczy, nazwa_folderu)
    os.chdir(nowy_folder_roboczy)