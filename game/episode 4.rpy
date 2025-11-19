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

    play music "main-menu.ogg"

    show cyra neutral-notab at right with dissolve
    cyra "(leaning on the table, teasing) {w}{p}Morning, rookie. You’ve got syrup on your data chip again."
    show cyra neutral2-notab
    mc "Wait—what? That’s not syrup—{w}it’s code ink!"
    mc "Great, now my bytes are sticky."

    show kai happy at left with dissolve
    kai "Sticky bytes. Wow. You’re a real mess of a coder."
    show kai happy2
    mc "At least I don’t short-circuit when someone mentions teamwork."

    show luna neutral at center with dissolve
    luna "Ooooh! Emotional operator triggered! {w}{b}MC > Kai == Burned!{/b}"
    show luna neutral2
    show mira happy at slightright with dissolve
    mira "Technically, that’s not valid syntax, Luna."
    show mira happy2
    show luna surprised
    luna "Syntax? I call it sass-tax!"

    show astra neutral at slightleft with dissolve:
        xzoom -1.0
    astra "(rolling eyes, sipping holographic tea){p}“You’re all hopeless. I’d delete you if I could… but you’d just respawn."
    show astra neutral2
    show cyra neutral-notab
    cyra "Astra, even your compliments sound like malware."
    show cyra neutral2-notab

    mspyIntercom "Students. {w}Holo-Classroom Alpha. {w}Five minutes." 
    mspyIntercom "Lesson: {i}Advanced Operators and Conditional Statements{/i}. {w}Be logical—or be lost."

    show kai neutral
    kai "She makes it sound like we’re going to war."
    show kai neutral2
    show cyra happy-notab
    cyra "Maybe we are. {w}Against your code, probably."
    show cyra happy2-notab

    show astra neutral
    astra "Then let’s not delay. I’d hate to be late for logic."

    hide astra with dissolve
    "Everyone groans, gathering their things as holographic trays vanish."

    stop music fadeout 2.0

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
            call ep4Scn2Q1Wrong from _call_ep4Scn2Q1Wrong

        "Good":
            show mspython happy
            mspy "Well done. {=code}elif{/code} adds flexibility."
            mspy "Remember, code reads from top to bottom."
            show mspython happy2
            show cyra happy-notab at right with dissolve
            cyra "You’re getting good at this, [name]. You might even beat Kai someday."
            hide mspython
            show kai neutral at slightright with dissolve:
                xzoom -1.0
            kai "As if."

        "Needs Improvement":
            call ep4Scn2Q1Wrong from _call_ep4Scn2Q1Wrong_1
    
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
    play sound "glitch_sound.ogg"
    $ red_effect()

    "Error Goblins spawn, glitchy and loud."

    show mira surprised at left with dissolve:
        xzoom -1.0
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
            play sound "punch_sound1.ogg"
            with hpunch
            hide bug
            hide ep4-scn3-txt1
            with dissolve

            show doctorbyte happy at left with dissolve
            dr "Nicely done. Subtraction operator and conditional logic—flawless."
            show doctorbyte happy2
            show luna happy at center with dissolve
            luna "Boom! Goblin de-spawned!"
            show cyra neutral at right with dissolve
            cyra "You’ve got the instincts."

        "Enemy Defeated!":
            play sound "glitch_sound.ogg"
            $ red_effect()
            luna "You made it stronger! Abort mission!"
            mspy "Let this be a reminder: Always test before you assume."

    scene black
    with fade
    pause 1.5

    scene classroom
    with dissolve
    show screen info_box("Mini-Lesson") with dissolve

    show mspython neutral at center with dissolve
    mspy "Conditional statements {=code}(if, elif, else){/code} let your code decide."
    show mspython neutral2 at right with move

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

    play music "chill_bg.ogg"

    "The Digital Garden — a serene simulation where holographic flowers bloom and neon fireflies drift through the air like floating pixels." 
    "Here the students unwind after an intense day of operator and logic lessons."

    "[name] walks along a glowing pathway lined with blue data-flowers."

    mc "After all those operator drills, I can’t tell if my brain’s processing or just overheating."
    "[name] sighs as [they] watches a holographic koi swim by."
    mc "But maybe talking to someone will help… or at least reset my mental RAM."

    menu:
        "Talk to Cyra":
            call Ep4Scn4Cyra from _call_Ep4Scn4Cyra
        "Talk to Kai":
            call Ep4Scn4Kai from _call_Ep4Scn4Kai
        "Talk to Luna":
            call Ep4Scn4Luna from _call_Ep4Scn4Luna
        "Talk to Mira":
            call Ep4Scn4Mira from _call_Ep4Scn4Mira

    scene black with fade
    pause 1.5
    scene garden #night
    with dissolve

    "Later that night the sky glows faintly with streaks of blue and violet. The others begin leaving for the dorms."
    mc "Operators, logic, conditions… Ms. Py Thon says code reflects the mind."
    mc "So what does it mean when I can’t stop thinking about the people behind it?"

    # play sound
    "A soft digital chime — footsteps approach."

    show mspython surprised at center with dissolve
    mspy "You’re still here, [name]?"
    show mspython surprised2
    mc "Just… thinking. About how logic and emotion don’t always match."
    show mspython neutral
    mspy "That’s because they never truly oppose each other."
    mspy "Logic is how we understand the world. Emotion is why we care to understand it."
    show mspython neutral2
    mc "That’s… deeper than any syntax rule."
    show mspython happy
    mspy "Perhaps. But remember — even the {i}cleanest code{/i} can hide bugs. {w}The same goes for {i}people{/i}."

    stop music fadeout 1.0

    show red with dissolve
    hide red with dissolve
    play sound "glitch_sound.ogg"
    show mspython neutral2
    "Suddenly, the neon sky flickers — static bursts across the horizon."
    
    mc "What was that?"
    show mspython neutral
    mspy "A data disturbance. {w}Someone—or something—is tampering with the Academy’s systems."
    show mspython neutral2

    play sound "glitch_sound.ogg"
    $ red_effect()
    "A faint red shimmer appears in the air — like a glitch shaped almost like a person. Long hair, sharp gaze, but too brief to see clearly."

    mc "Did you see that?!"
    show mspython neutral
    mspy "Yes… and that shadow doesn’t belong to any student."
    mspy "Be alert tomorrow, [name]. Not everything here runs on pure logic."
    hide mspython with dissolve

    "The glitch fades, leaving a faint whisper of corrupted code in the air."
    play sound "glitch_sound.ogg"
    show red with dissolve
    hide red with dissolve
    play sound "hologram.ogg"
    "A single red eye flickers open in the digital sky, then vanishes."

    scene black
    with dissolve
    pause 1.5

