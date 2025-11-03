default WC = 0
default password1 = "Five is greater than two!"

label ep1_scn4_txt2:
    "What is the correct syntax?"
    $ code = renpy.input("Type here:")
    $ code = code.strip()

    if code == password1:
        "CORRECT!"
        mspy "Nice work! You got it right."
        return
    else:
        $ WC += 1
        if WC >= 3:
            "You have reached the maximum attempts."
            jump explain
        else:
            "Wrong code!"
            "Try again. You have [3 - WC] attempt(s) left."
            jump ep1_scn4_txt2

    label explain:
    mspy "The correct output is: 'Five is greater than two!'"
    mspy "Make sure to include the exact syntax and punctuation."
    return