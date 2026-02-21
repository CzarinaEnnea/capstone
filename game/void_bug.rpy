label void_bug:
    $ WC_local = 0  # local attempt counter

    while True:
        $ answer = renpy.input('Bug = ____ \nprint(Bug) \nOutput: None').strip()


        if answer == "None":
            play sound "right_answer.ogg"
            "Correct! \n{color=#32CD32}{b}Output: None{/b}{/color}"
            hide screen info_box with dissolve
            play sound "hologram.ogg"
            hide void with dissolve

            show cyra happy
            cyra "Yay we did it!!"
            show kai happy2
            kai "Nice one [name]."
            return
        else:
            $ WC_local += 1
            if WC_local == 1:
                show kai angry
                kai "Bro it has to be None."
                show cyra disgusted
                cyra "Take it easy Kai, think carefully [name]."
            if WC_local >= 3:
                play sound "error_wrong.ogg"
                "{color=#ff4444}{b}Wrong!!{/b}{/color}"
                "The Bug Void Entity turns the sky dark and attacks."

                show classroom with dissolve:
                    subpixel True matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.12)*SaturationMatrix(0.99)*BrightnessMatrix(-0.4)*HueMatrix(630.0) 

                with vpunch
                play sound "punch_sound1.ogg"
                show red
                show kai angry2
                show cyra angry
                kai "Ahh..not again."
                cyra "Seriously..uhh."
                mc "uhhhh..."
                return  # or jump somewhere else if you want
            else:
                play sound "error_sound1.ogg"
                "{color=#ff4444}{b}Incorrect.{/b}{/color}"
                "Try again! You have [3 - WC_local] attempt(s) left."
