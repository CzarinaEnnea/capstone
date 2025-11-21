label episode2:
# SCENE 1
    scene black
    with dissolve

    show text "Episode 2 - Data Types and the Glitch Zone" at truecenter with dissolve
    pause 2
    hide text with fade

    scene hallway
    with dissolve

    play music "audio/opening.ogg"

    "The neon skyline of the Code Academy Nexus gleamed like a motherboard at sunrise."
    "Yesterday, I fought a monster made of syntax errors. Today, I’m back for more…"

    mc "New day, same universe. Yesterday was chaos. But today—"
    mc "Ms. Py Thon said we’ll go '{i}deeper{/i}'. {w}I just hope she means spiritually and not into a debug pit again."

    play sound "school-bell.ogg"

    show cyra happy at right
    with dissolve
    cyra "Morning, rookie. Ready for another brain workout?"

    show kai neutral at left
    with dissolve
    kai "We’ve got ‘{i}Data Types and Operations{/i}’ on the schedule." 
    kai "Sounds like she’s teaching us how to store our souls in variables."
    show kai neutral2

    show luna happy at center
    with dissolve
    luna "Oooh! Can we store glitter too?"

    show mira happy at slightleft with dissolve:
        xzoom -1.0
    mira "If it’s binary glitter… maybe?"
    show mira happy2

    mc "Haha! I’ll take binary glitter over binary panic any day."

    hide cyra
    hide kai
    hide luna
    hide mira
    with dissolve

    "The lights dim. Ms. Py Thon materializes from floating code glyphs."

    play sound hologram
    show mspython neutral at center
    with dissolve

    mspy "Good morning, coders."
    mspy "You survived variables — now it’s time to understand what they hold."
    mspy "Today’s topic: {b}Python’s Built-in Data Types{/b}."

    hide mspython
    with dissolve

    stop music fadeout 2.0

#SCENE 2

    play sound "door_opening_school_doorway.ogg"
    scene classroom
    with dissolve

    #play music "data_theme.ogg" fadein 2.0

    "Holographic lights swirl across the classroom. Data symbols — numbers, words, equations — orbit around {color=#00ffff}Ms. Py Thon{/color} like glowing satellites."
    "Each flicker of light hums softly, resonating like a heartbeat made of pure code."

    show mspython neutral at slightright with dissolve
    mspy "All things in Python — and in this universe — are made of {color=#00ff99}data types{/color}."
    mspy "Every spell, every system, every emotion — stored in a format your code understands."
    mspy "Let’s begin with the simplest…"
# --------------------------------------------------------------
# 1️⃣ TEXT TYPE: str
# --------------------------------------------------------------

    mspy "First, the {color=#00ffff}string type{/color}. ‘str’ — holds words, sentences, or any series of characters."
    mspy "For example:"
    show mspython neutral2

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
    kai "(deadpan) {p}More like a variable with an ego."
    cyra "Watch it, Volt-boy. I’ll concatenate your attitude."

    #change this image
    hide ep2-scn2-txt1
    hide screen info_box
    with dissolve 
    
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

    show mspython happy
    mspy "Excellent example, Ms. Byte. 'Concatenation' means joining strings using the + operator."
    show mspython happy2
    luna "(typing) {p}Luna + 'Shine' = 'LunaShine'{w} — It’s me, but sparkly!"
    show mspython neutral
    mspy "Yes Luna dear. {w}But if you want to add a space in your string you just add two double quotations and a space string like so:"
    
    #change this image
    hide ep2-scn2-txt2
    hide screen info_box
    with dissolve

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

    luna "Ohhhh… so that’s how you do it!"
    show mspython happy
    mspy "Do take note of this — it might come in handy later."

    #change this image
    hide ep2-scn2-txt3
    hide screen info_box 
    with dissolve
