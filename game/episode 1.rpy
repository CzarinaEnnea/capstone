# TODO: Change sprites and bg + animation.
#       Change visual aids

label episode1:
# TEST

    scene arena
    show doctorbyte at right
    with dissolve

    dr "Hi! This is a test"

    show doctorbyte sad at left with move

    dr "Do you hate me?!"

    show doctorbyte sad at slightleft with move

    dr "HaH!"

    show doctorbyte sad at slightright with move


# SCENE 1

    scene futuristic skyline
    with dissolve

    "A sleek hovertrain glides through a neon sky. The colossal Code Academy Nexus floats above the city — a fortress of glowing circuits and holographic towers."

    mc "They say if you can code it, you can create it."
    mc "At Code Academy Nexus, code is reality."
    mc "And today… it’s my first day."

    "The hovertrain doors slide open. [name] steps out, adjusting [their] backpack and looking around in awe."

    mc "Whoa… this place looks like a computer and a cathedral had a baby."
    
    "{color=#a14ae9}???{/color}" "And you must be the new kid who talks to themself."

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

    show mspython at slightleft
    with Dissolve(1.0)

    mspy "Headmaster, I’ll take it from here."

    show doctorbyte happy

    dr "The class is yours, Professor. Don’t melt too many brains on the first day."

    hide doctorbyte with dissolve
    "Dr. Byte fades out, leaving the place glowing with holographic light."


