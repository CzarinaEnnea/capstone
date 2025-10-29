# TODO: Change sprites and bg + animation.
#       Change visual aids

label episode1:
# SCENE 1

    scene futuristic skyline
    with dissolve

    show text "Episode 1 - “Welcome to Code Nexus Academy”" at truecenter with dissolve
    pause 2
    hide text with fade

    play music "audio/opening.ogg"

    "A sleek hovertrain glides through a neon sky. The colossal Code Academy Nexus floats above the city — a fortress of glowing circuits and holographic towers."

    mc "They say if you can code it, you can create it."
    mc "At Code Academy Nexus, code is reality."
    mc "And today… it’s my first day."

    "The hovertrain doors slide open. [name] steps out, adjusting [their] backpack and looking around in awe."

    mc "Whoa… this place looks like a computer and a cathedral had a baby."
    
    "{color=#a14ae9}???{/color}" "And you must be the new kid who talks to [them]self."

    "A girl with purple-streaked hair and a mischievous grin appears, holding a holo-tablet."

    show cyra neutral
    with dissolve

    cyra "Cyra Byte. Frontend Division. Top of the leaderboard, breaker of hearts, destroyer of broken CSS."
    mc "Uh… nice to meet you?"
    cyra "Nice to meet you, too, mystery newbie. You’ve got that first-day panic look. Adorable."
    mc "It’s called confidence. You’ll see."
    cyra "Mhm. We’ll see how long that lasts when you meet the Headmaster."

    "Suddenly, the air shimmers with light. A tall man in a glowing white coat appears, teleporting in with calm authority."

    show doctorbyte neutral at left
    with dissolve

    dr "Good morning, students. No teleportation mishaps this time, I hope."

    show cyra happy at slightright with move
    cyra "No promises, Headmaster."

    show doctorbyte neutral
    dr "I see you’ve met our new recruit. [name], isn’t it?"
    mc "Yes, sir! Reporting for— uh— coding?"
    show doctorbyte happy
    dr "Excellent enthusiasm. Welcome to Code Academy Nexus — where syntax becomes strength."
    show doctorbyte neutral
    dr "Now, you’ll be joining Professor Py Thon’s class. Don’t let her brilliance intimidate you."

    "A ripple of neon light forms into a tall woman with emerald lines of code flowing through her hair. Her eyes glow softly with wisdom."

    show mspython neutral at slightleft
    with Dissolve(1.0)

    mspy "Headmaster, I’ll take it from here."

    show doctorbyte happy

    dr "The class is yours, Professor. Don’t melt too many brains on the first day."

    hide doctorbyte with dissolve
    "Dr. Byte fades out, leaving the place glowing with holographic light."

    stop music fadeout 2.0


