# TODO: Change sprites and bg + animation.
#       Change visual aids

label episode1:
# SCENE 1

    scene black
    with dissolve

    play sound "train.ogg" fadeout 1.0

    show text "Episode 1 - “Welcome to Code Nexus Academy”" at truecenter with dissolve
    pause 10
    hide text with fade

    play sound "traindoor_opening.ogg" fadeout 1.0
    $ renpy.pause(3.5)

    play music "audio/opening.ogg"

    scene skyline
    with dissolve

    "A sleek hovertrain glides through a neon sky. The colossal Code Academy Nexus floats above the city — a fortress of glowing circuits and holographic towers."

    mc "They say if you can code it, you can create it."
    mc "At Code Academy Nexus, code is reality."
    mc "And today… it’s my first day."

    "The hovertrain doors slide open. [name] steps out, adjusting [their] backpack and looking around in awe."

    mc "Whoa… this place looks like a computer and a cathedral had a baby."
    
    "{color=#a14ae9}???{/color}" "And you must be the new kid who talks to [them]self."

    "A girl with purple-streaked hair and a mischievous grin appears, holding a holo-tablet."

    show cyra neutral
    with dissolve

    cyra "Cyra Byte. Frontend Division. Top of the leaderboard, breaker of hearts, destroyer of broken CSS."
    mc "Uh… nice to meet you?"
    show cyra happy
    cyra "Nice to meet you, too, mystery newbie. You’ve got that first-day panic look. Adorable."
    mc "It’s called confidence. You’ll see."

    show cyra neutral2
    cyra "Mhm. We’ll see how long that lasts when you meet the Headmaster."

    "Suddenly, the air shimmers with light. A tall man in a glowing white coat appears, teleporting in with calm authority."

    show doctorbyte neutral at left
    with dissolve

    dr "Good morning, students. No teleportation mishaps this time, I hope."

    show cyra neutral at right with move
    cyra "No promises, Headmaster."
    show cyra neutral2

    show doctorbyte neutral
    dr "I see you’ve met our new recruit. [name], isn’t it?"
    mc "Yes, sir! Reporting for— uh— coding?"
    show doctorbyte happy
    dr "Excellent enthusiasm. Welcome to Code Academy Nexus — where syntax becomes strength."
    show doctorbyte neutral
    dr "Now, you’ll be joining Professor Py Thon’s class. Don’t let her brilliance intimidate you."

    show doctorbyte neutral2
    "A ripple of neon light forms into a tall woman with emerald lines of code flowing through her hair. Her eyes glow softly with wisdom."

    show mspython neutral at center
    with Dissolve(1.0)

    mspy "Headmaster, I’ll take it from here."
    show mspython neutral2
    show doctorbyte happy

    dr "The class is yours, Professor. Don’t melt too many brains on the first day."

    hide doctorbyte with dissolve
    "Dr. Byte fades out, leaving the place glowing with holographic light."

    stop music fadeout 2.0