# SCENE 2: Syntax 101 – The First Spell

    scene classroom
    with dissolve

    "The students take their seats. Floating keyboards and holographic code scroll across the room."

    show mspython neutral
    with dissolve

    mspy "Welcome, young coders."
    mspy "Today, we begin with the most sacred of all spells."

    show mspython happy
    mspy "The {b}print(){/b} command!"

    "She waves her hand and code appears in the air."

    show mspython neutral at slightright with move

    show text1 at top_left_space #CHANGE THIS
    with dissolve

    mspy "This, my students, is your first incantation the spell that lets you speak to the machine."

    # show mspy smile
    # with dissolve

    mspy "Now, [name] tell me, what happens when this line is executed?"

    menu:
        "It prints “Hello, World!”":
            mc "It prints “Hello, World!” like telling the computer to say hello."
            mspy "Excellent! You’ve spoken your first line of Python with grace."
            mspy "A humble start… yet every coder’s journey begins with this very phrase."
            cyra "Congrats, newbie! You made the computer talk — and it didn’t roast you." #mock applause
            mc "Thanks… I think?"
            mspy "Do not underestimate simplicity, [name]. Even a whisper of logic can reshape reality."

            "{=gold}Syntax Confidence +2{/gold}"
            $ change_confidence(+2)

        "It explodes the computer":
            mc "It explodes the computer?"
            "The class bursts into laughter. Ms. Py Thon crosses her arms, amused."
            mspy "Ah, creativity — but no. This is Python, not Michael Bay Studios."
            cyra "Boom! First mistake of the semester." #snickers
            mspy "A safe answer would be wiser next time, [Ms][name]."

            "{=red}Syntax Confidence –1{/red}"
            $ change_confidence(-1)
            
        "It creates a cat video":
            mc "It creates a cat video?"
            cyra "Ha! I wish! If that worked, I’d have infinite playlists."
            mspy "Perhaps one day when you master APIs… but for now, no cats — only code."

            "{=red}Syntax Confidence –1{/red}"
            $ change_confidence(-1)

    # "Your Syntax Confidence: [syntaxConfidence]"

    mspy "Python is one of the world’s most flexible programming languages. Created by Guido van Rossum and released in 1991, it’s used for:"

    # Show image CHANGE THIS - Web development 🖥️
    hide text1
    show text2 at top_left_space 
    with dissolve

    luna "Python: adaptive, readable, and statistically likely to dominate human education."
    astra "Uh huh."
    mspy "Quite right, Luna. Python’s beauty lies in its simplicity."
    mspy "It reads almost like English — and runs instantly."
    mspy "That means your experiments come alive as you type them."
    mc "So… it’s easy to start with, but powerful enough for big stuff?"
    mspy "Exactly. It supports procedural, object-oriented, and functional programming — three paths, one language."

    "She gestures, and glowing indentation marks appear midair."

    mspy "Unlike many languages, Python doesn’t use semicolons or braces. It uses {b}indentation{/b} — spacing — to define code blocks."
    mc "So… even the spaces matter?"
    mspy "Yes. In Python, indentation isn’t optional. Disrespect it… and you’ll summon chaos."

    "The lights flicker. A faint growling noise is heard — a “bug” forming in the code."

    show cyra happy
    cyra "Oh, fun. Evil spaces. Love that."

    mspy "When you name a variable in Python, you can’t use spaces because Python would get confused — it would think you’re writing two separate things instead of one name."
    mspy "The underscore (_) acts like a small space — it helps make your variable name easy to read without breaking Python’s rules. Watch"

    hide text2
    show text1 at top_left_space
    with dissolve

    mspy "Instead, we do:"

    # show text2 at top_right_space
    # with dissolve

    mspy "Take note of this. Then you’ll enjoy your next challenge."

    "She waves her hand. The classroom morphs into a holographic battle arena — walls of blue code hum with energy"

    hide text1
    # hide text2
    with dissolve

    scene arena #or fade to black
    with dissolve

    mspy "Prepare yourselves for your first challenge anytime soon… {w}{b}The Syntax Bug Simulation{/b}. {w}Fix the code, or the Bug will replicate."
    mc "Bring it on."
    cyra "Just don’t explode the computer this time, rookie."
    mspy "Well then enjoy your break time" #smirks

    scene black
    with dissolve
    pause 0.5

    scene cafe
    with fade

    "After Class"

    mc "I fell drained already. Well atleast I can finally eat!"


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
    luna "Excuse you! That was one time. And it was fabulous."
    mira "You’re… kind of brave for surviving your first class, though. Ms. Py Thon can be scary."
    mc "Yeah, she smiled once — the projector flickered."

    show cyra happy
    show kai happy
    show luna happy
    show mira happy
    show astra happy
    "(Everyone laughs.)"

    "???" "[[Sound of Intercom Suddenly Rings]"

    mspyIntercom "Attention, Team Debugger. Before you relax too much {w}— SURPRISE QUIZZZ!"
    mspyIntercom "Let’s see if your new member can handle The Syntax Duel."
    astra "*grins* Ooooh, our favorite hazing ritual."
    kai "Not hazing. {i}Evaluation{/i}."
    luna "I brought popcorn! {w}Wait… is that allowed?"
    kai "You’ll probably spill it on the terminal again."
    cyra "Lets get this started!"

    scene classroom
    with dissolve

    mspyIntercom "Your first spell — fix this broken code: {w}{i}{size=+10}{color=#81f08aff}print(\"Hello World!){/color}{/size}{/i}"

    menu:
        "print(\"Hello World!\")":
            call question1Right
        "print('Hello World!')":
            call question1Right
        "print(Hello World!)":
            show bug at center
            $ red_effect()
            kai "Told you. Rookie nerves."
            cyra "Don’t panic! Try closing the quotes — fast!"
            with vpunch
            hide bug with dissolve
            "([name] fixes it. Bug fizzles. Team cheers.)"
            mspyIntercom "You can either use Double Quotation Marks “” or ‘’ Apostrophe to declare a string you want to print"
            "{=red}Syntax Confidence –1{/red}"
            $ change_confidence(-1)
        
    mspyIntercom "Assign 10 to variable x. In a Variable we can store data types we want for example let it be a number, a string and so on, first you have to name your variable it can be a string or a single letter."
    
    menu:
        "x = 10":
            kai "Simple. Efficient. You’d make a good teammate."
            "+1 Kai Affection"
            $ change_kaiAffection(+1)
            luna "You’re on fire! But like... in a non-combustion way!"
            astra "Careful, Kai. Compliments look good on you." #teasing
            "{=gold}Syntax Confidence +2{/gold}"
            $ change_confidence(+2)

        "int x = 10":
            call question2Wrong
        "x : 10":
            call question2Wrong
    
    mspyIntercom "Which of these can Python do?"

    menu:
        "Web applications":
            call question3Right
        "Control robots":
            call question3Right
        "Make coffee":
            mspyIntercom "If Python brewed coffee, I’d be a billionaire."
            "(Team laughs, [name] gets minor penalty.)"
            cyra "Well go for coffee break later. For now focus."
            "{=red}Syntax Confidence –1{/red}"
            $ change_confidence(-1)

    mspyIntercom "Which is true about Python syntax?"

    menu:
        "Uses indentation for scope":
            kai "Your precision is admirable."
            cyra "And that focus... kinda cool. You listen in class I see."
            "([name] blushes)"
            "{=gold}Syntax Confidence +2{/gold}"
            $ change_confidence(+2)

        "Uses curly braces":
            call question4Wrong

        "Needs semicolons":
            call question4Wrong

    luna "Okay, okay, my turn!"
    luna "What’s the name of the function used to display text?"

    menu:
        "prnt ()":
            call question5Wrong
        "print()":
            luna "YES! You pass the Luna test! You’re officially 90\% certified cool!"
            "(+1 Luna Friendship)" #luna flag?
            "{=gold}Syntax Confidence +2{/gold}"
            $ change_confidence(+2)
        "speak()":
            call question5Wrong

    mspyIntercom "You’ve all performed… adequately. Some of you even excelled."
    mspyIntercom "Tomorrow, we explore the {b}Variables of Destiny.{/b}"
    astra "(stretching) Destiny sounds boring. Can we just fight more Bugs?"
    cyra "Perfect as always…"
    kai "Discipline before battle, Astra."
    mira "He says, as if he’s not secretly obsessed with perfect syntax."
    cyra "You did great really great."
    luna "Group selfie before the next apocalypse! Say {w}{size=+10}{color=#81f08aff}print(\"Cheese!\"){/color}{/size}!"

    scene groupPhoto
    with dissolve
    "(They pose. Flash of neon light. Laughter.)"

    "And just like that, I wasn’t alone anymore."
    "A team of geniuses, chaos gremlins, and possible love interests."
    "At Code Academy Nexus… even friendship is coded in Python."
    return

