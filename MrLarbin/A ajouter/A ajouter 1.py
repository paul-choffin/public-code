def meteo(entree) :
    if entree != None:
        if "temps" in entree.lower():
            indx = entree.lower().split().index("temps")
            recherche = entree.lower().split()[index + 1:]
            if len(recherche) != 0:
                assistant_voix("recherche sur meteofrance .")
                webbrowser.open("https://meteofrance.com/previsions-meteo-france/lorient/56100" + "+".join(recherche), new = 2)
                
def application(entree):
    if entree != None:
        dico_app = {
            "calendrier" ["calendar","windows calendar"]
        }
        fini = False
        while not fini:
            for x in dico_app ["calendar"]:
                if x in entree.lower():
                    assistant_voix("Ouverture de calendar")
                    subbprocess.Popen('C\\Windows\\System32\\calendar.exe')
                    fini = True