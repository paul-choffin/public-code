
def musique :
    if entree != None :
        if "deezer" in entree lower():
            indx = entree lower(). split().index("deezer")
            recherche = entre.lower(). split()[indx + 1]
            if len (recherche) != 0:
                assistant_voix("rechercher sur deezer")
                webbrowser.open("https://www.deezer.com/fr/login" + "+".join (recherche), new = 2 )
        elif"spotify" in entree lower():
            indx = entree lower(). split().index("spotify")
            recherche = entre.lower(). split()[indx + 1]
            if len (recherche) != 0:
                assistant_voix("")
                webbrowser.open("https://accounts.spotify.com/fr/login/?continue=https:%2F%2Fopen.spotify.com%2F%3Fl2l%3D1" + "+".join (recherche), new = 2 )
                
                
                