# SCENE 2: Syntax 101 – The First Spell

    scene classroom
    with dissolve

    "The students take their seats. Floating keyboards and holographic code scroll across the room."

    show mspython neutral
    with dissolve

    mspy "Welcome, young coders."
    mspy "Today, we begin with the most sacred of all spells."

    show mspython vhappy
    mspy "The {b}print(){/b} command!"

    "She waves her hand and code appears in the air."

    show mspython neutral at slightright with move

    show ep1-scn2-txt1 at top_left_space
    with dissolve

    mspy "This, my students, is your first incantation the spell that lets you speak to the machine."
    mspy "Now, [name] tell me, what happens when this line is executed?"

    menu:
        extend ""

        "It prints “Hello, World!”":
            mc "It prints “Hello, World!” like telling the computer to say hello."
            show mspython vhappy
            mspy "Excellent! You’ve spoken your first line of Python with grace."
            mspy "A humble start… yet every coder’s journey begins with this very phrase."

            show cyra neutral at right with dissolve
            cyra "Congrats, newbie! You made the computer talk {w}— and it didn’t roast you." #mock applause
            mc "Thanks… I think?"
            show mspython neutral
            mspy "Do not underestimate simplicity, [name]. Even a whisper of logic can reshape reality."

            "{=gold}Syntax Confidence +2{/gold}"
            $ change_confidence(+2)

        "It explodes the computer":
            mc "It explodes the computer?"
            show mspython surprised
            "The class bursts into laughter. Ms. Py Thon crosses her arms, amused."
            mspy "Ah, creativity — but no. This is Python, not Michael Bay Studios."
            show cyra happy at right with dissolve
            cyra "Boom! First mistake of the semester."
            show mspython neutral
            mspy "A safe answer would be wiser next time, [Ms][name]."

            "{=red}Syntax Confidence –1{/red}"
            $ change_confidence(-1)
            
        "It creates a cat video":
            mc "It creates a cat video?"
            show cyra neutral at right with dissolve
            cyra "Ha! I wish! If that worked, I’d have infinite playlists."
            show mspython sad
            mspy "Perhaps one day when you master APIs… but for now, no cats —only code."

            "{=red}Syntax Confidence –1{/red}"
            $ change_confidence(-1)

    show mspython neutral
    hide cyra with dissolve
    mspy "Python is one of the world’s most flexible programming languages. Created by Guido van Rossum and released in 1991, it’s used for:"

    hide ep1-scn2-txt1
    show ep1-scn2-txt2 at top_left_space 
    with dissolve

    mspy "Web development, Software Creation, Mathematics and yes Automation and Scripting!"

    show luna neutral at right with dissolve
    luna "Python: adaptive, readable, and statistically likely to dominate human education."

    show astra neutral:
        subpixel True xpos 0.84 
        Null(411.0, 1080.0)
        'astra neutral' with dissolve

    astra "Uh huh."
    mspy "Quite right, Luna. Python’s beauty lies in its simplicity."
    mspy "It reads almost like English — and runs instantly."
    mspy "That means your experiments come alive as you type them."
    mc "So… it’s easy to start with, but powerful enough for big stuff?"
    mspy "Exactly. It supports procedural, object-oriented, and functional programming — three paths, one language."

    "She gestures, and glowing indentation marks appear midair."

    hide astra
    hide luna
    hide ep1-scn2-txt2
    show ep1-scn2-txt2-1 at top_left_space
    with dissolve

    show mspython neutral
    mspy "Don't worry about what this code means yet. Focus on the indention or space below the \"{size=+10}{color=#81f08aff}def greet():{/color}{/size}\"."
    mspy "Unlike many languages, Python doesn’t use semicolons or braces. It uses {b}indentation{/b} — spacing — to define code blocks."
    mc "So… even the spaces matter?"
    mspy "Yes. In Python, indentation isn’t optional. Disrespect it… and you’ll summon chaos."

    hide ep1-scn2-txt2-1
    show ep1-scn2-txt2-2 at top_left_space
    $ red_effect()

    "The lights flicker. A faint growling noise is heard — a “bug” forming in the code."

    show cyra happy at right with dissolve
    cyra "Oh, fun. Evil spaces. Love that."

    hide ep1-scn2-txt2-2
    show ep1-scn2-txt3 at top_left_space
    with dissolve

    show cyra neutral
    mspy "When you name a variable in Python, you can’t use spaces because Python would get confused — it would think you’re writing two separate things instead of one name."
    mspy "The underscore (_) acts like a small space — it helps make your variable name easy to read without breaking Python’s rules. Watch."

    mspy "Instead, we do:"

    show ep1-scn2-txt4 at top_right_space
    with dissolve

    mspy "Take note of this. Then you’ll enjoy your next challenge."

    "She waves her hand. The classroom morphs into a holographic battle arena — walls of blue code hum with energy."

    hide text1
    # hide text2
    with dissolve

    scene arena #or fade to black
    with dissolve

    mspy "Prepare yourselves for your first challenge anytime soon… {w}{b}The Syntax Bug Simulation{/b}. {w}Fix the code, or the Bug will replicate."
    mc "Bring it on."
    cyra "Just don’t explode the computer this time, rookie."
    mspy "Well then enjoy your break time."

    scene black
    with dissolve
    pause 0.5

    scene cafe
    with fade

    "After Class"

    mc "I felt drained already. Well atleast I can finally eat!"


