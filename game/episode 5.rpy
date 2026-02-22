label episode5:
# SCENE 1
    scene black
    with dissolve

    show text "{=title}Episode 5 - Loops of Destiny: The Function Awakening{/title}" at truecenter with dissolve
    pause 2
    hide text with fade

    scene garden
    with dissolve

    play music "chill_bg.ogg" volume 0.5

    mc "Code Academy mornings always feel… alive."
    mc "Too alive sometimes — like the campus itself is running in a loop."
    "({i}Cyra elbows [name] lightly.{/i})"

    show cyra neutral-notab at right with dissolve
    cyra "You’ve got scrambled-logic all over your face. Rough night?"
    show cyra neutral2-notab
    mc "It's not scrambled logic. It's just… learning overflow."

    show kai neutral at left with dissolve
    kai "(walking by, coffee steaming){p}Overflow? More like a {color=#81f08aff}while{/color} loop running without a break."
    show kai neutral2
    show luna happy at center with dissolve
    luna "(materializing behind [name]) {p}Like {color=#81f08aff}while True:{/color}{w} — endless despair!"
    show mira sad at slightright with dissolve
    mira "N-No… that would cause CPU meltdown…"
    mira "And possibly emotional damage…"
    show mira sad2
    show astra neutral at slightleft with dissolve:
        xzoom -1.0
    astra "(sipping pixel-tea calmly) {p}Honestly, watching you all struggle is the best entertainment on campus."
    show astra neutral2
    mc "I’m glad we amuse you."
    show astra happy
    astra "You’re welcome."
    show astra happy2

    play sound "school-bell.ogg"
    show luna neutral2 with dissolve
    "({i}The school bell echoes.{/i})"

    mspyIntercom "Students, class begins in three minutes."
    mspyIntercom "Today, we tackle loops — the rhythm of all programming."

    show astra neutral2 with dissolve
    show kai neutral
    kai "Great. More ways to break things."
    show kai neutral2
    show cyra happy-notab
    cyra "More ways for {b}{i}you{/i}{/b} to break things."
    show kai angry
    kai "Fight me."
    mc "Let’s just get to class before she initiates {w}{cps=20}{color=#81f08aff}LateStudentPunishment.exe.{/color}"
    show luna surprised
    luna "Oh! That one turns your clothes into a clown outfit."
    
    show cyra surprised2-notab
    show kai surprised2
    show astra sad2
    show mira surprised2
    "Everyone" "…"
    show cyra surprised-notab
    show kai surprised
    show astra sad
    show mira surprised
    "Everyone" "What?"
    show luna bleh
    luna "Kidding!"

    stop music fadeout 0.5
    show luna neutral2
    luna "…"
    show luna neutral
    luna "…Probably."

    scene black
    with fade
    pause 1.5

# SCENE 2
    play sound "door_opening_school_doorway.ogg"
    scene classroom
    with dissolve

    pause 1.5
    show mspython neutral at center with dissolve
    play music "audio/class.ogg" fadein 0.5 volume 0.3
    mspy "A for loop is used when you know how many times you want to repeat something." 
    mspy "It is controlled, predictable, and elegant."

    show mspython neutral2
    "A glowing table forms in the air."

    hide mspython with dissolve
    play sound "hologram.ogg"

    show screen loopTable with dissolve

    cyra "Kai’s brain could use that. Maybe he’d finally follow instructions."
    kai "I’d rather loop myself into a wall."
    astra "That would explain your logic errors."

    hide screen loopTable with dissolve
    # pause 1.0
    show mspython neutral at center with dissolve
    mspy "Now [name], predict the output."
    show mspython neutral2 at slightright with move
    show ep5-scn2-txt1 at top_left_space with dissolve

    menu:
        "Hi Hi":
            play sound "error_sound1.ogg"
            show mspython neutral
            mspy "Three iterations produce three outputs."
            show mspython neutral2
            play sound "punch_sound2.ogg"
            "(A tiny ‘{i}Hi{/i}’ bug bonks [name].)"
            luna "You’ve been greeted… violently."

        "Hi Hi hi":
            play sound "error_sound1.ogg"
            show mspython neutral
            mspy "Three iterations produce three outputs."
            show mspython neutral2
            play sound "punch_sound2.ogg"
            "(A tiny ‘{i}Hi{/i}’ bug bonks [name].)"
            luna "You’ve been greeted… violently."

        "Hi Hi Hi":
            play sound "right_answer.ogg"
            show mspython happy2
            luna "TRIPLE HI! MAXIMUM FRIENDSHIP!"
            cyra "Nice. You didn’t overthink it."
            kai "Huh. You’re learning."
    
    show mspython neutral with dissolve
    mspy "Now type a loop that prints numbers 1 to 3."
    show mspython neutral2
    call ep5_scn2_txt1

    stop music fadeout 0.5
    scene black
    with fade
    pause 1.5