# SCENE 2: Syntax 101 – The First Spell

    play sound "door_opening_school_doorway.ogg"
    scene classroom
    with dissolve

    "The students take their seats. Floating keyboards and holographic code scroll across the room."

    show mspython neutral
    with dissolve

    mspy "Welcome, young coders."
    mspy "Today, we begin with the most sacred of all spells."

    show mspython vhappy
    mspy "The {b}print(){/b} command!"

    "She waves her hand and code appears in the air."

    show mspython neutral at slightright with move

    show screen info_box("SYNTAX 101: print()") with dissolve
    show ep1-scn2-txt1 at top_left_space
    with dissolve

    mspy "This, my students, is your first incantation the spell that lets you speak to the machine."
    mspy "Now, [name] tell me, what happens when this line is executed?"

    menu:
        extend ""

        "It prints “Hello, World!”":
            mc "It prints “Hello, World!” like telling the computer to say hello."
            show mspython vhappy
            mspy "Excellent! You’ve spoken your first line of Python with grace."
            mspy "A humble start… yet every coder’s journey begins with this very phrase."
            show mspython happy2

            show cyra neutral-notab at right with dissolve
            cyra "Congrats, newbie! You made the computer talk {w}— and it didn’t roast you."
            show cyra neutral2-notab
            mc "Thanks… I think?"
            show mspython neutral
            mspy "Do not underestimate simplicity, [name]. Even a whisper of logic can reshape reality."

            play sound "right_answer.ogg"
            "{=gold}Syntax Confidence +2{/gold}"
            $ change_confidence(+2)

        "It explodes the computer":
            mc "It explodes the computer?"
            show mspython surprised2
            "The class bursts into laughter. Ms. Py Thon crosses her arms, amused."
            show mspython surprised
            mspy "Ah, creativity — but no. This is Python, not Michael Bay Studios."
            show cyra happy-notab at right with dissolve
            cyra "Boom! First mistake of the semester."
            show cyra happy2-notab
            show mspython neutral
            mspy "A safe answer would be wiser next time, [Ms][name]."

            play sound "error_sound1.ogg"
            "{=red}Syntax Confidence –1{/red}"
            $ change_confidence(-1)
            
        "It creates a cat video":
            mc "It creates a cat video?"
            show cyra neutral-notab at right with dissolve
            cyra "Ha! I wish! If that worked, I’d have infinite playlists."
            show mspython sad
            mspy "Perhaps one day when you master APIs… but for now, no cats —only code."

            play sound "error_sound1.ogg"
            "{=red}Syntax Confidence –1{/red}"
            $ change_confidence(-1)

    show mspython neutral
    hide screen info_box 
    hide ep1-scn2-txt1
    hide cyra 
    with dissolve
    mspy "Python is one of the world’s most flexible programming languages." 
    mspy "Created by Guido van Rossum and released in 1991, it’s used for:"

    show ep1-scn2-txt2 at top_left_space 
    with dissolve

    mspy "Web development, Software Creation, Mathematics and yes Automation and Scripting!"

    show mspython neutral2
    show luna neutral at right with dissolve
    luna "Python: adaptive, readable, and statistically likely to dominate human education."
    show luna neutral2

    # hide luna
    # show astra neutral at right 
    # with dissolve

    # astra "Uh huh."

    show mspython neutral
    mspy "Quite right, Luna. Python’s beauty lies in its simplicity."
    mspy "It reads almost like English — and runs instantly."
    mspy "That means your experiments come alive as you type them."
    show mspython neutral2
    mc "So… it’s easy to start with, but powerful enough for big stuff?"
    show mspython neutral
    mspy "Exactly. It supports procedural, object-oriented, and functional programming {w}— three paths, one language."

    show mspython neutral2
    "She gestures, and glowing indentation marks appear midair."

    play sound "hologram.ogg"

    hide astra
    hide luna
    hide ep1-scn2-txt2
    with dissolve

    show screen info_box("SYNTAX 101: Indentation") with dissolve
    show ep1-scn2-txt2-1 at top_left_space
    with dissolve

    show mspython neutral
    mspy "Don't worry about what this code means yet. {w}Focus on the indention or space below the \"{size=+10}{color=#81f08aff}def greet():{/color}{/size}\"."
    mspy "Unlike many languages, Python doesn’t use semicolons or braces. It uses {b}indentation{/b} — spacing — to define code blocks."
    show mspython neutral2
    mc "So… even the spaces matter?"
    show mspython neutral
    mspy "Yes. In Python, indentation isn’t optional. Disrespect it… and {i}you’ll summon chaos{/i}."

    hide ep1-scn2-txt2-1
    hide screen info_box
    with dissolve

    play sound "glitch_sound.ogg"

    show mspython neutral2
    show ep1-scn2-txt2-2 at top_left_space
    $ red_effect()

    "The lights flicker. A faint growling noise is heard — a “bug” forming in the code."

    show cyra happy-notab at right with dissolve
    cyra "Oh, fun. Evil spaces. Love that."

    hide ep1-scn2-txt2-2
    with dissolve
    
    show screen info_box("SYNTAX 101: Variable Name") with dissolve
    show ep1-scn2-txt3 at top_left_space
    with dissolve

    show cyra neutral2-notab
    show mspython neutral
    mspy "When you name a variable in Python, you can’t use spaces because Python would get confused — it would think you’re writing two separate things instead of one name."
    mspy "The underscore (_) acts like a small space — it helps make your variable name easy to read without breaking Python’s rules. Watch."

    mspy "Instead, we do:"

    hide mspython
    hide cyra
    show ep1-scn2-txt4 at top_right_space
    with dissolve

    mspy "Take note of this. Then you’ll enjoy your next challenge."

    "She waves her hand. The classroom morphs into a holographic battle arena — walls of blue code hum with energy."

    hide screen info_box
    with dissolve

    scene arena #or fade to black
    with dissolve

    mspy "Prepare yourselves for your first challenge anytime soon… {w}{b}The Syntax Bug Simulation{/b}. {w}Fix the code, or the Bug will replicate."
    mc "Bring it on."
    cyra "Just don’t explode the computer this time, rookie."
    mspy "Well then enjoy your break time."

    scene black
    with dissolve
    pause 0.5

    scene cafeteria
    with fade

    "After Class"

    # play music "chill_bg.ogg" fadein 1.0
    play music "main-menu.ogg"  #Try but might delete
    mc "I felt drained already. Well atleast I can finally eat!"