# Scene 3: “Meeting the Crew – Syntax Duel and Team Debugger”

    "After Ms. Py Thon’s class, my brain feels like scrambled code. The Student Lounge hums with energy — half café, half neon battlefield."
    "At the center table, five students argue over a glowing cube of light."
    "A sign above their table reads:"
    "{size=+10}TEAM DEBUGGER – We Don’t Panic, We Patch.{/size}"

    mc "...{w}Guess that’s my new squad."

    show cyra neutral with dissolve
    show cyra happy at slightright with move

    cyra "Oh! Everyone, meet our new recruit!!"

    show astra neutral at slightleft with dissolve
    astra "Oh, look. The new one survived Ms. Py Thon’s lecture that’s worth a celebration. {w}I’m Astra."

    show kai neutral at left with dissolve
    kai "Barely. I saw three students combust from syntax errors."

    show luna neutral at right with dissolve
    show luna happy at slightright with move
    show cyra surprised at center with move
    with hpunch

    luna "{b}Combust?! {w=1}I missed that again?!{/b} {w=1}By the way I’m Luna Hehe."

    show cyra angry
    cyra "{size=+10}{b}Hey!{/b}{/size}"

    show kai happy
    kai "Figures. Another bright-eyed beginner joining the chaos. {w}Kai by the way."

    show cyra neutral
    show kai neutral
    show mira neutral at right with dissolve
    mira "{cps=20}H-Hi there…{/cps} {w}I’m Mira Bite. {w}{cps=20}I handle support and… {w=1}um… {w=1}tea refills.{/cps}"



    menu:
        "Nice to meet you all! I’m [name] and ready to code my destiny.":
            show kai happy
            show astra happy
            "You saw Kai nods approvingly and Astra winks towards you"

        "Wait—did she say students combusted?":
            show luna surprised
            "Luna giggles at you and pretends to explode."
            show luna happy
            luna "Kabooom!"

        "Free tea? Best team ever.":
            show mira neutral: #or shy or surprised
                linear 0.7 xpos 0.9
            "You saw Mira turning red and hides herself behind Luna."

    show luna neutral
    astra "So, rookie, which division you thinking of joining? Frontend glam? Backend chaos? Or full-stack madness?"

    show cyra happy
    cyra "Relax, [theyre] still new."

    mc "Not sure yet. Still figuring out if I’m more “function” or “fashion.”"

    show luna happy
    luna "*gasp* {w}Be both! A stylish debugger! I can make you a glowing jacket that says {w}{i}{size=+10}{cps=20}{color=#81f08aff}while(True): Slay(){/color}{/cps}{/size}{/i}!"

    show kai sad
    show cyra sad

    "{color=#618ef0}Kai{/color} & {color=#a14ae9}Cyra{/color}" "…Please don’t."

    kai "Ignore Luna. Her projects usually end in smoke or spontaneous dancing LEDs."

    luna "Excuse you! That was one time. And it was {i}fabulous.{/i}"
    mira "You’re… {w}kind of brave for surviving your first class, though. Ms. Py Thon can be scary."
    mc "Yeah, she smiled once — the projector flickered."

    show cyra happy
    show kai happy
    show luna happy
    show mira happy
    show astra happy
    "(Everyone laughs.)"

    "???" "[[Sound of Intercom Suddenly Rings]"

    mspyIntercom "Attention, Team Debugger. Before you relax too much {w}— SURPRISE QUIZZZ!"

    show cyra surprised
    show kai surprised
    show luna surprised
    show mira surprised
    show astra surprised

    mspyIntercom "Let’s see if your new member can handle The Syntax Duel."
    show astra happy
    show mira neutral
    astra "*grins* Ooooh, our favorite hazing ritual."
    show kai neutral
    kai "Not hazing. {i}Evaluation{/i}."
    show luna neutral
    luna "I brought popcorn! {w}Wait… is that allowed?"
    kai "You’ll probably spill it on the terminal again."
    show cyra neutral
    cyra "Lets get this started!"

    scene classroom
    with dissolve

    #   QUESTION 1
    mspyIntercom "Your first spell — fix this broken code: {w}{i}{size=+10}{color=#81f08aff}print(\"Hello World!){/color}{/size}{/i}"
    
    menu:
        extend ""
        
        "print(\"Hello World!\")":
            call question1Right from _call_question1Right
        "print('Hello World!')":
            call question1Right from _call_question1Right_1
        "print(Hello World!)":
            show bug at top
            $ red_effect()

            show kai neutral at left with dissolve
            kai "Told you. Rookie nerves."
            show cyra surprised at slightright with dissolve
            cyra "Don’t panic! Try closing the quotes — fast!"
            with vpunch
            hide bug with dissolve
            "([name] fixes it. Bug fizzles. Team cheers.)"
            show cyra neutral
            mspyIntercom "You can either use Double Quotation Marks {=code}“”{/code} or {=code}‘’{/code} Apostrophe to declare a string you want to print"
            "{=red}Syntax Confidence –1{/red}"
            $ change_confidence(-1)

    #   QUESTION 2    
    mspyIntercom "Assign 10 to variable x. In a Variable we can store data types we want for example let it be a number, a string and so on. First you have to name your variable it can be a string or a single letter."
    mspyIntercom "I'll explain it more in a later class so don't worry if you got it wrong. {w}Now go Assign 10 to variable x"
    
    menu:
        extend ""

        "x = 10":
            show kai happy
            kai "Simple. Efficient. You’d make a good teammate."
            $ change_kaiAffection(+1)
            "{=gold}Kai’s Affection +1{/=gold}"
            show luna happy at center with dissolve
            luna "You’re on fire! But like... in a non-combustion way!"
            show astra neutral at slightleft with dissolve
            astra "Careful, Kai. Compliments look good on you." #teasing
            "{=gold}Syntax Confidence +2{/gold}"
            $ change_confidence(+2)

        "int x = 10":
            call question2Wrong from _call_question2Wrong
        "x : 10":
            call question2Wrong from _call_question2Wrong_1
    
    #   QUESTION 3
    mspyIntercom "Which of these can Python do?"

    menu:
        extend ""

        "Web applications":
            call question3Right from _call_question3Right
        "Control robots":
            call question3Right from _call_question3Right_1
        "Make coffee":
            mspyIntercom "If Python brewed coffee, I’d be a billionaire."
            "(Team laughs, [name] gets minor penalty.)"
            show cyra sad
            cyra "Well go for coffee break later. For now focus."
            "{=red}Syntax Confidence –1{/red}"
            $ change_confidence(-1)

    #   QUESTION 4
    mspyIntercom "Which is true about Python syntax?"

    menu:
        extend ""

        "Uses indentation for scope":
            show kai happy
            kai "Your precision is admirable."
            show cyra surprised 
            cyra "And that focus... kinda cool. You listen in class I see."
            "([name] blushes)"
            "{=gold}Syntax Confidence +2{/gold}"
            $ change_confidence(+2)
            show cyra neutral

        "Uses curly braces":
            call question4Wrong from _call_question4Wrong

        "Needs semicolons":
            call question4Wrong from _call_question4Wrong_1

    show luna happy at center with dissolve
    luna "Okay, okay, my turn!"
    show luna neutral
    luna "What’s the name of the function used to display text?"

    menu:
        extend ""

        "prnt ()":
            call question5Wrong from _call_question5Wrong
        "print()":
            
            show luna happy:
                subpixel True 
                parallel:
                    Null(411.0, 1080.0)
                    'luna happy'
                parallel:
                    ypos 1.0 
                    linear 0.14 ypos 1.04 
                    linear 0.17 ypos 1.0 
            with Pause(0.60)
            show luna happy:
                ypos 1.0
            luna "YES! You pass the Luna test! You’re officially 90\% certified cool!"
            "(+1 Luna Friendship)" #luna flag?
            "{=gold}Syntax Confidence +2{/gold}"
            $ change_confidence(+2)
        "speak()":
            call question5Wrong from _call_question5Wrong_1

    mspyIntercom "You’ve all performed… adequately. Some of you even excelled."
    mspyIntercom "Tomorrow, we explore the {b}Variables of Destiny.{/b}"
    show astra neutral at slightleft with dissolve
    astra "(stretching) Destiny sounds boring. Can we just fight more Bugs?"
    show cyra neutral
    cyra "Perfect as always…"
    show kai neutral
    kai "Discipline before battle, Astra."
    show mira neutral at right with dissolve
    mira "He says, as if he’s not secretly obsessed with perfect syntax."
    show cyra happy
    cyra "You did great really great."
    show luna happy at center with dissolve
    luna "Group selfie before the next apocalypse! Say {w}{size=+10}{color=#81f08aff}print(\"Cheese!\"){/color}{/size}!"

    scene groupPhoto
    with dissolve
    "(They pose. Flash of neon light. Laughter.)"

    "And just like that, I wasn’t alone anymore."
    "A team of geniuses, chaos gremlins, and possible love interests."
    "At Code Academy Nexus… even friendship is coded in Python."

