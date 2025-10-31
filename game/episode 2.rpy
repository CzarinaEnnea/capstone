label episode2:
# SCENE 1
    scene black
    with dissolve

    show text "Episode 2 - Data Types and the Glitch Zone" at truecenter with dissolve
    pause 2
    hide text with fade

    scene classroom_doorway
    with dissolve

    play music "audio/opening.ogg"

    "The neon skyline of the Code Academy Nexus gleamed like a motherboard at sunrise."
    "Yesterday, I fought a monster made of syntax errors. Today, I’m back for more…"

    mc "New day, same universe. Yesterday was chaos. But today—"
    mc "Ms. Py Thon said we’ll go 'deeper.' I just hope she means spiritually and not into a debug pit again."

    # play sound "school_bell.ogg"

    show cyra happy at right
    with dissolve
    show kai neutral at left
    with dissolve
    show luna neutral at center
    with dissolve
    show mira neutral at slightleft
    with dissolve
    show astra neutral at slightright
    with dissolve

    cyra "Morning, rookie. Ready for another brain workout?"
    kai "We’ve got ‘Data Types and Operations’ on the schedule. Sounds like she’s teaching us how to store our souls in variables."
    luna "Oooh! Can we store glitter too?"
    mira "If it’s binary glitter… maybe?"
    mc "Haha! I’ll take binary glitter over binary panic any day."

    hide cyra
    hide kai
    hide luna
    hide mira
    hide astra

    "The lights dim. Ms. Py Thon materializes from floating code glyphs."

    show mspy neutral at center
    with dissolve

    mspy "Good morning, coders."
    mspy "You survived variables — now it’s time to understand what they hold."
    mspy "Today’s topic: Python’s Built-in Data Types."

    hide mspy
    with fade

    stop music fadeout 2.0

#SCENE 2

    show text "2" at truecenter with dissolve
    pause 2
    hide text with fade

    #play music "data_theme.ogg" fadein 2.0

    "Holographic lights swirl across the classroom. Data symbols — numbers, words, equations — orbit around {color=#00ffff}Ms. Py Thon{/color} like glowing satellites."
    "Each flicker of light hums softly, resonating like a heartbeat made of pure code."

    show mspy neutral at slightright
    mspy "All things in Python — and in this universe — are made of {color=#00ff99}data types{/color}."
    mspy "Every spell, every system, every emotion — stored in a format your code understands."
    mspy "Let’s begin with the simplest…"
# --------------------------------------------------------------
# 1️⃣ TEXT TYPE: str
# --------------------------------------------------------------

    mspy "First, the {color=#00ffff}string type{/color}. ‘str’ — holds words, sentences, or any series of characters."
    mspy "For example:"

    #-------------------------------------------------Ep 2 code1 - string 
    #    name = "Code Nexus"
    #    print(name)
    #    OUTPUT:
    #    Code Nexus
    show screen info_box("1. TEXT TYPE: str") with dissolve
    
    #change this image
    show ep2-scn2-txt1 at top_left_space 
    with dissolve

    cyra "So, “Cyra the Great” is a string too?"
    kai "(deadpan) More like a variable with an ego."
    cyra "Watch it, Volt-boy. I’ll concatenate your attitude."

    #change this image
    hide ep2-scn2-txt1
    hide screen info_box 
    
    #-------------------------------------------------Ep 2 code2 - string concatenation
    #   first = "Cyra"
    #   last = "Byte"
    #   print(first + last)
    #   OUTPUT 
    #   CyraByte

    show screen info_box("TEXT TYPE: string concatenation") with dissolve
    
    #change this image
    show ep2-scn2-txt2 at top_left_space
    with dissolve

    mspy "Excellent example, Ms. Byte. 'Concatenation' means joining strings using the + operator."
    luna "(typing) Luna + 'Shine' = 'LunaShine' — It’s me, but sparkly!"
    mspy "Yes Luna dear. But if you want to add a space in your string you just add two double quotations and a space string like so:"
    
    #change this image
    hide ep2-scn2-txt2
    hide screen info_box 

    #-------------------------------------------------Ep 2 code3 - string concatenation
    #    first = "Luna"
    #    last = "Shine"
    #    print(first + " " + last)
    #    OUTPUT 
    #    Luna Shine

    show screen info_box("TEXT TYPE: concatenation with space") with dissolve
    
    #change this image
    show ep2-scn2-txt3 at top_left_space
    with dissolve

    "Ohhhh… so that’s how you do it!"
    mspy "(smirking) Do take note of this — it might come in handy later."

    #change this image
    hide ep2-scn2-txt3
    hide screen info_box 