# Scene 3: “Meeting the Crew – Syntax Duel and Team Debugger”

    "After Ms. Py Thon’s class, my brain feels like scrambled code. The Student Lounge hums with energy — half café, half neon battlefield."
    "At the center table, five students argue over a glowing cube of light."
    "A sign above their table reads:"
    "{size=+10}TEAM DEBUGGER – We Don’t Panic, We Patch.{/size}"

    mc "...{w}Guess that’s my new squad."

    show cyra neutral2-notab with dissolve
    show cyra happy-notab at slightright with move

    cyra "Oh! Everyone, meet our new recruit!!"

    show astra neutral at slightleft with dissolve:
        xzoom -1.0

    astra "Oh, look. The new one survived Ms. Py Thon’s lecture that’s worth a celebration. {w}I’m Astra."

    show kai neutral at left with dissolve
    kai "Barely. I saw three students combust from syntax errors."
    show kai neutral2
    show astra neutral2

    pause 0.5
    show luna neutral zorder 2 at right with dissolve
    show luna happy at slightright with move
    show cyra surprised2-notab at center with move
    with hpunch

    luna "{b}Combust?! {w=1}I missed that again?!{/b} {w=1}By the way I’m Luna Hehe."

    show cyra surprised-notab
    cyra "{size=+10}{b}Hey!{/b}{/size}"

    show kai neutral
    kai "Figures. Another bright-eyed beginner joining the chaos. {w}Kai by the way."

    show kai neutral2
    show mira neutral zorder 1 at right with dissolve
    mira "{cps=20}H-Hi there…{/cps} {w}I’m Mira Bite. {w}{cps=20}I handle support and… {w=1}um… {w=1}tea refills.{/cps}"
    show cyra neutral2-notab


    menu:
        "Nice to meet you all! I’m [name] and ready to code my destiny.":
            show astra happy
            "You saw Kai nods approvingly and Astra winks towards you"

        "Wait—did she say students combusted?":
            show luna happy2
            "Luna giggles at you and pretends to explode."
            show luna bleh
            luna "Kabooom!"

        "Free tea? Best team ever.":
            show mira surprised2-blush:
                linear 0.7 xpos 0.9
            show luna happy2
            "You saw Mira turning red and hides herself behind Luna."

    show astra neutral
    # show luna neutral2
    astra "So, rookie, which division you thinking of joining? Frontend glam? Backend chaos? Or full-stack madness?"

    show cyra happy-notab
    show astra neutral2
    cyra "Relax, [theyre] still new."

    mc "Not sure yet. Still figuring out if I’m more “function” or “fashion.”"

    show luna surprised3
    luna "*gasp*"
    show luna happy
    luna "Be both! A stylish debugger! I can make you a glowing jacket that says {w}{i}{size=+10}{cps=20}{color=#81f08aff}while(True): Slay(){/color}{/cps}{/size}{/i}!"

    show kai disgusted
    show cyra disgusted-notab

    "{color=#db345d}Kai{/color} & {color=#a14ae9}Cyra{/color}" "…Please don’t."

    show kai sad
    kai "Ignore Luna. Her projects usually end in smoke or spontaneous dancing LEDs."

    show kai sad2
    show luna angry
    luna "Excuse you! That was one time. And it was {i}fabulous.{/i}"
    show luna angry2
    show mira neutral at right with move
    mira "You’re… {w}kind of brave for surviving your first class, though." 
    mira "Ms. Py Thon can be scary."
    show mira neutral2
    mc "Yeah, she smiled once — the projector flickered."

    show cyra happy-notab
    show kai happy
    show luna happy-nostar
    show mira happy
    show astra happy
    "({i}Everyone laughs.{/i})"

    "???" "[[{i}Sound of Intercom Suddenly Rings{/i}]"

    mspyIntercom "Attention, Team Debugger. Before you relax too much {w}— SURPRISE QUIZZZ!"

    show cyra surprised-notab
    show kai surprised
    show luna surprised
    show mira surprised
    show astra surprised

    stop music fadeout 0.5

    mspyIntercom "Let’s see if your new member can handle The Syntax Duel."
    show astra happy
    show mira neutral2
    astra "*grins* Ooooh, our favorite hazing ritual."
    show astra happy2
    show kai neutral
    kai "Not hazing. {i}Evaluation{/i}."
    show kai neutral2
    show luna cookie
    luna "I brougfhtt coofkiesss!"
    show luna cookie2
    luna "{w}Waift… is dat allofwed?"
    show kai neutral
    kai "You’ll probably spill it on the terminal again."
    show kai neutral2
    show cyra neutral-notab
    cyra "Lets get this started!"

    scene black
    with dissolve
    pause 0.5

    scene arena
    with dissolve

    #   QUESTION 1
    mspyIntercom "Your first spell — fix this broken code: {w}{i}{size=+10}{color=#81f08aff}print(\"Hello World!){/color}{/size}{/i}"
    
    menu:
        extend ""
        
        "print(\"Hello World!\")":
            call question1Right from _call_question1Right
        "print('Hello World!')":
            call question1Right from _call_question1Right_1
        "print(Hello World!)":
            play sound glitch_sound
            show bug at top
            $ red_effect()

            show kai neutral at left with dissolve
            kai "Told you. Rookie nerves."
            show cyra surprised at slightright with dissolve
            cyra "Don’t panic! Try closing the quotes — fast!"
            play sound hologram
            with vpunch
            hide bug with dissolve
            "([name] fixes it. Bug fizzles. Team cheers.)"
            show cyra neutral
            mspyIntercom "You can either use Double Quotation Marks {=code}“”{/code} or {=code}‘’{/code} Apostrophe to declare a string you want to print"
            play sound error_sound1
            "{=red}Syntax Confidence –1{/red}"
            $ change_confidence(-1)

            show cyra neutral2
            show kai neutral2

    #   QUESTION 2    
    mspyIntercom "Assign 10 to variable x. In a Variable we can store data types we want for example let it be a number, a string and so on. First you have to name your variable it can be a string or a single letter."
    mspyIntercom "I'll explain it more in a later class so don't worry if you got it wrong. {w}Now go Assign 10 to variable x"
    
    menu:
        extend ""

        "x = 10":
            show kai happy
            kai "Simple. Efficient. You’d make a good teammate."

            play sound right_answer
            $ change_kaiAffection(+1)
            "{=gold}Kai’s Affection +1{/=gold}"

            show luna happy at center with dissolve
            luna "You’re on fire! But like... in a non-combustion way!"
            show astra neutral at slightleft with dissolve:
                xzoom -1.0
            astra "Careful, Kai. Compliments look good on you." #teasing
            show kai neutral2
            show astra neutral2

            play sound right_answer
            "{=gold}Syntax Confidence +2{/gold}"
            $ change_confidence(+2)

        "int x = 10":
            call question2Wrong from _call_question2Wrong

        "x : 10":
            call question2Wrong from _call_question2Wrong_1
    
    #   QUESTION 3
    mspyIntercom "Which of these can Python do?"

    menu:
        extend ""

        "Web applications":
            call question3Right from _call_question3Right
        "Control robots":
            call question3Right from _call_question3Right_1
        "Make coffee":
            mspyIntercom "If Python brewed coffee, I’d be a billionaire."
            "(Team laughs, [name] gets minor penalty.)"
            show cyra sad
            cyra "We'll go for coffee break later. For now focus."

            play sound error_sound1
            "{=red}Syntax Confidence –1{/red}"
            $ change_confidence(-1)

    #   QUESTION 4
    mspyIntercom "Which is true about Python syntax?"

    menu:
        extend ""

        "Uses indentation for scope":
            show kai happy
            kai "Your precision is admirable."
            show cyra surprised 
            cyra "And that focus... kinda cool. You listen in class I see."
            "([name] blushes)"

            play sound right_answer
            "{=gold}Syntax Confidence +2{/gold}"
            $ change_confidence(+2)
            show cyra neutral2

        "Uses curly braces":
            call question4Wrong from _call_question4Wrong

        "Needs semicolons":
            call question4Wrong from _call_question4Wrong_1

    show luna happy at center with dissolve
    luna "Okay, okay, my turn!"
    show luna neutral
    luna "What’s the name of the function used to display text?"

    menu:
        extend ""

        "prnt ()":
            call question5Wrong from _call_question5Wrong

        "print()":
            show luna happy:
                subpixel True 
                parallel:
                    Null(411.0, 1080.0)
                    'luna happy'
                parallel:
                    ypos 1.0 
                    linear 0.14 ypos 1.04 
                    linear 0.17 ypos 1.0 
            with Pause(0.60)
            show luna happy:
                ypos 1.0
            luna "YES! You pass the Luna test! You’re officially 90\% certified cool!"
            "(+1 Luna Friendship)" #luna flag?

            play sound right_answer
            "{=gold}Syntax Confidence +2{/gold}"
            $ change_confidence(+2)

        "speak()":
            call question5Wrong from _call_question5Wrong_1

    mspyIntercom "You’ve all performed… adequately. Some of you even excelled."
    mspyIntercom "Tomorrow, we explore the {b}Variables of Destiny.{/b}"
    show astra neutral at slightleft with dissolve
    astra "(stretching) Destiny sounds boring. Can we just fight more Bugs?"
    show astra neutral2
    show cyra neutral
    cyra "Perfect as always…"
    show cyra neutral
    show kai neutral
    kai "Discipline before battle, Astra."
    show kai neutral2
    show mira neutral at right with dissolve
    mira "He says, as if he’s not secretly obsessed with perfect syntax."
    show mira neutral2
    show cyra happy
    cyra "You did great really great."
    show luna happy at center with dissolve
    luna "Group selfie before the next apocalypse! Say {w}{size=+10}{color=#81f08aff}print(\"Cheese!\"){/color}{/size}!"

    play music "main-menu.ogg" #Try but might delete

    scene groupPhoto
    with dissolve
    "(They pose. Flash of neon light. Laughter.)"

    "And just like that, I wasn’t alone anymore."
    "A team of geniuses, chaos gremlins, and possible love interests."
    "At Code Academy Nexus… even friendship is coded in Python."

    stop music fadeout 0.5