# SCENE 4

    scene classroom
    with dissolve

    "Morning light streams through the digital windows of Code Nexus Academy."
    "After a long night of debugging simulations, the class gathers once again in {b}Ms. Py Thon’s Command Lab{/b}. Ready to dive deeper into the logic that powers their world."

    show mspython neutral
    with dissolve

    mspy "(Clapping her hands — and three glowing orbs float into the air.) {p}Good morning, little coders! Today, we explore the heart of every spell {w=1.5}— I mean, script {w=0.5}— in Python!"

    show cyra at right
    with dissolve
    cyra "Wake up Ms is here."
    mc "(Grinning, still sleepy.) {p}Uh… can the heart be caffeinated first?"

    show astra at slightright
    with dissolve
    astra "It's only the second day, and you're already sleeping LOL."

    show kai at left
    with dissolve
    kai "(Snickers.) {p}Guess someone didn’t def their sleep last night."

    show mspython neutral
    mspy "Ha! Save your excuses for the compiler. Now open your command lines!"

    show ep1-scn4-txt0 at top_left_space
    with dissolve

    mspy "As we learned before, Python syntax can be executed right in the command line, like so:"

    hide ep1-scn4-txt0
    show ep1-scn4-txt1 at top_left_space
    mspy "Or, by running it in a .py file through the server. It’s like two paths to the same spell."
    cyra "So basically… It’s like summoning magic either from your hand or your spellbook?"
    mspy "Exactly, my fiery apprentice! Python is both elegant and flexible."

    hide ep1-scn4-txt1
    show ep1-scn4-txt2-1 at top_left_space

    mspy "Now — behold the sacred rule: {i}Indentation matters!{/i}"

    hide ep1-scn4-txt2-1
    show ep1-scn4-txt2 at top_left_space

    mspy "If you skip the indentation, Python won’t forgive you."
    drIntercom "Neither will I."
    "Everyone" "(Laughs nervously.)"

    mspy "The number of spaces is your choice, but consistency is the key. {w}You must never mix your indentation styles… or the code will crumble!"
    mc "So, it’s kind of like teamwork? Everyone needs to keep their spacing aligned?"
    kai "Deep. Didn’t think you had that in you."
    cyra "Guess our hero’s got some brain cells after all."

    hide ep1-scn4-txt2
    show ep1-scn4-txt3-1 at top_left_space

    mspy "In Python, variables are born the moment you assign them a value — no declarations needed!"

    hide ep1-scn4-txt3-1
    show ep1-scn4-txt3 at top_left_space

    mspy "And comments begin with a {=code}#{/code}. It’s like whispering to your code — only you can hear it."

    hide ep1-scn4-txt3
    show ep1-scn4-txt4 at top_left_space

    kai "So… a comment’s like a secret message in a bottle?"
    mspy "Exactly, Kai. For once, you’re insightful."

    show cyra surprised

    cyra "Wait, so if I type {=code}# Cyra is awesome{/code}, it doesn’t actually do anything?"
    astra "You’re the only one who can see it, Cyra."
    mspy "Only boosts your ego, dear."

    hide ep1-scn4-txt4
    hide mspython
    hide kai
    hide cyra
    hide astra
    with dissolve

    "{b}After Class – Free Interaction Scene{/b}"
    "The class ends, and the students scatter. You can choose who to talk to before leaving."
    "Who do you want to talk to?"
    menu:
        extend ""

        "Talk to Cyra":
            call talkToCyra
        "Talk to Kai":
            call talkToKai
        "Talk to Ms. Py Thon":
            call talkToMsPython
        "Talk to Dr. Byte (via HoloCall)":
            call talkToDrByte
        "Talk to Astra":
            call talkToAstra

    "As class ends, you feel a small spark — not just of code, but connection."
    "Maybe this academy isn’t just about fighting bugs…"
    "Maybe it’s about the people who debug your heart."

