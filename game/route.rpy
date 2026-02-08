label cyra_route:
    scene classroom # Academy Rooftop
    with dissolve
    "Holographic clouds drift slowly."
    "The city’s code skyline glows gold."
    "Cyra leans against the railing, arms crossed—not defensive, just thinking."

    show cyra sad-notab at center with dissolve
    cyra "You know… I used to think logic was enough."
    "She glances sideways at [name]."
    cyra "If something worked, it didn’t need feelings."
    cyra "If it looked good, no one asked how it was built."
    "She exhales."
    cyra "Then you showed up."
    "[name] stays quiet. Lets her continue."

    cyra "You made mistakes."
    cyra "You asked questions."
    cyra "You didn’t pretend to be perfect."
    "She turns fully towards [name] now."
    cyra "And somehow… that made everything feel more stable."
    show cyra happy2-notab with dissolve
    "A small smile."
    cyra "I tease because it’s safer than admitting I care."
    cyra "But I don’t want safe anymore."
    "She extends her hand—hesitant, genuine."

    cyra "No conditions."
    cyra "No hidden logic."
    cyra "No escape clauses."
    "A pause."
    cyra "(soft) \n Just… {w}stay with me."
    "When [name] takes her hand, her grip tightens—just slightly."

    # NVL
    nvl clear
    mcNVL "For once, the system didn’t need validation." with dissolve
    mcNVL "It just… worked."
    return


label kai_route:
    scene training-chamber
    with dissolve

    show kai neutral2 at center with dissolve
    "Kai sits on the edge of the platform, staring at the floor."
    show kai neutral at center
    kai "You know what I hate most?"
    "[name] waits."
    kai "Losing control."
    "A short laugh."
    kai "I thought strength meant never hesitating."
    kai "Never backing down."
    kai "Never needing anyone."
    "He looks up."
    kai "Then you beat Mira… without overpowering her."
    "He stands, stepping closer."

    kai "That scared me."
    "A pause."
    kai "And impressed me."
    "His voice lowers."
    kai "You didn’t just win."
    kai "You chose restraint."
    "He scratches the back of his neck, clearly uncomfortable—but honest."

    kai "I don’t know how to say this without sounding stupid."
    "Then, directly:"
    kai "…Stay."
    "Not a demand. Not a challenge."
    "A request."
    kai "I want to figure this out."
    kai "With you."

    nvl clear
    mcNVL "{w}Strength wasn’t domination." with dissolve
    mcNVL "It was trust."
    return


label solo_route:
    scene garden
    with dissolve
    play music "chill_bg.ogg" volume 0.5

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
    mcNVL "Not every story needs a pair." with dissolve
    "Some just need understanding."
    "The system feels… complete."
    stop music fadeout 0.5
    return