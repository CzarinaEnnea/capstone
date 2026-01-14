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

    show luna sad2 at slightright with dissolve
    "Luna slowly waves a hand in front of a frozen student."
    show luna sad
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
    play sound "glitch_sound.ogg"
    scene black with dissolve
    $ red_effect()

    scene cafeteria #Suspended Reality Layer
    with dissolve

    "The floor becomes scrolling Python syntax."
    "Variables orbit Mira like constellations—stable, elegant."

    show kai sad at left with dissolve
    kai "Mira… what did you do?"
    show mira neutral at center with dissolve
    mira "I corrected inefficiency."
    show mira neutral2
    "She gestures."

    "Holo-screens appear—students failing exams, retrying challenges, looping tutorials."
    show mira neutral
    mira "They repeat the same errors."
    show cyra sad-notab at right with dissolve
    cyra "That’s called learning."
    show mira angry-nosign
    show cyra sad2-notab
    show kai sad2
    with hpunch
    mira "That’s called {b}waste{/b}."

    "{b}She turns to [name].{/b}"
    show mira neutral with dissolve
    mira "You understand optimization. {w}Why allow {b}failure{/b} when perfection is {b}calculable{/b}?"
    mc "Because failure teaches."
    show mira neutral2
    "{b}Mira’s fingers twitch.{/b}"
    show mira angry-nosign
    mira "Failure teaches pain."
    show mira serious
    "She raises her hand."
    show mira happy
    mira "I optimized the Academy so no one would be left behind again."
    show mira happy2
    show kai angry
    kai "You hijacked it!"
    show mira happy
    mira "I {i}saved{/i} it."
    show cyra sad-notab
    cyra "…You removed choice."
    show mira sad2
    "For a fraction of a second{w}—Mira hesitates."
    show mira sad
    mira "{size=-5}{cps=30}Choice introduces inconsistency.{/size}"

# SCENE 3
    hide kai
    hide cyra
    hide mira
    with dissolve
    "{color=#ff4444}{b}TRAINING MODE OVERRIDE — LOGIC CONFLICT DETECTED{/b}{/color}"
    "The suspended reality collapses."

    play sound "glitch_sound.ogg"
    scene black with dissolve
    $ red_effect()

    scene training-chamber
    with dissolve

    "The familiar Practice Chamber reforms around them—glowing grids, combat panels, live code projections."
    dr "She’s using the Academy’s own training system."
    mspy "Mira. Stop this."
    mira "I am teaching."
    "The chamber reshapes violently."
    "Error Constructs materialize—born from corrupted logic."
    mira "This lesson has only one outcome."

    play sound "glitch_sound.ogg"
    scene black with dissolve
    $ red_effect()

# SCENE 4
    with pixellate
    scene classroom # PIXEL GAME BG
    with dissolve

    "Grid lines light up."
    "Status panels appear."
    "{color=#32CD32}{b}TURN-BASED LOGIC ENGAGED{/b}{/color}"
    luna "{b}WAIT—{w}this looks like a game!!{/b}"
    kai "…Of course it does."
    cyra "She’s not fighting us directly."
    mc "She’s testing us."

    "Mira raises her hand calmly."
    mira "I don’t want to destroy you."
    mira "I want to {b}correct{/b} you."
    "She snaps her fingers."

# SCENE 5
    # BUG 1 — LOOPLING
    $ red_effect()
    "A small circular bug endlessly spinning appears."
    mira "Meet Loopling."
    mira "It exists only to repeat."
    "Everyone tries to access their terminal to fight Mira but only [name] has the authorization to code."
    cyra "What is this why can't I open my terminal?"
    "Kai, Luna, Astra" "What the…. Me too!!"
    mc "Uh ohh…."

    kai "Dont tell me your the only one with access!!"
    luna "Oh well…{w}we're doomed!"
    astra "What is this MIRA!"
    mira "HAHA….{w}To make it more interesting, {w}only [name] has access to fight."
    cyra "You can do it [name], remember our lessons!"
    mspy "Dont worry [name], I'll try and hack her system so everyone can help."
    mspy "But that’s all I can do, I can't fully stop her."
    mspy "Students' you need to defeat her yourself."

    "{color=#32CD32}{b}Authorization Upgraded!{/b}{/color}"
    "Everyone" "{b}Let’s do this!{/b}"


    return