# User Input: Gender, Name & Pronouns

label episode0:

    "Choose your gender" 

    menu:
        "Female":
            $ female = True
        "Male":
            $ male = True

    python:
        name = renpy.input("What's your name?")
        name = name.strip() or "Alex" # removes value and replace with default

    # they(she,he), them(her,him), their(her,his), theirs(hers,his), they're(she's, he's)
    "Choose pronouns that you prefer"
    menu:
        "She/Her":
            $ They = "She"
            $ they = "she"
            $ Them = "Her"
            $ them = "her"
            $ Their = "Her"
            $ their = "her"
            $ Theirs = "Hers"
            $ theirs = "hers"
            $ Theyre = "She's"
            $ theyre = "she's"
            $ Ms = "Ms."
        "He/Him":
            $ They = "He"
            $ they = "he"
            $ Them = "Him"
            $ them = "him"
            $ Their = "His"
            $ their = "his"
            $ Theirs = "His"
            $ theirs = "his"
            $ Theyre = "He's"
            $ theyre = "he's"
            $ Ms = "Mr."
        "They/Them":
            $ They = "They"
            $ they = "they"
            $ Them = "Them"
            $ them = "them"
            $ Their = "Their"
            $ their = "their"
            $ Theirs = "Theirs"
            $ theirs = "theirs"
            $ Theyre = "They're"
            $ theyre = "they're"
            $ Ms = ""

    # Test Only
    # if female == True:
    #     "[Their] name is [name] and [theyre] a female. [They]'ll kill you"
    # else:
    #     "[Their] name is [name] and [theyre] a female. [They]'ll kill you"

    return