# --------------------------------------------------------------
# 2️⃣ NUMERIC TYPES: int, float, complex
# --------------------------------------------------------------

    mspy "Next — {color=#00ffff}numbers{/color}. Integers, floats, and complex types."
    show screen info_box("2. Numeric Types: int, float, complex") with dissolve
    

    #-------------------------------------------------Ep 2 code4 - numbers 
    #    a = 5        # int
    #    b = 3.14     # float
    #    c = 2 + 3j   # complex
    #    OUTCOME:
    #    print(a)
    #    print(b)
    #    print(c)
    
    #change this image
    show ep2-scn2-txt4 at top_left_space
    with dissolve

    kai "Complex numbers? I already have one of those — it’s called my love life."
    "The room falls silent. A single cricket chirps."
    cyra "Correction — it’s called nonexistent."
    luna "(giggling) So 2 + 3j means… it’s literally imaginary?"
    mspy "Indeed. But even imaginary logic can create real outcomes — just ask quantum computers… or poets."

    #change this image
    hide ep2-scn2-txt4
    hide screen info_box 
# --------------------------------------------------------------
# 3️⃣ SEQUENCE TYPES: list, tuple, range
# --------------------------------------------------------------

    show screen info_box("3.Sequence Types: list, tuple, range") with dissolve
    mspy "Sequences hold multiple values in order — like an array of memories."

    #-------------------------------------------------Ep 2 code5 - numbers list, tuple, range
    #    fruits = ["apple", "banana", "cherry"]   # list
    #    numbers = (1, 2, 3)                      # tuple
    #    x = range(6)                             # range
    #    #OUTCOME:
    #    print(fruits)
    #    print(numbers)
    #    print(list(x)) 

    #change this image
    show ep2-scn2-txt5 at top_left_space
    with dissolve


    mira "So a list can change… but a tuple can’t, right?"
    mspy "Exactly. Lists are {color=#ffaa00}mutable{/color} — like you, young Mira.To print a list after setting the print syntax inside the parenthesis you have also to call “list” then the variable, because if you dont it will just print what you set the x variable."
    mspy  "Tuples are {color=#ffaa00}immutable{/color} — like Kai’s personality.  A tuple is a collection which is ordered and unchangeable. Unlike the others Tuples are written with round brackets."
    kai "Harsh, but fair."


    luna "What about {color=#00ffff}range{/color}?"
    mspy "Think of it as a spell that creates a sequence of numbers dynamically. Range function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and stops before a specified number."
    mspy "For example:"

    hide ep2-scn2-txt5

    #-------------------------------------------------Ep 2 code6 - numbers range
    #    for x in range(3):
    #        print(x)
    #    → Outputs: 0, 1, 2

    #change this image
    show ep2-scn2-txt6 at top_left_space
    with dissolve

    cyra "Nice. A loop with style."
    mc "(smirks) I might use that when I get lazy counting."
    mspy "(sighs) These students of mine…"
    
    #change this image
    hide ep2-scn2-txt6
    hide screen info_box 
