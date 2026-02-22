label episode3:
# SCENE 1
    scene black
    with dissolve

    show text "{=title}Episode 3 - Operators of Destiny: The Logic War Begins{/title}" at truecenter with dissolve
    pause 2
    hide text with fade
    
    scene classroom
    with dissolve

    play music "audio/class.ogg" fadein 0.5 volume 0.3
    
    show doctorbyte neutral at center with dissolve
    dr "Welcome, young coders. Today, your logic will be tested."
    show doctorbyte happy
    dr "Ms. Py Thon, would you do the honors?"

    hide doctorbyte
    show mspython happy zorder 3 at center 
    with dissolve
    mspy "Of course, Doctor."
    show mspython neutral
    mspy "Today’s lesson: {b}Operators{/b}. {w}They allow us to perform calculations and comparisons."
    mspy "In code, they define how data interacts."

    show mspython neutral2
    mc "Sounds easy enough… but with Ms. Py Thon teaching, I’m sure there’s a twist."

    show cyra neutral zorder 1 at right with dissolve
    cyra "Don’t worry, rookie. If you fail, I’ll tutor you." 
    show cyra happy
    cyra "If you treat me that is."

    show cyra happy2
    show kai happy at left with dissolve
    kai "Or maybe I’ll do it first. Gotta keep my rival sharp."

    show mspython neutral
    mspy "Let’s start with arithmetic operators." 
    mspy "Try this example."

    hide kai with dissolve
    show mspython neutral2 at slightright with move
    show ep3-scn1-txt1 at top_left_space
    with dissolve

    menu:
        "15":
            play sound right_answer
            show mspython happy
            mspy "Excellent! The {=code}*{/code} operator multiplies values."
            show cyra happy
            cyra "See? Total prodigy."
        "8":
            call ep3Scn1QuestionWrong from _call_ep3Scn1QuestionWrong
        "53":
            call ep3Scn1QuestionWrong from _call_ep3Scn1QuestionWrong_1

    show mspython neutral
    mspy "Remember you can also use other operators in here as well like {=code}+, /, - ,{/code} and more {w}as long as its basic calculation."
    mspy "If its complex you have to set the code for that as well, other ERROR!"

# SCENE 2
    scene classroom #training hub
    with dissolve

    show kai neutral at center with dissolve
    kai "Hey, [name]. Let’s see if you’re really getting it."

    show kai neutral2
    show ep3-scn2-txt1 at top_left_space
    with dissolve

    menu:
        "2":
            play sound right_answer
            show kai happy
            kai "Hmph… not bad. You know floor division."
            show cyra happy at right with dissolve
            cyra "Looks like someone’s {cps=20}impressed~"
            show kai embarassed
            kai "I’m not!"
            show cyra happy2
        "2.5":
            play sound error_sound1
            show kai neutral
            kai "Nah, rookie. {=code}//{/code} gives whole numbers only. Better remember that before your next duel."
        "0":
            play sound error_sound1
            show kai neutral
            kai "Nah, rookie. {=code}//{/code} gives whole numbers only. Better remember that before your next duel."
    
    show kai neutral2
    show luna happy at slightright with dissolve
    luna "Ooh, I wanna play too! Try mine!"

    hide ep3-scn2-txt1
    show ep3-scn2-txt2 at top_left_space
    with dissolve

    menu:
        "0":
            play sound right_answer
            hide cyra
            show astra neutral at right
            with dissolve
            astra "I guess you really are getting the hang of it, nice one [name]."
        "3":
            play sound error_sound1
            show luna sad
            luna "Nooo! That bug escaped! {=code}%%{/code} gives the remainder, silly!"
        "2":
            play sound error_sound1
            show luna sad
            luna "Nooo! That bug escaped! {=code}%%{/code} gives the remainder, silly!"

