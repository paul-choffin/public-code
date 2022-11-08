# -*-coding:utf-8 -*

from urllib.request import urlopen
import wolframalpha
from google_trans_new import google_translator
from random import choice
import speech_recognition as sr
import pyttsx3
import subprocess
import webbrowser
import wikipedia
from pygame import mixer
import time
import MrLarbin
import datetime
import requests
import pyautogui as pyk
import pywhatkit as kit
import webbrowser as web

def assistant_voix(sortie):
    if sortie != None:
        pas_compris = "Désolé, je n'ai pas compris."
        voix = pyttsx3.init()
        if sortie == pas_compris :
            print("A.I : " + sortie)
            voix.say(sortie)
            voix.runAndWait()
            #MrLarbin.dire(7)
            MrLarbin.dire(
                "bonjour monsieur")
        else :
            print("A.I : " + sortie)
            voix.say(sortie)
            voix.runAndWait()

def internet():
    try:
        urlopen('https://www.google.com', timeout=1)
        return True
    except:
        print("Déconnecté")
        return False

def reconnaissance():
    r = sr.Recognizer()
    r.energy_threshold = 4000
    pas_compris = "Désolé, je n'ai pas compris."
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        r.pause_threshold = 0.7
        print("..... ")
        audio = r.listen(source)
        if internet():
            try:
                vocal = r.recognize_google(audio, language = 'fr-FR')
                print(vocal)

                return vocal
            except sr.UnknownValueError:
                print(" Réessayez Maître :")
                # assistant_voix(pas_compris)

def application(entree):
    if entree != None:
        dico_apps = {
            "note": ["notepad","note pad","bloc-notes","text-editor"],
            "vscode": ["sublime","visual studio code"],
            "office": ["libre","office","libre office", "document texte"],
            "firefox": ["firefox"],
            "google": ["chrome","google"],
        }
        fini = False
        while not fini:
            for x in dico_apps["note"]:
                if x in entree.lower():    
                    assistant_voix("Ouverture d'un bloc-notes'.")
                    subprocess.Popen('/usr/bin/gnome-text-editor')
                    fini = True
            for x in dico_apps["sublime"]:
                if x in entree.lower():
                    assistant_voix("Ouverture de Visual Studio Code.")
                    subprocess.Popen('/snap/bin/code')
                    fini = True
            for x in dico_apps["office"]:
                if x in entree.lower():
                    assistant_voix("Ouverture de Libre office.")
                    subprocess.Popen('')
                    fini = True
            for x in dico_apps["edge"]:
                if x in entree.lower():
                    assistant_voix("Ouverture de Firefox.")
                    subprocess.Popen('/snap/bin/firefox')
                    fini = True
            for x in dico_apps["google"]:
                if x in entree.lower():
                    assistant_voix("Ouverture de spotify.")
                    subprocess.Popen('/snap/bin/spotify')
                    fini = True
            fini = True

def sur_le_net(entree):
    if entree != None:
        if "youtube" in entree.lower():
            recherche = entree.lower()
            try:
                recherche = recherche.replace("recherche ", "")
            except:
                recherche = recherche.replace("cherche ", "")
            finally:
                recherche = recherche.replace("sur youtube", "")
                print(recherche)
            if len(recherche) != 0:
                assistant_voix("recherche sur YouTube.")
                webbrowser.open("http://www.youtube.com/results?search_query=" + "+" + "".join(recherche), new = 2)
        elif "wikipédia" in entree.lower(): 
            wikipedia.set_lang("fr")
            try:
                recherche = entree.lower()
                try :
                    recherche = recherche.replace("recherche ","")
                except :
                    recherche = recherche.replace("cherche ", "")
                finally:
                    recherche = recherche.replace("sur wikipédia", "")
                    print(recherche)
                if recherche is not None:
                    resultat = wikipedia.summary(recherche, sentences = 2)
                    assistant_voix("recherche sur Wikipédia.")
                    webbrowser.open("https://www.wikipedia.org" + "+" + "".join(recherche), new = 2)
                    assistant_voix(resultat)
            except:
                assistant_voix("Désolé, aucune page trouvée.")
        else: 
            if "google" in entree.lower():
                try:
                    recherche = entree.lower()
                    try:
                        recherche = recherche.replace("recherche", "")
                    except:
                        recherche = recherche.replace("cherche", "")
                    finally:
                        recherche = recherche.replace("sur google", "")
                        print(recherche)
                    if len(recherche) != 0:
                        assistant_voix("recherche sur Google .")
                        webbrowser.open("https://www.google.com/search?q=" + "+" + "".join(recherche), new = 2)
                except:
                    assistant_voix("Désolé, aucune page trouvée.")
            elif "cherche" in entree.lower() or "recherche" in entree.lower():
                indx = entree.lower().split().index("cherche") 
                recherche = entree.lower().split()[indx + 1:]
                if len(recherche) != 0:
                    assistant_voix("recherche par défaut .")
                    webbrowser.open("https://www.google.com/search?q=" + "+".join(recherche), new = 2)
            elif "recherche" in entree.lower():
                    indx = entree.lower().split().index("recherche")
                    recherche = entree.lower().split()[indx + 1:]
                    if len(recherche) != 0:
                        assistant_voix("recherche sur Google .")
                        webbrowser.open("http://www.google.com/search?q=" + "+".join(recherche), new = 2)

