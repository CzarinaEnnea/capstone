# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define m = Character("Mimi", color="#31298a")
define mc = Character("[name]", color="#db345d")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    "You are running trying to find your room."

    scene salon

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show ryo
    with dissolve

    # These display lines of dialogue.

    "???" "Someone is in this room maybe I can ask her for directions."

    m "I think you are lost."

    m "Can I have your name student?"

    python:
        name = renpy.input("What's your name?")
        name = name.strip() or "Dimagiba Batumbakal" # removes value and replace with default

    m "You're [name]. Did I heard it right?"

    mc "Yes!"


    # This ends the game.

    return
