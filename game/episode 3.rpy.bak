label episode3:
# SCENE 1
    scene black
    with dissolve

    show text "Episode 3 - Operators of Destiny: The Logic War Begins" at truecenter with dissolve
    pause 2
    hide text with fade
    
    scene classroom
    with dissolve

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

    mc "Sounds easy enough… but with Ms. Py Thon teaching, I’m sure there’s a twist."

    show cyra neutral zorder 1 at right with dissolve    #teasing
    cyra "Don’t worry, rookie. If you fail, I’ll tutor you. {w}If you treat me that is"

    show kai neutral at left with dissolve      #snickering
    kai "Or maybe I’ll do it first. Gotta keep my rival sharp."

    mspy "Let’s start with arithmetic operators. Try this example:"

    hide kai
    show mspython at slightright with move
    show ep3-scn1-txt1 at top_left_space
    with dissolve

    menu:
        "15":
            show mspython happy
            mspy "Excellent! The {=code}*{/code} operator multiplies values."
            show cyra happy
            cyra "See? Total prodigy."
        "8":
            jump ep3Scn1QuestionWrong
        "53":
            jump ep3Scn1QuestionWrong

    show mspython neutral
    mspy "Remember you can also use other operators in here as well like {=code}+, /, - ,{/code} and more {w}as long as its basic calculation."
    mspy "If its complex you have to set the code for that as well, other ERROR!"

# SCENE 2
    scene classroom #training hub
    with dissolve

    show kai neutral at center with dissolve
    kai "Hey, [name]. Let’s see if you’re really getting it."

    # show kai neutral2 at slightright with move
    show ep3-scn2-txt1 at top_left_space
    with dissolve

    menu:
        "2":
            show kai neutral
            kai "Hmph… not bad. You know floor division."
            show cyra neutral at right with dissolve
            cyra "Looks like someone’s {cps=20}impressed~"
            show kai angry
            kai "I’m not!"
            show kai neutral
        "2.5":
            kai "Nah, rookie. {=code}//{/code} gives whole numbers only. Better remember that before your next duel."
        "0":
            kai "Nah, rookie. {=code}//{/code} gives whole numbers only. Better remember that before your next duel."
    
    show luna neutral at slightright with dissolve
    luna "Ooh, I wanna play too! Try mine!"

    hide ep3-scn2-txt1
    show ep3-scn2-txt2 at top_left_space
    with dissolve

    menu:
        "0":
            hide cyra
            show astra neutral at right
            with dissolve
            astra "I guess you really are getting the hang of it, nice one [name]"
        "3":
            show luna sad
            luna "Nooo! That bug escaped! {=code}%%{/code} gives the remainder, silly!"
        "2":
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

    show cyra neutral at right with dissolve
    cyra "(leans back in her chair, smirking) {w}{p}So it’s like… coding with attitude. If it’s true, do this. If not, do something else."

    show kai neutral at left with dissolve
    kai "Sounds like my kind of logic. All or nothing."

    show mira neutral at slightright with dissolve
    mira "Um… that’s like… {w}if something’s true, it does one thing, if not, another?"

    show mspython happy
    mspy "Exactly, Mira. Let’s try this together."

    hide mira
    hide kai
    hide cyra
    show ep3-scn3-txt1 at top_left_space
    with dissolve

    show mspython neutral
    mspy "Here, the condition {=code}x > 5{/code} is evaluated. {w}If it’s {b}True{/b}, Python runs the first block — printing {i}‘Big number!’{/i}. {w}Otherwise, the {=code}else{/code} block runs."
    mspy "So what do you think it will print?"

    menu:
        "Big number!":
            show mira at right with dissolve
            mira "It printed Big number! because ten is greater than five!"
            show mspython happy
            mspy "Well reasoned, Mira. You’re starting to think like a coder."
            hide mira with dissolve
        "Small number!":
            call ep3Scn3QuestionWrong
        "Error":
            call ep3Scn3QuestionWrong

    show luna at right with dissolve
    luna "Conditional powers are like doors! Only one opens if your statement is true! The others stay locked!"

    hide ep3-scn3-txt1
    show ep3-scn3-txt2 at top_left_space
    with dissolve

    show mspython neutral
    mspy "Precisely. You can even add more doors using {=code}elif{/code}, short for {b}else if{/b}."
    mspy "This code checks multiple possibilities. Try to picture the logic flow — {w}one condition at a time."

    show kai happy at slightright with dissolve
    kai "So, it’s a test of judgment — like choosing the right move in battle."

    hide luna
    show cyra neutral at right 
    with dissolve
    cyra "Let’s hope you pick better than last time, {i}rookie coder{/i}."
    mc "Just watch me."

    scene black
    with dissolve
    pause 1.0

