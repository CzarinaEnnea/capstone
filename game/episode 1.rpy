# TODO: Change sprites and bg + animation.
#       Change visual aids

label episode1:
# SCENE 1

    scene salon #futuristic skyline
    with dissolve

    "A sleek hovertrain glides through a neon sky. The colossal Code Academy Nexus floats above the city — a fortress of glowing circuits and holographic towers."

    mc "They say if you can code it, you can create it."
    mc "At Code Academy Nexus, code is reality."
    mc "And today… it’s my first day."

    "The hovertrain doors slide open. [name] steps out, adjusting [their] backpack and looking around in awe."

    mc "Whoa… this place looks like a computer and a cathedral had a baby."
    
    "{color=#a14ae9}???{/color}" "And you must be the new kid who talks to themself."

    "A girl with purple-streaked hair and a mischievous grin appears, holding a holo-tablet."

    show cyra #smirking
    with dissolve

    cyra "Cyra Byte. Frontend Division. Top of the leaderboard, breaker of hearts, destroyer of broken CSS."
    mc "Uh… nice to meet you?"
    cyra "Nice to meet you, too, mystery newbie. You’ve got that first-day panic look. Adorable."
    mc "It’s called confidence. You’ll see."
    cyra "Mhm. We’ll see how long that lasts when you meet the Headmaster."

    "Suddenly, the air shimmers with light. A tall man in a glowing white coat appears, teleporting in with calm authority."

    # show drbyte
    # with dissolve

    dr "Good morning, students. No teleportation mishaps this time, I hope."
    cyra "No promises, Headmaster."

    # show drbyte smile
    dr "I see you’ve met our new recruit. [name], isn’t it?"
    mc "Yes, sir! Reporting for— uh— coding?"
    # show drbyte laugh
    dr "Excellent enthusiasm. Welcome to Code Academy Nexus — where syntax becomes strength."
    dr "Now, you’ll be joining Professor Py Thon’s class. Don’t let her brilliance intimidate you."

    "A ripple of neon light forms into a tall woman with emerald lines of code flowing through her hair. Her eyes glow softly with wisdom."

    mspy "Headmaster, I’ll take it from here."
    dr "The class is yours, Professor. Don’t melt too many brains on the first day."

    # hide drbyte
    "Dr. Byte fades out, leaving the classroom glowing with holographic light."


# SCENE 2: Syntax 101 – The First Spell

    "The students take their seats. Floating keyboards and holographic code scroll across the room."

    mspy "Welcome, young coders."
    mspy "Today, we begin with the most sacred of all spells — the {b}print(){/b} command."

    "She waves her hand and code appears in the air."

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

            # "{i}{color=#fdf57b}Syntax Confidence +2{/color}{/i}"
            "{=gold}Syntax Confidence +2{/gold}"
            $ change_confidence(+2)

        "It explodes the computer":
            mc "It explodes the computer?"
            "The class bursts into laughter. Ms. Py Thon crosses her arms, amused."
            mspy "Ah, creativity — but no. This is Python, not Michael Bay Studios."
            cyra "Boom! First mistake of the semester." #snickers
            mspy "A safe answer would be wiser next time, [Ms] [name]."

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

    #grinning
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

    # scene arena

    mspy "Prepare yourselves for your first challenge anytime soon… {b}The Syntax Bug Simulation{/b}. Fix the code, or the Bug will replicate."
    mc "Bring it on."
    cyra "Just don’t explode the computer this time, rookie."
    mspy "Well then enjoy your break time" #smirks

    scene black
    with dissolve
    pause 0.5

    scene salon #cafe
    with fade

    "After Class"

    mc "I fell drained already. Well atleast I can finally eat!"


# Scene 3: “Meeting the Crew – Syntax Duel and Team Debugger”

    "After Ms. Py Thon’s class, my brain feels like scrambled code. The Student Lounge hums with energy — half café, half neon battlefield."
    "At the center table, five students argue over a glowing cube of light."
    "A sign above their table reads:"
    "{size=+10}TEAM DEBUGGER – We Don’t Panic, We Patch.{/size}"

    mc "Guess that’s my new squad."



    return