# --------------------------------------------------------------
# 2️⃣ NUMERIC TYPES: int, float, complex
# --------------------------------------------------------------

    show mspython neutral
    mspy "Next — {color=#00ffff}numbers{/color}. Integers, floats, and complex types."
    show mspython neutral2
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

    kai "Complex numbers? I already have one of those {w}— it’s called my love life."
    mc "..."
    "The room falls silent. A single cricket chirps."
    cyra "Correction {w}— it’s called nonexistent."
    luna "(giggling) {p}So 2 + 3j means… {w}it’s literally imaginary?"
    show mspython neutral
    mspy "Indeed. But even imaginary logic can create real outcomes — just ask quantum computers… {w}or poets."

    #change this image
    hide ep2-scn2-txt4
    hide screen info_box 
    with dissolve
# --------------------------------------------------------------
# 3️⃣ SEQUENCE TYPES: list, tuple, range
# --------------------------------------------------------------

    show screen info_box("3.Sequence Types: list, tuple, range") with dissolve

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

    show mspython neutral at right with move
    mspy "Sequences hold multiple values in order — like an array of memories."

    show mspython neutral2
    mira "So a list can change… but a tuple can’t, right?"
    show mspython happy
    mspy "Exactly. Lists are {color=#ffaa00}mutable{/color} — like you, young Mira."
    mspy "To print a list after setting the print syntax inside the parenthesis you have also to call “{b}list{/b}” then the {b}variable{/b},{w} because if you dont it will just print what you set the x variable."
    show mspython neutral
    mspy "Tuples are {color=#ffaa00}immutable{/color} {w}— like Kai’s personality." 
    mspy "A tuple is a collection which is ordered and unchangeable. Unlike the others Tuples are written with round brackets."
    show mspython neutral2
    kai "Harsh, but fair."


    luna "What about {color=#00ffff}range{/color}?"
    show mspython neutral
    mspy "Think of it as a spell that creates a sequence of numbers dynamically." 
    mspy "Range function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and stops before a specified number."
    mspy "For example:"
    show mspython neutral2

    hide ep2-scn2-txt5
    with dissolve

    #-------------------------------------------------Ep 2 code6 - numbers range
    #    for x in range(3):
    #        print(x)
    #    → Outputs: 0, 1, 2

    #change this image
    show ep2-scn2-txt6 at top_left_space
    with dissolve

    cyra "Nice. A loop with style."
    mc "(smirks) {p}I might use that when I get lazy counting."
    show mspython sad
    mspy "(sighs) {p}These students of mine…"
    
    #change this image
    hide ep2-scn2-txt6
    hide screen info_box 
    with dissolve
# --------------------------------------------------------------
# 4️⃣ MAPPING TYPE: dict
# --------------------------------------------------------------
    show mspython neutral2 at slightright with move

    show screen info_box("4. Mapping Type: dict") with dissolve
    
    #change this image
    show ep2-scn2-txt7 at top_left_space
    with dissolve

    show mspython neutral
    mspy "Now, the {color=#00ffff}dictionary{/color}. It stores key-value pairs — a mapping of logic." 
    mspy "Here we see If you want to print all you’ve set."


    #-------------------------------------------------Ep 2 code7 - numbers list, tuple, range
    #student = {
    #    "name": "Alex",
    #    "team": "Debugger",
    #    "rank": 5
    #    }
    #   print(student)
    #   OUTPUT: 
    #   {'name': 'Alex', 'team': 'Debugger', 'rank': 5}

    mspy "But if you only want to show one variable-"

    #change this image
    hide ep2-scn2-txt7
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

    mspy "We do it like so."
    mc "So it’s like… storing traits for a character?"
    show mspython happy
    mspy "Exactly. You, for example, are a dictionary of courage and confusion."
    show mspython happy2
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

    show mspython neutral
    mspy "Booleans — True or False. The pillars of all logic."
    show mspython neutral2

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
    show mspython neutral
    mspy "If you code correctly — True. If not — False…" 
    show mspython happy
    mspy "{w}And maybe detention."

    hide screen info_box
    with dissolve
    
    #change this image
    hide ep2-scn2-txt11
    with dissolve
