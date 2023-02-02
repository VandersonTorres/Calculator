##########################                          CALCULATOR                       ##########################
##                                                                                                           ##
##                       Aplication to make simple calculations using Simple GUI TKINTER                     ##
##                                                                                                           ##
###############################################################################################################

###############################             LIMIT OF 120 CHARACTER BY LINE              ################################

from tkinter import *

##########################                      WINDOW CREATION                    ##########################

window = Tk()                                                      # To create a new Window
window.title("Vanderson Torres")                                   # Window's Title

# COLORS DEFINITION (made Through "color picker" on google)
color1 = "#0a0a0a"                                                 # black 
color2 = "#025216"                                                 # green
color3 = "#6b786e"                                                 # gray
color4 = "#d7ded9"                                                 # white
color5 = "#870903"                                                 # red

# WINDOW LAYOUT
window.geometry("433x255")                                    # Width and height values of the Window, respectively
window.config(bg=color4)

# FRAMES CREATION
window_frame = Frame(window, width=433, height=50, bg=color1) # Window dimensions and background color choosing
window_frame.grid(columnspan=5)
main_frame = Frame(window, width=450, height=255)             # Second part dimensions
main_frame.grid(row=1, column=0)

##########################            LOGIC PART - CALCULATOR FUNCTIONS            ##########################

text_values = StringVar()
error = StringVar()
values = ""

def value_entry(valor):                   # Data show in the Window
    global values
    values += str(valor)                  # Add a argument in the global variable 'values' 
    text_values.set(values)               # Show the passed argument (ex: numbers and signals)

def clean_widescreen():                   # Function assigned to 'CLEAN BUTTON' to clean any data 
    global values                      
    values = ""                           # Clean all values stored at globals variables 
    text_values.set("")
    error.set("")

def calculate():                          # Function assigned to 'EQUAL BUTTON' to evaluate data 
    try:                                  # This 'try' execute all available simple operations
        global values
        global error
        result = eval(values)
        text_values.set(str(result))
        values = str(result)              # Transform 'result' values in str again, to continue making operations 
        error.set(str(""))                # In case of previous error, pushing 'equal button' errase error message
    except ZeroDivisionError:             # Error message for division by 0
        text_values.set(str("ERROR"))
        values = str("")                  # Transform global variable in str again and clean the Window
        message = ('Cannot divide by "0"')
        error.set(str(message))
    except:
        text_values.set(str("NULL"))
        values = str("")
        message = ("Try a valid operation")
        error.set(str(message))

##############################                LABELS CREATION               ##############################

app_lable = Label(
        window_frame, textvariable=text_values, width=24, height=2,
        padx=5, relief=SOLID, anchor="e", justify=RIGHT, font=("Arial 19 bold"), bg=color1, fg=color4
    )
app_lable.place(x=30,y=0)

error_type = Label(
        main_frame, textvariable=error, font=("Arial 19 bold"), width=30, height=1,
        relief=FLAT, justify=CENTER, fg=color1, bg=color4
    )
error_type.place(x=50, y=3)

##############################                BUTTONS CREATION               ##############################

# 1ª LINHA =============================================================================================================

btn_c = Button(                                                                               # Clean Button
        main_frame, text="C", width=14, height=2, bg=color5, fg=color4, font=("Ivy 9 bold"),
        relief=RAISED, overrelief=RIDGE, command=clean_widescreen
    ) 
btn_c.grid(row=0,column=0)

# 2ª LINHA =============================================================================================================

btn_add = Button(                                                                             # '+' Button
        main_frame, text="+", width=14, height=2, bg=color2, fg=color4, font=("Ivy 9 bold"),
        relief=RAISED, overrelief=RIDGE, command=lambda: value_entry('+')
    ) 
btn_add.grid(row=2,column=0)

btn_7 = Button(                                                                               # '7' Button
        main_frame, text="7", width=14, height=2, bg=color3, font=("Ivy 9 bold"),
        relief=RAISED, overrelief=RIDGE, command=lambda: value_entry('7')
    )
btn_7.grid(row=2,column=1)

btn_8 = Button(                                                                               # '8' Button
        main_frame, text="8", width=14, height=2, bg=color3, font=("Ivy 9 bold"),
        relief=RAISED, overrelief=RIDGE, command=lambda: value_entry('8')
    ) 