# SCENE 5
    scene classroom
    with dissolve

    "The students file into the glowing Holo-Classroom. Floating screens flicker alive with Python symbols."
    show mspython neutral at center with dissolve
    mspy "Good morning, coders. Today’s lesson will push your logic a step further."
    mspy "We’ll explore how Python {i}decides{/i} what to do — the art of conditional statements."

    show cyra neutral at right with dissolve
    cyra "So basically… we’re teaching computers how to think?"
    mspy "Exactly. The {b}if{/b}, {b}elif{/b}, and {b}else{/b} statements form the brain of your code."
    "She pauses, raising her hand — a holographic brain made of light appears"
    mspy "They decide what happens next based on conditions."

    show kai neutral at left with dissolve
    kai "So… if I skip breakfast, then I get cranky. Else, I’m fine."
    show luna neutral at slightright with dissolve
    luna "If Luna sees pancakes: print(‘Yum!’). Else: print(‘Sad.’)"
    show mira neutral at slightleft with dissolve
    mira "That’s actually… a perfect example."
    show mspython happy2
    mspy "Correct, Mira. Let’s try a coding version."
    
    hide mira
    hide kai
    hide luna
    hide cyra
    with dissolve

    "She gestures, and a glowing Python terminal materializes mid-air."

    show ep4-scn5-txt1 at top_left_space
    with dissolve

    show mspython neutral at slightright 
    with move

    mspy "Here’s the structure:"
    mc "So the code checks each line until one is true?"
    mspy "Exactly. Python runs {b}top-down{/b}. {w}Once it finds a {b}true{/b} condition, it {b}stops checking the rest{/b}."

    hide ep4-scn5-txt1
    show ep4-scn5-txt2 at top_left_space
    with dissolve

    mspy "Your turn, [name]. Complete this program. It determines a user’s mood based on energy level."

    menu:
        "Hyper Mode!":
            call ep4Scn5Q1Wrong from _call_ep4Scn5Q1Wrong
        "Normal Mode":
            show mspython happy
            mspy "Excellent logic. You’ve evaluated your condition precisely."
            cyra "You’re really getting the hang of this."
            kai "Hmph. Beginner’s luck."
        "Sleep Mode":
            call ep4Scn5Q1Wrong from _call_ep4Scn5Q1Wrong_1

    hide mspython
    with dissolve

    hide ep4-scn5-txt2
    with dissolve

    show doctorbyte neutral at slightright
    with dissolve

    dr "(Appears on a floating holo-screen){p}Time for some environmental testing." 
    dr "You must control the Academy’s climate with logic!"

    show ep4-scn5-txt3 at top_left_space
    with dissolve

    cyra "Temperature at 35... So?"
    mc "35 is more than 25 but less than 40…"

    menu:
        "Warning: Overheating!":
            call ep4Scn5Q2Wrong from _call_ep4Scn5Q2Wrong
        "System Stable.":
            show doctorbyte happy
            dr "Good. You prevented a meltdown."
            show mspython happy at right with dissolve
            mspy "Excellent application of logical range."
        "Cooling Activated.":
            call ep4Scn5Q2Wrong from _call_ep4Scn5Q2Wrong_1

    scene classroom
    with dissolve
    pause 1.0

    show mspython neutral at center
    with dissolve
    mspy "Remember — {=code}if, elif, and else{/code} are your best friends for decision-making. {w}They help your program respond intelligently."

    show kai neutral at left with dissolve
    kai "(leaning on desk){p}So... it’s all about testing conditions."
    kai "Like, {i}if Cyra smiles at MC: MC.blush(True). Else: MC.debug_emotions().{/i}"

    show cyra neutral at right with dissolve
    cyra "Nice try, Volt. Your syntax’s off."

    show luna neutral at slightright with dissolve
    luna "Aww, just admit it — you two are in the same ‘if’ block!"

    show mira happy at slightleft with dissolve
    mira "Or maybe the wrong loop entirely..."

    hide kai
    hide cyra
    hide luna
    hide mira
    with dissolve

    show doctorbyte at slightleft 
    with dissolve
    dr "Focus, class. Next simulation — real-time logic defense."
    mspy "Prepare yourselves. What happens next… depends on your conditions."

    scene black
    with dissolve
    pause 1.5

