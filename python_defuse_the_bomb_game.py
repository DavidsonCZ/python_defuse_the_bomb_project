import tkinter.font as tkfont
import customtkinter as ctk
import tkinter as tk
import time
import pygame
import random
from PIL import Image


pygame.init()

pygame.mixer.init()

sound = pygame.mixer.Sound("python1_1.wav")
sound_timer = pygame.mixer.Sound("python1_2.wav")
#print("game")

#head of aplication
app=ctk.CTk()
app.geometry("700x600")
app.title("assistent_app")
app.configure(fg_color="#010B1D")

def counter_update():
    counter_label.configure(text=str(counter))

counter = 0

header_frame=ctk.CTkFrame(app, fg_color="transparent")
header_frame.pack(pady=(20,0))

counter_label=ctk.CTkLabel(header_frame, width=60, height=60, fg_color="#071F39", text_color="#FAF5E9", text=str(counter), font=("Zen Dots",30), corner_radius=20)
counter_label.pack(side="left")

timer = 10
def function_timer(timer):
    global core_colors
    counter_time_label.configure(text=str(timer))
    if timer >0:
        app.after_id = app.after(1000, function_timer, timer-1)
        sound_timer.play()
    else:
        sound.play()
        write_output("time")
        core_colors = ""
        app.after(1000, clear_output)  

def stop_timer():
    global timer
    if hasattr(app, "after_id"):
        try:
            app.after_cancel(app.after_id)
        except Exception:
            pass
    timer = 10
    counter_time_label.configure(text=str(timer))

counter_time_label=ctk.CTkLabel(header_frame, width=60, height=60, fg_color="#071F39", text_color="#FAF5E9", text=str(timer), font=("Zen Dots",30), corner_radius=20)
counter_time_label.pack(side="right")

#greeting from aplication
hello_label=ctk.CTkButton(header_frame, width=290, height=60, fg_color="#071F39", text_color="#FAF5E9", text="game", font=("Zen Dots",30), corner_radius=20, hover=False, state="disabled")
hello_label.pack(side="left",padx=(20))

#button_play=ctk.CTkButton(app, width=60, height=20, fg_color="#2B4141", text_color="#8AB9B5", text="start", font=("Zen Dots",30), corner_radius=20, command=function_core_generator)
#button_play.pack(pady=20)

image_cable_red = ctk.CTkImage(light_image=Image.open("python_game_color_cable_red.png"), size=(200,20))
image_cable_red_cut = ctk.CTkImage(light_image=Image.open("python_game_color_cable_red_cut.png"), size=(200,20))
image_cable_green = ctk.CTkImage(light_image=Image.open("python_game_color_cable_green.png"), size=(200,20))
image_cable_green_cut = ctk.CTkImage(light_image=Image.open("python_game_color_cable_green_cut.png"), size=(200,20))
image_cable_blue = ctk.CTkImage(light_image=Image.open("python_game_color_cable_blue.png"), size=(200,20))
image_cable_blue_cut = ctk.CTkImage(light_image=Image.open("python_game_color_cable_blue_cut.png"), size=(200,20))

user_colors = ""
core_colors = ""

colors=["red", "green", "blue"]
def function_core_generator():
    global core_colors, user_colors
    clear_output()
    game_state = True
    core_colors = ""
    user_colors = ""
    color=random.sample(colors, len (colors))
    for x in color:
        write_output(x)
        core_colors+= x + ","
    function_timer(timer)
    #write_output(core_colors)
    reset_cables()

button_play=ctk.CTkButton(app, width=60, height=20, fg_color="#071F39", text_color="#FAF5E9", text="start", font=("Zen Dots",30), corner_radius=20, command=lambda: (function_core_generator(), function_core_number_generator()))
button_play.pack(pady=20)

def instructions():
    write_output("cut the cables in the right sequence")
    write_output("good luck")
    output_text_number.insert("end", "number sequence")

button_instructions=ctk.CTkButton(app, width=60, height=20, fg_color="#071F39", text_color="#FAF5E9", text="instructions", font=("Zen Dots",30), corner_radius=20, command= instructions)
button_instructions.place(x=20, y=20)

def write_output_number(text):
    output_text_number.insert("end", "       " + text + "   ")
    output_text_number.see("end")

user_numbers = ""
core_numbers = ""
game_state = False

numbers=["1", "2", "3", "4", "5", "6", "7", "8", "9"]
def function_core_number_generator():
    global core_numbers, game_state
    core_numbers = ""
    game_state = True
    for x in range(6):
        number=numbers[random.randint(0,8)]
        core_numbers+= number + " "
    write_output_number(core_numbers)

