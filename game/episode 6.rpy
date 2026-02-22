label episode6:
# SCENE 1
    scene black
    with dissolve

    show text "{=title}Episode 6 - The One Who Chose the Loop{/title}" at truecenter with dissolve
    pause 2
    hide text with fade

    scene hallway #CONTROL HALL
    with dissolve

    play sound emergency_alarm
    $ red_effect()
    play music "audio/battle-silent_struggle.ogg" fadein 1.0 volume 0.3
    "The Emergency holograms flicker."

    show red at truecenter with dissolve
    "Loops stutter. Systems lag for half a second {w}— then recover."
    hide red with dissolve

    stop sound fadeout 3.0

    show doctorbyte angry at left with dissolve
    dr "These loop anomalies… they’re intentional."
    show doctorbyte angry2
    show mspython angry2 at right with dissolve
    mspy "They’re too precise to be bugs."
    show cyra sad-notab at slightright with dissolve
    cyra "So someone’s rewriting the Academy?"
    show kai angry2 at slightleft with dissolve
    kai "Who could even do that?"

    "The screen displays logs."
    play sound "glitch_sound.ogg"
    "{color=#ff3e3e}{b}SOURCE: UNKNOWN \nACCESS LEVEL: ROOT{/b}{/color}"

    show luna sad at center with dissolve
    luna "Root access is… {w}scary high."

    hide doctorbyte
    hide mspython
    hide cyra
    hide kai
    hide luna
    with dissolve

    pause 1.0
    mc "...."
    mc "Root access meant only one thing."
    mc "Whoever did this knew the system better than we did..."

    stop music fadeout 0.5
    scene black
    with fade
    pause 1.5

# SCENE 2
    scene cafeteria #Support Wing
    with dissolve

    "Mira sits alone, surrounded by floating repair drones."
    show mira sad2 at center with dissolve
    play music "audio/sad_Sadness and Solo-8 Bit Lofi Hip Hop.ogg" fadein 0.5 volume 0.8
    "She looks exhausted."

    mc "Mira… you missed class."
    show mira surprised
    mira "!!"
    show mira neutral
    mira "…I was fixing something."
    show cyra sad-notab at right with dissolve
    cyra "You okay? You look like you haven’t logged out in days."
    show mira neutral2
    "Mira hesitates."
    show mira sad
    mira "Do you ever wonder… {w}if we’re just repeating the same mistakes?"
    show kai neutral at left
    show cyra sad2-notab
    with dissolve
    kai "That’s… oddly philosophical for a support check."
    show kai neutral2
    show mira happy2
    "Mira smiles faintly."
    show mira happy
    mira "Sorry. Ignore me."

    pause 1.0

    show mira neutral with dissolve
    "But as she stands, {b}her terminal flickers.{/b}"
    "{color=#32CD32}{b}while future == \"collapse\": {p}{space=110}rewrite(){/b}{/color}"

    "[name] notices."
    mc "…Mira?"
    show mira surprised
    play sound "hologram.ogg"
    "She closes the terminal instantly."
    mira "It’s nothing."
    hide mira with dissolve
    show kai surprised2
    show cyra surprised2-notab
    mc "...."

    stop music fadeout 0.5
    scene black
    with fade
    pause 2.5

# SCENE 3
    scene mspythonlab # Restricted Zone
    with dissolve

    play music "audio/battle-silent_struggle.ogg" fadein 0.5 volume 0.3
    
    "A sealed gate labeled:"
    "{b}{size=+10}AUTHORIZED PERSONNEL ONLY — DR. BYTE{/size}{/b}"

    play sound emergency_alarm
    $ red_effect()
    "Alarms sound."

    mspy "Someone breached the core."
    dr "That layer… should be impossible."
    stop sound fadeout 3.0
    "The doors open anyway."
    play sound "traindoor_opening.ogg"
    "Inside {w}— {b}Mira{/b}."
    show mira serious at center with dissolve
    "Calm. {w}Focused."
    "Not surprised."

    cyra "…Mira?"
    kai "What are you doing here?"

    stop music fadeout 0.5

    "Mira turns."
    show mira happy
    mira "I was hoping you wouldn’t come."

    play music "audio/revelation_z3r0-8bitSyndrome.ogg" fadein 0.5 volume 0.4
    "Silence crashes."

