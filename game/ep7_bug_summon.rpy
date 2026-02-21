label bug_summon_phase1:
    $ console_text = "Enemy Effect: Regenerates every turn unless stopped correctly"
    ""
    mspy2 neutral "Choose wisely."
    mspy2 neutral "You are not attacking—"
    mspy2 neutral "You are {b}changing behavior.{/b}"

    $ question_text = "while loop_active: {p}{space=40}_________"
    $ console_text = "Type the missing code in the Panel"
    with dissolve
    ""
    # input+question

    # if correct
    mira "…You didn’t delete it."

    # if wrong hint 1 and 2
    mspy "What makes repetition stop?"

    cyra "Don’t overpower it—contain it."

    # if failed
    "Loopling duplicates."
    "Academy stability –10%%."

    return

label bug_summon_phase2:
    return