import pygame
from pygame.locals import *
from pygame import mixer
import codecs


main_script_file = codecs.open('script.ce', 'r', 'UTF-8') # open main script file
main_script = main_script_file.read()

dialogs = []
dialogs_index = 1


pygame.init()
mixer.init() # init music mixer

fenetre = pygame.display.set_mode((1920, 1080))


background_image_resolution = (1728, 972) # TODO: delete this at some point | 100%: (1920, 1080) ; 125%: (1728, 972)

textbox_x = (1920 - 816) // 2 # TODO: get textbox_x and textbox_y automatically instead of hardcoding them as constants
textbox_y = background_image_resolution[1] - 146 - 40

namebox_x = textbox_x
namebox_y = textbox_y - 32



""" SCENE INITIALIZATION FUNCTIONS BELOW """

def set_background(path):
    image = pygame.image.load(path).convert()
    image = pygame.transform.scale(image, (background_image_resolution[0], background_image_resolution[1]))  # BONNE RESOLUTION POUR 125 : 1728	, 972
    fenetre.blit(image, (0, 0))
    pygame.display.update()


def set_music(path):
    mixer.music.load(path) 
    mixer.music.set_volume(0.7) # TODO: let the script developer handle the volume by themselve
    mixer.music.play() 



def render_textbox(path="textbox.png"): # TODO: let the script dev specify the path for textbox image
    textbox = pygame.image.load(path).convert_alpha() 
    fenetre.blit(textbox, (textbox_x, textbox_y))

def render_namebox(path="namebox.png"): # TODO: let the script dev specify the path for namebox image
    namebox = pygame.image.load(path).convert_alpha()
    fenetre.blit(namebox, (namebox_x, namebox_y))


""" SCENE EVENTS FUNCTIONS BELOW """

def new_character(path):
    character = pygame.image.load(path).convert_alpha()
    fenetre.blit(character, (719.5, 200)) #calcul précis (lol lemon)

    """ WE HAVE TO RENDER THE TEXTBOX AND NAMEBOX AGAIN IN ORDER FOR THE CHARACTER TO STAY "BEHIND" THESE """
    render_textbox()
    render_namebox()


def render_name(name):
    font = pygame.font.SysFont('DejaVu Sans', 25)
    name_rendered = font.render(name, True, (224, 125, 194, 253))

    name_x = namebox_x + (168 - name_rendered.get_width()) // 2
    name_y = namebox_y + (39 - name_rendered.get_height()) // 2

    fenetre.blit(name_rendered, (name_x, name_y))


def say(text):
    font = pygame.font.SysFont('DejaVu Sans', 30)
    rendered_text = font.render(text, True, (255, 255, 255))

    text_x = textbox_x + 20
    text_y = textbox_y + 15

    fenetre.blit(rendered_text, (text_x, text_y))
    pygame.display.update()


""" MAIN SCRIPT PARSING LOOP """

for ligne in main_script.splitlines():
    if ligne.startswith("init_scene('") and ligne.endswith("')"):
        arguments = ligne.replace("init_scene('", "").replace("')", "").split("', '") #temporaire car pue la merde comme méthode
        set_background(arguments[0])
        set_music(arguments[1])

    elif ligne.startswith("new_character('") and ligne.endswith("')"):
        print(ligne)
        path = ligne.replace("new_character('", "").replace("')", "")
        new_character(path)
        
    elif ligne.startswith("say('") and ligne.endswith("')"):
        script = ligne.replace("say('", "").replace("')", "")
        print(script)
        dialogs.append(script)


render_name("Lemon")

continuer = True

while continuer:
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == QUIT:
            continuer = False

        elif event.type == MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos

            
            if textbox_x <= mouse_x <= textbox_x + 816 and textbox_y <= mouse_y <= textbox_y + 146:

                render_textbox()
                render_namebox()
                render_name("Lemon")
                say(dialogs[dialogs_index])

                if dialogs_index + 1 < len(dialogs):
                    dialogs_index += 1
                    
                # TODO : Faire en sorte que si on clique, mais que le texte est en train de s'écrire, on affiche tout d'un coup, puis on reclique pour passer au texte suivant

pygame.quit()


"""
index = 0
start_time = time.time()
text_speed = 0.03 #vitesse du texte


loop:
    current_time = time.time()

    if index < len(full_text) and current_time - start_time >= text_speed:
        text += full_text[index]
        rendered_text = font.render(text, True, (255, 255, 255))
        fenetre.blit(textbox, (textbox_x, textbox_y))  # Redessiner la textbox pour effacer l'ancien texte
        fenetre.blit(rendered_text, (text_x, text_y))
        
        index += 1
        start_time = current_time
"""