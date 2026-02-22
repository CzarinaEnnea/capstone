
##-----------------------------------------------
##-------CODEX ENTRY NAVIGATION------------------
##-----------------------------------------------
screen ep3_nav():
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
            textbutton "Arithmetic Operators" action ShowMenu("ep3_1")
            textbutton "Comparison Operators" action ShowMenu("ep3_2")
            textbutton "Conditional Statements" action ShowMenu("ep3_3")


            ##The following button will require a condition to be true in order to appear.
            #if persistent.bob:
            #   textbutton "Bob" action ShowMenu("bob")

    textbutton "Back" action ShowMenu("category_welcome") yoffset 950 xoffset 25
    textbutton "Main Menu" action Return() yoffset 1000 xoffset 25

##-----------------------------------------------
##-------------CODEX WELCOME---------------------
##-----------------------------------------------
screen episode_3():
    ##This is the "People" category's welcome page. This is the first screen players see after they select a category.

    tag menu
    use ep3_nav

    style_prefix "codex"
    vbox:
            xsize 850
            xalign 0.5 yalign 0.5
            xoffset 200
            text _("In this category you can read about all the lessons in Episode 3")
            text _p("This will also serve as a review sheet, incase you forgot 😊")



##-----------------------------------------------
##----------ENTRIES START HERE-------------------
##-----------------------------------------------
screen ep3_1():

    tag menu
    use ep3_nav

    style_prefix "codex"
    label "Arithmetic Operators"

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

            text _p(" {b}Operations: ")
            text _p("")
            text _p("{color=#32CD32}{b}+ - Addition")
            text _p("")
            text _p("{color=#32CD32}{b}- - Subtraction")
            text _p("")
            text _p("{color=#32CD32}{b}* - Multiplication")    
            text _p("")        
            text _p("{color=#32CD32}{b}/ - Division")
            text _p("")
            text _p("{color=#32CD32}{b}// - Floor Division")
            text _p("")
            text _p("{color=#32CD32}{b}% - Modulus (remainder)")

            text _p("")                
            text _p("Examples:")
            text _p("{color=#32CD32}{b}print(10 // 4)")
            text _p("{color=#00BFFF}{b}Output: 2")
            text _p("")
            text _p("{color=#32CD32}{b}print(6 % 2)")
            text _p("{color=#00BFFF}{b}Output: 0")

## ---------------------------------------------------------------------------------
screen ep3_2():

    tag menu
    use ep3_nav

    style_prefix "codex"
    label "Comparison Operators"

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

            text _p(" {b}Operations: ")
            text _p("")
            text _p("{color=#32CD32}{b}> - Greater than")
            text _p("")
            text _p("{color=#32CD32}{b}< - Less than")
            text _p("")
            text _p("{color=#32CD32}{b}>= - Greater-than or equal to")    
            text _p("")        
            text _p("{color=#32CD32}{b}<= - Less-than or equal to")
            text _p("")
            text _p("{color=#32CD32}{b}== - Equal to")
            text _p("")
            text _p("{color=#32CD32}{b}!= - Not equal")

## ---------------------------------------------------------------------------------
screen ep3_3():

    tag menu
    use ep3_nav

    style_prefix "codex"
    label "Conditional Statements"

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

            text _p(" {b}Structures: ")
            text _p("")
            text _p("{color=#00BFFF}{b}\"if\" {/color}- {/b}Runs if True")
            text _p("{color=#00BFFF}{b}\"elif\" {/color}- {/b}Additional Condition")
            text _p("{color=#00BFFF}{b}\"else\" {/color}- {/b}Runs if all above are False")    
            text _p("")   

            text _p("{b}Example:")
            text _p("{color=#32CD32}{b}x = 0")
            text _p("{color=#32CD32}{b}if x > 0")
            text _p("{color=#000000}_________{color=#32CD32}{b}print(\"Positive\")")   
            text _p("{color=#32CD32}{b}elif x == 0:")
            text _p("{color=#000000}_________{color=#32CD32}{b}print(\"Zero\")")  
            text _p("{color=#32CD32}{b}else:")
            text _p("{color=#000000}_________{color=#32CD32}{b}print(\"Negative\")")   
            text _p("{color=#00BFFF}{b}Output: Zero")

            text _p("")
            text _p("{b}Core Logic Concepts:")
            text _p("{i}True conditions execute")
            text _p("{i}False conditions are skipped")
            text _p("{i}Logical errors cause program failure")