# SCENE 4

    scene classroom
    with dissolve

    "Morning light streams through the digital windows of Code Nexus Academy."
    "After a long night of debugging simulations, the class gathers once again in {b}Ms. Py Thon’s Command Lab{/b}. Ready to dive deeper into the logic that powers their world."

    show mspython neutral2 zorder 4 at center
    with dissolve

    "(Clapping her hands — and three glowing orbs float into the air.)"
    show mspython neutral
    mspy "Good morning, little coders! Today, we explore the heart of every spell {w=1.5}— I mean, script {w}— in Python!"
    show mspython neutral2

    show cyra surprised-notab zorder 3 at right
    with dissolve
    cyra "Wake up Ms is here."
    show cyra surprised2-notab
    mc "(Grinning, still sleepy.) {p}Uh… can the heart be caffeinated first?"

    show astra neutral at left with dissolve:
        xzoom -1.0
    astra "It's only the second day, and you're already sleeping LOL."
    show astra neutral2

    show kai happy zorder 2 at slightright:
        xzoom -1.0
    with dissolve
    kai "Guess someone didn’t def their sleep last night."

    show mspython angry
    mspy "Ha! Save your excuses for the compiler. Now open your command lines!"

    show kai surprised
    show astra surprised
    show cyra surprised-notab

    mc "!!!"

    hide kai
    hide cyra
    hide astra
    with dissolve

    show ep1-scn4-txt0 at top_left_space
    with dissolve

    show mspython neutral at slightright with move
    mspy "Now class."
    mspy "As we learned before, Python syntax can be executed right in the command line, like so:"

    hide ep1-scn4-txt0
    show ep1-scn4-txt1 at top_left_space
    with dissolve

    mspy "Or, by running it in a .py file through the server. It’s like two paths to the same spell."
    cyra "So basically… It’s like summoning magic either from your hand or your spellbook?"
    show mspython happy
    mspy "Exactly, my fiery apprentice! Python is both elegant and flexible."

    hide ep1-scn4-txt1
    show ep1-scn4-txt2-1 at top_left_space
    with dissolve

    mspy "Now — behold the sacred rule: {i}Indentation matters!{/i}"

    hide ep1-scn4-txt2-1
    show ep1-scn4-txt2 at top_left_space
    with dissolve

    mspy "If you skip the indentation, Python won’t forgive you."
    drIntercom "Neither will I."
    "Everyone" "(Laughs nervously.)"

    show mspython neutral
    mspy "The number of spaces is your choice, but consistency is the key. {w}You must never mix your indentation styles… or the code will crumble!"
    show mspython neutral2
    mc "So, it’s kind of like teamwork? Everyone needs to keep their spacing aligned?"
    kai "Deep. Didn’t think you had that in you."
    cyra "Guess our hero’s got some brain cells after all."

    hide ep1-scn4-txt2
    show ep1-scn4-txt3-1 at top_left_space
    with dissolve

    show mspython neutral
    mspy "In Python, variables are born the moment you assign them a value — no declarations needed!"

    hide ep1-scn4-txt3-1
    show ep1-scn4-txt3 at top_left_space
    with dissolve

    mspy "Like so."

    mspy "And comments begin with a {=code}#{/code}. It’s like whispering to your code — only you can hear it."

    hide ep1-scn4-txt3
    show ep1-scn4-txt4 at top_left_space
    with dissolve

    kai "So… a comment’s like a secret message in a bottle?"
    show mspython happy
    mspy "Exactly, Kai. For once, you’re insightful."

    hide ep1-scn4-txt4
    show mspython neutral2 at center with move
    show cyra surprised at right
    with dissolve

    cyra "Wait, so if I type {=code}# Cyra is awesome{/code}, it doesn’t actually do anything?"
    show cyra surprised2
    show astra neutral at left with dissolve:
        xzoom -1.0
    astra "You’re the only one who can see it, Cyra."
    show astra neutral2
    show mspython happy
    mspy "Only boosts your ego, dear."

    hide astra
    hide mspython
    hide cyra
    with dissolve

    scene classroom
    with fade

    "{b}After Class – Free Interaction Scene{/b}"
    "The class ends, and the students scatter. You can choose who to talk to before leaving."
    "Who do you want to talk to?"
    menu:
        extend ""

        "Talk to Cyra":
            call talkToCyra from _call_talkToCyra
        "Talk to Kai":
            call talkToKai from _call_talkToKai
        "Talk to Ms. Py Thon":
            call talkToMsPython from _call_talkToMsPython
        "Talk to Dr. Byte (via HoloCall)":
            call talkToDrByte from _call_talkToDrByte
        "Talk to Astra":
            call talkToAstra from _call_talkToAstra

    "As class ends, you feel a small spark — not just of code, but connection."
    "Maybe this academy isn’t just about fighting bugs…"
    "Maybe it’s about the people who debug your heart."