# --------------------------------------------------------------
# 6️⃣ NONE TYPE: NoneType
# --------------------------------------------------------------

    show mspython neutral with dissolve
    mspy "And finally… {color=#ff66ff}None{/color} — the void. {w}Used when there’s no data, no value, no purpose."
    show screen info_box("6. None Type: NoneType") with dissolve
    
    #change this image
    show ep2-scn2-txt12 at top_left_space 
    with dissolve
    #-------------------------------------------------Ep 2 code9 - None
    #    x = None
    #    print(x)

    show mspython sad
    mspy "Some coders fear the void. Others learn to use it."
    cyra "That’s… kinda dramatic. I like it."

    hide screen info_box with dissolve
    
    #change this image
    hide ep2-scn2-txt12
    with dissolve

    show mspython happy at center with move
    mspy "Excellent work today, Debuggers." 
    mspy "Tomorrow, we’ll test how these data types interact {w}— through operations and logic."
    show mspython happy2

    mc "(smiles) {p}Guess that means more chaos… and more code."

    scene black with fade

#SCENE 3
    scene classroom #Dome Background
    with fade

    "The next day."
    play music "emergency_alarm.ogg"
    show red at truecenter with dissolve 

    drIntercom "Attention, Team Debugger. A Glitch Portal has opened inside the training grid."
    drIntercom "This anomaly threatens to overwrite your classroom simulation. Prepare for deployment"
    
    stop music fadeout 3.0

    play sound "glitch_sound.ogg"
    show mspython neutral at center
    mspy "Excellent timing. You’ll be applying your knowledge today — in combat."
    mspy "Remember, each Bug manifests from broken logic. Data types are your weapons."
    show mspython neutral2
    mc "Wait, we're fighting... with code?"
    hide mspython with dissolve

    show cyra neutral at right with dissolve
    cyra "Finally, a class that gets my blood pumping. Hope you can keep up, rookie."
    show cyra neutral2
    show kai neutral at left with dissolve
    kai "Hmph. Let’s see if you can debug faster than you talk."
    show kai neutral2

    show luna surprised3 at center with dissolve
    luna "A real glitch portal?!"
    show luna happy
    luna "Sparkly destruction! Let’s gooo!"
    show mira neutral at slightright with dissolve
    mira "Just—{w}just stay close, everyone. {w}I’ll monitor system output from the console."
    show mira neutral2

    show astra neutral at slightleft with dissolve:
        xzoom -1.0
    astra "Oh, relax. It’s just data gone wild. We tame it, we go home."
    show astra happy
    astra "Easy as {color=#00ffff}print(\"Victory\"){/color}."

    scene black with fade
    pause 1.0

    # change location to glitch zone
    scene classroom
    with dissolve

    pause 0.5
  
    play sound "glitch_sound.ogg"
    show classroom with dissolve:
        subpixel True matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.12)*SaturationMatrix(0.99)*BrightnessMatrix(-0.09)*HueMatrix(630.0) 

    mc "Whoa… it’s like stepping into a corrupted dream."
    show cyra neutral at right with dissolve
    cyra "Or my first web project after no sleep. Same energy"
    show cyra neutral2
    
    show luna happy-nostar at slightright with dissolve
    luna "I love it! It’s creepy and shiny!"
    show mspython neutral at center with dissolve
    mspy "Focus, Debuggers. Each Bug’s nature corresponds to a Python data type."
    mspy "Identify it. Use the right logic to neutralize it. {w}Let’s begin."

    hide mspython 
    hide luna
    hide cyra
    with dissolve

    #String leech shows
    $ red_effect()
    show screen info_box("Bug #1 – The String Leech") with dissolve
    play sound "glitch_sound.ogg"
    show bug at top_left_space with dissolve #change location later

    "A pulsating worm of text hovers midair, echoing 'ErrorErrorError...'"

    mspy "This one loops through text patterns. Use string operations to break the cycle."
    mspy "Remember: in Python, multiplying a string repeats it or removes it."

    show cyra neutral at right with dissolve
    cyra "Like {color=#00ffff}print('LOL' * 3){/color} — my favorite debugging noise."
    show cyra neutral2

    show kai happy at center with dissolve:
        xzoom -1.0
    kai "You would weaponize sarcasm."

    "Type the missing syntax!!"
    "How will you handle the String Leech?"

    #1Bug String Leech code input----------------------------------------------------------------  
    call string_leech from _call_string_leech
    hide screen info_box with dissolve
    hide bug with dissolve

    #bug 2---------------
    $ red_effect()
    show screen info_box("Bug #2 – The Numeric Ogre") with dissolve
    play sound "glitch_sound.ogg"
    show bugOgre at top_left_space with dissolve

    show kai surprised2
    show cyra neutral2
    "A massive creature stomps in, chanting: 'Divide by Zero! Divide by Zero!'"
    show kai neutral2

    mspy "Arithmetic operators — +, -, *, / — handle calculations."
    mspy "But dividing by zero causes catastrophic failure. Proceed carefully."

    mc "So… never trust a zero. Got it."
    show cyra neutral
    cyra "Or trust Kai with math."
    show kai embarassed
    kai "Funny. Let’s see if you still laugh after you lose the leaderboard."
    show cyra neutral2
    show kai neutral2
    mspy "FOCUS! Students."

    "Construct the right code to defeat the Numeric Orge!"
    "How do you calm the Numeric Ogre?"

    #--------------Numberic Org ----------------------
    call numeric_org from _call_numeric_org
    hide screen info_box
    hide bugOgre
    with dissolve

    #bug 3---------------
    $ red_effect()
    show screen info_box("Bug #3 – The List Hydra") with dissolve
    play sound "glitch_sound.ogg"
    show bugHydra at top_left_space with dissolve

    "Three heads emerge, hissing binary streams."

    mspy "Lists are mutable — you can modify them."
    mspy "To contain the Hydra, use {color=#00ffff}.append(){/color} to add each head into your list."
    show cyra surprised
    show kai neutral2
    cyra "So… we’re making a 'Hydra shopping list'? Nice."
    show cyra neutral2

    hide bugHydra
    hide screen info_box
    with dissolve

    mspy "Example:"
    show ep2-scn3-txt1 at top_left_space with dissolve
    mspy "The append() method adds items to the end of a list."

    hide ep2-scn3-txt1 with dissolve

    $ red_effect()
    show screen info_box("Bug #3 – The List Hydra") with dissolve
    play sound "glitch_sound.ogg"
    show bugHydra at top_left_space with dissolve

    #List Hydra call here-----------------------------------------------------------------------------------------------------
    "How do you trap the Hydra?"
    "Append the \"heads\" to seal away the \"Hydra\""

    call list_hydra from _call_list_hydra
    hide screen info_box with dissolve
    hide bugHydra with dissolve
    
    #bug 4------------
    $ red_effect()
    show screen info_box("Bug #4 – The Boolean Phantom") with dissolve
    play sound "glitch_sound.ogg"
    show bugPhantom at top_left_space with dissolve

    show kai surprised
    show cyra surprised
    "A ghost flickers in and out, whispering 'True… False…'"
    show kai neutral2
    show cyra neutral2
    mspy "Booleans control logic flow. Use {color=#00ffff}if{/color} statements to make code decisions."
    show kai neutral
    kai "So, we’re exorcising with logic? My kind of fight."
    show kai neutral2
    show cyra happy
    cyra "This will be easy!"
    mc "Got it. Let's Go!"
    show cyra neutral2

    #Bug Phantom call here--------------------------------------
    "What code do you use to reveal the truth?"
    call bug_phanthom from _call_bug_phanthom
    hide bugPhantom with dissolve
    hide screen info_box with dissolve


    # Final Boss----------
    show cyra neutral2
    show kai neutral2
    $ red_effect()
    show screen info_box("Bug #5 Final Boss: The Void Entity") with dissolve
    play sound "glitch_sound.ogg"
    show bugVoid at top_left_space with dissolve

    "The entire room shakes. A massive shadow rises — pure black code swirling like smoke."

    mspy "This one... is made of NoneType — the absence of data. Only creation — something from nothing — can undo it."
    show cyra neutral
    cyra "That’s… deep. We code meaning into nothingness?"
    show cyra neutral2
    mc "Let’s give it something real."

    "What do you assign to restore balance?"
    #Bug Void call here---------------------------------------
    call void_bug from _call_void_bug
    hide bugVoid with dissolve
    hide screen info_box with dissolve

    # End of battle simulation------------------------------
    stop music fadeout 2.0 #fight music stop here
    #play music "ending_theme.ogg" fadein 2.0  #start ending music here

    scene black with fade

    scene classroom with dissolve
    drIntercom "Simulation success. Excellent teamwork, Debuggers."
    show mspython happy at center
    with dissolve
    mspy "You’ve done well. Every operation, every decision — builds the foundation of your code."

    hide mspython with dissolve

    show cyra happy-notab at right with dissolve
    cyra "Next time, I call dibs on the final blow."
    show kai neutral at left with dissolve
    kai "You? You barely handled one Boolean ghost."
    show kai neutral2
    show cyra neutral-notab
    cyra "Says the guy who screamed when the Hydra burped."
    show cyra neutral2-notab
    show luna happy2 at center with dissolve
    luna "Aww, you’re all such cute bugs yourselves!"
    show astra neutral at slightleft with dissolve:
        xzoom -1.0
    astra "The real fun starts when the logic turns against you. Remember that."
    show astra neutral2
    show mira sad at slightright with dissolve
    mira "{size=-5}Logic… turning against us…?{/size}"
    mc "You said something Mira?"
    show mira neutral
    mira "Nothing. {w}I’m fine."
    show mira neutral2

    mspyIntercom "Team Debugger — class dismissed. Tomorrow, we learn about Operators and If/Else."

    scene black
    with fade
    pause 1.0

