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

    scene black
    with fade
    pause 1.5

# SCENE 2
    scene cafeteria #Support Wing
    with dissolve

    "Mira sits alone, surrounded by floating repair drones."
    show mira sad2 at center with dissolve
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

    scene black
    with fade
    pause 2.5

# SCENE 3
    scene mspythonlab # Restricted Zone
    with dissolve

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
    "Mira turns."
    show mira happy
    mira "I was hoping you wouldn’t come."
    "Silence crashes."

# SCENE 4
    "Mira gestures."
    "Hundreds of simulations unfold mid-air."
    "Academy destroyed."
    "Students erased."
    "Bugs overrunning the system."
    "Again. {p}And again. {p}And again."

    show mira angry-nosign
    mira "I ran every condition."
    # CODE
    mira "There was only one path where everyone lived."
    return