# SCENE 5
    scene arena #training chamber
    with dissolve

    "After yesterday’s lesson on syntax and indentation, today’s session promises something new — something powerful"
    show mspython neutral at center 
    with dissolve
    mspy "Class, welcome to the second pillar of programming — {w}{b}Variables!{/b}"

    show mspython neutral2
    
    show astra neutral at slightleft:
        xzoom -1.0
    with dissolve
    astra "Another day to learn coding."

    show astra neutral2

    show luna neutral zorder 2 at slightright with dissolve
    luna "Yay. I get to show how awesome I am again, Hehe."
    show luna neutral2

    show cyra neutral zorder 1 at right
    with dissolve
    cyra "(Stretching.){p}Finally! Something we can actually {i}use.{/i}"

    show cyra neutral2

    show kai neutral at left
    with dissolve
    kai "Yeah, because totally, printing {w}{cps=20}{i}‘Hello, World!’{/i} changed my life."

    show kai surprised2
    show mspython angry zorder 3 with dissolve
    mspy "It {b}should{/b} have, Mr. Sarcasm. Now, pay attention."

    hide astra
    hide luna
    hide cyra
    hide kai
    with dissolve

    "The board glows with code examples."

    show ep1-scn4-txt3 at top_left_space
    with dissolve

    show mspython neutral at slightright with move

    mspy "In Python, variables are containers for storing data values. Think of them as—"

    play sound hologram    
    show doctorbyte neutral with dissolve:
        xzoom -1.0
        xalign 1.1
        subpixel True alpha 0.74 additive 0.14 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(0.14)*HueMatrix(459.0) 



    drHologram "—as magical sigils that store the essence of logic itself."

    show mspython angry
    mspy "Yes, thank you, Headmaster. I {i}was{/i} getting there."

    show doctorbyte happy
    drHologram "Continue. I’ll just observe. Don’t mind me."

    hide doctorbyte with dissolve

    show mspython neutral
    mspy "Variables are created when you assign them a value. There’s no need for declarations — {w}Python trusts your logic."

    hide ep1-scn4-txt3
    show ep1-scn5-txt2 zorder 6 at top_left_space
    with dissolve

    mspy "And the result is simple — {b}10 Cyra{/b}. Beautiful, no?"

    show cyra surprised at right
    with dissolve
    cyra "Wait, why am {i}I{/i} a variable now?"

    show kai neutral zorder 1 at center
    with dissolve
    kai "Because you’re unpredictable."

    show kai neutral2
    "Everyone laughs."

    show cyra angry
    cyra "Keep talking, Kai, and I’ll assign {b}you{/b} to a trash variable."

    mc "(Laughing quietly.){p}Guess that’s one way to ‘delete’ him."

    show mspython angry zorder 5
    mspy "Okay class be quiet."

    hide kai
    hide cyra
    with dissolve

    show mspython neutral
    mspy "Now, let’s test your understanding! I’ll ask one question — answer wisely."

    hide ep1-scn5-txt2
    show ep1-scn5-txt3 zorder 6 at top_left_space
    with dissolve
    mspy "What will this code output?"

    define scene5Wrong = False

    call ep1_scn5_txt3

    pause 1
    show mspython neutral with dissolve
    mspy "Variables can hold numbers, words, even data from sensors and magic circuits. They are the foundation of digital alchemy."

    show kai neutral at left with dissolve
    show mspython neutral2
    kai "Digital… alchemy? Cool. So I’m basically a wizard?"
    show kai neutral2
    show mspython neutral
    mspy "Only if your spells compile, dear."

    scene classroom
    with fade

    "{b}After Class – Team Interaction{/b}"

    if scene5Wrong == True:
        show cyra neutral-notab at center with dissolve
        cyra "You did great back there, [name]. Even when you got it wrong, you didn’t panic."
        show cyra happy-notab
        cyra "That’s… kinda cool."
        show cyra happy2-notab
        "{=gold}Cyra’s affection slightly increases.{/gold}"
        $ change_cyraAffection(+1)

        show kai happy2 at left with dissolve
        kai "Don’t let her get to your head, rookie. We’ve got bigger bugs to squash soon."
        "{=gold}Kai smirks — affection slightly increases.{/gold}"
        $ change_kaiAffection(+1)
    else:
        show cyra neutral-notab at center with dissolve
        cyra "You did great back there, [name]. You didn’t panic and got it right even if you're new."
        show cyra happy-notab
        cyra "That’s really cool!"
        show cyra happy2-notab

        play sound right_answer
        "{=gold}Cyra’s affection increases.{/gold}"
        $ change_cyraAffection(+2)

        show kai happy at left with dissolve
        kai "Don’t let her get to your head, rookie. We’ve got bigger bugs to squash soon."

        play sound right_answer
        "{=gold}Kai smirks — affection increases.{/gold}"
        $ change_kaiAffection(+2)

    show luna happy at rise_up

    show cyra neutral2-notab at slightright with move
    luna "Speaking of bugs—don’t squash them! {w}They’re {b}adorable!{/b}"
    show luna neutral
    luna "I named one ‘Syntaxy.’ He’s missing a colon, but he’s trying his best!"
    show luna neutral2
    show cyra happy-notab
    show kai sad
    "Everyone groans. Cyra laughs while Kai facepalms."

    show cyra neutral-notab
    cyra "Luna, you seriously need a hobby that doesn’t involve feeding your code errors."
    show luna sad
    luna "They’re misunderstood! Like me, when I use too many print statements."
    show kai neutral2
    show luna neutral2
    show cyra neutral2-notab

    show astra neutral at right
    with dissolve
    astra "Well, well… look at you, [name]." 
    astra "First day and already getting attention. Not bad for a newbie."
    "She smirks, eyes glinting mysteriously."
    show kai neutral
    kai "Don’t start, Astra. You just want to recruit [name] for your ‘{i}secret AI project{/i}’ again."
    show kai neutral2
    show astra happy
    astra "Maybe I do. A good coder recognizes potential… {w}and [name]’s code doesn’t just run—it flows."

    show cyra embarrassed-notab
    "Cyra looks slightly flustered and looks away."

    hide kai
    hide cyra
    hide luna
    hide astra
    with dissolve

    show mspython neutral at center with dissolve
    mspy "That’s enough, everyone. You’ve all done well today."
    show mspython neutral2
    "Ms Py Thon claps her hand softly. Her calm but commanding tone fills the room."
    show mspython neutral
    mspy "Remember — variables are the foundation of all programs."
    mspy "They hold your data, your progress… {w}even your mistakes."
    mspy "Learn to manage them, and you control your code — and your destiny."
    show mspython neutral2

    drIntercom "Indeed. Your first mission awaits tomorrow. Prepare yourselves…"
    drIntercom "The next challenge won’t be so forgiving."
    play sound hologram
    "Lights dim. The holographic classroom fades into lines of binary code swirling around [name]."

    hide mspython with dissolve

    show luna cookie at slightright with dissolve
    luna "Oooh, a mission! Can we bring snacks? My debug chips are gluten-free!"
    show cyra happy-notab at right with dissolve
    cyra "Luna, you’re hopeless."
    show kai happy at left with dissolve
    kai "Let’s see if [name] can survive it without breaking the compiler this time."

    hide kai
    hide luna
    hide cyra
    with dissolve

    scene classroom

    pause 1.0

    show mspython neutral at center
    with dissolve
    mspy "Tomorrow… {w}they will learn the weight of logic."
    show mspython neutral2
    "Her eyes gleam faintly, as if hiding a deeper plan."

    scene black
    with dissolve
    pause 2