#SCENE 4
    scene cafeteria #lounge
    with dissolve

    # play music "lounge_theme.ogg" fadein 2.0
    play music "opening.ogg"

    "Soft neon glows fill the Debuggers' Lounge, the hum of holographic screens buzzing in the background."
    "Steam rises from mugs of synthe-tea. Outside, the city flickers like a living circuit board under the digital sunset."
    "After surviving the Glitch Zone, the team finally breathes."

    show luna sad at center with dissolve
    luna "Uggggh… my brain feels like it’s been formatted twice and recompiled with extra exhaustion."
    show cyra neutral-notab at right with dissolve
    cyra "You did great, Luna. Especially when you tried to high-five the Boolean ghost."
    show cyra happy-notab
    cyra "Very brave. Very stupid, but brave."
    show cyra happy2-notab
    show luna surprised3
    luna "Hey! It looked friendly until it tried to eat my code history!"
    show luna neutral2
    show kai neutral at left with dissolve
    kai "That’s what happens when you try to debug with pure optimism."
    show kai neutral2

    mc "Worked better than your '{i}Punch the Hydra until it obeys{/i}' plan."
    show kai happy
    kai "It was experimental logic. Sometimes violence *is* the answer{w} ..in pseudocode."
    show cyra neutral-notab
    cyra "Yeah, sure, Mr. 'divide by zero.' Real smooth operator there."
    show kai angry2
    kai "Tch. Low blow, Byte."
    show cyra happy-notab
    show luna happy-nostar
    "Laughter fills the lounge, echoing off the neon-lit walls."

    show kai neutral2
    show mira neutral at slightright with dissolve
    mira "I… I’m just glad everyone’s okay. The system was on the verge of collapse." 
    show mira sad
    mira "If we’d delayed even a second longer, the Glitch could’ve—"
    show mira sad2
    "She pauses, catching herself before overanalyzing again."
    mc "You held the whole simulation together, Mira. You saved us."
    show mira surprised
    mira "O-oh… I just followed the algorithm. Anyone could’ve done it."

    show astra neutral at slightleft with dissolve:
        xzoom -1.0
    astra "Not anyone. I saw your override code."
    astra "That wasn’t textbook. You rewrote the logic mid-run."
    show astra neutral2
    show mira surprised-blush
    mira "It—It was just a… reflex. A patch job. Nothing special."
    show mira surprised2-blush
    "Her voice wavers slightly — her eyes flicker faintly with a red glitch, almost imperceptible."
    show luna surprised2
    luna "Whoa, Mira! Your eyes just did the glow thing! So cool!"
    show mira sad
    mira "Just—just reflection from the holo screen. I’m fine."
    show mira sad2

    pause 1.0

    show cyra neutral-notab
    cyra "You should’ve seen your face during the fight, [name]." 
    cyra "That ‘String Leech’ almost had you — until you went full coder mode."
    show cyra happy-notab
    cyra "Not bad for a rookie."
    show cyra happy2-notab
    show luna neutral2
    mc "Guess I’m starting to get the hang of this Python thing."
    mc "(pauses, looking around) {p}And maybe… getting to know this team too."

    show kai neutral
    kai "Don’t get comfortable yet. Next round, I’m taking the top score back."
    kai "No hard feelings."
    show cyra neutral-notab
    cyra "You mean when I take it first."
    show kai happy
    kai "Dream on."
    show luna neutral
    luna "(Throws a chip bag) {p}Ship yourselves already!"
    show luna neutral2

    show cyra surprised-notab
    cyra "Wha—?!"
    show kai surprised
    kai "What are you talking about?!"
    show mira happy2
    show luna happy-nostar
    show astra happy2
    "Everyone bursts into laughter — except Mira, who gives a faint, strained smile."
    show astra happy
    astra "Some things never change. Team chaos, through and through."

    hide kai
    hide cyra
    hide luna
    hide mira
    hide astra
    with dissolve

    # Ms. Py Thon Hologram Appears
    play sound "hologram.ogg"
    show mspython happy at center with dissolve:
        subpixel True alpha 0.79 additive 0.22 blur 0.0 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(0.08)*HueMatrix(576.0) 

    mspy "Excellent work today, Debuggers. Your teamwork was… mostly functional."
    show mspython happy2
    show luna happy2 at slightright with dissolve
    luna "(salutes dramatically) Mission accomplished, Ms. Python! No existential crises left behind!"
    show mspython happy
    mspy "Tomorrow’s module will be Operators and Conditional Statements. Prepare your minds."
    mspy "We will learn how the simplest symbols {w}{=code}— +, -, *, /, and, or, not{/code}{w} — can reshape digital reality itself."

    hide mspython with dissolve

    show cyra sad-notab at right with dissolve
    cyra "Oh great. Math with consequences."
    show kai sad at left with dissolve
    kai "Oh joy. Logic puzzles. My favorite way to suffer."
    show luna sad
    luna "Oh no… homework."
    show mira neutral at center with dissolve
    mira "{size=-5}Logic defines fate. Every choice… changes the outcome.{/size}"
    show astra neutral2 at slightleft with dissolve:
        xzoom -1.0
    "Astra watches Mira carefully."
    show astra neutral with dissolve
    astra "Hmm. Spoken like someone who’s seen both sides of the code."
    show mira surprised
    mira "I—I didn’t mean—"
    show mira neutral
    mira "Never mind."
    show mira neutral2

    show astra neutral2
    show kai sad2
    show cyra sad2-notab
    show luna sad2
    "The atmosphere shifts — subtle tension beneath the glow. [name] looks between them, uneasy."
    "What will you do?"

    # --- Optional Interactions ---
    menu:
        
        "Talk to Cyra":
            hide kai 
            hide astra 
            hide mira 
            hide luna
            show cyra neutral2-notab at center with move
            mc "You really kept your cool out there. You always this confident?"
            show cyra happy-notab
            cyra "(leaning closer) {p}Confidence is just caffeine and chaos, rookie. {w}But… maybe I just wanted to impress someone."
            show cyra blush-notab
            "She laughs softly, brushing her hair aside."

            play sound "right_answer.ogg"
            $ change_confidence(+1)
            "{=gold}Syntax Confidence +1{/=gold}"
            play sound "right_answer.ogg"
            $ change_cyraAffection(+1)
            "{=gold}Cyra’s Affection +1{/=gold}"
            mc "(grinning) {p}Mission accomplished."

        "Talk to Kai":
            hide cyra
            hide astra
            hide luna
            hide mira
            show kai neutral2 at center with move
            mc "You were solid out there. {w}Even when the Hydra bit your arm."
            show kai happy
            kai "It’s fine. I’ve had worse bugs. But don’t think I’ll let you beat me again."
            show kai happy2
            kai "Next time, I’m going all in. No mercy coding."

            play sound "right_answer.ogg"
            $ change_confidence(+1)
            "{=gold}Syntax Confidence +1{/=gold}"
            play sound "right_answer.ogg"
            $ change_kaiAffection(+1)
            "{=gold}Kai’s Affection +1{/=gold}"
            mc "You’re on, Kai."

        "Talk to Mira":
            hide cyra
            hide astra
            hide luna
            hide kai
            show mira neutral2 at center 
            with dissolve
            mc "You seemed worried during the mission. Everything okay?"
            show mira sad
            mira "(looking distant) {p}Just… residual static. Sometimes I see patterns where there shouldn’t be any. {w}It’s probably nothing."
            "Her datapad flickers with corrupted code for a split second — {color=#ff4444}ACCESS DENIED{/color}."
            mc "(concerned) Mira…?"
            show mira happy
            mira "(forcing a smile) I’m fine, really. Just tired."

            play sound "error_sound2.ogg"
            $ change_confidence(-1)
            "{=red}Syntax Confidence -1{/=red}"
            "You feel a strange unease — like something in the code just shifted."

    # --- Glitch Sequence ---

    scene cafeteria
    with dissolve

    
    show cafeteria with dissolve:
        subpixel True matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(-0.54)*HueMatrix(0.0)

    scene cafeteria
    with dissolve

    "Suddenly, the lounge lights flicker."
    play sound "glitch_sound.ogg"
    "The holo-screen flashes — a shadowed figure appears, typing rapidly on a terminal. The image distorts before vanishing."

    show luna surprised2 at center with dissolve
    luna "(sits up) {p}Uh… anyone else see that?"
    show cyra sad-notab at right with dissolve
    cyra "Probably just lag from the system reboot."
    show astra sad at slightleft with dissolve:
        xzoom -1.0
    astra "(low voice, almost to herself) {p}No… that was intentional. {w}Someone’s inside the code."
    show mira sad at slightright with dissolve
    mira "(gripping her datapad) {p}...We should go. It’s late."
    show kai neutral at left with dissolve
    kai "Agreed. Tomorrow’s going to be a long one."
    mspyIntercom "Rest well, Debuggers. Tomorrow — we calculate destiny."

    hide kai
    hide luna
    hide astra
    hide mira
    hide cyra
    with dissolve

    mc "Calculate destiny, huh?"
    mc "(smiles faintly) {p}Bring it on."

    stop music fadeout 3.0
    scene black with fade
    "To be continued..."
    return