# --------------------------------------------------------------
# 4️⃣ MAPPING TYPE: dict
# --------------------------------------------------------------

    show screen info_box("4. Mapping Type: dict") with dissolve
    
    #change this image
    show ep2-scn2-txt7 at top_left_space
    with dissolve
    mspy "Now, the {color=#00ffff}dictionary{/color}. It stores key-value pairs — a mapping of logic.If you want to print all you’ve set:"


    #-------------------------------------------------Ep 2 code7 - numbers list, tuple, range
    #student = {
    #    "name": "Alex",
    #    "team": "Debugger",
    #    "rank": 5
    #    }
    #   print(student)
    #   OUTPUT: 
    #   {'name': 'Alex', 'team': 'Debugger', 'rank': 5}
    
    #change this image
    hide ep2-scn2-txt7

    mspy "But if you only want to show one variable:"

    #change this image
    show ep2-scn2-txt8 at top_left_space
    with dissolve

    # student = {
    #    "name": "Alex",
    #    "team": "Debugger",
    #    "rank": 5
    #    }
    #    print(student[“name”])
    # OUTPUT:
    #   Alex

    mc "So it’s like… storing traits for a character?"
    mspy "Exactly. You, for example, are a dictionary of courage and confusion."
    cyra "And sarcasm."
    kai "Don’t forget questionable decision-making."
    
    "The class bursts into laughter."
    hide screen info_box
    
    #change this image
    hide ep2-scn2-txt8
    with dissolve
# --------------------------------------------------------------
# 5️⃣ BOOLEAN TYPE: bool
# --------------------------------------------------------------

    show screen info_box("5. Boolean Type: bool") with dissolve
    
    #change this image
    show ep2-scn2-txt11 at top_left_space
    with dissolve
    mspy "Booleans — True or False. The pillars of all logic."

    #-------------------------------------------------Ep 2 code8 - numbers list, tuple, range
    #    a = 60
    #    b = 100
    #    passing_grade = 100
    #    c = "Grade:"
    #    if passing_grade < a:
    #        print(c + "Failed")
    #    else:
    #        print(c + "Passed")

    cyra "So... Boolean’s basically the Academy’s grading system?"
    mspy "If you code correctly — True. If not — False… and maybe detention."

    hide screen info_box
    
    #change this image
    hide ep2-scn2-txt11
    with dissolve
# --------------------------------------------------------------
# 6️⃣ NONE TYPE: NoneType
# --------------------------------------------------------------

    mspy "And finally… {color=#ff66ff}None{/color} — the void. Used when there’s no data, no value, no purpose."
    show screen info_box("6. None Type: NoneType") with dissolve
    
    #change this image
    show ep2-scn2-txt12 at top_left_space 
    with dissolve
    #-------------------------------------------------Ep 2 code9 - None
    #    x = None
    #    print(x)

    mspy "(solemnly) Some coders fear the void. Others learn to use it."
    cyra "That’s… kinda dramatic. I like it."

    hide screen info_box
    
    #change this image
    hide ep2-scn2-txt12
    with dissolve

    mspy "Excellent work today, Debuggers. Tomorrow, we’ll test how these data types interact — through operations and logic."

    mc "(smiles) Guess that means more chaos… and more code."

    stop music fadeout 3.0
    scene black with fade

