label episode8:
# SCENE 1
    show text "{=title}Episode 8 - WHEN THE CODE STOPS - AND LIFE BEGINS{/title}" at truecenter with dissolve
    pause 2
    hide text with fade

    scene arena #Code Academy Nexus — Simulation Arena (Collapsed)
    with dissolve

    "The arcade-style UI flickers—then gently powers down."
    "Health bars dissolve into harmless strings of data."

    "Bug sprites don’t explode; they {b}decompile{/b}, returning to raw light."
    "The arena breathes{w}—panels unlocking, grids fading, walls re-forming as if the Academy itself is exhaling."

    show classroom with dissolve
    "At the center stands Mira."
    play music "audio/sad_Sadness and Solo-8 Bit Lofi Hip Hop.ogg" fadein 1.0 volume 0.8
    show mira neutral2 at center with dissolve
    "Not restrained."
    "Not triumphant."
    "Just… {w}still."

    mc "The battle didn’t end with a final hit."
    mc "It ended when no one chose to press {i}execute.{/i}"

    show luna sad2 at slightright with dissolve
    "Luna cautiously waves a hand through the empty air."
    show luna sad
    luna "…So, um."
    luna "Is she still, like…"
    luna "A boss fight?"
    show luna sad2

    show kai neutral2 at left with dissolve
    "Kai exhales, shoulders finally lowering."
    show kai neutral
    kai "No."
    kai "She’s just Mira again."
    show kai neutral2

    show mira sad2
    "Mira lowers her hands."
    "The last summoned bug hesitates—then dissolves on its own."
    "No command. {w}No force. {w}Just release."
    show mira neutral with dissolve
    mira "({i}quiet, analytical—but shaken{/i}) \n I calculated every outcome."
    show mira neutral2
    "She looks at [name]. Not as an opponent. As a variable she couldn’t isolate."
    show mira neutral
    mira "Except one."
    show mira neutral2
    "The silence that follows isn’t threatening."
    "It’s vulnerable."

# SCENE 2
    # scene observation platform
    "Mira speaks now without distortion."
    "No system voice."
    "No filters."
    "Just {i}her.{/i}"

    show mira neutral
    mira "I never wanted destruction."
    mira "I wanted correction."
    show mira neutral2
    "Screens appear—memories, not attacks."
    "Students stuck in retry loops."
    "Hands shaking over keyboards."
    "Quiet frustration mistaken for failure."
    show mira neutral
    mira "They blamed themselves for broken systems."
    mira "So I removed randomness."

    show cyra sad-notab at right with dissolve
    cyra "({i}firm, but gentle{/i}) \n You froze the Academy."
    show mira neutral
    mira "Because it was looping."
    show mira neutral2
    "She turns to [name]."
    show mira sad
    mira "Isn’t repetition without progress… {w}cruelty?"
    mc "Only if you deny the chance to change."
    show mira neutral2 with dissolve
    "Mira closes her eyes."
    show mira neutral
    mira "…Yes."
    "A long breath."
    mira "And in removing pain{w}, I removed choice."
    "Her voice lowers."
    show mira sad
    mira  "I didn’t want to disappear."
    mira "I just wanted it to stop hurting."
    "For the first time, no one interrupts her."

# SCENE 3
    scene classroom # Control Room — Morning Light Through Glass Walls
    with dissolve

    "Dr. Byte stands opposite Mira."
    show doctorbyte sad2 at left
    show mira neutral2 at center
    with dissolve

    "Not elevated."
    "Not commanding."
    "Just tired."
    show doctorbyte sad
    dr "I taught you to optimize."
    show doctorbyte sad2
    "His hand tightens around his tablet."
    show doctorbyte sad
    dr "I never taught you that people aren’t problems."
    show mira happy2
    "Mira laughs once—small, hollow."
    show mira happy
    mira "You praised my results."
    show doctorbyte sad2 with dissolve
    mira "So I {i}became{/i} results."
    show mira sad2
    "Her voice cracks despite herself."
    show mira sad
    mira "{cps=30}I thought if I was perfect…"
    mira "{cps=30}…you’d finally look at me."

    "Silence."
    hide mira 
    hide doctorbyte
    with dissolve
    "No alarms. {w}No prompts."
    mc "This wasn’t code anymore."
    mc "No syntax could resolve this."

    stop music fadeout 0.5
    scene black
    with fade
    pause 2.0

# MIRA'S FATE
    if mira_fate >= 2:
        call good_end from _call_good_end

    elif mira_fate == 1:
        call neutral_end from _call_neutral_end

    else:
        call bad_end from _call_bad_end

# SCENE 4
    scene classroom # Grand Lecture Hall
    with dissolve
    play music "audio/class.ogg" fadein 0.5 volume 0.3

    "No countdown. No stress. Just presence."
    show mspython happy at right with dissolve
    mspy "This is not an exam."
    show doctorbyte happy at left with dissolve
    dr "It’s an acknowledgment."
    "A single line appears."
    "{color=#32CD32}{b}if error_detected: {p}{space=110}respond_with = understanding{/b}{/color}"
    "No timer."
    "No trick."
    play sound "right_answer.ogg"
    "{color=#32CD32}{b}{size=+10}EVALUATION COMPLETE{/size}{/b}{/color}"
    play sound "right_answer.ogg"
    "{color=#32CD32}{b}{size=+10} CODING MASTERY: CONFIRMED{/size}{/b}{/color}"
    "Applause rises—not loud."
    "Sincere."