# SCENE 6
    scene arena
    with dissolve

    play sound glitch_sound
    "The class stands in a glowing dome. Holographic bugs crawl across the air — twisted lines of corrupted code."
    show doctorbyte neutral at left with dissolve
    dr "These are minor data Bugs. Harmless individually, but in numbers… they destroy systems."
    show mspython neutral at right with dissolve
    show doctorbyte neutral2
    mspy "Your task — use what you’ve learned. Variables, syntax, and teamwork."
    mspy "[name] your group will be with Kai, and Cyra. {w}Now GO!"

    hide doctorbyte
    hide mspython
    with dissolve

    "The Bugs surge forward — glowing red code glitches fill the room."
    show bug at top
    $ red_effect()

    show cyra neutral at right with dissolve
    cyra "Time to test our skills!"
    show cyra neutral2
    show kai neutral at left with dissolve
    kai "[name], back me up!"
    show kai neutral2

    $ ep1Scn6Right = False

    "{b}Choose your Attack!{/b}"
    menu:
        "Kai = 100":
            $ ep1Scn6Right = True

            "{b}Assign a value to Kai’s defense module.{/b}"
            mc "{=code}Kai = 100!{/code}"
            mspy "Excellent variable usage!"
            show kai surprised # Add Shine
            kai "Whoa— I feel 100x stronger!"
            play sound right_answer
            "{=gold}Team gains shield.{/gold}"

            hide bug 
            with dissolve

        "Bug = 1":
            "{b}if Bug > 0: print(‘Attack!’){/b}"
            mc "{=code}if Bug > 0: print(‘Attack!’){/code}"
            "Forget to indent your code."
            "Error beeps loudly."
            play sound error_wrong
            $ red_effect()

            mspy "Indentation, [name]! {b}Indentation!{/b}"
            show kai angry
            show cyra surprised
            with hpunch
            "{i}A Bug hits Kai’s barrier.{/i}"
            play sound punch_sound2
            "{=red}Minor damage.{/red}"

            show screen info_box("Correct Syntax:") with dissolve
            "{=code}if Bug > 0:{p}{space=40}print(‘Attack!’){/code}"

            hide screen info_box
            hide bug
            hide kai
            hide cyra 
            with dissolve

        "print(\"Target Locked!\")":
            $ ep1Scn6Right = True

            "{b}Print a debug message.{/b}"
            mc "{=code}print(\"Target Locked!\"){/code}"
            "The code glows; the Bug freezes."
            with hpunch
            play sound punch_sound1
            show cyra happy
            show kai happy
            hide bug with dissolve

            "{=gold}Bug defeated.{/gold}"

    if ep1Scn6Right == True:
        show cyra happy at slightright with move
        cyra "Nice one, [name]! You’re getting the hang of this!"
        show cyra happy2
        show kai happy
        kai "Not bad… {w}for a newbie."
        show kai happy2
    else:
        show doctorbyte sad at slightleft with dissolve
        dr "Well you did your best."

    show doctorbyte neutral at slightleft with dissolve
    dr "Lesson complete. You’ve survived your first encounter."
    show mspython neutral at right with dissolve
    mspy "But this is just the beginning."
    mspy "The real Bugs — the ones corrupting our network — are out there, waiting."

    scene arena
    with fade
    show bug at top with dissolve
    
    "Cut to Luna and Astra’s group"
    show astra neutral at slightleft with dissolve:
        xzoom -1.0
    "Bright flashes illuminate their side of the dome. Astra flicks her fingers like she’s playing a piano of light."
    astra "Variable set, loop engaged… {w}and {b}delete!{/b}"
    hide bug with dissolve
    with vpunch
    play sound punch_sound1
    show astra happy
    "A bug explodes into binary dust."

    show luna happy at slightright with dissolve
    luna "{cps=20}Wheeeeeeee!"
    show luna happy2
    show astra happy2
    luna "The bugs make sparkly confetti when they {size=+10}{b}die!{/b}{/size} {w}Can I keep one as a pet?"
    show mira neutral at right with dissolve
    mira "Please don’t. {w}That’s… {w}not sanitary."
    show mira sad
    mira "Digitally speaking."
    show mira sad2
    show astra neutral
    astra "Oh, lighten up. It’s just corrupted code — not actual bacteria."
    show astra sad
    astra "Probably."
    "Their group clears their entire wave in seconds."

    scene arena 
    with fade

    show screen scoreboard
    show mspython happy at right
    show doctorbyte happy at left 
    with dissolve

    mspy "Well done, everyone. Even those who stumbled… {w}learned."
    mspy "Remember — a single missing space can change everything."
    show doctorbyte neutral
    dr "Coding isn’t just about writing commands. It’s about thinking clearly under pressure."

    hide doctorbyte
    hide mspython
    with dissolve

    show cyra neutral-notab at right with dissolve
    cyra "Hey, [name]… {w}if we’re going to fight together, you’d better not slow me down."
    show cyra neutral2-notab
    show kai neutral at left with dissolve
    kai "Yeah. And next time, try not to blow up my defense system."
    show kai neutral2
    mc "Guess I’ll have to keep practicing… {w}or maybe I just enjoy keeping you both on edge."
    show cyra happy-notab
    show kai happy2
    "Cyra chuckles; Kai rolls his eyes but smiles faintly."

    hide screen scoreboard
    hide kai
    hide cyra
    with dissolve

    show luna happy-nostar at right with dissolve
    luna "Good job, [name]! You didn’t crash this time!"
    "Luna giggles and waves from across the dome."
    show astra neutral at left with dissolve:
        xzoom -1.0
    astra "Not bad… for a beginner. But let’s see how long you can keep up."
    "For a fleeting moment, her eyes flicker — a sharp digital glow."

    hide astra
    hide luna
    with dissolve

    pause 0.5

    show mspython neutral at center
    with dissolve
    
    mspy "Good. Because next time… you’ll be writing more than code."
    show mspython happy
    mspy "You’ll be writing your fate."
    show mspython happy2
    "And as the simulation fades, one thought burns bright in your mind."
    "This academy isn’t just about learning code…"
    "It’s about surviving in a world where logic is power."

    return