def calcul(entree):
    if entree != None:
        entree = entree.replace('calcule', '')
        translator = google_translator()
        traduction = translator.translate(entree,lang_tgt='en')
        app_id = "L5H3JP-ERXK3EVKGW"
        client = wolframalpha.Client(app_id)
        res = client.query(traduction)
        try:
            reponse = next(res.results).text
            traduction_reponse = str(translator.translate(reponse,lang_tgt='fr'))
            reponse_calcule = "le résultat est " + traduction_reponse
            assistant_voix(reponse_calcule)
        except:
            assistant_voix("Il y'a eu une erreur, désolé")

def answer(entree):
    if entree != None:
        entree = entree.replace('calcule', '')
        translator = google_translator()
        traduction = translator.translate(entree,lang_tgt='en')
        app_id = "L5H3JP-ERXK3EVKGW"
        client = wolframalpha.Client(app_id)
        res = client.query(traduction)
        try:
            reponse = next(res.results).text
            traduction_reponse = str(translator.translate(reponse,lang_tgt='fr'))
            reponse_calcule = "le résultat est " + traduction_reponse
            assistant_voix(reponse_calcule)
        except:
            assistant_voix("Il y'a eu une erreur, désolé")

def meteo(entree):
    if entree != None:
        entree = entree.lower()
        entre = entree.split()
        lieu = ""
        prep_lieu = ""
        entree = entree.replace(' la ville de', '')
        entree = entree.replace(' la région', '')
        entree = entree.replace(' les', '')
        preposition_lieu = ["à","en","dans", "au", "dans les"]
        api_key="3b31a7e394e41c3a30759dfde1a3383e"
        base_url="https://api.openweathermap.org/data/2.5/weather?"
        for x in range(len(entre)):
            for prep in range(len(preposition_lieu)):
                if entre[x] == preposition_lieu[prep]:
                    nb_chara = 0
                    avant = preposition_lieu[prep]
                    print(avant)
                    for l in range(x + 1):
                        nb_chara += len(entre[l])
                    nb_chara += x + 1
                    for y in range(nb_chara,len(entree)) :
                        if entree[y] != " ":
                            lieu += entree[y]
                        else:
                            break
                    prep_lieu = str(avant + " " + lieu + " ")
        print(prep_lieu)
        print(lieu)
        complete_url = base_url + "appid=" + api_key + "&q=" + lieu
        response = requests.get(complete_url)
        result = response.json()
        if result["cod"] == "400":
            lieu = ""
            while lieu == "":
                assistant_voix("Vous n'avez pas indiqué de lieu, de quel endroit voulez-vous connaitre la météo ?")
                lieu = reconnaissance()
            complete_url = base_url + "appid=" + api_key + "&q=" + lieu
            response = requests.get(complete_url)
            result = response.json()
        if result["cod"] != "404":
            y = result["main"]
            temperature = round(y["temp"] - 273.15, 2)
            temperature = str(temperature)
            humidite = y["humidity"]
            humidite = str(humidite)
            z = result["weather"]
            description = z[0]["description"]
            translator = google_translator()
            description = translator.translate(description, lang_tgt='fr')
            meteo_ajd = str(prep_lieu + "La température est de " + temperature + " degrés celsius, avec " + description + ", et " + humidite + " pourcents d'humidité.")
            assistant_voix(meteo_ajd)
        else :
            assistant_voix("Il y'a eu une erreur, désolé")

def volume(entree):
    mute = ["éteins", "mute", "coupe", "remets", "active"]
    plus = ["augmente", "monte"]
    moins = ["diminue", "baisse"]
    last_val = 0
    for x in range(len(mute)):
        if mute[x] in entree.lower():
            pyk.press('volumemute')

    for x in range(len(plus)):
        act = False
        if plus[x] in entree.lower():
            for nb in range(1,50):
                if str(nb) in entree.lower():
                    act = True
                    last_val = nb
            for loop in range(int(last_val)):
                pyk.press('volumeup')
            if act == False :
                pyk.press('volumeup')


    for x in range(len(moins)):
        act = False
        if moins[x] in entree.lower():
            for nb in range(1,50):
                if str(nb) in entree.lower():
                    act = True
                    last_val = nb
            for loop in range(int(last_val)):
                pyk.press('volumedown')
            if act == False :
                pyk.press('volumedown')


'''
def play_media(entree):
    lancement = ["lance", "mets", "lance une vidéo de", "mets une vidéo de", "lance une musique de", "mets une musique de"]
    entree = entree.lower()
    if entree != None:
        for x in range(len(lancement)):
            if lancement[x] in entree:
                entree = entree.replace(lancement[x] + " ", '')
                entree = entree.replace(" sur youtube","")
                kit.playonyt(entree)
                #response = requests.get(f"https://mypywhatkit.herokuapp.com/playonyt?topic={entree}")
                #web.open(response.content.decode('ascii'))
'''