# SCENE 3
    scene classroom # code chamber
    with dissolve

    show mspython neutral at center with dissolve
    mspy "Let’s raise the stakes, class."
    mspy "{b}Operators{/b} give power — but combine them with {b}conditions{/b}, and you gain control."

    mspy "In Python, {i}conditional statements{/i} let us make decisions." 
    mspy "The most common one is the {=code}if{/code} statement. {w}It checks whether something is true."

    show mspython neutral2
    show cyra neutral at right with dissolve
    cyra "(leans back in her chair, smirking) {w}{p}So it’s like… coding with attitude. If it’s true, do this. If not, do something else."

    show cyra neutral2
    show kai neutral at left with dissolve
    kai "Sounds like my kind of logic. All or nothing."

    show kai neutral2
    show mira neutral at slightright with dissolve
    mira "Um… that’s like… {w}if something’s true, it does one thing, if not, another?"

    show mira neutral2
    show mspython happy
    mspy "Exactly, Mira. Let’s try this together."

    hide mira
    hide kai
    hide cyra
    with dissolve

    show ep3-scn3-txt1 at top_left_space
    with dissolve

    show mspython neutral at slightright with move
    mspy "Here, the condition {=code}x > 5{/code} is evaluated. {w}If it’s {b}True{/b}, Python runs the first block — printing {i}‘Big number!’{/i}. {w}Otherwise, the {=code}else{/code} block runs."
    mspy "So what do you think it will print?"

    menu:
        "Big number!":
            play sound "right_answer.ogg"
            show mira happy at right with dissolve
            mira "It printed Big number! because ten is greater than five!"
            show mira happy2
            show mspython happy
            mspy "Well reasoned, Mira. You’re starting to think like a coder."
            hide mira with dissolve
            show mspython happy2 
        "Small number!":
            call ep3Scn3QuestionWrong from _call_ep3Scn3QuestionWrong
        "Error":
            call ep3Scn3QuestionWrong from _call_ep3Scn3QuestionWrong_1

    show luna neutral at right with dissolve
    luna "Conditional powers are like doors! Only one opens if your statement is true! The others stay locked!"

    hide ep3-scn3-txt1
    show ep3-scn3-txt2 at top_left_space
    with dissolve

    show luna neutral2
    show mspython neutral
    mspy "Precisely. You can even add more doors using {=code}elif{/code}, short for {b}else if{/b}."
    mspy "This code checks multiple possibilities. Try to picture the logic flow — {w}one condition at a time."
    show mspython neutral2

    hide mspython
    hide luna 
    show kai happy at right:
        xzoom -1.0
    with dissolve

    kai "So, it’s a test of judgment — like choosing the right move in battle."

    show cyra neutral-notab at center:
        xzoom -1.0
    with dissolve
    cyra "Let’s hope you pick better than last time, {i}rookie coder{/i}."
    show cyra neutral2-notab
    mc "Just watch me."

    stop music fadeout 0.5

    scene black
    with dissolve
    pause 1.0

