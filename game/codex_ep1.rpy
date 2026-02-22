
##-----------------------------------------------
##-------CODEX ENTRY NAVIGATION------------------
##-----------------------------------------------
screen ep1_nav():
    add "gui/overlay/game_menu.png"

    viewport:
        xpos 25 ypos 400
        xsize 350 ysize 350
        mousewheel True
        draggable True
        pagekeys True
        side_yfill True
        scrollbars "vertical"
        vbox:
            spacing 10
            xoffset 350
            textbutton "print()" action ShowMenu("ep1_1")
            textbutton "Strings Rules" action ShowMenu("ep1_2")
            textbutton "Variables" action ShowMenu("ep1_3")
            textbutton "Indentation" action ShowMenu("ep1_4")
            textbutton "Comments" action ShowMenu("ep1_5")

            ##The following button will require a condition to be true in order to appear.
            #if persistent.bob:
            #   textbutton "Bob" action ShowMenu("bob")

    textbutton "Back" action ShowMenu("category_welcome") yoffset 950 xoffset 25
    textbutton "Main Menu" action Return() yoffset 1000 xoffset 25

##-----------------------------------------------
##-------------CODEX WELCOME---------------------
##-----------------------------------------------
screen episode_1():
    ##This is the "People" category's welcome page. This is the first screen players see after they select a category.

    tag menu
    use ep1_nav

    style_prefix "codex"
    vbox:
            xsize 850
            xalign 0.5 yalign 0.5
            xoffset 200
            text _("In this category you can read about all the lessons in Episode 1")
            text _p("This will also serve as a review sheet, incase you forgot 😊")



##-----------------------------------------------
##----------ENTRIES START HERE-------------------
##-----------------------------------------------

screen ep1_1():

    tag menu
    use ep1_nav

    style_prefix "codex"
    label "The print() Function"

    viewport:
        xsize 1300
        ysize 800
        xalign 0.5
        xoffset 200 yoffset 250
        side_yfill True
        scrollbars "vertical"
        mousewheel True
        draggable True
        pagekeys True


        vbox:
            #You write the actual entry here. I suggest you split your text into smaller text _p sections, otherwise the text might overlap with
            #the scrollbars. If you're sure that your text fits the screen and scrolling is not needed then comment out everything starting from "scrollbars vertical" to
            #"pagekeys True" as seen in the next entry. If you do this, splitting the text is not needed.

            text _p(" - \"{b}print(){/b}\" displays output to the screen.")

            text _p("")

            text _p("- Strings must be inside {b}\"text\"{/b} quotation marks.")

            text _p("")

            text _p("Example:")

            text _p("")

            text _p("""
            {color=#32CD32}{b}Code: print("Hello, Worlld"){/color}""")
            text _p("""
            {color=#32CD32}{b}Result: Hello, World{/color}
            """)

            text _p("")

            text _p("**It will display the exact string you have written inside the parenthesis**")

##--------------------------------------------------------------------------------------------------------------------------------------------------------------------

screen ep1_2():

    tag menu
    use ep1_nav

    style_prefix "codex"
    label "Strings & Quotation Rules"

    viewport:
        xsize 1300
        ysize 800
        xalign 0.5
        xoffset 200 yoffset 250
        side_yfill True
        #scrollbars "vertical"
        #mousewheel True
        #draggable True
        #pagekeys True

        vbox:
            text _p("- Missing quotation marks cause syntax errors.")
            text _p("")
            text _p("Examples:")
            text _p("")

            text _p("{b}Error:")
            text _p("""
            {color=#32CD32}{b}Code: print("Hello World!)""")
            text _p("""
            {color=#FF6347}{b}Result: SyntaxError
            """)

            text _p("")
            text _p("{b}Correct:")
            text _p("""
            {color=#32CD32}{b}Code: print("Hello World!")""")
            text _p("""
            {color=#FF6347}{b}Result: Hello World!
            """)

            text _p("")
            text _p("**This code will be able to print correctly because proper quotation mark was placed**")

##--------------------------------------------------------------------------------------------------------------------------------------------------------------------

screen ep1_3():

    tag menu
    use ep1_nav

    style_prefix "codex"
    label "Variables"

    viewport:
        xsize 1300
        ysize 800
        xalign 0.5
        xoffset 200 yoffset 250
        side_yfill True
        #scrollbars "vertical"
        #mousewheel True
        #draggable True
        #pagekeys True

        vbox:
            text _p("- Variables are created when assigned.")
            text _p("- Python does not require type declaration.")
            
            text _p("")
            text _p("Examples:")
            text _p("""
            {color=#32CD32}{b}Code: x = 10""")
            text _p("""
            {color=#32CD32}{b}Result: Stores the integer 10\n
            """)

            text _p("""
            {color=#32CD32}{b}Code: name = "Cyra" """)
            text _p("""
            {color=#32CD32}{b}Result: Stores the string Cyra
            """)

            text _p("")

            text _p("{b}Important!:")
            text _p("- Variable names cannot contain spaces.")
            text _p("- Use underscores instead.")

            text _p("")
            text _p("Example:")
            text _p("""
            {color=#32CD32}{b}Code: my_name = "Kai" """)
            text _p("""
            {color=#32CD32}{b}Result: Valid variable name
            """)

##--------------------------------------------------------------------------------------------------------------------------------------------------------------------

screen ep1_4():

    tag menu
    use ep1_nav

    style_prefix "codex"
    label "indentation"

    viewport:
        xsize 1300
        ysize 800
        xalign 0.5
        xoffset 200 yoffset 250
        side_yfill True
        #scrollbars "vertical"
        #mousewheel True
        #draggable True
        #pagekeys True

        vbox:
            text _p("- Python uses indentation to define code blocks.")
            
            text _p("")
            text _p("Correct:")
            text _p("{color=#32CD32}{b}Code: if 5 > 2")
            text _p("{color=#000000}_____________{/color}{color=#32CD32}{b}print(\"Five is greater than two\")")
            text _p("")
            text _p("Meaning: The print line belongs to the if statement")
            text _p("")

            text _p("""Incorrect indentation causes errors.""")
            text _p("Python does not use curly braces {{} or semicolons.")
            text _p("Spacing defines structure.")

##--------------------------------------------------------------------------------------------------------------------------------------------------------------------

screen ep1_5():

    tag menu
    use ep1_nav

    style_prefix "codex"
    label "Comments"

    viewport:
        xsize 1300
        ysize 800
        xalign 0.5
        xoffset 200 yoffset 250
        side_yfill True
        #scrollbars "vertical"
        #mousewheel True
        #draggable True
        #pagekeys True

        vbox:
            text _p("- Comments begin with {b}\"#\"{/b} Hashtag.")
            text _p("Comments are ignored during execution")
            
            text _p("")
            text _p("Example:")
            text _p("{color=#32CD32}{b}Code: # This is a comment")
            text _p("")
            text _p("Meaning: This will be ignored by Python")
            text _p("")


