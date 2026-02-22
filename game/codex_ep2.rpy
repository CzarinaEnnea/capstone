
##-----------------------------------------------
##-------CODEX ENTRY NAVIGATION------------------
##-----------------------------------------------
screen ep2_nav():
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
            textbutton "Text Type" action ShowMenu("ep2_1")
            textbutton "Numeric Types" action ShowMenu("ep2_2")
            textbutton "List (Mutable)" action ShowMenu("ep2_3")
            textbutton "Tuples (Immutalbe)" action ShowMenu("ep2_4")
            textbutton "Range Function" action ShowMenu("ep2_5")
            textbutton "Dictionaries" action ShowMenu("ep2_6")
            textbutton "Sets" action ShowMenu("ep2_7")
            textbutton "Booleans" action ShowMenu("ep2_8")
            textbutton "NoneType" action ShowMenu("ep2_9")


            ##The following button will require a condition to be true in order to appear.
            #if persistent.bob:
            #   textbutton "Bob" action ShowMenu("bob")

    textbutton "Back" action ShowMenu("category_welcome") yoffset 950 xoffset 25
    textbutton "Main Menu" action Return() yoffset 1000 xoffset 25

##-----------------------------------------------
##-------------CODEX WELCOME---------------------
##-----------------------------------------------
screen episode_2():
    ##This is the "People" category's welcome page. This is the first screen players see after they select a category.

    tag menu
    use ep2_nav

    style_prefix "codex"
    vbox:
            xsize 850
            xalign 0.5 yalign 0.5
            xoffset 200
            text _("In this category you can read about all the lessons in Episode 2")
            text _p("This will also serve as a review sheet, incase you forgot 😊")



##-----------------------------------------------
##----------ENTRIES START HERE-------------------
##-----------------------------------------------
screen ep2_1():

    tag menu
    use ep2_nav

    style_prefix "codex"
    label "Text Type — str"

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

            text _p(" {b}String: ")
            text _p("{color=#32CD32}{b}name = \"Code Nexus\"")
            text _p("{color=#32CD32}{b}print(name)")
            text _p("{color=#00BFFF}{b}Output: Code Nexus")

            text _p("")
            text _p("{b}String Concatenation:")
            text _p("{color=#32CD32}{b}first = \"Cyra\"")
            text _p("{color=#32CD32}{b}last = \"Byte\"")
            text _p("{color=#32CD32}{b}print(first+last)")
            text _p("{color=#00BFFF}{b}Output: CyraByte")

            text _p("")
            text _p("{b}Adding Space (use space as a string inside \"___\").")
            text _p("{color=#32CD32}{b}print(first + " " + last)")
            text _p("{color=#00BFFF}{b}Output: Cyra Byte")

            text _p("")
            text _p("{b}String Multiplication")
            text _p("{color=#32CD32}{b}print(\"Error\" * 3)")
            text _p("{color=#00BFFF}{b}Output: ErrorErrorErrord")
##--------------------------------------------------------------------------------------------------------------------------------------------------------------------
screen ep2_2():

    tag menu
    use ep2_nav

    style_prefix "codex"
    label "Numeric Types"

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

            text _p(" {b}Types of number variables in Python ")

            text _p("")
            text _p("{b}Integer")
            text _p("{color=#32CD32}{b}int = 5")
            text _p("{color=#00BFFF}{b}Integers(int) store whole numbers (e.g., 5, -12).")

            text _p("")
            text _p("{b}Float")
            text _p("{color=#32CD32}{b}float = 3.14")
            text _p("{color=#00BFFF}{b}store numbers with decimals (e.g., 3.14, -0.5, 2.0).")

            text _p("")
            text _p("{b}Complex")
            text _p("{color=#32CD32}{b} complex = 2 + 3j")
            text _p("{color=#00BFFF}{b}Complex is a data type that can represent numbers with both a real and an imaginary part")

##--------------------------------------------------------------------------------------------------------------------------------------------------------------------
screen ep2_3():

    tag menu
    use ep2_nav

    style_prefix "codex"
    label "List (Mutable)"

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

            text _p("{b}List{/b} is a built-in data type used to store an ordered, changeable (mutable) collection of items. It uses \"[[]\" square brackets to create a list.")
            text _p("")

            text _p("{b}Key Features of a List:")
            text _p("{i}{b}Ordered{/b}{i} - Items have a defined order and maintain it.")
            text _p("{i}{b}Mutable{/b}{/i} - You can change, add, or remove items after creation.")
            text _p("{i}{b}Allows duplicates{/b}{/i} - Lists can contain the same value multiple times.")
            text _p("{i}{b}Heterogeneous{/b}{/i} - Can store different data types in the same list.")

            text _p("")
            text _p("Example:")
            text _p("{color=#32CD32}{b}fruits = [[\"apple\", \"banana\"]")
            text _p("{color=#00BFFF}{b}Will create a list that has both apple and banana")

            text _p("")
            text _p("{b}Append")
            text _p("If you want to add another to the list:")
            text _("{color=#32CD32}{b}fruits.append(\"cherry\")")
            text _p("{color=#00BFFF}{b}Adds cherry to the list")