# Scene 6
    scene MsPythonLab
    with dissolve
    
    "The students gather in Ms. Py Thon’s lab. The walls flicker with moving code lines — like veins of light."
    show mspython neutral zorder 4 at center with dissolve
    mspy "Something’s interfering with the Academy’s mainframe. I want you to test the defense code."
    show cyra surprised-notab at right with dissolve
    cyra "Like a coding firewall?"
    mspy "Yes. But this time… the system will fight back."

    show kai happy at left with dissolve
    kai "Finally, something fun."
    show luna neutral at slightleft with dissolve
    luna "Fun? More like terrifying!"
    show mira at slightright with dissolve
    mira "I think… {w}it’ll be fine. {w}We just have to think logically."
    "Her eyes flicker faintly pink again — unnoticed"

    hide cyra
    hide kai
    hide luna
    hide mira
    with dissolve

    show ep4-scn6-txt1 at top_left_space
    with dissolve

    show mspython neutral at slightright with move
    mspy "Input your logic here. The simulation will react to your conditions."

    menu:
        "Activate Shields!":
            hide ep4-scn6-txt1
            hide mspython
            with dissolve
            
            show doctorbyte neutral at center with dissolve
            dr "Shields up! Good thinking."
            show cyra happy-notab at right with dissolve
            cyra "Nice save, [name]. You really know when to act."
            show kai happy2 at left with dissolve
            kai "Not bad. Just don’t get cocky."
        "Monitor Threat.":
            call ep4Scn6Q1Wrong from _call_ep4Scn6Q1Wrong
        "All Systems Normal.":
            call ep4Scn6Q1Wrong from _call_ep4Scn6Q1Wrong_1

    scene MsPythonLab
    with dissolve

    # play sound alarm
    $ red_effect()

    show mspython surprised at center with dissolve
    mspy "Impossible… The code is rewriting itself!"

    show doctorbyte surprised at slightleft with dissolve
    dr "Someone’s accessing the system externally. But how?"

    show cyra angry at right with dissolve #remove angry sign
    cyra "I’m locking down the firewalls— wait, something’s inside the logic chain!"

    show kai angry2 at left with dissolve #remove angry sign
    kai "Can we trace it?"

    show luna surprised at slightright with dissolve
    luna "Uhh... guys? The sky just turned purple in the simulator!"

    mc "It’s… it’s like the system’s {i}alive{/i}."

    hide kai
    hide cyra
    hide doctorbyte
    hide mspython
    hide luna
    with dissolve

    $ red_effect()
    "The holographic display flickers {w}— a figure made of static appears briefly. Long hair. Glowing violet eyes."

    "??? (distorted voice)" "If condition: chaos == True… execute."

    show astra neutral at center with dissolve
    astra "(steps forward calmly){p}That voice… I’ve heard it before."
    show mspython neutral at right with dissolve
    mspy "Explain."
    astra "Not sure. But it feels... {w}{i}familiar{/i}. {w}Like a program I once wrote."

    show mira neutral at left with dissolve
    mira "{cps=5}....."
    mira "Creepy. {w}Let’s hope it doesn’t crash us next time."
    "Her tone lingers a moment too long. The lights flicker in sync with her eyes — pink again — before returning to normal."

    hide astra
    hide mira
    show doctorbyte neutral at left
    with dissolve

    dr "Students, that’s enough for tonight. The system will stabilize... hopefully."
    mspy "Go rest. Tomorrow, we'll investigate who — or what — is inside the mainframe."

    hide doctorbyte
    hide mspython
    with dissolve

    show cyra sad-notab at right with dissolve
    cyra "This is getting serious. Just… stay close, alright?"

    show kai neutral at left with dissolve
    kai "Don’t tell me you’re scared."

    show kai neutral2
    show cyra neutral-notab
    cyra "Just cautious."

    show cyra neutral2-notab
    mc "Operators. Logic. Conditions. {w}But this... this is something deeper."
    mc "Someone’s controlling the code."

    hide kai
    hide cyra
    with dissolve

    "The camera pans up to the Academy’s central core — faint pink code lines ripple across the walls."
    "A soft whisper echoes from within the system:"
    "???" "If truth == hidden: continue program."

    scene black
    with fade

    return