#SCENE 3
    show text "Scene 3" at truecenter with dissolve #placeholder remove later
    pause 2
    scene classroom #Dome Background
    with fade

    "The next day."
    #play music "alarm.ogg"
    show red at truecenter 

    dr "Attention, Team Debugger. A Glitch Portal has opened inside the training grid.
        This anomaly threatens to overwrite your classroom simulation.Prepare for deployment"
    
    stop music fadeout 3.0

    #play music "glitch_theme.ogg" fadein 2.0 #replace with classic bmg
    show mspy neutral at center
    mspy "Excellent timing. You’ll be applying your knowledge today — in combat.
        Remember, each Bug manifests from broken logic. Data types are your weapons."
    mc "Wait, we're fighting... with code?"
    hide mspy with dissolve

    show cyra neutral at right with dissolve
    cyra "Finally, a class that gets my blood pumping. Hope you can keep up, rookie."
    show kai neutral at slightleft with dissolve
    kai "Hmph. Let’s see if you can debug faster than you talk."
    show luna happy at left
    show mira neutral at slightright
    show astra neutral at truecenter
    with dissolve

    luna "A real glitch portal? Sparkly destruction! Let’s gooo!"
    mira "Just—just stay close, everyone. I’ll monitor system output from the console."
    astra "Oh, relax. It’s just data gone wild. We tame it, we go home. Easy as {color=#00ffff}print(\"Victory\"){/color}."

    stop music fadeout 3.0
    scene black with fade

    # change location to glitch zone
    scene glitch_zone
    with dissolve

    mc "Whoa… it’s like stepping into a corrupted dream."
    show cyra neutral at slightright with dissolve
    cyra "Or my first web project after no sleep. Same energy"
    
    show luna happy at right with dissolve
    luna "I love it! It’s creepy and shiny!"
    mspy "Focus, Debuggers. Each Bug’s nature corresponds to a Python data type.
        Identify it. Use the right logic to neutralize it. Let’s begin."

    show screen info_box("Bug #1 – The String Leech") with dissolve
    show bug at top_left_space #change location later
    $ red_effect()

    "A pulsating worm of text hovers midair, echoing 'ErrorErrorError...'"

    show mspython neutral at center with dissolve
    mspy "This one loops through text patterns. Use string operations to break the cycle."
    mspy "Remember: in Python, multiplying a string repeats it."
    hide mspython with dissolve

    show cyra smile at right with dissolve
    cyra "Like {color=#00ffff}print('LOL' * 3){/color} — my favorite debugging noise."

    show kai smirk at slightright with dissolve
    kai "You would weaponize sarcasm."

    "Choose the correct syntax!!"
    "How will you handle the String Leech?"
        

    menu:
        extend ""

        "print('Error' * 3)":
            # put sound here for correct answer
            with hpunch
            "The Bug vibrates, then dissolves into glowing pixels."
            mspy "Perfect. You matched its pattern."
            cyra "Nice echo control, coder."
            # hide red with fade
            hide bug with dissolve
            $ change_cyraAffection(+1)

        "x = 3 + 'Error'":
            # put sound here for wrong answer
            with vpunch
            $ red_effect()
            "The Bug screams! The dome shakes — fragments of red text fly."
            mspy "TypeError! You cannot add integers and strings. Data types must match."
            kai "Rookie mistake. Don’t worry — happens to the best of us."
            hide bug with dissolve

        "del 'Error'":
            # put sound here for wrong answer
            $ red_effect()
            "A syntax flashback explodes."
            luna "You can’t just delete a word from reality!"
            mspy "Indeed. Strings are immutable — once defined, you cannot delete literal values directly."
            hide bug with dissolve

    hide screen info_box with fade

    pause .5


    #bug 2
    show screen info_box("Bug #2 – The Numeric Ogre") with dissolve
    show bugOrge at top_left_space
    $ red_effect()

    "A massive creature stomps in, chanting: 'Divide by Zero! Divide by Zero!'"

    mspy "Arithmetic operators — +, -, *, / — handle calculations."
    mspy "But dividing by zero causes catastrophic failure. Proceed carefully."

    luna "So… never trust a zero. Got it."
    cyra "Or trust Kai with math."
    kai "Funny. Let’s see if you still laugh after you lose the leaderboard."

    "Choose the correct numeric operation!!"
    "How do you calm the Numeric Ogre?"

    menu:
        extend ""

        "x = 10 / 2":
            #put sound here for correct answer
            "A calm blue wave stabilizes the bug."
            mspy "Excellent. Division complete without error."
            kai "Clean logic. You’ve got quick hands, MC."
            $ change_kaiAffection(+1)
            hide bugOrge with dissolve
            hide screen info_box with move


        "x = 10 / 0":
            #explosion sound
            $ red_effect()
            with vpunch
            "Explosion of red light — alarms blare."
            mspy "DivideByZeroError! Impossible operation — logic fails!"
            mira "The bug’s feeding on it! I’m losing control of the data flow!"
            astra "Back it up, newbie. Keep your variables alive next time."
            hide bugOrge with move
            hide screen info_box with move

        "x = 'Ten' + 2":
            #error sound
            $ red_effect()
            "The code distorts — random characters appear."
            mspy "Invalid operation. You can’t combine strings and integers with +."
            cyra "Oof, classic mistake. Mixing data types — every beginner’s heartbreak."
            hide bugOrge with move
            hide screen info_box with move      
    
    pause .5
    show red at truecenter with fade

    #bug 3
    show screen info_box("Bug #3 – The List Hydra") with fade

    show bugHydra at top_left_space with dissolve
    $ red_effect()

    "Three heads emerge, hissing binary streams."

    mspy "Lists are mutable — you can modify them."
    mspy "To contain the Hydra, use {color=#00ffff}.append(){/color} to add each head into your list."
    cyra "So… we’re making a 'Hydra shopping list'? Nice."

    hide screen info_box with move
    hide bugHydra with move
    mspy "Example:"
    show ep2-scn3-txt1 at top_left_space with move
    mspy "The append() method adds items to the end of a list."

    hide ep2-scn3-txt1 with move    
    show bugHydra at top_left_space with move
    show screen info_box("Bug #3 – The List Hydra") with move

    "How do you trap the Hydra?"
    menu:
        "heads = [[]\n heads.append('Hydra')":
            # put sound here for correct answer
            "The Hydra turns to harmless data bubbles."
            luna "Hydra captured! Friendship and Python win again!"
            astra "Nicely done. You’ve mastered list manipulation."
            hide bugHydra with move
            hide screen info_box with move
            hide red with dissolve

        "heads = ('Hydra')":
            # put sound here for wrong answer
            "The heads multiply!"
            mspy "Incorrect — parentheses create a string, not a list. Lists use brackets [[]."
            cyra "Guess we’re snake food now."
            hide bugHydra with move
            hide screen info_box with move

        "heads = range('Hydra')":
            # put sound here for wrong answer
            "The system glitches violently."
            mspy "TypeError. range() only accepts numbers, not strings. Be precise!"
            mira "I’ll stabilize it— wait… it’s resisting my override..."
            hide bugHydra with move
            hide screen info_box with move
    
    #bug 4
    show screen info_box("Bug #4 – The Boolean Phantom")

    show bugPhantom at top_left_space with move

    "A ghost flickers in and out, whispering 'True… False…'"

    mspy "Booleans control logic flow. Use {color=#00ffff}if{/color} statements to make code decisions."
    kai "So, we’re exorcising with logic? My kind of fight."

    "What code do you use to reveal the truth?"
    menu:

            "if True: print('Visible')":
                # put sound here for correct answer
                "The ghost solidifies and vanishes in light."
                mspy "Perfect control. True conditions execute the code block."
                kai "You handle pressure well, MC."
                $ change_kaiAffection(+1)
                hide red with dissolve
                hide bugPhantom with move
                hide screen info_box with move

            "if None: print('Visible')":
                #put sound here for wrong answer
                "The ghost duplicates!"
                mspy "None is not a Boolean value — logic collapsed!"
                luna "Aah! Now we have two ghosts! Double the haunted homework!"
                hide bugPhantom with move
                hide screen info_box with move

            "if False: print('Visible')":
            #put sound here for wrong answer
                "The ghost turns invisible — then jumpscares the team."
                cyra "WAAH! Remind me to never trust False again."
                mspy "False conditions skip execution — your action didn’t trigger the code."
                hide bugPhantom with move
                hide screen info_box with move

    # Final Boss
    show screen info_box("Boss: The Void Entity")

    show bugVoid at top_left_space with move
    "The entire forest shakes. A massive shadow rises — pure black code swirling like smoke."

    mspy "This one... is made of NoneType — the absence of data. Only creation — something from nothing — can undo it."
    cyra "That’s… deep. We code meaning into nothingness?"
    mc "Let’s give it something real."

    "What do you assign to restore balance?"
    menu:

            "x = None":
                #put sound here for wrong answer
                "The void expands, draining color."
                mspy "Wrong. Assigning None gives it power. None means emptiness."
                astra "Careful — feed darkness and it grows."
                hide bugVoid with move
                hide screen info_box with move
                hide red with dissolve

            "x = 'Hope'":
                # put sound here for correct answer
                "The word 'Hope' appears in glowing light, shattering the Void."
                mspy "Beautifully done. Creation defeats emptiness."
                luna "YAY! We beat the void with positivity and variable assignment!"
                hide bugVoid with move
                hide screen info_box with move

            "del x":
                #put sound here for wrong answer
                "The code destabilizes. Chaos follows."
                mspy "Deleting variables erases value entirely!"
                mira "It’s rewriting the environment— STOP!"
                hide bugVoid with move
                hide screen info_box with move

    stop music fadeout 2.0 #fight music stop here
    #play music "ending_theme.ogg" fadein 2.0  #start ending music here

    scene classroom_day with fade
    dr "Simulation success. Excellent teamwork, Debuggers."
    show mspy happy at center
    with move
    mspy "You’ve done well. Every operation, every decision — builds the foundation of your code."

    show cyra neutral at slightleft with move
    show kai neutral at left with move
    show luna happy at right with move
    show mira neutral at slightright with move
    show astra neutral at truecenter with move

    cyra "Next time, I call dibs on the final blow."
    kai "You? You barely handled one Boolean ghost."
    cyra "Says the guy who screamed when the Hydra burped."
    luna "Aww, you’re all such cute bugs yourselves!"
    astra "The real fun starts when the logic turns against you. Remember that."
    mira "(quietly) Logic… turning against us…? Nothing. I’m fine."

    mspy "Team Debugger — class dismissed. Tomorrow, we learn about Operators and If/Else."

