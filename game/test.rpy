init python:
    def search_wiki(statement, defaultText):
        statement = statement.strip()

        global wikiResults

        wikiResults = defaultText

        if statement:
            import requests

            response = requests.get(
                'https://en.wikipedia.org/w/api.php',
                params={
                    'action': 'query',
                    'format': 'json',
                    'titles': statement,
                    'prop': 'extracts',
                    'exintro': True,
                    'explaintext': True
                }
            ).json()

            page = next(iter(response['query']['pages'].values()))

            try: wikiResults = page['extract']
            except Exception as error: print(error)
            finally:
                del response
                del page

label test:
    "Warning: this game will be pretty fun!"

    $ gameOver = False

    while not gameOver:
        play sound "audio/heh.ogg"

        show eileen talk with ease:
            xalign 0.5
            yalign 0

        e "Hello again [p.name]!"

        show eileen happy with ease:
            xalign 0.5
            yalign 0.5

        speak e "How are you doing?"

        call menu_test from _call_menu_test

    return

label end_test:
    speak e "Goodbye [p.name]!"
    return

label input_test:
    python:
        povname = renpy.input("What's your name?", length=32).strip()

        speak_eileen()

        if not povname:
            povname = "dude"
            phrase = "I guess I will just call you [p.name]"
        else:
            phrase = "Nice to meet you [p.name]!"

        p = Character(povname)
        renpy.say(e, phrase)
    return

label menu_test:
    $ speak_eileen()

    menu:
        e "What are we testing today [p.name]?"

        "Get to know each other":
            call meet_test
            jump data_test

        "Let's test some input!":
            jump input_test

        "Teach me some things!":
            jump wikipedia_test

        "Let's play the old demo!":
            jump old_demo

        "Text generation!":
            jump text_generation

        "Nothing!":
            $ gameOver = True
            jump end_test
    return

label text_generation:
    $ i = 0
    label gameloop:
        python:
            import subprocess
            text = subprocess.check_output(['/home/rontero/.bun/bin/bun', '/home/rontero/Documents/Projects/JavascriptProjects/HistoryGenerator/index.ts'], text=True)

        $ speak_eileen()
        e "[text]"

        $ i += 1
        if i < 5:
            jump gameloop

    $ speak_eileen()
    e "That's all for now!"
    return

label data_test:
    $ speak_eileen()

    menu:
        e "Anything you are interested in?"

        "Yeah, actually,,,":
            jump knowledge_test

        "Not really":
            show eileen sad
            speak e "Is that so?"
    return

label knowledge_test:
    python:
        likes = renpy.input("I'm really into...")
        search_wiki(likes, "Well I don't know much about it, but I hope you can teach me!")

    if likes:
        speak e "Mmm... So you are into [likes]..."

        show eileen talk

        speak e "What I know about [likes] is..."
        speak e "[wikiResults]"

    $ speak_eileen()
    menu:
        e "Anything else I should know about?"

        "Actually, also about...":
            jump knowledge_test

        "Nope":
            show eileen:
                ease .5 zoom 1.5
            speak e "Well I'm glad I got to know you better!"
    return

label meet_test:
    speak e "My name is Eileen!"

    show eileen cheeky

    speak e "As you can read on the box below!, hehe..."

    show eileen happy

    speak e "Is nice to meet you [p.name]"

    return

label wikipedia_test:
    python:
         statement = renpy.input("What do you wanna know?", length=32)
         search_wiki(statement, "I don't know anything about [statement] sorry!")

    speak e "[wikiResults]"
    return

## ------------------------------------ Old Demo ------------------------------------

define stats = {
    'patience': 5,
    'agressiveness': 5,
    'compassion': 5,
    'fucksgiven': 5,
    'simp': 5
}

define loopcount = 0

init python:
    def get_name(question):
        global p

        name = renpy.input(question, length=32).strip()

        if name: p = Character(name)

    def stats_jump(stat, greater, lower, range=5):
        renpy.jump(greater if stats[stat] > range else lower)

    def change_stat(stat, amount=1):
        stats[stat] = stats[stat] + amount

label old_demo:
    stop music fadeout 1
    scene black

    "Hello, is anyone there?"

    "Come on, say something..."

    menu:
        "Are you there?"

        "Yes, hello?":
            $ get_name("Well, hello there. I'm...")

        "Who are you?":
            $ change_stat('patience', -1)
            $ get_name("Directly to the point huh? I'm...")

    p "I'm [p.name]!"

    p "Wait, what?"

    play music "audio/music/dokidoki.ogg" volume .5

    p "Oh, yeah!"

    p "I forgot I have to make dinner today!"

    p "Blablabla... Let's get to school. I'm a student still btw!"

    jump get_school

    label get_school:
        scene bg school

        if not renpy.music.is_playing('music'):
            play music "audio/music/dokidoki.ogg" volume .5

        p "Looks like we got to school early..."

        menu:
            p "What should I do?"

            "Wait until next period":
                jump wait_school

            "Go do something else":
                jump leave_school

        ## This is a decision
        label leave_school:
            show eileen talk:
                xalign 1
                yalign 0.4

            show eileen with ease:
                xalign 0.5
                yalign 0.5
                ease .25 zoom 1.5

            p "Huh?!"

            speak unknown "Ouch, my head!"

            menu:
                p "I-I!..."

                "Apologize":
                    jump apologize

                "Ignore":
                    $ change_stat('fucksgiven')
                    return

                "Insult":
                    $ change_stat('agressiveness')
                    return

                "Warn her!" if loopcount > 0:
                    p "WAIT!"
                    speak unknown "W-What?"
                    p "Just don't move just yet please!"
                    return

            ## Decision
            label apologize:
                p "I'm so sorry! Are you okay?"

                python:
                    change_stat('simp')
                    change_stat('compassion')

                show eileen cheeky

                speak unknown "Yeah, don't worry about it!"

                show eileen talk

                speak unknown "Gotta go!"

                show eileen with ease:
                    xalign 2
                    yalign 0.5

                stop music

                scene black

                p "W-what?"

                $ loopcount += 1
                jump get_school

                ## apologize return
                return

            ## leave_school return
            return

        ## This is a decision
        label wait_school:
            p "I guess I'll wait until next period!"

            pause 1

            p "..."
            p "I can't just stand here..."

            menu:
                p "Where should I move now?"

                "Beside the tree":
                    p "Let's just wait beside that tree over there!"

                "Just stand here":
                    p "Let's just stand here I guess?"

                "In the classroom":
                    p "I'll just wait inside the classroom until the next period..."

            ## wait_school return
            return

        ## get_school return
        return

    ## main return
    return