# SCENE 5
    scene training chamber
    with dissolve

    "After yesterday’s lesson on syntax and indentation, today’s session promises something new — something powerful"
    
    return



# Scene 3 Quizzes Other Branch
label question1Right:
    mspyIntercom "Well done. Your syntax is strong. Print is used to show the strings you want to say strings are the words."

    show astra at slightleft with dissolve
    astra "Nice reflexes, rookie. Fast and clean — just my type."

    show kai happy at left with dissolve
    kai "Consistent. I like that."
    $ change_kaiAffection(+1)
    "{=gold}Kai’s Affection +1{/=gold}"

    show cyra happy at slightright with dissolve
    cyra "You did it! The Bug didn’t even hiss at you!"
    "{=gold}Syntax Confidence +2{/gold}"
    $ change_confidence(+2)
    return

label question2Wrong:
    show kai neutral
    kai "Yawn. Even my grandma can assign variables."
    show mira neutral at right with dissolve
    mira "It’s okay, everyone starts somewhere!"
    "(A mini Bug appears, shaped like a “?”; [name] zaps it.)"
    show cyra neutral
    cyra "Dont mind him, when he was new he was even worse"

    "{=red}Syntax Confidence –1{/red}"
    $ change_confidence(-1)
    return

label question3Right:
    show luna neutral at center with dissolve
    luna "Imagine if it could make coffee, though."
    show astra neutral at slightleft with dissolve
    astra "I’d marry Python."
    "(Kai raises eyebrow.)"
    show astra happy
    astra "Relax, Kai— it’s just a language."

    "{=gold}Syntax Confidence +2{/gold}"
    $ change_confidence(+2)
    return

