label list_hydra:
    $ WC_local = 0  # local attempt counter

    while True:
        $ answer = renpy.input('heads = [[] \n{color=#ff4444}{b}________{/b}{/color} \nprint(heads) \nOutput: [[\'Hydra\'] ').strip()

        if answer == "heads.append('Hydra')" or "heads.append(\"Hydra\")":
            show kai happy
            show cyra happy
            play sound "right_answer.ogg"
            "Correct! \n{color=#32CD32}{b}Output: [[\'Hydra']{/b}{/color}"
            # show bugHydra jail #make a sprite with the bug inside a Jail
            show kai happy2
            show cyra happy2
            "The Hydra got sent to jail and will probably never come back...."
            pause 1
            "Unless proven innocent..0_0"
            play sound "hologram.ogg"
            hide bughydra with dissolve
            hide screen info_box with dissolve
            show cyra happy
            show kai happy
            kai "Hydra captured! Python win again!"
            show cyra neutral
            cyra "Nicely done. You’ve mastered list manipulation."
            show cyra neutral2
            return
        else:
            $ WC_local += 1
            if WC_local == 1:
                show kai angry2
                kai "It's \"heads\" bro [name], not \"head\"!"
                show cyra neutral
                cyra "We also need to only use {color=#ff4444}{b}two single quotations{/b}{/color} not double quotations!"
                show kai neutral2
                show cyra neutral2
            if WC_local >= 3:
                play sound "error_wrong.ogg"
                "You have reached the maximum attempts."
                "As the List Hydra was about to imprison you"
                show red
                show cyra angry
                show kai angry
                pause 1
                kai "Ughh.. Let me do this"
                kai "{color=#ff4444}{b}heads.append('Hydra'){/b}{/color}"
                "Output: \n{color=#32CD32}{b}['Hydra']{/b}{/color}"

                hide screen info_box with dissolve
                play sound "hologram.ogg"
                hide bughydra with dissolve
                hide red with dissolve
                
                show kai neutral2
                show cyra surprised
                cyra "Wow Kai you did it!"
                show kai happy
                kai "And thats how its done."
                show cyra neutral2
                mc "Thanks Kai, and sorry guys...."
                show kai angry2
                kai "Dude you gotta be careful on what you type, it has consequences."
                return  # or jump somewhere else if you want
            else:
                play sound "error_sound1.ogg"
                "{color=#ff4444}{b}Incorrect.{/b}{/color}"
                "Try again! You have [3 - WC_local] attempt(s) left."