# SCENE 4
    scene arena
    play sound "glitch_sound.ogg"
    $ red_effect()
    show red
    with dissolve

    play music "audio/battle-silent_struggle.ogg" fadein 0.5 volume 0.3
    
    show luna surprised at center with dissolve
    luna "Uh-oh! A Logic Bug invaded the system again! It’s bouncing through code like a broken loop!"

    show cyra neutral-notab at right with dissolve
    cyra "Looks like class just turned into a boss battle."

    show cyra neutral2-notab
    show kai neutral at left with dissolve
    kai "Good. I was getting bored of theory."

    hide kai
    hide cyra
    hide luna
    with dissolve

    show mspython neutral at right with dissolve
    mspy "Class, this is your next lesson — and your first true test."
    mspy "The Logic Bug thrives on flawed operators and weak conditions." 
    mspy "You must counter it using if-else logic."

    show mspython neutral2
    show doctorbyte neutral at left with dissolve
    dr "Let’s see if your logic holds under pressure." 
    dr "Remember — one wrong operator, and it strikes back."

    hide mspython
    hide doctorbyte
    with dissolve

    hide red
    show bug2 at top_right_space
    play sound "glitch_sound.ogg"
    $ red_effect()

    "The Logic Bug materializes — a dark swirling mass of red binary code, screeching in distortion."

    mspy "Remember, operators are the tools that let us manipulate data. Let’s test your aim with arithmetic and comparison operators."

    show ep3-scn4-txt1 at top_left_space
    with dissolve

    mspy "Observe: {=code}a * b{/code} means multiplication. The {=code}>={/code} checks if the product is {b}greater than or equal to 20{/b}. {w}{p}Now, [name] what’s the correct output?"

    menu:
        # extend ""

        "Strike Successful!":
            play sound "right_answer.ogg"
            mc "It’s greater than 20 — so, Strike Successful!"
            play sound "punch_sound2.ogg"
            with hpunch
            mspy "Excellent. That’s True logic in motion."
            cyra "I love watching you in action, [name]. {w}You make math look… {w}charming."
            kai "Tch… don’t let it get to your head."
            luna "Boom! The bug just lost 50 HP! Logic laser activated!"
            mira "Wow… you’re really good at this…"
        "Attack Failed!":
            play sound "glitch_sound.ogg"            
            $ red_effect()
            "Virus" "Hissss! I feed on mistakes!"
            mspy "Focus. {w}The condition {b}a * b equals 21 — that’s greater than 20{/b}." 
            mspy "You must always test your expressions carefully."
            kai "You call that logic? You’re better than this."
            cyra "Don’t sweat it. Even pros debug."
            luna "Let’s fix the bug {i}before{/i} it eats the system!"

    mspy "The {=code}if{/code} statement checks if a condition is True. {w}If not, the {=code}else{/code} part activates." 
    mspy "Think of it as a decision tree — your code chooses based on truth or falsehood."
    dr "And so, does life. Every choice branches your future."

    hide ep3-scn4-txt1
    with dissolve

    mspy "Next, let’s see how you fare with logical operators. Remember-"
    mspy "{color=#81f08aff}{b}and{/b}{/color} means {b}both{/b} conditions must be {b}True{/b}. {w}{p}{color=#81f08aff}{b}or{/b}{/color} means at least {b}one{/b} condition must be {b}True{/b}.{w}{p}{color=#81f08aff}{b}not{/b}{/color} {b}reverses{/b} the condition."
    
    show ep3-scn4-txt2 at top_left_space
    with dissolve

    mspy "[name], analyze this. The character is alive, but has no energy. {w}What’s the output?"

    menu:
        # extend ""

        "Ready!":
            play sound "error_wrong.ogg"
            $ red_effect()
            hide bug2 with dissolve
            hide ep3-scn4-txt2 with dissolve
            show luna surprised at slightright with dissolve
            luna "Uh-oh! You fainted! I’ll respawn you!"
            show mspython angry at center with dissolve
            mspy "Incorrect logic means lost rounds, [name]." 
            mspy "Study how and evaluates conditions."
            show mspython angry2
            show doctorbyte sad at slightleft with dissolve
            dr "The smallest error in logic can topple the mightiest code."
            show doctorbyte sad2

            show cyra surprised-notab at right with dissolve
            cyra "Hey, deep breath. We’ll debug together next round."
            show cyra surprised2-notab
            show kai neutral at left with dissolve
            kai "Try thinking before typing next time."

            hide kai
            hide cyra
            hide mspython
            hide doctorbyte
            hide luna
            with dissolve
            pause 1.0
            stop music fadeout 0.5

            show mira happy at center
            with dissolve
            mira "It’s okay… everyone makes mistakes…"
            show mira neutral
            mira "But mistakes have consequences."
            show mira happy2
            "..."
            pause 1.0
            
        "Low Resources!":
            play sound "right_answer.ogg"
            mc "{=code}hp > 0{/code} is True, but {=code}energy > 0{/code} is False — since both need to be True{w}, it’s Low Resources!"
            with hpunch
            play sound "punch_sound1.ogg"
            hide bug2 with dissolve
            hide ep3-scn4-txt2 with dissolve
            show mspython happy at center with dissolve
            mspy "Excellent deduction! Logical precision, that’s the coder’s blade."
            show mspython happy2
            show luna happy-nostar at slightright with dissolve
            luna "Ha! The bug’s running in circles!"
            show cyra happy-notab at right with dissolve
            cyra "Nice one. You’re sharper than I expected."
            show cyra happy2-notab
            show kai happy at left with dissolve
            kai "Hmph. Good catch, rookie."
            show doctorbyte neutral  at slightleft with dissolve
            dr "Logic stabilized. The Arena holds steady — {w}for now."

            hide kai
            hide cyra
            hide mspython
            hide doctorbyte
            hide luna
            with dissolve

            stop music fadeout 0.5
            pause 1.0
            
            show mira sad at center
            with dissolve
            mira "{size=25}You’re all so proud of your logic… {w}{cps=20}but even logic can be rewritten.{/size}"
            show mira sad2
            "Her tone is low — almost unheard beneath the static."
            pause 1.0

    scene black
    with fade

    pause 1.0

    scene arena
    with dissolve

    play music "audio/class.ogg" fadein 0.5 volume 0.3

    show screen info_box("Reminder: Operators") with dissolve
    show mspython neutral at center with dissolve
    mspy "Operators are the foundation of all calculations:"

    show ep3-scn4-txt3 at top_left_space
    with dissolve

    show mspython neutral at slightright with move
    mspy "Combine them with {=code}if{/code} and {=code}else{/code} to make choices in your code."
    mspy "In Python — just like in life — one wrong condition can change everything."

    show mspython neutral2
    show doctorbyte neutral at right with dissolve:
        xzoom -1.0 

    dr "Remember those words, students. You’ll need them for what’s coming next."
    hide screen info_box
    stop music fadeout 0.5

