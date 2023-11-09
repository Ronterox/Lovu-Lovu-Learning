## ---------------
## Game Objective (Demo):
## ---------------
## Non linear Visual Novel that learns with the Player
## AI created randomize stories
## Fixed stories per Demo download
##
## ---------------
## System:
## ---------------
## Based on stats
## Story related to personality
## Affects:
## - Characters personality and usage
## - Quantity and quality of decisions
## - All story dialogues
##
## You can wish in your sleep for a new adventure
## Will adjust based on your new stats
## And your answers of you liked it before sleeping

define e = Character("Eileen")
define unknown = Character("???")

define p = Character("Player")

define cfg = {
    'choice': 5,
    'romance': 5,
    'action': 5,
    'happy': 5,
    'sad': 5,
    'thrill': 5
}

label start:
    jump test
    return

init python:
    def change_cfg(configuration, change=1): cfg[configuration] = cfg[configuration] + change

label main:
    $ gameOn = True

    while gameOn:
        python:
            for c in cfg:
                speak_eileen()
                val = cfg[c]
                renpy.say(e,"You have [c] in [val]")

            speak_eileen()
        menu:
            e "What you wanna do?"

            "I love refrigerators!":
                $ change_cfg('romance')

            "Stop asking me questions!":
                python:
                    change_cfg('choice', -1)
                    gameOn = False
    return
