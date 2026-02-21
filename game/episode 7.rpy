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
    stop music

    with pixellate
    scene training-chamber
    with dissolve
    "Grid lines light up."
    "Status panels appear."

    play sound glitch_sound
    show screen battle_ui with pixellate
    $ player_name = name.upper()
    $ console_text = "TURN-BASED LOGIC ENGAGED"
    pause

    ""
    luna2 surprised3 "{b}WAIT—{w}this looks like a game!!{/b}"
    kai2 angry2 "…Of course it does."
    cyra2 surprised "She’s not fighting us directly."
    mc "She’s testing us."
    astra2 sad "Mira.."
    mspy2 neutral "Focus everyone."

    "Mira raises her hand calmly."
    mira2 neutral "I don’t want to destroy you."
    mira2 happy "I want to {b}correct{/b} you."
    "She snaps her fingers."

# SCENE 5
    # BUG 1 — LOOPLING
    play sound glitch_sound
    $ red_effect()

    $ round_info = "BUG 1 — LOOPLING"
    $ bug_name = "LOOPLING"

    # REPLACE BUGS
    show stringleech-pixel:
        subpixel True pos (0.78, 0.95) zoom 3.28
    
    show stringleech-pixel with dissolve:
        subpixel True pos (0.53, 0.08)

    $ console_text = "A circular bug endlessly spinning appears."
    ""
    mira2 neutral "Meet Loopling."
    mira2 neutral "It exists only to repeat."
    "Everyone tries to access their terminal to fight Mira but only [name] has the authorization to code."
    cyra2 angry "What is this why can't I open my terminal?"
    "Kai, Luna, Astra" "What the…. Me too!!"
    mc "Uh ohh…."

    kai2 angry2 "Dont tell me your the only one with access!!"
    luna2 surprised "Oh well…"
    luna2 neutral "We're doomed!"
    astra2 angry "What is this MIRA!"
    mira2 happy "HAHA….{w}To make it more interesting, {w}only [name] has access to fight."
    cyra2 happy "You can do it [name], remember our lessons!"
    mspy2 angry-nosign "Dont worry [name], I'll try and hack her system so everyone can help."
    mspy2 sad "But that’s all I can do, I can't fully stop her."
    mspy2 neutral "Students you need to defeat her yourself."

    play sound hologram
    $ console_text = "AUTHORIZATION UPGRADED!"
    ""
    "Everyone" "{b}Let’s do this!{/b}"

    call bug_summon_phase1

# SCENE 6
    "A crystalline bug splitting into fragments appeared"
    mira "This one holds data that was never acknowledged."
    kai "…That sounds personal."
    cyra "Let’s preserve the data [name]."

    call bug_summon_phase2


# SCENE 7


# SCENE 8
    "Mira stands alone now."
    show mira sad2 at center with dissolve
    "No bugs left."
    show mira sad
    mira "…You didn’t fight me."
    show mira sad2
    mc "We fought the mistakes."
    show mira sad
    mira "…Why?"
    show mira sad2
    mc "Because you’re not one."
    "Silence."

# RESULT HANDLING (LOCKED FOR EPISODE 8)
    "{color=#ff3e3e}{b}LOGIC CONFLICT UNRESOLVED{/b}{/color}"
    show doctorbyte sad at left with dissolve
    dr "This battle ends without a winner."
    show doctorbyte sad2
    show mspython neutral at right with dissolve
    mspy "And without destruction."
    show mspython neutral2
    show mira neutral2 at center with dissolve
    "Mira looks at [name]."
    show mira neutral
    mira "Then next time…"
    mira "we decide what correction really means."
    "The arena fades."

    scene black
    with fade

# Cliffhanger
    scene black
    with fade

    mc "We didn’t defeat her."
    mc "We reached her."
    mc "But understanding…"
    mc "Isn’t resolution."
    "{color=#32CD32}{b}ENDING ROUTE PENDING{/b}{/color}"

    return