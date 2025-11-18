default WC = 0
default passwordB = "PythonRocks!"

label ep1_scn5_txt3:
    "What will be the Output?"

    $ code = renpy.input("Type here:")
    $ code = code.strip()

    if code == passwordB:
        jump explain

    else:
        $ WC += 1
        if WC == 1:
            "{color=#32CD32}{b}Hint: Observe the parenthesis in 3rd line{/b}{/color}"
        if WC >= 3:
            "You have reached the maximum attempts."

            menu:
                "Multiple Choice Bonus."

                "PythonRocks!":
                    jump explain

                "Python Rocks!":
                    $ scene5Wrong = True
                    show mspython sad
                    mspy "Incorrect. Remember the {=code}+{/code} operator joins strings directly. No space unless you add one." 
                    "{color=#32CD32}{b}Correct Answer: PythonRocks!{/b}{/color}"
                    show mspython neutral
                    mspy "If you do want to add one just set the space as a string like so."

                    hide ep1-scn5-txt3
                    show ep1-scn5-txt4 zorder 6 at top_left_space
                    with dissolve

                    "Class giggles softly. [name] loses a bit of confidence."
                    play sound "error_sound1.ogg"
                    "{=red}Syntax Confidence –1{/red}"
                    $ change_confidence(-1)


                    hide ep1-scn5-txt4 with dissolve

                "Error":
                    $ scene5Wrong = True
                    show mspython sad
                    mspy "Not quite! That would happen only if we tried to combine incompatible data types."
                    "You learn something from your mistake."

                    "{color=#32CD32}{b}Correct Answer: PythonRocks!{/b}{/color}"

                    hide ep1-scn5-txt3 with dissolve

        else:
            play music error_sound1 noloop
            "{color=#ff4444}{b}Wrong code!{/b}{/color}"
            "Try again. You have [3 - WC] attempt(s) left."
            jump ep1_scn5_txt3

    return

    label explain:
    play music right_answer noloop
    "{color=#32CD32}{b}CORRECT!{/b}{/color}"
    show mspython happy
    mspy "Nice work! You got it right."
    mspy "The {=code}+{/code} operator combines strings — just like teamwork combines talent!"
    show mspython happy2
    "The class claps. [name]’s confidence increases."
    "{=gold}Syntax Confidence +2{/gold}"
    $ change_confidence(+2)
    hide ep1-scn5-txt3 with dissolve
    return