# SCENE 3
    scene training-chamber
    with dissolve

    show doctorbyte neutral at right with dissolve:
        xzoom -1.0
    dr "Loops shape reality here."
    dr "Control the loop — control the outcome."
    show doctorbyte neutral2

    play music "audio/class.ogg" fadein 0.5 volume 0.3

    # QUIZ 1
    show ep5-scn3-txt1 at top_left_space with dissolve
    call ep5_scn3_txt1
    hide ep5-scn3-txt1 with dissolve

    # QUIZ 2
    show doctorbyte neutral2
    show ep5-scn3-txt2 at top_left_space 
    with dissolve
    call ep5_scn3_txt2
    hide ep5-scn3-txt2 with dissolve

    # QUIZ 3
    show doctorbyte neutral with dissolve
    dr "Now Write a loop that prints ‘Debug’ five times."
    show doctorbyte neutral2
    show ep5-scn3-txt3 at top_left_space with dissolve
    call ep5_scn3_txt3
    hide ep5-scn3-txt3 with dissolve

    stop music fadeout 0.5
    scene black
    with fade
    pause 2.0

# SCENE 4
    scene garden
    with dissolve
    play music "chill_bg.ogg" volume 0.5

    "Neon flowers pulse gently, opening and closing like animated brackets. Floating lanterns display scrolling lines of harmless code." 
    "The day’s tension finally begins to unwind."

    mc "After hours of loops and logic, the garden feels… calm."
    mc "Like a breakpoint in the middle of chaos."
    mc "Maybe this is where you process things — code, emotions, people."

    # play sound "chime.ogg"
    "A soft chime appears in the air."

    "Who do you spend time with?"
    menu:
        "Talk to Cyra":
            call Ep5Scn4Cyra
        "Talk to Kai":
            call Ep5Scn4Kai
        "Talk to Luna":
            call Ep5Scn4Luna
        "Talk to Mira":
            call Ep5Scn4Mira

    scene black with dissolve
    pause 0.5
    scene garden with dissolve
    "The garden lights dim slightly as students start moving."

    mc "Break time never lasts long here."
    cyra "(quietly, as they walk) {p}Hey… don’t overthink it. You’re doing fine."

    play sound "school-bell.ogg"
    "System Chime."
    mspyIntercom "Students, return to the Holo-Classroom."

    "The group heads inside."
    mc "Back to class."
    mc "Back to code."

    stop music fadeout 1.0
    scene black
    with fade
    pause 1.5