def main():
    #MrLarbin.dire(6)
    #MrLarbin.help()
    #assistant_voix("Bonjour maitre Pablo, je suis totalement dévoué. Dîtes-moi ce que je doit faire pour vous.")
    fermer = ["arrête-toi","arrêter","éteins-toi","tais-toi","ta gueule", "casse-toi","ferme-la", "arrête"] #permet de se défouler lors d'un bug
    ouvrir = ["ouvre","ouvrir"]
    cherche = ["cherche sur youtube","cherche sur google","cherche sur wikipédia","cherche","recherche"]
    calculs = ["calcul","moins"," - ","plus"," + "," x "," / ","calcule la somme de","calcule la différence de"," calcule le produit de","calcule le quotient de","calcule"]
    question = ["combien","quel","quelle","quand","qu'est-ce-que","qu'","qui est","que","quoi","est-ce que"]
    age = ["tu as quel âge", "quel est ton âge", "tu es vieux"]
    nom = ["ton nom","tu t'appelles","ton prénom","ton identité"]
    presentation = ["présente-toi","qui es-tu"]
    salutation = ["bonjour", "enchanté", "bonsoir"]
    time = ["il est quelle heure","quelle heure est-il","donner l'heure","donne-moi l'heure","donne l'heure",]
    date = ["quel jour","la date d'aujourd'hui","la date","date aujourd'hui"]
    temps = ["météo","quel temps", "est-ce qu'il fait beau", "est-ce que il va faire beau", "quelle est la température","combien de degrés","comment est le temps"]
    vol = ["le volume", "le son"]
    pause = ["lance", "play", "jouer", "pause", "remets"]
    play_yt = ["lance", "mets", "lance une vidéo de", "mets une vidéo de", "lance une musique de", "mets une musique de"]
    suivant = ["prochaine vidéo", "vidéo suivante", "musique suivante", "prochaine musique", "titre suivant", "prochain titre"]
    previous = ["précédente vidéo", "vidéo précédente", "musique précédente", "précédente musique", "précédent titre", "titre précédent", "musique d'avant", "titre d'avant", "vidéo d'avant"]
    actif = True
    while actif:
        entree = reconnaissance()
        requete = False
        if entree is not None:
            for x in range(len(ouvrir)):
                if ouvrir[x] in entree.lower():
                    application(entree)
                    requete = True
                    break
            for x in range(len(cherche)):
                if cherche[x] in entree.lower():
                    sur_le_net(entree)
                    requete = True
                    break
            for x in range(len(calculs)):
                if calculs[x] in entree.lower():
                    calcul(entree)
                    requete = True
                    break
            for x in range(len(age)):
                if age[x] in entree.lower():
                    assistant_voix("j'ai 20 ans")
                    requete = True
                    break
            for x in range(len(nom)):
                if nom[x] in entree.lower():
                    MrLarbin.dire(2)
                    requete = True
                    break
            for x in range(len(presentation)):
                if presentation[x] in entree.lower():
                    MrLarbin.dire(6)
                    requete = True
                    break
            for x in range(len(time)):
                if time[x] in entree.lower():
                    heure = datetime.datetime.now()
                    heur = str(heure.hour) + " heure et " + str(heure.minute) + " minutes"
                    assistant_voix(heur)
                    requete = True
                    break
            for x in range(len(date)):
                if date[x] in entree.lower():
                    date_ajd = datetime.datetime.now()
                    dat = date_ajd.strftime('%Y-%m-%d')
                    assistant_voix(dat)
                    requete = True
                    break
            for x in range(len(temps)):
                if temps[x] in entree.lower():
                    meteo(entree)
                    requete = True
                    break
            for x in range(len(salutation)):
                if salutation[x] in entree.lower():
                    MrLarbin.dire(6)
                    requete = True
                    break
            '''
            for x in range(len(play_yt)):
                if play_yt[x] in entree.lower():
                    if "youtube" in entree.lower():
                        play_media(entree)
                        requete = True
                        break
            '''
            for x in range(len(vol)):
                if vol[x] in entree.lower():
                    volume(entree)
                    requete = True
                    break
            for x in range(len(suivant)):
                if suivant[x] in entree.lower():
                    pyk.press('nexttrack')
                    print("next")
                    requete = True
                    break
            for x in range(len(previous)):
                if previous[x] in entree.lower():
                    pyk.press('prevtrack')
                    print("prev")
                    requete = True
                    break
            for x in range(len(fermer)):
                if fermer[x] in entree.lower():
                    #MrLarbin.dire(4)
                    #assistant_voix("A bientôt vénérable maitre.")
                    actif = False


            if requete == False:
                for x in range(len(question)):
                    if question[x] in entree.lower():
                        answer(entree)
                        break
                for x in range(len(pause)):
                    if pause[x] in entree.lower():
                        pyk.press('playpause')
                        print("pause")
                        break


if __name__ == '__main__':
    main()