# Scene 2 Quizzes Other Branch
label ep4Scn2Q1Wrong:
    show mspython sad
    mspy "Review your conditions. Logic rewards patience."
    show kai neutral at right with dissolve:
        xzoom -1.0
    kai "Told you not to rush it."
    return

# Scene 4 Talk to Others
label Ep4Scn4Cyra:
    "[name] saw Cyra sitting by the pond, typing on a holographic pad."
    show cyra neutral at center with dissolve
    cyra "Hey, [name]. You handled those operator exercises really well earlier."
    show cyra neutral2
    mc "Thanks. I’m still mixing up ‘==’ and ‘=’, though. I keep assigning when I should be comparing."
    show cyra happy
    cyra "Don’t worry. Everyone’s done that at least once."
    cyra "The important part is that you noticed it. That’s what real coders do."
    show cyra happy2
    mc "Coming from you, that means a lot."
    "She puts down her holopad and looks up at you."
    show cyra surprised-notab with dissolve
    cyra "You’ve got a good rhythm."
    show cyra neutral-notab
    cyra "You read problems the way I read front-end code {w}— through instinct."
    show cyra happy-notab
    cyra "Keep that up, and you’ll catch up to me in no time."
    show cyra happy2-notab

    mc "Oh, so it’s a challenge now?"
    show cyra neutral-notab
    cyra "Everything’s a challenge if you want to get better. Besides…"
    show cyra blush2-notab
    cyra "Coding’s more fun when there’s someone worth competing with."
    "She says it so casually, but… somehow, it sticks."
    return

