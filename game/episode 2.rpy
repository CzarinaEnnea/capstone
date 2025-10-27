label episode2:
# SCENE 1
    scene classroom_doorway
    with fade

    show text "Operators of Fate" at truecenter with dissolve
    pause 2
    hide text with fade

    "The neon skyline of the Code Academy Nexus gleamed like a motherboard at sunrise."
    "Yesterday, I fought a monster made of syntax errors. Today, I’m back for more…"

    mc "New day, same universe. Yesterday was chaos. But today—"
    mc "Ms. Py Thon said we’ll go 'deeper.' I just hope she means spiritually and not into a debug pit again."

    # play sound "school_bell.ogg"

    show cyra happy at left
    with dissolve
    show kai neutral at right
    with dissolve
    show luna neutral at center
    with dissolve
    show mira neutral at slightleft
    with dissolve
    show astra neutral at slightright
    with dissolve

    cyra "Morning, rookie. Ready for another brain workout?"
    kai "We’ve got ‘Data Types and Operations’ on the schedule. Sounds like she’s teaching us how to store our souls in variables."
    luna "Oooh! Can we store glitter too?"
    mira "If it’s binary glitter… maybe?"
    mc "Haha! I’ll take binary glitter over binary panic any day."

    hide cyra
    hide kai
    hide luna
    hide mira
    hide astra

    "The lights dim. Ms. Py Thon materializes from floating code glyphs."

    show mspy neutral at center
    with dissolve

    mspy "Good morning, coders."
    mspy "You survived variables — now it’s time to understand what they hold."
    mspy "Today’s topic: Python’s Built-in Data Types."

    hide mspy
    with fade

#SCENE 2

#SCENE 3

