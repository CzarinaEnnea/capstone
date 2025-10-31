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