##--------------------------------------------------------------------------------------------------------------------------------------------------------------------
screen ep2_4():

    tag menu
    use ep2_nav

    style_prefix "codex"
    label "Tuples (Immutable)"

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

            text _p("{b}Tuple{/b} a collection of items stored together in order, but it cannot be changed after creation")
            text _p("")

            text _p("Example:")
            text _p("{color=#32CD32}{b}numbers = (1,2,3)")
            text _p("{color=#00BFFF}{b}This will create a tuple, Unlike List where it uses Brackets Tupples uses \"()\" Parenthesis")

##--------------------------------------------------------------------------------------------------------------------------------------------------------------------
screen ep2_5():

    tag menu
    use ep2_nav

    style_prefix "codex"
    label "Range Function"

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

            text _p("""{b}Range{/b} - range() function creates a sequence of numbers that you can loop through — but it doesn’t store all numbers in memory at once.
                It returns a special numeric sequence type called a range object, which is immutable (cannot be changed) and lazy (numbers are generated when needed).""")
            text _p("")

            text _p("Example:")
            text _p("{color=#32CD32}{b}for x in range(3)")
            text _p("{color=#000000}_________{/color}{color=#32CD32}{b}print(x)")
            text _p("{color=#00BFFF}{b}Output: 012{/color}")

            text _p("")
            text _p("{color=#32CD32}{b}range(n){/b}{/color} starts at 0 and stops before n.")

##--------------------------------------------------------------------------------------------------------------------------------------------------------------------
screen ep2_6():

    tag menu
    use ep2_nav

    style_prefix "codex"
    label "Dictionaries"

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

            text _p("""{b}Dictionary{/b} - in Python s a built‑in data structure used to store data in key–value pairs.
            """)
            text _p("")

            text _p("Example:")
            text _p("""{color=#32CD32}{b}
            student = {{\n
            \"name\": \"Luna\",\n
            \"age\": 17,\n
            \"rank\": 5,\n}""")

            text _p("{color=#00BFFF}{b}Student ditionary created!{/color}")

            text _p("")
            text _p("{b}To print:")
            text _p("{color=#32CD32}{b}print(student[[\"name\"])")
            text _p("{color=#00BFFF}{b}Output: Luna")

##--------------------------------------------------------------------------------------------------------------------------------------------------------------------
screen ep2_7():

    tag menu
    use ep2_nav

    style_prefix "codex"
    label "Sets"

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

            text _p("In {b}Sets{/b} Duplicate values are removed automatically.")
            text _p("")

            text _p("Example:")
            text _p("""{color=#32CD32}{b}tools = {{
            \"Laptop\", 
            \"Keyboard\", 
            \"Laptop\"}
            """)

            text _p("{color=#00BFFF}{b}Output: {{\"laptop\", \"keyboard\"}{/color}")

##--------------------------------------------------------------------------------------------------------------------------------------------------------------------
screen ep2_8():

    tag menu
    use ep2_nav

    style_prefix "codex"
    label "Booleans"

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

            text _p("{b}Boolean{/b} is a data type that has only two possible values: {b}{i}True and False{/i}{/b}. It is used in conditions")
            text _p("")

            text _p("Example:")
            text _p("{color=#32CD32}{b}if a < b:")
            text _p("{color=#000000}_________{/color}{color=#32CD32}{b}print(a is less than b)")
            text _p("{color=#32CD32}{b}else:")
            text _p("{color=#000000}_________{/color}{color=#32CD32}{b}print(a is greater than b)")
            text _p("")
            text _p("{color=#00BFFF}{b}Runs based on True or False")

##--------------------------------------------------------------------------------------------------------------------------------------------------------------------
screen ep2_9():

    tag menu
    use ep2_nav

    style_prefix "codex"
    label "NoneType"

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

            text _p("{b}NoneType{/b} is the type of the special value None. It represents the absence of a value or a null reference.")
            text _p("")

            text _p("Example:")
            text _p("{color=#32CD32}{b}x = None")
            text _p("")
            text _p("{color=#00BFFF}{b}Represents absence of value")