# SCENE 4
    "Mira gestures."
    play sound "glitch_sound.ogg"
    $ red_effect() 

    scene mspythonlab with dissolve:
        subpixel True matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(-0.17)*HueMatrix(0.0) 

    "Hundreds of simulations unfold mid-air."
    "Academy destroyed."
    show mira serious at center with dissolve
    "Students erased."
    "Bugs overrunning the system."
    "Again. {p}And again. {p}And again."

    show mira angry-nosign
    mira "I ran every condition."
    "{color=#32CD32}{b}{cps=20}for future in all_possible_futures: {p}{space=110}if future.survives(): {p}{space=160}{cps=0}break{/b}{/color}"
    play sound "glitch_sound.ogg"
    mira "There was only one path where everyone lived."

    mc "And what was the cost?"
    show mira sad2
    "Mira looks away."
    show mira neutral
    mira "Me."

    show cyra angry at right with dissolve
    with hpunch
    cyra "You don’t get to decide that!"

    show mira happy
    mira "I already did."

# SCENE 5
    show doctorbyte sad2 at left with dissolve
    "Dr. Byte steps forward slowly."

    show doctorbyte sad
    dr "Mira… {w}stop."
    show mira neutral2 with dissolve
    "She finally looks at him — not angry, not cold."
    "Just tired."

    show mira neutral
    mira "You taught me optimization."
    mira "You taught me sacrifice."
    show mira sad
    mira "You never taught me how to live with uncertainty."
    show doctorbyte sad2 with dissolve
    show cyra sad with dissolve
    play sound "glitch_sound.ogg"
    "The system reacts to her emotions."

    hide doctorbyte
    hide mira
    hide cyra
    with dissolve
    "{color=#32CD32}{b}while world.exists(): {p}{space=110}Mira.controls(){/b}{/color}"

    show mspython sad at right with dissolve
    mspy "She’s locking the world into a single outcome."
    show kai sad at left with dissolve
    kai "She’s turning choice into a constant."

# SCENE 6
    hide mspython 
    hide kai
    with dissolve

    "Mira steps back into the core light."
    play sound "hologram.ogg"

    # DRONES
    show bug1 with dissolve:
        subpixel True ypos 0.02 
    
    show bug2 with dissolve:
        subpixel True pos (0.17, 0.37) 

    show bug3 with dissolve:
        subpixel True pos (0.49, 0.08) 

    "Her support drones reconfigure — combat-ready."

    show mira neutral with dissolve
    mira "If I become the villain…"
    pause 1.0
    show mira happy with dissolve
    mira "…then you can be the heroes."
    show mira happy2

    "She activates the protocol."
    play sound "hologram.ogg"
    "{color=#32CD32}{b}INITIATE: ABSOLUTE LOOP{/b}{/color}"

    show luna sad at right with dissolve
    luna "Mira… {w}{cps=20}please…"

    show mira sad
    mira "I’m sorry."
    show mira happy
    mira "This is the only solution that compiles."

    "{b}The system locks.{/b}"
    play sound "glitch_sound.ogg"
    $ red_effect()
    with vpunch
    "{color=#ff4444}{b}{size=+20}POINT OF NO RETURN REACHED{/size}{/b}{/color}"

    play sound "glitch_sound.ogg"
    # nvl clear
    # mcNVL "..." with dissolve
    # mcNVL "She wasn’t trying to destroy the world." with dissolve
    # mcNVL "She was trying to {b}freeze{/b} it." with dissolve

    scene black with fade
    pause 2.0
    show text "{=title}She wasn’t trying to destroy the world.{/title}" at truecenter with dissolve
    pause 2.0
    hide text with dissolve

    pause 1.0
    show text "{=title}She was trying to FREEZE it.{/title}" at truecenter with dissolve
    pause 3.0
    hide text with dissolve

    pause 1.0
    show text "{=title}When logic removes choice, someone must become the enemy.{/title}" at truecenter with dissolve
    pause 3.5
    hide text with dissolve

    show text "{=title}To be continued...{/title}" at truecenter with dissolve
    pause 2
    hide text with dissolve
    stop music fadeout 0.5
    return