# Scene 3 Quizzes Other Branch
label question1Right:
    mspyIntercom "Well done. Your syntax is strong. Print is used to show the strings you want to say strings are the words."

    show astra happy at slightleft with dissolve:
        xzoom -1.0
    astra "Nice reflexes, rookie. Fast and clean — just my type."

    show kai happy at left with dissolve
    kai "Consistent. I like that."

    play sound right_answer
    $ change_kaiAffection(+1)
    "{=gold}Kai’s Affection +1{/=gold}"

    show cyra happy at slightright with dissolve
    cyra "You did it! The Bug didn’t even hiss at you!"
    play sound right_answer
    "{=gold}Syntax Confidence +2{/gold}"
    $ change_confidence(+2)

    show astra happy2
    show cyra happy2
    show kai happy2
    return

label question2Wrong:
    show kai neutral
    kai "Yawn. Even my grandma can assign variables."
    show kai neutral2
    show mira neutral at right with dissolve
    mira "It’s okay, everyone starts somewhere."
    show mira neutral2
    play sound hologram
    "(A mini Bug appears, shaped like a “?”; [name] zaps it.)"
    show cyra neutral
    cyra "Dont mind him, when he was new he was even worse"
    show cyra neutral2

    play sound error_sound1
    "{=red}Syntax Confidence –1{/red}"
    $ change_confidence(-1)

    return