# SCENE 4
    scene arena
    $ red_effect()
    show red
    with dissolve
    
    show luna at center with dissolve
    luna "Uh-oh! A Logic Bug invaded the system again! It’s bouncing through code like a broken loop!"

    show cyra neutral at right with dissolve
    cyra "Looks like class just turned into a boss battle."

    show kai neutral at left with dissolve
    kai "Good. I was getting bored of theory."

    show luna at slightright with move
    show mspython at center with dissolve
    mspy "Class, this is your next lesson — and your first true test."
    mspy "The Logic Bug thrives on flawed operators and weak conditions. You must counter it using if-else logic."

    show doctorbyte at slightleft with dissolve
    dr "Let’s see if your logic holds under pressure. Remember — one wrong operator, and it strikes back."

    hide red
    show bug at top
    $ red_effect()

    "The Logic Bug materializes — a dark swirling mass of red binary code, screeching in distortion."

    hide mspython
    hide doctorbyte
    hide kai
    hide cyra
    hide luna
    with dissolve

    mspy "Remember, operators are the tools that let us manipulate data. Let’s test your aim with arithmetic and comparison operators."

    show ep3-scn4-txt1 at top_left_space
    with dissolve

    mspy "Observe: {=code}a * b{/code} means multiplication. The {=code}>={/code} checks if the product is {b}greater than or equal to 20{/b}. {w}{p}Now, [name] what’s the correct output?"

    menu:
        extend ""

        "Strike Successful!":
            mc "It’s greater than 20 — so, Strike Successful!"
            with hpunch
            mspy "Excellent. That’s True logic in motion."
            cyra "I love watching you in action, [name]. {w}You make math look… {w}charming."
            kai "Tch… don’t let it get to your head."
            luna "Boom! The bug just lost 50 HP! Logic laser activated!"
            mira "Wow… you’re really good at this…"
        "Attack Failed!":
            $ red_effect()
            "Virus" "Hissss! I feed on mistakes!"
            mspy "Focus. {w}The condition {b}a * b equals 21 — that’s greater than 20{/b}. You must always test your expressions carefully."
            kai "You call that logic? You’re better than this."
            cyra "Don’t sweat it. Even pros debug."
            luna "Let’s fix the bug {i}before{/i} it eats the system!"

    mspy "The {=code}if{/code} statement checks if a condition is True. If not, the {=code}else{/code} part activates." 
    mspy "Think of it as a decision tree — your code chooses based on truth or falsehood."
    dr "And so, does life. Every choice branches your future."

    hide ep3-scn4-txt1
    with dissolve

    mspy "Next, let’s see how you fare with logical operators. Remember-"
    mspy "{color=#81f08aff}{b}and{/b}{/color} means {b}both{/b} conditions must be {b}True{/b}. {w}{p}{color=#81f08aff}{b}or{/b}{/color} means at least {b}one{/b} condition must be {b}True{/b}.{w}{p}{color=#81f08aff}{b}not{/b}{/color} {b}reverses{/b} the condition."
    
    show ep3-scn4-txt2 at top_left_space
    with dissolve

    mspy "[name], analyze this. The character is alive, but has no energy. What’s the output?"

    menu:
        extend ""

        "Ready!":
            $ red_effect()
            hide bug with dissolve
            hide ep3-scn4-txt2 with dissolve
            show luna surprised at slightright with dissolve
            luna "Uh-oh! You fainted! I’ll respawn you!"
            show mspython neutral at center with dissolve
            mspy "Incorrect logic means lost rounds, [name]. Study how and evaluates conditions."
            show doctorbyte neutral  at slightleft with dissolve
            dr "The smallest error in logic can topple the mightiest code."
            show cyra surprised at right with dissolve
            cyra "Hey, deep breath. We’ll debug together next round."
            show kai neutral at left with dissolve
            kai "Try thinking before typing next time."

            hide kai
            hide cyra
            hide mspython
            hide doctorbyte
            hide luna
            with dissolve
            pause 1.0

            show mira neutral at center
            with dissolve
            mira "It’s okay… everyone makes mistakes… {w}but mistakes have consequences."
            
        "Low Resources!":
            mc "{=code}hp > 0{/code} is True, but {=code}energy > 0{/code} is False — since both need to be True{w}, it’s Low Resources!"
            with hpunch
            hide bug with dissolve
            hide ep3-scn4-txt2 with dissolve
            show mspython happy at center with dissolve
            mspy "Excellent deduction! Logical precision, that’s the coder’s blade."
            show luna happy at slightright with dissolve
            luna "Ha! The bug’s running in circles!"
            show cyra happy at right with dissolve
            cyra "Nice one. You’re sharper than I expected."
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
            pause 1.0
            
            show mira neutral at center
            with dissolve
            mira "{size=25}You’re all so proud of your logic… {w}{cps=20}but even logic can be rewritten.{/size}"
            "Her tone is low — almost unheard beneath the static."

    scene arena
    with dissolve

    show mspython neutral at center with dissolve
    mspy "Operators are the foundation of all calculations:"

    show ep3-scn4-txt3 at top_left_space
    with dissolve

    show mspython neutral at slightright with move
    mspy "Combine them with {=code}if{/code} and {=code}else{/code} to make choices in your code."
    mspy "In Python — just like in life — one wrong condition can change everything."

    # show doctorbyte neutral at right with dissolve flipped
    show doctorbyte neutral at right:
        xzoom -1.0 
    with dissolve

    dr "Remember those words, students. You’ll need them for what’s coming next."