label question4Wrong:
    kai "Pfft. Rookie mistake."
    show luna neutral at center with dissolve
    luna "Hey, {b}Kai{/b}, remember when you broke your code with 18 curly braces?"
    show kai happy
    kai "That was style."
    show cyra neutral
    cyra "Sure it was……."
    show astra at slightleft with dissolve
    astra "Nice try though [name]"
    "{=red}Syntax Confidence –1{/red}"
    $ change_confidence(-1)
    "(Team laughs; Bug spawns and gets squashed.)"
    return

label question5Wrong:
    show luna sad
    luna "Awww, close! But hey, you tried! Here, have a sticker that says “Mostly Human.”"
    "{=red}Syntax Confidence –1{/red}"
    $ change_confidence(-1)
    return

# Scene 4: Free Interaction Choices
label talkToCyra:
    show cyra neutral at center
    with dissolve

    mc "That was a cool metaphor earlier — the magic spell thing."
    cyra "You think so? Coding’s kinda like fire… {w}control it right, and you create something amazing."
    cyra "Lose control, and you burn your whole system."

    menu:
        "You sound like you’ve done that before.":
            show cyra happy
            cyra "Maybe once… {w}or twice. {w}You’ll learn to handle the fire someday."
            "{=gold}Cyra’s affection slightly increases.{/gold}"
            $ change_cyraAffection(+1)

        "That’s too dramatic for me.":
            cyra "Then you’ll never survive Ms. Py Thon’s next exam."
            "{i}No affection change.{/i}"
    return

