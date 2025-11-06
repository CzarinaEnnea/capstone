label episode4:
# SCENE 1
    scene black
    with dissolve

    show text "Episode 4 - Conditional Hearts and Logical Storms" at truecenter with dissolve
    pause 2
    hide text with fade

    scene cafe
    with dissolve

    show text "\"In logic we trust... but in emotion, we believe.\"" at truecenter with dissolve
    pause 2
    hide text with fade

    show cyra neutral-notab at right with dissolve
    cyra "(leaning on the table, teasing) {w}{p}Morning, rookie. You’ve got syrup on your data chip again."
    show cyra neutral2-notab
    mc "Wait—what? That’s not syrup—{w}it’s code ink!"
    mc "Great, now my bytes are sticky."

    show kai neutral at left with dissolve
    kai "Sticky bytes. Wow. You’re a real mess of a coder."
    show kai neutral2
    mc "At least I don’t short-circuit when someone mentions teamwork."

    show luna neutral at center with dissolve
    luna "Ooooh! Emotional operator triggered! {w}{b}MC > Kai == Burned!{/b}"
    show mira neutral at slightleft with dissolve
    mira "Technically, that’s not valid syntax, Luna."
    luna "Syntax? I call it sass-tax!"

    show astra neutral at slightright with dissolve
    astra "(rolling eyes, sipping holographic tea){p}“You’re all hopeless. I’d delete you if I could… but you’d just respawn."
    show cyra neutral-notab
    cyra "Astra, even your compliments sound like malware."
    show cyra neutral2-notab

    mspyIntercom "Students. {w}Holo-Classroom Alpha. {w}Five minutes." 
    mspyIntercom "Lesson: {i}Advanced Operators and Conditional Statements{/i}. {w}Be logical—or be lost."

    show kai neutral
    kai "She makes it sound like we’re going to war."
    show kai neutral2
    show cyra happy-notab
    cyra "Maybe we are. Against your code, probably."

    show astra neutral
    astra "Then let’s not delay. I’d hate to be late for logic."

    hide astra with dissolve
    "Everyone groans, gathering their things as holographic trays vanish."

# SCENE 2
    scene classroom
    with dissolve

    show mspython neutral at center with dissolve
    mspy "Welcome, students. Today, we dive deeper into the language of logic {w}— Python Operators and Conditional Statements."
    mspy "They are not mere syntax. They are... choices. Rules that shape results."

    mc "So, kind of like how our decisions affect what happens to us?"

    show mspython happy
    mspy "Exactly, [name]. Every {=code}if{/code} in your life has an {=code}else{/code} waiting."

    show mspython neutral
    mspy "Now, There are different types of operators in Python." 

    show mspython neutral at slightright with move
    show ep4-scn2-txt1 at top_left_space
    with dissolve

    mspy "Arithmetic, Comparison, Logical, Assignment, and more."
    show mspython neutral2
    luna "So {=code}!={/code} means… {b}NOT{/b} equal?!"
    luna "(leans toward Mira) {p}“That’s how I feel about broccoli!\""
    mira "And yet, your lunch was 80%% green code."
    cyra "So if I write {=code}Cyra > Kai{/code}, Python would print {=code}True{/code}, right?"
    kai "Try it and watch your IDE crash."

    show mspython happy
    mspy "Focus, class. Remember—logic doesn’t play favorites."
    show mspython neutral
    mspy "Now, let’s test your logic."

    hide ep4-scn2-txt1
    show ep4-scn2-txt2 at top_left_space
    with dissolve

    mspy "[name], what will Python print?"

    menu:
        extend ""

        "Excellent":
            call ep4Scn2Q1Wrong

        "Good":
            show mspython happy
            mspy "Well done. {=code}elif{/code} adds flexibility."
            mspy "Remember, code reads from top to bottom."
            show cyra happy at right with dissolve
            cyra "You’re getting good at this, [name]. You might even beat Kai someday."
            hide mspython
            show kai neutral at slightright 
            with dissolve
            kai "As if."

        "Needs Improvement":
            call ep4Scn2Q1Wrong
    
    scene black with fade
    pause 1.5

# SCENE 3
    scene arena
    with dissolve

    show doctorbyte neutral at center with dissolve
    dr "Time to practice." 
    dr "Each of you will face a logic-based opponent." 
    dr "Defeat them using the right operator."

    hide doctorbyte
    with dissolve

    show bug at top_right_space
    $ red_effect()

    "Error Goblins spawn, glitchy and loud."

    show mira surprised at left with dissolve
    mira "T-they look angry!"

    show luna neutral at slightleft with dissolve
    luna "They smell like unclosed parentheses!"

    hide mira
    hide luna
    with dissolve

    show ep4-scn3-txt1 at top_left_space
    with dissolve

    "Choose what Python will print to defeat the bug."

    menu:
        extend ""
        "Enemy Still Alive!":
            with hpunch
            hide bug
            hide ep4-scn3-txt1
            with dissolve

            show doctorbyte neutral at center with dissolve
            dr "Nicely done. Subtraction operator and conditional logic—flawless."
            show luna happy at left with dissolve
            luna "Boom! Goblin de-spawned!"
            show cyra neutral at right with dissolve
            cyra "You’ve got the instincts."

        "Enemy Defeated!":
            $ red_effect()
            luna "You made it stronger! Abort mission!"
            mspy "Let this be a reminder: Always test before you assume."

    scene black
    with fade
    pause 1.5

    scene classroom
    with dissolve
    show screen info_box("Mini-Lesson") with dissolve

    show mspython neutral at slightright with dissolve
    mspy "Conditional statements {=code}(if, elif, else){/code} let your code decide."

    show ep4-scn3-txt2 at top_left_space with dissolve
    kai "So... kind of like relationships. If Cyra’s mad: disaster. Else: peace."
    cyra "See? Even Kai can code emotions now."

    hide screen info_box 
    scene black
    with fade
    pause 1.5

# SCENE 4
    scene garden
    with dissolve

    "The Digital Garden — a serene simulation where holographic flowers bloom and neon fireflies drift through the air like floating pixels." 
    "Here the students unwind after an intense day of operator and logic lessons."

    "[name] walks along a glowing pathway lined with blue data-flowers."

    mc "After all those operator drills, I can’t tell if my brain’s processing or just overheating."
    "[name] sighs as [they] watches a holographic koi swim by."
    mc "But maybe talking to someone will help… or at least reset my mental RAM."

    menu:
        "Talk to Cyra":
            pass
        "Talk to Kai":
            pass
        "Talk to Luna":
            pass
        "Talk to Mira":
            pass

    return

# Scene 2 Quizzes Other Branch
label ep4Scn2Q1Wrong:
    show mspython sad
    mspy "Review your conditions. Logic rewards patience."
    show kai neutral at right with dissolve
    kai "Told you not to rush it."
    return