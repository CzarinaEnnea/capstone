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
    mspy "A for loop is used when you know how many times you want to repeat something. {w}It is controlled, predictable, and elegant."

    "A glowing table forms in the air."

    cyra "Kai’s brain could use that. Maybe he’d finally follow instructions."
    kai "I’d rather loop myself into a wall."
    astra "That would explain your logic errors."

    mspy "[name], predict the output."

    menu:
        "Hi Hi":
            mspy "Three iterations produce three outputs."
            "(A tiny ‘Hi’ bug bonks MC.)"
            luna "You’ve been greeted… violently."
        "Hi Hi hi":
            mspy "Three iterations produce three outputs."
            "(A tiny ‘Hi’ bug bonks MC.)"
            luna "You’ve been greeted… violently."
        "Hi Hi Hi":
            luna "TRIPLE HI! MAXIMUM FRIENDSHIP!"
            cyra "Nice. You didn’t overthink it."
            kai "Huh. You’re learning."
    
    mspy "Now type a loop that prints numbers 1 to 3."

    return