# Quizzes Other Branch
label question1Right:
    mspyIntercom "Well done. Your syntax is strong. Print is used to show the strings you want to say strings are the words."
    astra "Nice reflexes, rookie. Fast and clean — just my type."

    kai "Consistent. I like that."
    "+1 Kai Affection"
    $ change_kaiAffection(+1)

    cyra "You did it! The Bug didn’t even hiss at you!"
    "{=gold}Syntax Confidence +2{/gold}"
    $ change_confidence(+2)
    return

label question2Wrong:
    kai "Yawn. Even my grandma can assign variables."
    mira "It’s okay, everyone starts somewhere!"
    "(A mini Bug appears, shaped like a “?”; player zaps it.)"
    show cyra happy
    cyra "Dont mind him, when he was new he was even worse"

    "{=red}Syntax Confidence –1{/red}"
    $ change_confidence(-1)
    return

label question3Right:
    luna "Imagine if it could make coffee, though."
    astra "I’d marry Python."
    "(Kai raises eyebrow.)"
    astra "Relax, Kai— it’s just a language."

    "{=gold}Syntax Confidence +2{/gold}"
    $ change_confidence(+2)
    return

label question4Wrong:
    kai "Pfft. Rookie mistake."
    luna "Hey, {b}Kai{/b}, remember when you broke your code with 18 curly braces?"
    kai "That was style."
    cyra "Sure it was……."
    astra "Nice try though [name]"
    "{=red}Syntax Confidence –1{/red}"
    $ change_confidence(-1)
    "(Team laughs; Bug spawns and gets squashed.)"
    return

label question5Wrong:
    luna "Awww, close! But hey, you tried! Here, have a sticker that says “Mostly Human.”"
    "{=red}Syntax Confidence –1{/red}"
    $ change_confidence(-1)
    return