def function_user_number_1():
    global user_numbers
    number="1"
    user_numbers+=number + " "

def function_user_number_2():
    global user_numbers
    number="2"
    user_numbers+=number + " "

def function_user_number_3():
    global user_numbers
    number="3"
    user_numbers+=number + " "

def function_user_number_4():
    global user_numbers
    number="4"
    user_numbers+=number + " "

def function_user_number_5():
    global user_numbers
    number="5"
    user_numbers+=number + " "

def function_user_number_6():
    global user_numbers
    number="6"
    user_numbers+=number + " "

def function_user_number_7():
    global user_numbers
    number="7"
    user_numbers+=number + " "

def function_user_number_8():
    global user_numbers
    number="8"
    user_numbers+=number + " "

def function_user_number_9():
    global user_numbers
    number="9"
    user_numbers+=number + " "

def reset_cables():
    button_red.configure(state = "normal", image = image_cable_red)
    button_green.configure(state = "normal", image = image_cable_green)
    button_blue.configure(state = "normal", image = image_cable_blue)

def clear_output():
    output_text.delete(1.0, "end")
    output_text_number.delete(1.0, "end")

def write_output(text):
    output_text.insert("end", "\n" + text + "\n")
    output_text.see("end")

def function_user_red():
    global user_colors
    color="red"
    user_colors+=color + ","
    button_red.configure(image = image_cable_red_cut)
    button_red.configure(state = "disabled")

def function_user_green():
    global user_colors
    color="green"
    user_colors+=color + ","
    button_green.configure(image = image_cable_green_cut)
    button_green.configure(state = "disabled")

def function_user_blue():
    global user_colors
    color="blue"
    user_colors+=color + ","
    button_blue.configure(image = image_cable_blue_cut)
    button_blue.configure(state = "disabled")

def function_submit():
    global user_colors, core_colors, counter, timer, user_numbers, core_numbers
    if game_state == False:
        write_output("BOOM")
        sound.play()
        stop_timer()
    elif user_colors.rstrip(",") == core_colors.rstrip(",") and user_numbers.strip() == core_numbers.strip():
        write_output("win")
        user_colors=""
        user_numbers=""
        counter+=1
        counter_update()
        stop_timer()
        reset_cables()
    else:
        stop_timer()
        write_output("BOOM")
        sound.play()
        user_colors=""
        user_numbers=""
        reset_cables()
    app.after(1000, clear_output)

output_text=ctk.CTkTextbox(app, height=200, width=400, text_color="#EDEDED", font=("Zen Dots",16), fg_color="#010209")
output_text.pack(pady=(0,0))

button_frame=ctk.CTkFrame(app, fg_color="transparent", width=300, height=300)
button_frame.pack(pady=(0,0))

button_number_frame=ctk.CTkFrame(app, fg_color="transparent", width=400, height=310)
button_number_frame.place(x=1109, y=374)

#images
image_module_number = ctk.CTkImage(light_image=Image.open("python_game_color_module_number.png"), size=(290,300))
image_module = ctk.CTkImage(light_image=Image.open("python_game_color_module2.png"), size=(300,290))
image_cable_red = ctk.CTkImage(light_image=Image.open("python_game_color_cable_red.png"), size=(310,20))
image_cable_red_cut = ctk.CTkImage(light_image=Image.open("python_game_color_cable_red_cut.png"), size=(310,20))
image_cable_green = ctk.CTkImage(light_image=Image.open("python_game_color_cable_green.png"), size=(310,20))
image_cable_green_cut = ctk.CTkImage(light_image=Image.open("python_game_color_cable_green_cut.png"), size=(310,20))
image_cable_blue = ctk.CTkImage(light_image=Image.open("python_game_color_cable_blue.png"), size=(310,20))
image_cable_blue_cut = ctk.CTkImage(light_image=Image.open("python_game_color_cable_blue_cut.png"), size=(310,20))
#button_red=ctk.CTkButton(button_frame, width=60, height=20, fg_color="#871F1F", text_color="#FAF5E9",text="0", font=("Zen Dots",30), corner_radius=60,hover_color="#6C1717", command=function_user_red)
#button_red.pack(side="left",padx=20)


#buttons
module_image=ctk.CTkLabel(button_frame, image=image_module, text="")
module_image.place(x=0, y=0)

button_red=ctk.CTkButton(button_frame, image=image_cable_red, text="", fg_color="#02060d", hover_color="#02060d", command=function_user_red)
button_red.place(x=-10, y=90)

