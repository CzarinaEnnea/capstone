label void_bug:
    $ WC_local = 0  # local attempt counter

    while True:
        $ answer = renpy.input('Bug = ____ \nprint(Bug) \nOutput: None').strip()


        if answer == "None":
            play music right_answer noloop
            "Correct! \n{color=#32CD32}{b}Output: None{/b}{/color}"
            show cyra happy2
            cyra "Yay we did it!!"
            show kai happy2
            kai "Nice one [name]."
            hide bugVoid
            return
        else:
            $ WC_local += 1
            if WC_local == 1:
                show kai angry
                kai "Bro it has to be None."
                show cyra disgusted-notab
                cyra "Take it easy Kai, think carefully [name]."
                show kai neutral
                show cyra disgusted
                show cyra neutral2
                show kai neutral2
            if WC_local >= 3:
                play music error_wrong noloop
                "{color=#ff4444}{b}Wrong!!{/b}{/color}"
                "The Bug Void Entity turns the sky dark and attacks."
                play music punch_sound1 noloop
                show red
                show kai angry
                show cyra angry
                kai "ahh..not again."
                cyra "Seriously..uhh."
                mc "uhhhh..."
                hide bugVoid with dissolve
                hide red
                return  # or jump somewhere else if you want
            else:
                play music error_sound1 noloop
                "{color=#ff4444}{b}Incorrect.{/b}{/color}"
                "Try again! You have [3 - WC_local] attempt(s) left."