#SCENE 4
    scene lounge
    with fade

    # play music "lounge_theme.ogg" fadein 2.0

    "Soft neon glows fill the Debuggers' Lounge, the hum of holographic screens buzzing in the background."
    "Steam rises from mugs of synthe-tea. Outside, the city flickers like a living circuit board under the digital sunset."
    "After surviving the Glitch Zone, the team finally breathes."

    show luna tired at left
    with dissolve
    show cyra happy at slightleft
    with dissolve
    show kai smirk at right
    with dissolve
    show mira neutral at center
    with dissolve
    show astra neutral at slightright
    with dissolve

    luna "Uggggh… my brain feels like it’s been formatted twice and recompiled with extra exhaustion."
    cyra "You did great, Luna. Especially when you tried to high-five the Boolean ghost. Very brave. Very stupid, but brave."
    luna "Hey! It looked friendly until it tried to eat my code history!"
    kai "That’s what happens when you try to debug with pure optimism."
    mc "Worked better than your 'punch the Hydra until it obeys' plan."
    kai "It was experimental logic. Sometimes violence *is* the answer… in pseudocode."
    cyra "Yeah, sure, Mr. 'divide by zero.' Real smooth operator there."
    kai "Tch. Low blow, Byte."
    "Laughter fills the lounge, echoing off the neon-lit walls."

    mira "I… I’m just glad everyone’s okay. The system was on the verge of collapse. If we’d delayed even a second longer, the Glitch could’ve—"
    "She pauses, catching herself before overanalyzing again."
    mc "You held the whole simulation together, Mira. You saved us."
    mira "O-oh… I just followed the algorithm. Anyone could’ve done it."
    astra "Not anyone. I saw your override code. That wasn’t textbook. You rewrote the logic mid-run."
    mira "It—It was just a… reflex. A patch job. Nothing special."
    "Her voice wavers slightly — her eyes flicker faintly with a red glitch, almost imperceptible."
    luna "Whoa, Mira! Your eyes just did the glow thing! So cool!"
    mira "Just—just reflection from the holo screen. I’m fine."
    cyra "You should’ve seen your face during the fight, MC. That ‘String Leech’ almost had you — until you went full coder mode. Not bad for a rookie."
    mc "Guess I’m starting to get the hang of this Python thing."
    mc "(pauses, looking around) And maybe… getting to know this team too."

    kai "Don’t get comfortable yet. Next round, I’m taking the top score back. No hard feelings."
    cyra "You mean when I take it first."
    kai "Dream on."
    luna "(throws a chip bag) Ship yourselves already!"
    cyra "Wha—?!"
    kai "What are you talking about?!"
    "Everyone bursts into laughter — except Mira, who gives a faint, strained smile."
    astra "(smirking slightly) Some things never change. Team chaos, through and through."

    # Ms. Py Thon Hologram Appears
    show mspy happy at center
    with dissolve
    # play sound "hologram_on.ogg"
    # put hologram sound here for Ms. Py Thon entrance

    mspy "Excellent work today, Debuggers. Your teamwork was… mostly functional."
    luna "(salutes dramatically) Mission accomplished, Ms. Python! No existential crises left behind!"
    mspy "(smiling faintly) Tomorrow’s module will be Operators and Conditional Statements. Prepare your minds."
    mspy "We will learn how the simplest symbols — +, -, *, /, and, or, not — can reshape digital reality itself."

    cyra "Oh great. Math with consequences."
    kai "Oh joy. Logic puzzles. My favorite way to suffer."
    luna "Oh no… homework."
    mira "(quietly) Logic defines fate. Every choice… changes the outcome."
    astra "(watching her carefully) Hmm. Spoken like someone who’s seen both sides of the code."
    mira "(startled) I—I didn’t mean—never mind."

    "The atmosphere shifts — subtle tension beneath the glow. MC looks between them, uneasy."

    # --- Optional Interactions ---
    menu:
        "What will you do?"
        
        "Talk to Cyra":
            mc "You really kept your cool out there. You always this confident?"
            cyra "(smiling, leaning closer) Confidence is just caffeine and chaos, rookie. But… maybe I just wanted to impress someone."
            "She laughs softly, brushing her hair aside."
            $ change_confidence(+1)
            "{=gold}Syntax Confidence +1{/=gold}"
            $ change_cyraAffection(+1)
            "{=gold}Cyra’s Affection +1{/=gold}"
            mc "(grinning) Mission accomplished."

        "Talk to Kai":
            mc "You were solid out there. Even when the Hydra bit your arm."
            kai "(chuckling) It’s fine. I’ve had worse bugs. But don’t think I’ll let you beat me again."
            kai "(grins) Next time, I’m going all in. No mercy coding."
            $ change_confidence(+1)
            "{=gold}Syntax Confidence +1{/=gold}"
            $ change_kaiAffection(+1)
            "{=gold}Kai’s Affection +1{/=gold}"
            mc "You’re on, Kai."

        "Talk to Mira":
            mc "You seemed worried during the mission. Everything okay?"
            mira "(looking distant) Just… residual static. Sometimes I see patterns where there shouldn’t be any. It’s probably nothing."
            "Her datapad flickers with corrupted code for a split second — {color=#ff4444}ACCESS DENIED{/color}."
            mc "(concerned) Mira…?"
            mira "(forcing a smile) I’m fine, really. Just tired."
            $ change_confidence(-1)
            "{=red}Syntax Confidence -1{/=red}"
            "You feel a strange unease — like something in the code just shifted."

    # --- Glitch Sequence ---
    "Suddenly, the lounge lights flicker."
    # play sound "glitch_static.ogg" 
    #play glitch sound effect
    "The holo-screen flashes — a shadowed figure appears, typing rapidly on a terminal. The image distorts before vanishing."
    luna "(sits up) Uh… anyone else see that?"
    cyra "(frowning) Probably just lag from the system reboot."
    astra "(low voice, almost to herself) No… that was intentional. Someone’s inside the code."
    mira "(gripping her datapad) ...We should go. It’s late."
    kai "Agreed. Tomorrow’s going to be a long one."
    mspy "Rest well, Debuggers. Tomorrow — we calculate destiny."
    hide mspy with dissolve

    mc "(to self) Calculate destiny, huh?"
    mc "(smiles faintly) Bring it on."

    stop music fadeout 3.0
    scene black with fade
    "To be continued..."
    return