# SCENE 5
    scene black
    with fade

    pause 1.0

    scene classroom
    with dissolve

    play music "audio/opening.ogg"
    show mira happy at center with dissolve
    mira "You were amazing out there, [name]… {w}I mean, {w}logically speaking!"

    show mira happy2
    show luna happy-nostar at slightright with dissolve
    luna "Buggy McByteFace is now tamed!"

    show cyra happy-notab at right with dissolve
    cyra "Told you you’d look good in combat mode."

    show cyra happy2-notab
    show kai happy at left with dissolve
    kai "Hmph. Don’t let that praise get to your head."

    show kai happy2
    show astra sad at slightleft with dissolve:
        xzoom -1.0
    astra "(Walking Past){p}You did fine. But logic isn’t everything…" 
    show astra sad
    astra "Trust can fail too."

    show astra sad2
    mc "Operators, logic, teamwork… {w}maybe this academy’s teaching me more than just code."

    stop music fadeout 0.5
    scene black
    with dissolve
    pause 1.0

# SCENE 6
    scene cafeteria
    with dissolve

    play music "main-menu.ogg"

    "The cafeteria is dimly lit. Holographic menus flicker above the tables. A few students linger, typing quietly."
    "[name] enters, still buzzing from the intense coding session earlier."

    show cyra happy2-notab at slightright
    with dissolve

    "You saw Cyra grinning and waving at you at a table."
    show cyra happy-notab
    cyra "Hey, [name]! Over here!"
    cyra "I saved you a seat… and maybe some fries. {w}Maybe."
    mc "Maybe? You mean you already ate half of it."
    show cyra neutral-notab
    cyra "Correction: {cps=20}seventy-five percent."
    show cyra surprised-notab
    cyra "But in my defense, debugging burns calories!"

    "Kai slides his tray onto the table with a smirk."
    show kai happy at slightleft
    with dissolve
    kai "More like you burned the code. I saw your logic statement loop five times before you fixed it."

    show cyra angry-notab
    cyra "Hey, at least my loops {i}looped!{/i} Yours froze the whole simulation!"
    show cyra angry2-notab
    mc "(chuckles) {p}Should I step in before this turns into a logic war?"

    show cyra surprised2-notab at right with move
    show kai surprised2 at left with move
    show luna happy at rise_up
    with dissolve
    luna "Too late! Logic war initiated! {w}Beeep- Boop- Bap!"
    luna "If (Kai > Cyra): {p}{space=30}declare_winner(Kai) {p}else: {p}{space=30}declare_winner(Cyra)"

    show kai neutral
    kai "Luna, that’s not even how comparisons work."
    show luna neutral
    luna "Tell that to my soda, it’s glowing blue for {i}false!{/i}"

    show kai happy2
    show luna happy-nostar
    show cyra happy2-notab
    "They all laugh. Ms. Py Thon enters quietly, holding a tablet. She seems serene, but observant."
    show mspython happy at slightright with dissolve
    mspy "Still awake, I see. Perhaps I should add a {i}‘Sleep()’{/i} function to your schedules."
    mc "(smiling) {p}We were… reviewing operators. In our own way."
    mspy "Ah, the best learning happens when you forget you’re learning."
    "She glances at the group, fondly"
    mspy "Remember — logic and emotion don’t have to conflict. The strongest code is balanced, just like the strongest hearts."
    show mspython happy2

    if cyraAffection >= 3:
        show cyra blush-notab
        "Cyra looks at [name] with a soft smile, brushing a strand of hair behind her ear."
    
    show cyra happy-notab
    cyra "Guess that means even bugs can teach us something, huh?"
    show kai happy
    kai "Yeah — like how not to {i}write{/i} your code."
    show cyra angry2-notab
    mc "(laughs) {p}I think we all learned that one the hard way."
    "Ms. Py Thon turns toward the window, the night sky reflected on her tablet screen. Her voice turns thoughtful."
    
    stop music fadeout 1.0
    
    show mspython neutral
    mspy "There are… darker codes out there. Ones written with no balance." 
    mspy "Promise me you’ll all keep learning — not just for power, but for purpose."
    hide mspython with dissolve

    show kai neutral2
    show cyra neutral2-notab
    show luna neutral2
    "The group quiets for a moment. The wind hums through the vents."
    show cyra sad2-notab
    show luna sad2
    "On their faces reads — curiosity, camaraderie, and just a hint of unease."

    show luna neutral
    luna "Sooo… {w}who’s up for another mini-game before bed?"

    play music "main-menu.ogg"
    show luna bleh
    luna "Maybe a ‘Guess the Operator’ challenge?"
    show kai happy
    kai "Count me in. I’ll prove I can out-code Cyra any day."
    show cyra happy-notab
    cyra "Bring it, Voltage Boy."
    mc "Let’s see who short-circuits first."
    "They all laugh again, the tension fading — but as the camera pans to the window, a faint flicker of code appears reflected in the glass." 
    play sound "glitch_sound.ogg"
    "A pair of glowing digital eyes blink once, then vanish into static..."

    nvl clear
    n "{b}{size=+10}LESSON SUMMARY{/size}{/b}"
    n "{=code}+ - * / %% // **{/code} {space=40}Arithmetic Operators"
    n "{=code}> < >= <= == !={/code} {space=40}Comparison Operators"
    n "{=code}and, or, not{/code} {space=40}Logical Operators"
    n "{=code}if, elif, else{/code} {space=40}Conditional Decisions"

    stop music fadeout 1.0

    scene black
    with dissolve
    nvl clear
    return


label ep3Scn1QuestionWrong:
    play sound error_sound1
    show mspython sad
    mspy "Incorrect. Multiplication uses {=code}*{/code}, not concatenation."
    show mspython neutral
    mspy "Don’t worry, we’ll fix that logic."
    return

label ep3Scn3QuestionWrong:
    play sound "error_sound1.ogg"
    show astra neutral at right with dissolve
    astra "Careless logic, rookie."
    astra  "x is 10 — greater than 5. Easy math."
    show astra neutral2
    show mspython sad
    mspy "Logic errors can be fixed… but only if you observe your conditions clearly. Always think before you code."
    show mspython sad2
    hide astra with dissolve
    return