# SCENE 5
    play sound "door_opening_school_doorway.ogg"
    scene classroom with dissolve

    "Ms. Py Thon adjusts her glasses dramatically, Detective-Conan style. A magnifying-glass icon flashes."
    play music "audio/class.ogg" fadein 0.5 volume 0.3

    show mspython neutral at center with dissolve
    mspy "Class, focus."
    mspy "A {color=#81f08aff}while loop{/color} runs as long as its condition remains {b}true{/b}."
    "{i}She snaps her fingers. A glowing table floats into the air.{/i}"

    hide mspython with dissolve
    show screen whileLoopTable with dissolve

    mira "So it checks… again and again… {w}until the condition becomes false?"
    mspy "Exactly."
    mspy "But forget the {b}update—{/b}"

    hide screen whileLoopTable
    show screen whileLoopTableB 
    with dissolve
    "The lights flicker. A swirling cartoon portal labeled INFINITE LOOP opens."

    mspy "—and the loop never ends."
    luna "THE LOOP IS EATING THE NUMBERS—!"
    kai "Like Astra’s ego."
    astra "Rude."
    astra "Accurate. {w}But rude."
    mspy "Enough commentary."
    hide screen whileLoopTableB with dissolve

    show mspython neutral2 at slightright with dissolve
    "She points dramatically at the board."
    show ep5-scn5-txt1 at top_left_space with dissolve
    show mspython happy
    mspy "Now—test time."
    mspy "How many times will the word ‘Looping’ appear?"
    show mspython happy2

    menu:
        "One time":
            play sound "glitch_sound.ogg"
            "The portal grows. The word “Looping” repeats endlessly on the board."
            show mspython neutral with dissolve
            mspy "Incorrect. Watch carefully."
            show mspython neutral2
            hide ep5-scn5-txt1
            show ep5-scn5-txt1-1 at top_left_space 
            with dissolve
            "She highlights the condition and update step."
            show mspython neutral
            mspy "The {b}condition{/b} is checked {b}before{/b} every loop."
            mspy "The {b}update{/b} controls {b}when it stops{/b}."
            show mspython neutral2
            kai "You answered before the loop finished."

            play sound "error_sound1.ogg"
            "{=red}Logic Fatigue — Confidence –1{/red}"
            "{=red}Next quiz requires typing, not choices.{/red}"
            $ change_confidence(-1)
            "The portal resets. Class continues."

        "Two times":
            play sound "glitch_sound.ogg"
            "The portal grows. The word “Looping” repeats endlessly on the board."
            show mspython neutral with dissolve
            mspy "Incorrect. Watch carefully."
            show mspython neutral2
            hide ep5-scn5-txt1
            show ep5-scn5-txt1-1 at top_left_space 
            with dissolve
            "She highlights the condition and update step."
            show mspython neutral
            mspy "The {b}condition{/b} is checked {b}before{/b} every loop."
            mspy "The {b}update{/b} controls {b}when it stops{/b}."
            show mspython neutral2
            kai "You answered before the loop finished."

            play sound "error_sound1.ogg"
            "{=red}Logic Fatigue — Confidence –1{/red}"
            "{=red}Next quiz requires typing, not choices.{/red}"
            $ change_confidence(-1)
            "The portal resets. Class continues."

        "Three times":
            play sound "hologram.ogg"
            "The portal shrinks and vanishes."
            show mspython happy
            mspy "Correct. The loop repeats three times before the condition becomes false."
            show mspython happy2
            luna "THREE LOOPINGS! PERFECT LOOP COUNT!"
            cyra "You paused and thought. Good habit."

            play sound "right_answer.ogg"
            "{=gold}Syntax Confidence +1{/gold}"
            $ change_confidence(+1)

    hide ep5-scn5-txt1
    hide ep5-scn5-txt1-1
    with dissolve

    play sound "glitch_sound.ogg"
    $ red_effect()
    show ep5-scn5-txt2 at top_left_space with dissolve
    "Red warning text flashes."
    show mspython neutral with dissolve
    mspy "This loop is broken."
    mspy "Fix it before it becomes infinite."
    show mspython neutral

    "HINT!! : Result must show numbers 1 to 6"

    call ep5_scn5_txt2

    mspy "Loops are tools."
    mspy "Control defines mastery."


# SCENCE 6
    scene classroom with dissolve

    show mspython neutral at right with dissolve
    mspy "Loops are powerful—but responsibility matters more than speed."
    show mspython neutral2
    show doctorbyte neutral at left with dissolve
    dr "Infinite loops don’t break systems."
    dr "Ignoring them does."
    hide mspython
    hide doctorbyte
    with dissolve

    show cyra neutral at right with dissolve
    cyra "Don’t beat yourself up. You learned."
    show cyra neutral2
    show kai neutral at left with dissolve
    kai "Yeah. Everyone locks a loop at least once."
    show kai neutral2
    show mira neutral at center with dissolve
    mira "You… {w}didn’t give up."
    show mira happy
    mira "That counts."

    hide cyra
    hide kai
    hide mira
    with dissolve

    pause 1.0

    mc "Mistakes repeat."
    mc "But understanding breaks the loop."

    

    scene black with fade
    show text "{=title}To be continued...{/title}" at truecenter with dissolve
    pause 2
    stop music fadeout 0.5
    hide text with dissolve
    
    return


label Ep5Scn4Cyra:
    show cyra sad2-notab at center with dissolve
    "Cyra stands by the railing, watching the digital sun dip below the skyline."
    "Her expression is thoughtful — less teasing than usual."

    show cyra sad-notab
    cyra "You know… most first-years panic when loops get complicated."
    mc "I panicked internally. I just didn’t let it crash."
    show cyra happy2-notab
    cyra "That’s still control. A lot of people fake confidence."
    show cyra happy-notab
    cyra "You actually {i}learn{/i}."

    play sound "hologram.ogg"
    "She taps the railing; glowing code ripples outward."

    show cyra sad-notab
    cyra "Frontend looks flashy, but it’s all structure underneath."
    cyra "Same with people."
    show cyra sad2-notab

    mc "You talking about code… {w}or yourself?"
    "{i}Cyra pauses, then shrugs.{i}"
    cyra "..."
    show cyra happy-notab
    cyra "Both, I guess."
    "{i}A comfortable silence.{i}"

    show cyra sad-notab
    cyra "Just— {w}don’t burn yourself out trying to keep up with everyone else."
    cyra "You don’t need to prove anything yet."

    hide cyra with dissolve

    "She feels different. No flirting. No jokes."
    "Just… {w}genuine advice."

    play sound right_answer
    "{=gold}Cyra Trust +1{/gold}"
    $ change_cyraAffection(+1)
    $ change_confidence(+1)

    return

