label numeric_org:
    $ WC_local = 0  # local attempt counter

    while True:
        $ answer = renpy.input('#What should be the right operator so the answer will be 15? \na = 30 \nb = 2 \nprint(a __ b)').strip()


        if answer == "/":
            "a = 30 \nb = 2 \nprint(a {color=#ff4444}{b}/{/b}{/color} b) \nOutput: 15"
            play music right_answer noloop
            show kai happy
            show cyra happy2
            "{color=#32CD32}{b}Correct!{/b}{/color} \nThe Numeric Org turns into binary dust."
            hide bugOrge
            "Schreeechhh"
            show cyra happy
            cyra "Yay!!! [name]!!!"
            hide cyra happy 
            show cyra neutral at right
            show kai surprised2
            kai "I thought it was subtract."
            show kai neutral 
            show cyra happy
            cyra "Told you Kai was bad at math."
            hide cyra happy at right
            show cyra neutral at right
            show kai embarassed2
            kai "Hey! not that bad."
            mc "*Laughts* \nIt's okay Kai, you'll get it someday."
            show kai neutral
            return
        else:
            $ WC_local += 1
            if WC_local == 1:
                show kai neutral
                kai "Bro come one even I can solve this!"
                cyra "Use your math skills [name]!"
                hide kai neutral
                show kai neutral2
            if WC_local >= 3:
                play music error_wrong noloop
                "You have reached the maximum attempts."
                "The Numeric Org throws Binary numbers"
                show red at truecenter
                show cyra angry
                show kai angry
                show red
                pause 1
                cyra "Owwwwww."
                kai "tch...really [name]."
                cyra "I'll handle this!"
                cyra "a = 30 \nb=2 \nprint(a {color=#ff4444}{b}/{/b}{/color} b) \nOUTPUT: 15 "
                hide red
                hide kai angry
                hide cyra angry
                show kai neutral at center
                show cyra neutral at right
                kai "Nice save Cyra!"
                cyra "phew...made it"
                mc "Sorrryyyy"
                show kai happy at center
                kai "Bro that was simple math, even I can solve that!"
                cyra "Really Kai.....Anyways with a little more practice [name] can do it!"
                hide bugOrge with dissolve
                show kai neutral
                show cyra neutral2
                return  # or jump somewhere else if you want
            else:
                play music error_sound1 noloop
                "{color=#ff4444}{b}Incorrect.{/b}{/color}"
                "Try again! You have [3 - WC_local] attempt(s) left."
