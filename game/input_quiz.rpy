default WC = 0
default passwordA = "PythonRocks!"

label ep1_scn5_txt3:
    "What is the correct syntax?"

    $ code = renpy.input("Type here:")
    $ code = code.strip()

    if code == passwordA:
        jump explain

    else:
        $ WC += 1
        if WC >= 3:
            "You have reached the maximum attempts."

            menu:
                extend ""

                "PythonRocks!":
                    jump explain

                "Python Rocks!":
                    $ scene5Wrong = True
                    show mspython sad
                    mspy "Incorrect. Remember the {=code}+{/code} operator joins strings directly. No space unless you add one." 
                    show mspython neutral
                    mspy "If you do want to add one just set the space as a string like so."

                    hide ep1-scn5-txt3
                    show ep1-scn5-txt4 zorder 6 at top_left_space
                    with dissolve

                    "Class giggles softly. [name] loses a bit of confidence."
                    "{=red}Syntax Confidence –1{/red}"
                    $ change_confidence(-1)

                    hide ep1-scn5-txt4 with dissolve

                "Error":
                    $ scene5Wrong = True
                    mspy "Not quite! That would happen only if we tried to combine incompatible data types."
                    "You learn something from your mistake."
                    hide ep1-scn5-txt3 with dissolve

        else:
            "Wrong code!"
            "Try again. You have [3 - WC] attempt(s) left."
            jump ep1_scn5_txt3

    return

    label explain:
    "CORRECT!"
    show mspython happy
    mspy "Nice work! You got it right."
    mspy "The {=code}+{/code} operator combines strings — just like teamwork combines talent!"
    "The class claps. [name]’s confidence increases."
    "{=gold}Syntax Confidence +2{/gold}"
    $ change_confidence(+2)
    hide ep1-scn5-txt3 with dissolve
    return