label Ep4Scn4Kai:
    show kai neutral at center with dissolve
    kai "You didn’t freeze back there. Impressive."
    show kai neutral2
    mc "Were you expecting me to?"
    show kai happy
    kai "Maybe. Most first-timers panic when Ms. Py Thon brings up logic puzzles."
    mc "I guess I work better under pressure."
    show kai neutral
    kai "Good. Because this place doesn’t slow down for anyone."
    show kai neutral2
    pause 1.0
    "He pauses, looking towards the horizon"
    show kai neutral
    kai "But… you’re learning fast."
    kai "Keep that up, and maybe I’ll actually have a rival worth my time."
    show kai neutral2
    mc "So that’s your way of saying ‘good job’?"
    show kai embarassed
    kai "Don’t push it."
    mc "His words sound cold, but… I can tell he means it."
    return

label Ep4Scn4Luna:
    show luna neutral at center with dissolve
    luna "[name]! Did you know True + True equals 2?"
    show luna happy
    luna "That’s friendship math!"
    mc "That’s… actually clever, Luna."
    show luna neutral
    luna "Right?! But then False + True = 1, so maybe that’s like… {w}halfway friends?"
    mc "Or someone you just met."
    luna "Yeah! Like a {i}‘loading friendship’{/i}!"
    show luna happy
    "Luna spins around excitedly, accidentally bumping into a data bush that glitches for a second."
    with hpunch
    show luna surprised
    luna "Ooops—{w} don’t worry, nature.exe is fine!"
    mc "Every time you talk, it’s like listening to live code poetry."
    show luna neutral
    luna "Aw, thanks! I’ll add that to my variable list of compliments."
    show luna happy
    luna "(pretends to type in air) {p}Luna.Feeling = Happy."
    mc "(laughs){p}You’re one of a kind."
    return

label Ep4Scn4Mira:
    show mira neutral at center with dissolve
    mira "Oh… h-hi, [name]."
    show mira surprised
    mira "(Looks up from a holographic data notebook.){p}Sorry, I was just reviewing the syntax notes from class."
    show mira surprised2
    mc "Studying already? You never stop learning, huh?"
    show mira happy
    mira "It helps me stay calm. I liked how you used nested conditions earlier {w}that was neat."
    show mira happy2
    mc "I just tried to keep it simple."
    show mira neutral
    mira "That’s usually the best way."
    show mira sad
    mira "Sometimes, we overthink things… {w}in code and in life."
    show mira sad2
    mc "Yeah. If only we had an if-else for decision-making."
    show mira happy
    mira "If only."

    show mira neutral
    mira "{size=25}{i}If nervous == True: pretend_to_study().{/i}{/size}"
    show mira neutral2
    mc "(smiling){p}{i}And if shy == True: still adorable.{/i}"
    show mira surprised-blush
    mira "W-What? I—uh—thank you."
    show mira happy2
    "Mira looks down quickly, hiding her smile"
    mc "She’s so genuine… it’s kind of hard not to smile back."
    return

# Scene 5 Q Wrong
label ep4Scn5Q1Wrong:
    show mspython sad
    mspy "Think carefully — which range includes 65?"
    luna "Awww, the program got sleepy instead!"
    kai "You’d better recharge that logic chip."
    return

label ep4Scn5Q2Wrong:
    hide ep4-scn5-txt3
    hide doctorbyte
    with dissolve

    show luna surprised at slightright with dissolve
    luna "Oh no! We just froze the cafeteria!"
    show cyra sad-notab at right with dissolve
    cyra "That’s one way to get ice cream faster."
    return

# Scene 6 Wrong
label ep4Scn6Q1Wrong:
    hide ep4-scn6-txt1
    with dissolve

    show luna surprised at right with dissolve
    luna "Oh no, the system’s shaking!"
    show mspython angry
    mspy "Incorrect logic can trigger chaos — remember that."
    return