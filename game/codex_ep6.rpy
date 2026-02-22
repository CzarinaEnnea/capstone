
##-----------------------------------------------
##-------CODEX ENTRY NAVIGATION------------------
##-----------------------------------------------
screen ep6_nav():
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
            textbutton "Loops" action ShowMenu("ep6_1")
            textbutton "Functions" action ShowMenu("ep6_2")
            textbutton "Arrays" action ShowMenu("ep6_3")


            ##The following button will require a condition to be true in order to appear.
            #if persistent.bob:
            #   textbutton "Bob" action ShowMenu("bob")

    textbutton "Back" action ShowMenu("category_welcome") yoffset 950 xoffset 25
    textbutton "Main Menu" action Return() yoffset 1000 xoffset 25

##-----------------------------------------------
##-------------CODEX WELCOME---------------------
##-----------------------------------------------
screen episode_6():
    ##This is the "People" category's welcome page. This is the first screen players see after they select a category.

    tag menu
    use ep6_nav

    style_prefix "codex"
    vbox:
            xsize 850
            xalign 0.5 yalign 0.5
            xoffset 200
            text _("In this category you can read about all the lessons in Episode 6")
            text _p("This will also serve as a review sheet, incase you forgot 😊")



##-----------------------------------------------
##----------ENTRIES START HERE-------------------
##-----------------------------------------------
screen ep6_1():

    tag menu
    use ep6_nav

    style_prefix "codex"
    label "Loops"

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
            
            text _p("{b}Loop")
            text _p(" {b}For Loop{/b} is used to iterate (loop) over a sequence of items and execute a block of code for each item in that sequence. ")

            text _p("Example:")
            text _p("{color=#32CD32}{b}for x in range(5):")
            text _p("{color=#000000}_________{color=#32CD32}{b}print(x)")  
            text _p("{color=#00BFFF}{b}Output: 01234") 
            text _p("")

            text _p("{b}Looping through a list:")

            text _p("Example:")
            text _p("{color=#32CD32}{b}for fruit in fruits:")
            text _p("{color=#000000}_________{color=#32CD32}{b}print(fruit)")  
            text _p("{color=#00BFFF}{b}Output: Will print each item") 
            text _p("")

            text _p("{b}While Loop:")

            text _p("Example:")
            text _p("{color=#32CD32}{b}x = 0")
            text _p("{color=#32CD32}{b}while x < 3:")
            text _p("{color=#000000}_________{color=#32CD32}{b}print(x)")  
            text _p("{color=#000000}_________{color=#32CD32}{b}x += 1")  
            text _p("{color=#00BFFF}{b}Output: Runs until condition is False") 
            text _p("")

            text _p("{b}Infinite Loop:")

            text _p("Example:")
            text _p("{color=#32CD32}{b}while True:")
            text _p("{color=#000000}_________{color=#32CD32}{b}print(\"Looping Forever\")")  
            text _p("{color=#00BFFF}{b}Output: Runs Forever") 
            text _p("")

## --------------------------------------------------------------------------------
screen ep6_2():

    tag menu
    use ep6_nav

    style_prefix "codex"
    label "Functions"

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
            
            text _p("{b}Basic Function")
            text _p(" - will define and call a function you have set.")

            text _p("Example:")
            text _p("{color=#32CD32}{b}def greet():")
            text _p("{color=#000000}_________{color=#32CD32}{b}print(\"Hello\")")
            text _p("{color=#000000}_________{color=#32CD32}{b}greet()")  
            text _p("{color=#00BFFF}{b}Output: Hello") 
            text _p("")

            text _p("{b}Function with parameter")
            text _p(" - is a function that accepts input values when it is called")

            text _p("Example:")
            text _p("{color=#32CD32}{b}def greet():")
            text _p("{color=#000000}_________{color=#32CD32}{b}print(\"Hello\")")
            text _p("{color=#000000}_________{color=#32CD32}{b}greet(\"Cyra\")")  
            text _p("{color=#00BFFF}{b}Output: Hello, Cyra") 
            text _p("")

            text _p("{b}Function with return value")
            text _p(" - is a function that sends data back to the place where it was called using the return statement.")

            text _p("Example:")
            text _p("{color=#32CD32}{b}def add(a,b):")
            text _p("{color=#000000}_________{color=#32CD32}{b}return a + b")
            text _p("{color=#32CD32}{b}result = add(5,3)")
            text _p("{color=#32CD32}{b}print(resullt)")
            text _p("{color=#00BFFF}{b}Output: 8") 
            text _p("")

            text _p("{b}Why functions matter:")
            text _p("- Prevent repetition")
            text _p("- Improve readability")
            text _p("- Organize logic\n")
            text _p("- Make large systems manageable")

## --------------------------------------------------------------------------------
screen ep6_3():

    tag menu
    use ep6_nav

    style_prefix "codex"
    label "Functions"

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
            
            text _p("{b}Arrays (Lists in Python)")
            text _p(" - Python uses lists instead of traditional arrays.")

            text _p("{b}Creating a list:")
            text _p("{color=#32CD32}{b}numbers = [[10, 20, 30]") 
            text _p("{color=#00BFFF}{b}Output: List is now created and can be used") 
            text _p("")

            text _p("{b}Accessing elements:")
            text _p("{color=#32CD32}{b}print(numbers[[0])") 
            text _p("{color=#00BFFF}{b}Output: 10 - (this is the first \"0\" in the list)") 
            text _p("")

            text _p("{b}Modifying:")
            text _p("{color=#32CD32}{b}numbers[[1]] = 25") 
            text _p("{color=#32CD32}{b}print(numbers[[1]]) ") 
            text _p("{color=#00BFFF}{b}Output: 25 - (this updates the value of the specified field)") 
            text _p("")

            text _p("{b}Adding:")
            text _p("{color=#32CD32}{b}numbers.append(40)") 
            text _p("{color=#32CD32}{b}print(numbers[[1]]) ") 
            text _p("{color=#32CD32}{b}print(numbers)") 
            text _p("{color=#00BFFF}{b}Output: 10,25,30,40 - (this adds 40 on the last of the list)") 
            text _p("")

            text _p("{b}Removing:")
            text _p("{color=#32CD32}{b}numbers.remove(10)") 
            text _p("{color=#32CD32}{b}print(numbers)") 
            text _p("{color=#00BFFF}{b}Output: 25,30,40 - (this removes the first \"10\" on the list)") 
            text _p("")

            text _p("{b}Looping through a list:")
            text _p("{color=#32CD32}{b}for num in numbers:") 
            text _p("{color=#32CD32}{b}print(num)") 
            text _p("{color=#00BFFF}{b}Output: this will print each number in the list") 
            text _p("")