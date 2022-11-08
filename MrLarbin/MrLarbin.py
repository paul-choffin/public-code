from pygame import mixer
import time


def dire(entree):
    piste = 'larbin' + str(entree) + '.mp3'
    print(piste)
    mixer.init()
    mixer.music.load(str(piste))
    mixer.music.play()
    time.sleep(2)

def help():
    print('''larbin1 : "Le plus important, c'est de rester calme !" \nlarbin2 : "C'est moi Mr Larbin !" \nlarbin3 : "Avant de partir, je dois remplire ma mission jusqu'à la fin" \nlarbin4 : "À votre service !" \nlarbin5 : "Je vais essayer quelque chose!" \nlarbin6 : "C'est moi Mr Larbin, à votre service !" \nlarbin7 : "Mais le plus important, C'est de rester calme!"''')