#SCENE 4
    scene lounge
    with fade

    # play music "lounge_theme.ogg" fadein 2.0

    "Soft neon glows fill the Debuggers' Lounge, the hum of holographic screens buzzing in the background."
    "Steam rises from mugs of synthe-tea. Outside, the city flickers like a living circuit board under the digital sunset."
    "After surviving the Glitch Zone, the team finally breathes."

    show luna tired at left
    with dissolve
    show cyra happy at slightleft
    with dissolve
    show kai smirk at right
    with dissolve
    show mira neutral at center
    with dissolve
    show astra neutral at slightright
    with dissolve

    luna "Uggggh… my brain feels like it’s been formatted twice and recompiled with extra exhaustion."
    cyra "You did great, Luna. Especially when you tried to high-five the Boolean ghost. Very brave. Very stupid, but brave."
    luna "Hey! It looked friendly until it tried to eat my code history!"
    kai "That’s what happens when you try to debug with pure optimism."
    mc "Worked better than your 'punch the Hydra until it obeys' plan."
    kai "It was experimental logic. Sometimes violence *is* the answer… in pseudocode."
    cyra "Yeah, sure, Mr. 'divide by zero.' Real smooth operator there."
    kai "Tch. Low blow, Byte."
    "Laughter fills the lounge, echoing off the neon-lit walls."

    mira "I… I’m just glad everyone’s okay. The system was on the verge of collapse. If we’d delayed even a second longer, the Glitch could’ve—"
    "She pauses, catching herself before overanalyzing again."
    mc "You held the whole simulation together, Mira. You saved us."
    mira "O-oh… I just followed the algorithm. Anyone could’ve done it."
    astra "Not anyone. I saw your override code. That wasn’t textbook. You rewrote the logic mid-run."
    mira "It—It was just a… reflex. A patch job. Nothing special."
    "Her voice wavers slightly — her eyes flicker faintly with a red glitch, almost imperceptible."
    luna "Whoa, Mira! Your eyes just did the glow thing! So cool!"
    mira "Just—just reflection from the holo screen. I’m fine."
    cyra "You should’ve seen your face during the fight, MC. That ‘String Leech’ almost had you — until you went full coder mode. Not bad for a rookie."
    mc "Guess I’m starting to get the hang of this Python thing."
    mc "(pauses, looking around) And maybe… getting to know this team too."

    kai "Don’t get comfortable yet. Next round, I’m taking the top score back. No hard feelings."
    cyra "You mean when I take it first."
    kai "Dream on."
    luna "(throws a chip bag) Ship yourselves already!"
    cyra "Wha—?!"
    kai "What are you talking about?!"
    "Everyone bursts into laughter — except Mira, who gives a faint, strained smile."
    astra "(smirking slightly) Some things never change. Team chaos, through and through."

    # Ms. Py Thon Hologram Appears
    show mspy happy at center
    with dissolve
    # play sound "hologram_on.ogg"
    # put hologram sound here for Ms. Py Thon entrance

    mspy "Excellent work today, Debuggers. Your teamwork was… mostly functional."
    luna "(salutes dramatically) Mission accomplished, Ms. Python! No existential crises left behind!"
    mspy "(smiling faintly) Tomorrow’s module will be Operators and Conditional Statements. Prepare your minds."
    mspy "We will learn how the simplest symbols — +, -, *, /, and, or, not — can reshape digital reality itself."

    cyra "Oh great. Math with consequences."
    kai "Oh joy. Logic puzzles. My favorite way to suffer."
    luna "Oh no… homework."
    mira "(quietly) Logic defines fate. Every choice… changes the outcome."
    astra "(watching her carefully) Hmm. Spoken like someone who’s seen both sides of the code."
    mira "(startled) I—I didn’t mean—never mind."

    "The atmosphere shifts — subtle tension beneath the glow. MC looks between them, uneasy."

    # --- Optional Interactions ---
    menu:
        "What will you do?"
        
        "Talk to Cyra":
            mc "You really kept your cool out there. You always this confident?"
            cyra "(smiling, leaning closer) Confidence is just caffeine and chaos, rookie. But… maybe I just wanted to impress someone."
            "She laughs softly, brushing her hair aside."
            $ change_confidence(+1)
            "{=gold}Syntax Confidence +1{/=gold}"
            $ change_cyraAffection(+1)
            "{=gold}Cyra’s Affection +1{/=gold}"
            mc "(grinning) Mission accomplished."

        "Talk to Kai":
            mc "You were solid out there. Even when the Hydra bit your arm."
            kai "(chuckling) It’s fine. I’ve had worse bugs. But don’t think I’ll let you beat me again."
            kai "(grins) Next time, I’m going all in. No mercy coding."
            $ change_confidence(+1)
            "{=gold}Syntax Confidence +1{/=gold}"
            $ change_kaiAffection(+1)
            "{=gold}Kai’s Affection +1{/=gold}"
            mc "You’re on, Kai."

        "Talk to Mira":
            mc "You seemed worried during the mission. Everything okay?"
            mira "(looking distant) Just… residual static. Sometimes I see patterns where there shouldn’t be any. It’s probably nothing."
            "Her datapad flickers with corrupted code for a split second — {color=#ff4444}ACCESS DENIED{/color}."
            mc "(concerned) Mira…?"
            mira "(forcing a smile) I’m fine, really. Just tired."
            $ change_confidence(-1)
            "{=red}Syntax Confidence -1{/=red}"
            "You feel a strange unease — like something in the code just shifted."

    # --- Glitch Sequence ---
    "Suddenly, the lounge lights flicker."
    # play sound "glitch_static.ogg" 
    #play glitch sound effect
    "The holo-screen flashes — a shadowed figure appears, typing rapidly on a terminal. The image distorts before vanishing."
    luna "(sits up) Uh… anyone else see that?"
    cyra "(frowning) Probably just lag from the system reboot."
    astra "(low voice, almost to herself) No… that was intentional. Someone’s inside the code."
    mira "(gripping her datapad) ...We should go. It’s late."
    kai "Agreed. Tomorrow’s going to be a long one."
    mspy "Rest well, Debuggers. Tomorrow — we calculate destiny."
    hide mspy with dissolve

    mc "(to self) Calculate destiny, huh?"
    mc "(smiles faintly) Bring it on."

    stop music fadeout 3.0
    scene black with fade
    "To be continued..."
    return
