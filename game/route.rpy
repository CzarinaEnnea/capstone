label cyra_route:
    scene classroom # Academy Rooftop
    with dissolve
    play music "chill_bg.ogg" volume 0.5 fadein 1.0
    "Holographic clouds drift slowly."
    "The city’s code skyline glows gold."
    "Cyra leans against the railing, arms crossed—not defensive, just thinking."

    show cyra sad-notab at center with dissolve
    cyra "You know… I used to think logic was enough."
    show cyra sad2-notab
    "She glances sideways at [name]."
    show cyra sad-notab
    cyra "If something worked, it didn’t need feelings."
    cyra "If it looked good, no one asked how it was built."
    show cyra sad2-notab
    "She exhales."
    show cyra happy-notab
    cyra "Then you showed up."
    "[name] stays quiet. Lets her continue."

    cyra "You made mistakes."
    cyra "You asked questions."
    cyra "You didn’t pretend to be perfect."

    show cyra neutral2-notab with dissolve
    "She turns fully towards [name] now."
    show cyra happy-notab with dissolve
    cyra "And somehow… that made everything feel more stable."
    show cyra happy2-notab with dissolve
    "A small smile."
    cyra "I tease because it’s safer than admitting I care."
    cyra "But I don’t want safe anymore."
    show cyra embarrassed-notab with dissolve
    "She extends her hand—hesitant, genuine."

    show cyra happy2-notab with dissolve
    cyra "No conditions."
    cyra "No hidden logic."
    cyra "No escape clauses."
    "A pause."

    show cyra blush2-notab with dissolve
    cyra "(soft) \n Just… {w}stay with me."
    "When [name] takes her hand, her grip tightens—just slightly."

    # NVL
    nvl clear
    mcNVL "For once, the system didn’t need validation." with dissolve
    mcNVL "It just… worked."
    stop music fadeout 0.5
    return


label kai_route:
    scene training-chamber
    with dissolve

    play music "chill_bg.ogg" volume 0.5

    show kai neutral2 at center with dissolve
    "Kai sits on the edge of the platform, staring at the floor."
    show kai neutral at center
    kai "You know what I hate most?"
    show kai neutral2
    "[name] waits."
    show kai neutral
    kai "Losing control."
    show kai neutral2
    "..."
    show kai angry with dissolve
    kai "I thought strength meant never hesitating."
    kai "Never backing down."
    kai "Never needing anyone."
    show kai sad2 with dissolve
    "He looks up."
    show kai sad
    kai "Then you beat Mira… without overpowering her."
    show kai sad2
    "He stands, stepping closer."
    show kai sad
    kai "That scared me."
    show kai sad2
    "A pause."
    show kai happy with dissolve
    kai "And impressed me."
    "His voice lowers."
    show kai happy2
    kai "You didn’t just win."
    kai "You chose restraint."
    "He scratches the back of his neck, clearly uncomfortable—but honest."
    show kai embarassed2 with dissolve
    kai "I don’t know how to say this without sounding stupid."
    "Then, directly:"
    show kai blush with dissolve
    kai "…Stay."
    show kai blush2
    "Not a demand. Not a challenge."
    "A request."
    show kai blush
    kai "I want to figure this out."
    kai "With you."

    nvl clear
    mcNVL "{w}Strength wasn’t domination." with dissolve
    mcNVL "It was trust."

    stop music fadeout 0.5
    return


label solo_route:
    scene garden
    with dissolve
    play music "chill_bg.ogg" volume 0.5 fadein 1.0

    "The Academy hums softly around [name]."
    "Students laugh in the distance."
    "Lights flicker gently overhead."
    "[name] stands alone."
    "But not abandoned."

    mc "I came here looking for answers."
    mc "I found something quieter."
    "Confidence."
    "Clarity."
    "Choice."

    nvl clear
    n "Not every story needs a pair." with dissolve
    n "Some just need understanding."
    n "The system feels… {w}complete."
    stop music fadeout 0.5
    return