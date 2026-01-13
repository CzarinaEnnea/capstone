label episode7:
# SCENE 1
    scene black
    with dissolve
    pause 2.0
    show text "{=title}Episode 7 - BREAK THE LOOP - AND THE GIRL INSIDE IT{/title}" at truecenter with dissolve
    pause 2
    hide text with fade

    scene cafeteria #Central Corridor
    with dissolve

    "Time stutters."
    "A tray of holo-coffee hangs mid-air."
    "A student’s laugh cuts off halfway through a breath."
    "Even the neon lights flicker{w}—then stop."
    "The world becomes still."

    "{color=#ff4444}{b}{size=+10}WARNING: UNAUTHORIZED CONTROL FLOW DETECTED{/size}{/b}{/color}"

    show luna neutral2 at slightright with dissolve
    "Luna slowly waves a hand in front of a frozen student."
    show luna neutral
    luna "…Okay. This is officially not funny."
    show kai angry2 at left with dissolve
    kai "No jitter. No rollback. This isn’t a glitch."
    show cyra sad2-notab at right with dissolve
    "Cyra looks around, looking serious for once."
    show cyra sad-notab
    cyra "This is deliberate. Someone locked the Academy into a master loop."

    nvl clear
    mcNVL "Everything froze." with dissolve
    mcNVL "Time. {w}Motion. {w}Sound."
    mcNVL "Everything—"
    mcNVL "Except us."

    hide kai 
    hide luna 
    hide cyra 
    with dissolve
    "A soft sound echoes through the corridor." with dissolve

    #Add slow clapping sound
    "{b}Clap. {p}Clap. {p}Clap.{/b}"
    "The sound reverberates unnaturally, like it’s bouncing inside the code itself."
    mira "Good. You’re still responsive."
    "A distortion ripples forward."
    play sound "glitch_sound.ogg"
    show mira neutral2 at center with dissolve
    "Mira steps out—calm, composed, eyes glowing faintly with cascading code."
    "She looks at each of them—not threatening. Almost… {w}relieved."
    show mira happy with dissolve
    mira "You reached the final iteration."

# SCENE 2
    "The corridor dissolves beneath their feet."
    return