label talkToKai:
    show kai neutral at center
    with dissolve

    kai "(Leaning back in his chair, smirking.) {p}So… how’s the new hero of Code Nexus liking syntax so far?"
    menu:
        "It’s kinda fun actually.":
            show kai happy
            kai "Heh, didn’t expect you to say that. Maybe you’re not as hopeless as I thought."
            "{=gold}Kai’s affection slightly increases.{/gold}"
            $ change_kaiAffection(+1)
        "Boring. I want action.":
            kai "Pfft. Patience, rookie. You can’t fight ‘Bugs’ without knowing how to debug."
            "Kai teases you. {i}No affection change.{/i}"
    return

label talkToMsPython:
    show mspython neutral at center
    with dissolve

    mc "Ms. Py Thon, you make syntax sound way cooler than it should be."
    show mspython happy
    mspy "Of course! Syntax is the melody that runs the digital universe."
    mspy "Master it, and you can {i}sing your will into the code.{/i}"

    menu:
        "That’s poetic.":
            show mspython neutral
            mspy "Coding is poetry, if you write it with care."
            "You gain respect from Ms. Py Thon."
        "That’s… kind of creepy.":
            show mspython sad
            mspy "Then you’ve never seen true beauty in logic."
            "Slight awkwardness."
    return

label talkToDrByte:
    show doctorbyte neutral at center
    with dissolve

    dr "You’re improving. Ms. Py Thon reports progress."
    mc "Really? That’s… good, I think?"
    dr "But remember — the Bugs grow stronger every time someone forgets a semicolon."
    mc "Uh, Python doesn’t use semicolons."
    dr "...."
    dr "…{w}I was testing you."

    hide doctorbyte with dissolve
    "He cuts the call..."
    "Everyone nearby bursts out laughing."
    return

label talkToAstra:
    show astra neutral at center
    with dissolve

    astra "(Leaning against the window, arms crossed, a confident grin on her face.){p}So, newbie, surviving your first code storm?"
    mc "Somehow, yeah. Though I think the real storm was Ms. Py Thon’s syntax lecture."
    show astra happy
    astra "Ha! You’ll get used to it. Syntax is the easy part {w}— it’s the logic battles that’ll fry your circuits later."

    menu:
        "Logic battles?":
            show astra neutral
            astra "Oh, you’ll see. Ever heard of a recursive loop that eats your project alive? Yeah, fun times"
            "{i}You laugh nervously.{/i}"
            show astra happy
            astra "Don’t worry. If you ever crash, I’ll show you how to reboot — in life and in code."
        "You sound like you’ve seen some chaos.":
            show astra sad
            astra "Let’s just say… I’ve debugged my share of nightmares."
            show astra neutral
            "Her tone softens for a second before she smirks again."
            astra "Stick close, rookie. You might learn more than you expect."
    return