label Ep5Scn4Kai:
    show kai angry2 at center with dissolve
    "Kai sits on a bench, twirling a holo-wrench between his fingers."
    "He looks annoyed — at himself, not you."

    show kai angry
    kai "You know what’s worse than infinite loops?"
    mc "Let me guess. Losing?"

    show kai angry2
    kai "Getting stuck repeating the same mistakes."
    "{i}He looks up at you.{/i}"
    show kai neutral
    kai "You didn’t freeze today. Even when the nested loop went wild."
    show kai neutral2
    mc "Coming from you, that sounds like praise."
    show kai embarassed2
    kai "…Don’t get used to it."

    "A beat."

    show kai sad
    kai "When I was new, I tried to brute-force everything."
    kai "Thought speed mattered more than logic."
    show kai sad2
    mc "And?"
    show kai sad
    kai "And I crashed a training server so hard Dr. Byte still brings it up."
    "{i}You laugh. Kai almost smiles.{/i}"
    show kai embarassed
    kai "Point is— {w}don’t rush. {w}Control beats power."

    play sound right_answer
    "{=gold}Kai Respect +1{/gold}"
    $ change_kaiAffection(+1)
    $ change_confidence(+1)

    return

label Ep5Scn4Luna:
    show luna cookie2 at center with dissolve
    "Luna is lying on the grass, arms spread, staring at floating Boolean symbols drifting above."
    show luna cookie

    show luna happy with dissolve
    luna "[name]! Come look! That cloud looks like a {color=#81f08aff}True{/color} statement!"
    mc "…You’ve been staring at code too long."

    show luna surprised3
    luna "{b}Impossible. Code is life.{/b}"
    "{i}She suddenly sits up.{/i}"

    show luna neutral
    luna "Did you know loops are just time travel with rules?"
    show luna neutral2
    mc "I feel like that explanation should worry me."
    show luna neutral
    luna "While {color=#81f08aff}loops{/color} are dangerous, but {color=#81f08aff}for loops{/color} are cozy."
    show luna happy-nostar
    luna "They’re like: ‘{i}I know exactly how many times I’ll mess up.{/i}’"
    mc "That’s… weirdly comforting."

    show luna happy
    luna "Right?! If emotions had syntax, I’d just write—"
    luna "{color=#32CD32}while sad: {p}{space=138}hug_friends(){/color}"
    mc "That loop would never end."
    show luna bleh
    luna "Exactly!"

    play sound right_answer
    "{=gold}Luna Friendship +1{/gold}"
    $ change_confidence(+1)

    return

label Ep5Scn4Mira:
    show mira sad2 at center with dissolve
    "Mira kneels near a glowing flower, adjusting its flickering code. Her hands shake slightly."

    show mira surprised-blush
    mira "O-Oh! Sorry, I didn’t see you there."
    mc "You’re fine. Fixing bugs?"
    show mira sad
    mira "Small ones. I like fixing things before they… spiral."
    show mira sad2
    "{i}She hesitates.{/i}"

    show mira neutral
    mira "You were really calm in the loop lab."
    show mira neutral2
    mc "I didn’t feel calm."
    show mira sad
    mira "That’s okay. Control doesn’t mean fear disappears…"
    show mira neutral
    mira "It just means you don’t let it decide for you."
    show mira neutral2
    "{i}She looks up. For a split second, her neural nodes pulse faint pink.{/i}"
    play sound "hologram.ogg"
    "..."
    show mira happy
    mira "Loops repeat… {w}but people don’t have to."

    hide mira with dissolve
    "{i}She smiles quickly, almost too quickly, and looks away.{/i}"
    mc "That felt… deeper than it should have."

    # play sound right_answer
    "{=gold}Mira Bond +1{/gold}"
    # $ change_confidence(+1)

    return