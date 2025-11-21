label numeric_org:
    $ WC_local = 0  # local attempt counter

    while True:
        $ answer = renpy.input('#What should be the right operator so the answer will be 15? \na = 30 \nb = 2 \nprint(a __ b)').strip()


        if answer == "/":
            "a = 30 \nb = 2 \nprint(a {color=#ff4444}{b}/{/b}{/color} b) \nOutput: 15"
            play sound "right_answer.ogg"
            show kai happy
            show cyra happy2
            "{color=#32CD32}{b}Correct!{/b}{/color} \nThe Numeric Org turns into binary dust."

            hide screen info_box with dissolve
            play sound "hologram.ogg"
            hide bugOgre with dissolve

            "Schreeechhh"
            show cyra happy
            cyra "Yay!!! [name]!!!"
            show cyra happy2
            show kai surprised
            kai "I thought it was subtract."
            show cyra happy
            cyra "Told you Kai was bad at math."
            show kai embarassed2
            kai "Hey! not that bad."
            mc "*Laughs* \nIt's okay Kai, you'll get it someday."
            show kai neutral2
            kai "Hmph."
            return
        else:
            $ WC_local += 1
            if WC_local == 1:
                show kai neutral
                kai "Bro come one even I can solve this!"
                show kai neutral2
                show cyra sad
                cyra "Use your math skills [name]!"
                show cyra sad2
            if WC_local >= 3:
                play sound "error_wrong.ogg"
                "You have reached the maximum attempts."
                "The Numeric Ogre throws Binary numbers"
                with hpunch
                play sound "punch_sound1.ogg"
                show red
                show cyra angry
                show kai angry
                pause 1
                cyra "Owwwwww."
                kai "Tch...really [name]."
                cyra "I'll handle this!"
                cyra "a = 30 \nb=2 \nprint(a {color=#ff4444}{b}/{/b}{/color} b) \nOUTPUT: 15"

                hide screen info_box with dissolve
                play sound "hologram.ogg"
                hide bugOgre with dissolve
                hide red with dissolve

                show kai happy2
                kai "Nice save Cyra!"
                show cyra neutral
                cyra "Phew...made it"
                show cyra neutral2
                mc "Sorrryyyy"
                show kai happy
                kai "Bro that was simple math, even I can solve that!"
                show cyra neutral
                cyra "Really Kai.....Anyways with a little more practice [name] can do it!"
                show kai neutral2
                show cyra neutral2
                return  # or jump somewhere else if you want
            else:
                play sound "error_sound1.ogg"
                "{color=#ff4444}{b}Incorrect.{/b}{/color}"
                "Try again! You have [3 - WC_local] attempt(s) left."