# SCENE 5
    scene arena
    with dissolve

    show mira happy at right with dissolve
    mira "You were amazing out there, [name]… {w}I mean, {w}logically speaking!"

    show luna happy at slightright with dissolve
    luna "Buggy McByteFace is now tamed!"

    show cyra happy at center with dissolve
    cyra "Told you you’d look good in combat mode."

    show kai happy at slightleft with dissolve
    kai "Hmph. Don’t let that praise get to your head."

    show astra at left with dissolve
    astra "You did fine. But logic isn’t everything… trust can fail too."

    mc "Operators, logic, teamwork… {w}maybe this academy’s teaching me more than just code."

    scene black
    with dissolve
    pause 1.0

# SCENE 6
    scene cafe
    with dissolve

    "The cafeteria is dimly lit. Holographic menus flicker above the tables. A few students linger, typing quietly."
    "[name] enters, still buzzing from the intense coding session earlier."

    show cyra happy at slightright
    with dissolve

    "You saw Cyra grinning and waving at you at a table."
    cyra "Hey, [name]! Over here!" 
    cyra "I saved you a seat… and maybe some fries. {w}Maybe."
    mc "Maybe? You mean you already ate half of it."
    cyra "Correction: {cps=20}seventy-five percent."
    cyra "But in my defense, debugging burns calories!"

    "Kai slides his tray onto the table with a smirk."
    show kai happy at slightleft
    with dissolve
    kai "More like you burned the code. I saw your logic statement loop five times before you fixed it."

    show cyra angry
    cyra "Hey, at least my loops {i}looped!{/i} Yours froze the whole simulation!"
    mc "(chuckles) {p}Should I step in before this turns into a logic war?"

    show luna happy at rise_up
    with dissolve
    luna "Too late! Logic war initiated! {w}Beeep- Boop- Bap!"
    luna "If (Kai > Cyra): {p}{space=30}declare_winner(Kai) {p}else: {p}{space=30}declare_winner(Cyra)"

    kai "Luna, that’s not even how comparisons work."
    show luna neutral
    luna "Tell that to my soda, it’s glowing blue for {i}false!{/i}"

    show kai happy
    show luna happy
    show cyra happy
    "They all laugh. Ms. Py Thon enters quietly, holding a tablet. She seems serene, but observant."
    show mspython happy at right with dissolve
    mspy "Still awake, I see. Perhaps I should add a {i}‘Sleep()’{/i} function to your schedules."
    mc "(smiling) {p}We were… reviewing operators. In our own way."
    mspy "Ah, the best learning happens when you forget you’re learning."
    "She glances at the group, fondly"
    mspy "Remember — logic and emotion don’t have to conflict. The strongest code is balanced, just like the strongest hearts."
    
    if cyraAffection > 5:
        show cyra neutral
        "Cyra looks at MC with a soft smile, brushing a strand of hair behind her ear."
    
    show cyra happy
    cyra "Guess that means even bugs can teach us something, huh?"
    show kai happy
    kai "Yeah — like how not to {i}write{/i} your code."
    mc "(laughs) {p}I think we all learned that one the hard way."
    "Ms. Py Thon turns toward the window, the night sky reflected on her tablet screen. Her voice turns thoughtful."
    show mspython neutral
    mspy "There are… darker codes out there. Ones written with no balance." 
    mspy "Promise me you’ll all keep learning — not just for power, but for purpose."
    hide mspython with dissolve
    "The group quiets for a moment. The wind hums through the vents."
    show kai neutral
    show cyra neutral
    show luna neutral
    "On their faces reads — curiosity, camaraderie, and just a hint of unease."

    luna "Sooo… {w}who’s up for another mini-game before bed?"
    luna "Maybe a ‘Guess the Operator’ challenge?"
    show kai happy
    kai "Count me in. I’ll prove I can out-code Cyra any day."
    show cyra happy
    cyra "Bring it, Voltage Boy."
    mc "Let’s see who short-circuits first."
    "They all laugh again, the tension fading — but as the camera pans to the window, a faint flicker of code appears reflected in the glass." 
    "A pair of glowing digital eyes blink once, then vanish into static..."

    n "{b}{size=+10}LESSON SUMMARY{/size}{/b}"
    n "{=code}+ - * / %% // **{/code} {space=40}Arithmetic Operators"
    n "{=code}> < >= <= == !={/code} {space=40}Comparison Operators"
    n "{=code}and, or, not{/code} {space=40}Logical Operators"
    n "{=code}if, elif, else{/code} {space=40}Conditional Decisions"

    scene black
    with dissolve
    return

label ep3Scn1QuestionWrong:
    show mspython sad
    mspy "Incorrect. Multiplication uses {=code}*{/code}, not concatenation."
    show mspython neutral
    mspy "Don’t worry, we’ll fix that logic."
    return

label ep3Scn3QuestionWrong:
    show astra neutral at right with dissolve
    astra "Careless logic, rookie. x is 10 — greater than 5. Easy math."
    show mspython sad
    mspy "Logic errors can be fixed… but only if you observe your conditions clearly. Always think before you code."
    hide astra with dissolve