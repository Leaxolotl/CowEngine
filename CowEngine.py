import pygame
from pygame.locals import *
from pygame import mixer
import time

pygame.init()
mixer.init()

f = open('script.ce', 'r')
file_contents = f.read()

fenetre = pygame.display.set_mode((1920, 1080))


textbox_x = (1920 - 816) // 2
textbox_y = 972 - 146 - 40


def set_background(path):
    image = pygame.image.load(path).convert()
    image = pygame.transform.scale(image, (1728, 972))  # BONNE RESOLUTION POUR 125 : 1728	, 972
    fenetre.blit(image, (0, 0))
    pygame.display.update()


def new_character(path):
    char = pygame.image.load(path).convert_alpha()
    fenetre.blit(char, (719.5, 200)) #calcul précis

def set_music(path):
    mixer.music.load(path) 
    mixer.music.set_volume(0.7)
    mixer.music.play() 

def say(script):
    font = pygame.font.SysFont('DejaVu Sans', 25)
    full_text = font.render(script, True, (255, 255, 255))
    text_x = textbox_x + 20
    text_y = textbox_y + 15
    fenetre.blit(full_text, (text_x, text_y))
    pygame.display.update()

    




for ligne in file_contents.splitlines():

    if ligne.startswith("set_background('") and ligne.endswith("')"):
        path = ligne.replace("set_background('", "").replace("')", "")
        set_background(path)

    elif ligne.startswith("set_music('") and ligne.endswith("')"):
        path = ligne.replace("set_music('", "").replace("')", "")
        set_music(path)
 
    elif ligne.startswith("new_character('") and ligne.endswith("')"):
        path = ligne.replace("new_character('", "").replace("')", "")
        new_character(path)

    elif ligne.startswith("say('") and ligne.endswith("')"):
        script = ligne.replace("say('", "").replace("')", "")
        say(script)


namebox_x = textbox_x
namebox_y = textbox_y - 32


textbox = pygame.image.load("textbox.png").convert_alpha()
fenetre.blit(textbox, (textbox_x, textbox_y))

namebox = pygame.image.load("namebox.png").convert_alpha()
fenetre.blit(namebox, (namebox_x, namebox_y))
pygame.display.update()





#affichage nom
font_name = pygame.font.SysFont('DejaVu Sans', 25)
text_name = font_name.render('Lemon', True, (224,125,194,253))

name_x = namebox_x + (168 - text_name.get_width()) // 2
name_y = namebox_y + (39 - text_name.get_height()) // 2

fenetre.blit(text_name, (name_x, name_y))


"""
index = 0
start_time = time.time()
text_speed = 0.03 #vitesse du texte
"""
continuer = True

while continuer:
    pygame.display.update()

    for event in pygame.event.get():

        if event.type == QUIT:
            continuer = False

        elif event.type == MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos

            if textbox_x <= mouse_x <= textbox_x + 816 and textbox_y <= mouse_y <= textbox_y + 146:
                print("Text box cliqué!")
                # Faire en sorte que si on clique, mais que le texte est en train de s'écrire, on affiche tout d'un coup
                # Puis on reclique pour passer au texte suivant

"""
#défilement du texte
    current_time = time.time()

    if index < len(full_text) and current_time - start_time >= text_speed:
        text += full_text[index]
        rendered_text = font.render(text, True, (255, 255, 255))
        fenetre.blit(textbox, (textbox_x, textbox_y))  # Redessiner la textbox pour effacer l'ancien texte
        fenetre.blit(rendered_text, (text_x, text_y))
        
        index += 1
        start_time = current_time
"""
    


pygame.quit()