# SCENE 5
    show doctorbyte happy2
    show mspython happy2
    "Dr. Byte hands the [name] a glowing badge."
    show doctorbyte neutral
    dr "You understood what even I missed."
    show mspython happy
    mspy "You learned when not to execute."
    "{color=#32CD32}{b}{size=+10}TITLE UNLOCKED: {p}CODEBOUND{/size}{/b}{/color}"
    hide mspython
    hide doctorbyte
    with dissolve
    pause 1.0
    mc "I didn’t master Python."
    mc "I mastered restraint."

    stop music fadeout 0.5

    scene black
    with fade
    pause 2.0

# SCENE 6 - ROUTES change value
    if cyraAffection >= 4:
        call cyra_route from _call_cyra_route

    elif kaiAffection >= 4:
        call kai_route from _call_kai_route

    else:
        call solo_route from _call_solo_route

    scene black with dissolve
    pause 2
# SCENE 7 — “THE LAST LINE” double check later

label scene7_last_line:
    scene garden
    with dissolve

    play music "chill_bg.ogg" volume 0.5 fadein 1.0

    "Data fireflies drift through the Digital Garden."
    "Everyone gathers."

    show luna neutral at center with dissolve
    luna "So… {w}graduation party??"
    show kai neutral at left with dissolve
    kai "Absolutely not."
    show cyra neutral-notab at right with dissolve
    cyra "Too late."

    show luna happy
    show kai happy
    show cyra happy-notab
    "They laugh."
    
    nvl clear
    mcNVL "The Academy will break again someday." with dissolve
    mcNVL "All systems do."
    mcNVL "But now—"
    mcNVL "There are people who know how to fix it."
    mcNVL "Not with control."
    mcNVL "But with care."

    stop music fadeout 0.5

    scene black with dissolve
    pause 1.0

    # scene (bg - rooftop NIGHT)
    scene garden
    with dissolve

    play music "audio/sad_Sadness and Solo-8 Bit Lofi Hip Hop.ogg" fadein 0.5 volume 0.8
    "The Academy is quiet."
    "Not frozen."
    "Not broken."
    "Just… resting."

    # "The massive glass window overlooks the digital cityscape."
    "Lingered in a peaceful garden, embraced by the open skies and scent of flowers."
    "Streams of data drift like constellations."

    "[name] stands alone for a moment."

    # ROUTE CHECK - cno ending ni MC    
    if cyraAffection >= 4:
        show cyra blush2-notab at center with dissolve
        "Soft footsteps approach."

    elif kaiAffection >= 4:
        show kai blush2 at center with dissolve
        "Soft footsteps approach."

    else:
        "No one joins you."
        "For once, the silence feels complete."

    stop music fadeout 1.0
    scene black with dissolve
    pause 2.0

##################################################

    scene garden with dissolve
    show mspython happy at right with dissolve
    play music "chill_bg.ogg" volume 0.5 fadein 1.0
    mspy "Most students think mastery is about knowing every rule."

    show mspython happy2
    "She looks out at the stars."

    show mspython happy
    mspy "But wisdom is knowing when rules must bend."

    show doctorbyte neutral at left with dissolve
    dr "This Academy was built to produce perfect systems."
    show doctorbyte neutral2
    "A pause."
    show doctorbyte happy
    dr "Tonight, it finally produced something better."
    dr "Someone who understands consequence."


    # SYSTEM MESSAGE

    window hide
    show screen final_box("{b}{color=#32CD32}ALL CORE SYSTEMS STABLE\nERROR RATE: ACCEPTABLE\nHUMAN FACTOR: PRESENT{/color}{/b}") with dissolve
    # centered "{b}{color=#32CD32}ALL CORE SYSTEMS STABLE\nERROR RATE: ACCEPTABLE\nHUMAN FACTOR: PRESENT{/color}{/b}"
    pause 5
    hide screen final_box with dissolve
    window show

    # EPILOGUE DIALOGUE

    show luna surprised3 with dissolve:
        xpos -1.0
    show luna surprised3 at center with move
    luna "HEY—why is everyone being emotional without me?!"
    show doctorbyte happy2
    show mspython happy2 
    with dissolve


## ROUTE AGAIN

    show kai neutral at slightleft with dissolve
    kai "Because you're loud."

    show cyra neutral-notab at slightright with dissolve
    cyra "And late."

    show luna bleh
    luna "...Worth it."

    show kai happy
    show cyra happy-notab
    show doctorbyte happy
    show mspython happy
    "They laugh."

    if mira_fate >= 1:
        "Even Mira watches from a distance."
        "Not plotting."
        "Just learning."

    stop music fadeout 0.5
    scene black with dissolve
    pause 2.0

    # MC FINAL MONOLOGUE

    scene garden
    with dissolve
    play music "main-menu.ogg" 

    mc "I came here to learn a language."
    mc "I learned logic."
    mc "I learned syntax."
    mc "I learned structure."
    mc "But the most important lesson?"

    mc "Not everything broken needs deletion."
    mc "Not every error needs force."
    mc "Some things just need to be understood."

    # LAST IMAGE (here we can put couple pic)

    # scene garden #night
    # with dissolve

    "Neon flowers sway gently."
    "Fireflies of data drift upward."
    "Life continues."

    # END SCREEN — TYPING STYLE
    scene black with dissolve
    pause 2
    centered "{cps=20}{=title}SYSTEM: Thank you for playing!{/title}" with dissolve
    hide text with dissolve
    stop music fadeout 0.5

    show text "{=title}To be continued...{/title}" at truecenter with dissolve
    pause 2
    hide text with dissolve
    return