label question3Right:
    show luna neutral at center with dissolve
    luna "Imagine if it could make coffee, though."
    show luna neutral2
    show astra neutral at slightleft with dissolve:
        xzoom -1.0
    astra "I’d marry Python."
    show kai neutral2
    "(Kai raises eyebrow.)"
    show astra happy
    astra "Relax, Kai— it’s just a language."
    show astra happy2

    play sound right_answer
    "{=gold}Syntax Confidence +2{/gold}"
    $ change_confidence(+2)
    return

label question4Wrong:
    show kai neutral
    kai "Pfft. Rookie mistake."
    show kai neutral2
    show luna neutral at center with dissolve
    luna "Hey, {b}Kai{/b}, remember when you broke your code with 18 curly braces?"
    show luna neutral2
    show kai happy
    kai "That was style."
    show cyra neutral
    cyra "Sure it was……."
    show cyra neutral2
    show astra neutral at slightleft with dissolve:
        xzoom -1.0
    astra "Nice try though [name]."
    show astra neutral2

    play sound error_sound1
    "{=red}Syntax Confidence –1{/red}"
    $ change_confidence(-1)

    "(Team laughs; Bug spawns and gets squashed.)"
    return

label question5Wrong:
    show luna sad
    luna "Awww, close! But hey, you tried! Here, have a sticker that says “Mostly Human.”"
    show luna sad2

    play sound error_sound1
    "{=red}Syntax Confidence –1{/red}"
    $ change_confidence(-1)
    return

# Scene 4: Free Interaction Choices
label talkToCyra:
    show cyra neutral2 at center
    with dissolve

    mc "That was a cool metaphor earlier — the magic spell thing."
    show cyra neutral
    cyra "You think so? Coding’s kinda like fire… {w}control it right, and you create something amazing."
    show cyra disgusted
    cyra "Lose control, and you burn your whole system."

    menu:
        "You sound like you’ve done that before.":
            show cyra happy
            cyra "Maybe once… {w}or twice. {w}You’ll learn to handle the fire someday."
            "{=gold}Cyra’s affection slightly increases.{/gold}"
            $ change_cyraAffection(+1)

        "That’s too dramatic for me.":
            show cyra neutral
            cyra "Then you’ll never survive Ms. Py Thon’s next exam."
            "{i}No affection change.{/i}"

    hide cyra
    with dissolve

    return

label talkToKai:
    show kai neutral2 at center
    with dissolve

    "You saw Kai leaning back in his chair."

    show kai neutral
    kai "So… how’s the new hero of Code Nexus liking syntax so far?"
    menu:
        "It’s kinda fun actually.":
            show kai surprised
            kai "Heh, didn’t expect you to say that." 
            show kai happy2
            kai "Maybe you’re not as hopeless as I thought."
            "{=gold}Kai’s affection slightly increases.{/gold}"
            $ change_kaiAffection(+1)
        "Boring. I want action.":
            show kai happy2
            kai "Pfft. Patience, rookie." 
            show kai happy
            kai "You can’t fight ‘Bugs’ without knowing how to debug."
            "Kai teases you. {i}No affection change.{/i}"

    hide kai
    with dissolve

    return

label talkToMsPython:
    show mspython neutral2 at center
    with dissolve

    mc "Ms. Py Thon, you make syntax sound way cooler than it should be."
    show mspython surprised
    mspy "Of course! Syntax is the melody that runs the digital universe."
    show mspython neutral
    mspy "Master it, and you can {i}sing your will into the code.{/i}"

    menu:
        "That’s poetic.":
            show mspython happy
            mspy "Coding is poetry, if you write it with care."
            show mspython happy2
            "You gain respect from Ms. Py Thon."
        "That’s… kind of creepy.":
            show mspython sad
            mspy "Then you’ve never seen true beauty in logic."
            "Slight awkwardness."

    hide mspython
    with dissolve

    return

label talkToDrByte:
    show doctorbyte happy at center
    with dissolve

    dr "You’re improving. Ms. Py Thon reports progress."
    mc "Really? That’s… good, I think?"
    show doctorbyte neutral
    dr "But remember — the Bugs grow stronger every time someone forgets a semicolon."
    mc "Uh, Python doesn’t use semicolons."
    show doctorbyte surprised
    dr"!!!"
    show doctorbyte sad
    dr "...."
    show doctorbyte happy2
    dr "....."
    show doctorbyte happy-flower
    dr "…I was testing you."

    hide doctorbyte with dissolve
    "He cuts the call..."
    "Everyone nearby bursts out laughing."
    
    return

label talkToAstra:
    show astra neutral2 at center
    with dissolve

    "You saw Astra leaning against the window, arms crossed with a confident grin on her face."
    show astra neutral
    astra "So, newbie, surviving your first code storm?"
    show astra neutral2
    mc "Somehow, yeah. Though I think the real storm was Ms. Py Thon’s syntax lecture."
    show astra neutral
    astra "Ha! You’ll get used to it. Syntax is the easy part {w}— it’s the logic battles that’ll fry your circuits later."

    menu:
        "Logic battles?":
            show astra neutral
            astra "Oh, you’ll see. Ever heard of a recursive loop that eats your project alive? Yeah, fun times"
            show astra neutral2
            "{i}You laugh nervously.{/i}"
            show astra happy
            astra "Don’t worry. If you ever crash, I’ll show you how to reboot{w} — in life and in code."
        "You sound like you’ve seen some chaos.":
            show astra sad
            astra "Let’s just say… I’ve debugged my share of nightmares."
            "Her tone softens for a second before she smirks again."
            show astra neutral
            astra "Stick close, rookie. You might learn more than you expect."

    hide astra
    with dissolve

    return