btn_8.grid(row=2,column=2)

btn_9 = Button(                                                                               # '9' Button
        main_frame, text="9", width=14, height=2, bg=color3, font=("Ivy 9 bold"),
        relief=RAISED, overrelief=RIDGE, command=lambda: value_entry('9')
    ) 
btn_9.grid(row=2,column=3)

# 3ª LINHA =============================================================================================================

btn_sub = Button(                                                                             # '-' Button
        main_frame, text="-", width=14, height=2, bg=color2, fg=color4, font=("Ivy 9 bold"),
        relief=RAISED, overrelief=RIDGE, command=lambda: value_entry('-')
    ) 
btn_sub.grid(row=3,column=0)

btn_4 = Button(                                                                               # '4' Button
        main_frame, text="4", width=14, height=2, bg=color3, font=("Ivy 9 bold"),
        relief=RAISED, overrelief=RIDGE, command=lambda: value_entry('4')
    ) 
btn_4.grid(row=3,column=1)

btn_5 = Button(                                                                               # '5' Button
        main_frame, text="5", width=14, height=2, bg=color3, font=("Ivy 9 bold"),
        relief=RAISED, overrelief=RIDGE, command=lambda: value_entry('5')
    ) 
btn_5.grid(row=3,column=2)

btn_6 = Button(                                                                               # '6' Button
        main_frame, text="6", width=14, height=2, bg=color3, font=("Ivy 9 bold"),
        relief=RAISED, overrelief=RIDGE, command=lambda: value_entry('6')
    ) 
btn_6.grid(row=3,column=3)

# 4ª LINHA =============================================================================================================

btn_multi = Button(                                                                           # '*' Button
        main_frame, text="*", width=14, height=2, bg=color2, fg=color4, font=("Ivy 9 bold"),
        relief=RAISED, overrelief=RIDGE, command=lambda: value_entry('*')
    ) 
btn_multi.grid(row=4,column=0)

btn_1 = Button(                                                                               # '1' Button
        main_frame, text="1", width=14, height=2, bg=color3, font=("Ivy 9 bold"),
        relief=RAISED, overrelief=RIDGE, command=lambda: value_entry('1')
    ) 
btn_1.grid(row=4,column=1)

btn_2 = Button(                                                                               # '2' Button
        main_frame, text="2", width=14, height=2, bg=color3, font=("Ivy 9 bold"),
        relief=RAISED, overrelief=RIDGE, command=lambda: value_entry('2')
    ) 
btn_2.grid(row=4,column=2)

btn_3 = Button(                                                                               # '3' Button
        main_frame, text="3", width=14, height=2, bg=color3, font=("Ivy 9 bold"),
        relief=RAISED, overrelief=RIDGE, command=lambda: value_entry('3')
    ) 
btn_3.grid(row=4,column=3)

# 5ª LINHA =============================================================================================================

btn_division = Button(                                                                        # '/' Button
        main_frame, text="/", width=14, height=2, bg=color2, fg=color4, font=("Ivy 9 bold"),
        relief=RAISED, overrelief=RIDGE, command=lambda: value_entry('/')
    ) 
btn_division.grid(row=5,column=0)

btn_dot = Button(                                                                             # '.' Button
        main_frame, text=".", width=14, height=2, bg=color3, font=("Ivy 9 bold"),
        relief=RAISED, overrelief=RIDGE, command=lambda: value_entry('.')
    ) 
btn_dot.grid(row=5,column=1)

btn_0 = Button(                                                                               # '0' Button
        main_frame, text="0", width=14, height=2, bg=color3, font=("Ivy 9 bold"),
        relief=RAISED, overrelief=RIDGE, command=lambda: value_entry('0')
    )
btn_0.grid(row=5,column=2)

btn_equal = Button(                                                                           # '=' Button
        main_frame, text="=", width=14, height=2, bg=color5, fg=color4, font=("Ivy 9 bold"),
        relief=RAISED, overrelief=RIDGE, command=calculate
    ) 
btn_equal.grid(row=5,column=3)

###############################             LIMIT OF 120 CHARACTER BY LINE              ################################

window.mainloop()