button_green=ctk.CTkButton(button_frame, image=image_cable_green, text="", fg_color="#02060d", hover_color="#02060d", command=function_user_green)
button_green.place(x=-10, y=140)

button_blue=ctk.CTkButton(button_frame, image=image_cable_blue, text="", fg_color="#02060d", hover_color="#02060d", command=function_user_blue)
button_blue.place(x=-10, y=170)

#buttons number
module_number_image=ctk.CTkLabel(button_number_frame, image=image_module_number, text="")
module_number_image.place(x=0, y=0)

button_number1=ctk.CTkButton(button_number_frame, width=60, height=60, text="1", font=("Zen Dots", 20), fg_color="#001f42", hover_color="#02060d", command=function_user_number_1)
button_number1.place(x=60, y=220)

button_number2=ctk.CTkButton(button_number_frame, width=60, height=60, text="2", font=("Zen Dots", 20), fg_color="#001f42", hover_color="#02060d", command=function_user_number_2)
button_number2.place(x=140, y=220)

button_number3=ctk.CTkButton(button_number_frame, width=60, height=60, text="3", font=("Zen Dots", 20), fg_color="#001f42", hover_color="#02060d", command=function_user_number_3)
button_number3.place(x=220, y=220)

button_number4=ctk.CTkButton(button_number_frame, width=60, height=60, text="4", font=("Zen Dots", 20), fg_color="#001f42", hover_color="#02060d", command=function_user_number_4)
button_number4.place(x=60, y=140)

button_number5=ctk.CTkButton(button_number_frame, width=60, height=60, text="5", font=("Zen Dots", 20), fg_color="#001f42", hover_color="#02060d", command=function_user_number_5)
button_number5.place(x=140, y=140)

button_number6=ctk.CTkButton(button_number_frame, width=60, height=60, text="6", font=("Zen Dots", 20), fg_color="#001f42", hover_color="#02060d", command=function_user_number_6)
button_number6.place(x=220, y=140)

button_number7=ctk.CTkButton(button_number_frame, width=60, height=60, text="7", font=("Zen Dots", 20), fg_color="#001f42", hover_color="#02060d", command=function_user_number_7)
button_number7.place(x=60, y=60)

button_number8=ctk.CTkButton(button_number_frame, width=60, height=60, text="8", font=("Zen Dots", 20), fg_color="#001f42", hover_color="#02060d", command=function_user_number_8)
button_number8.place(x=140, y=60)

button_number9=ctk.CTkButton(button_number_frame, width=60, height=60, text="9", font=("Zen Dots", 20), fg_color="#001f42", hover_color="#02060d", command=function_user_number_9)
button_number9.place(x=220, y=60)

output_text_number=ctk.CTkTextbox(button_number_frame, height=20, width=200, text_color="#EDEDED", font=("Zen Dots",16), fg_color="#010209")
output_text_number.place(x=70, y=10)

#button_green=ctk.CTkButton(button_frame, width=60, height=20, fg_color="#09814A", text_color="#FAF5E9",text="0", font=("Zen Dots",30), corner_radius=60,hover_color="#076239", command=function_user_green)
#button_green.pack(side="left",padx=20)

#button_blue=ctk.CTkButton(button_frame, width=60, height=20, fg_color="#0B396A", text_color="#FAF5E9",text="0", font=("Zen Dots",30), corner_radius=60,hover_color="#092F57", command=function_user_blue)
#button_blue.pack(side="left",padx=20)

button_submit=ctk.CTkButton(button_frame, width=60, height=20, fg_color="#960000", text_color="#FAF5E9",text="BOOM", font=("Zen Dots",30), corner_radius=20, hover_color="#6C0000", bg_color="transparent", command=function_submit)
button_submit.place(x=87, y=230)

"""
user_input = input("type Y if you want to play or N to not ")

if user_input == "Y":
    print("play")
elif user_input == "N":
    pass

user_colors = ""
core_colors = ""

while user_colors == core_colors:

    colors=["red", "green", "blue"]
    core_colors = ""
    for x in range (3):
        color=random.randint(0,2)
        print(colors[color])
        core_colors+=colors[color] + ","
    print(core_colors)

    user_colors = ""
    for x in range (3):
        user_input_colors = input("type colors ")
        user_colors+=user_input_colors + ","
    print(user_colors)

    if user_colors == core_colors:
        print("win")
    else:
        print("neco")"""
#end of the aplication
app.mainloop()