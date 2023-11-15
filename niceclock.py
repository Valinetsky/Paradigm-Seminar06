""" 
Оригинал:
https://gist.github.com/m5wdev/c10429705a14771511a64227cf7d7335
Подробный разбор:
https://www.youtube.com/watch?v=6H7zgcbBj6A

Вынес настройки в блок 'Fonts and colors'
"""

from tkinter import Tk, Frame, Label, Button, Entry, StringVar
from tkinter.ttk import Notebook

from datetime import datetime, timedelta

# Fonts and colors
main_font = "OCR A Std"
# WILD WEST Font .)
# main_font="Rosewood Std Regular"

size_font_big = 50
size_font_medium = 30
size_font_small = 18
# size_font_start_button=18

fonts_big_color = "#7cccbf"
main_background = "#002f2f"


def clock():
    date_time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    date, time = date_time.split()
    date_label.config(text=date)
    time_label.config(text=time)
    time_label.after(1000, clock)


# Stopwatch
stopwatch_running = False
stopwatch_counter = 0


def set_start_stopwatch():
    global stopwatch_running
    stopwatch_running = True


def set_stopwatch_pause():
    global stopwatch_running
    stopwatch_running = False


def set_stopwatch_reset():
    global stopwatch_running, stopwatch_counter
    stopwatch_running = False
    stopwatch_counter = 0


def set_stopwatch_default_label():
    stopwatch_label.config(text="0:00:00.000")


def stopwatch(action=None):
    global stopwatch_counter

    if action == "start":
        stopwatch_counter = 0
        set_start_stopwatch()

    if action == "pause":
        set_stopwatch_pause()

    if action == "resume":
        set_start_stopwatch()

    if action == "reset":
        set_stopwatch_reset()
        set_stopwatch_default_label()

    if stopwatch_running:
        # format_time = str(timedelta(seconds=stopwatch_counter)) # convert number to time format '00:00:00'
        # stopwatch_label.after(1000, stopwatch)

        # format_time = str(timedelta(milliseconds=stopwatch_counter)) # convert number to time format '00:00:00.000000'
        format_time = str(timedelta(milliseconds=stopwatch_counter))[
            :-3
        ]  # '00:00:00.000'
        stopwatch_label.config(text=format_time)
        stopwatch_label.after(1, stopwatch)
        stopwatch_counter += 1


# Timer
timer_seconds_overall = 0
timer_running = False


def set_timer_run():
    global timer_running
    timer_running = True


def timer(action=None):
    global timer_running, timer_seconds_overall

    get_timer_entry = timer_entry.get()
    # print('get_timer_entry', get_timer_entry)
    timer_label.config(text=get_timer_entry)

    hours, minutes, seconds = get_timer_entry.split(":")
    # print('hours:', hours, 'minutes:', minutes, 'seconds:', seconds)

    seconds_in_hours = (int(hours) * 60) * 60
    # print('seconds_in_hours:', seconds_in_hours)

    seconds_in_minutes = int(minutes) * 60
    # print('seconds_in_minutes:', seconds_in_minutes)

    seconds_overall = seconds_in_hours + seconds_in_minutes + int(seconds)
    # print('seconds_overall:', seconds_overall)

    if action == "start":
        set_timer_run()
        timer_seconds_overall = seconds_overall

    if timer_seconds_overall <= 0:
        timer_running = False
        timer_seconds_overall = 0
        timer_label.config(text="STOP")
        play_sound()

    if timer_running:
        format_time = str(timedelta(seconds=timer_seconds_overall))
        timer_label.config(text=format_time)
        timer_label.after(1000, timer)
        timer_seconds_overall -= 1


def play_sound():
    import platform
    import os
    import winsound

    if platform.system() == "Windows":
        # winsound.Beep(5000, 1000) # крайне противный звук (частота, длительность)
        winsound.Beep(1000, 100)
        winsound.Beep(1000, 100)
        winsound.Beep(1000, 100)
        winsound.Beep(1000, 300)
        winsound.Beep(1000, 300)
        winsound.Beep(1000, 300)
        winsound.Beep(1000, 100)
        winsound.Beep(1000, 100)
        winsound.Beep(1000, 100)
    elif platform.system() == "Linux":
        os.system("beep -f 5000")


tk = Tk()
tk.title("Clock\\Stopwatch\\Timer")
tk.geometry("600x280")
tk.configure(background="blue")


tabs = Notebook(tk)
clock_tab = Frame(tabs, background=main_background)
stopwatch_tab = Frame(tabs, background=main_background)
timer_tab = Frame(tabs, background=main_background)
tabs.add(clock_tab, text="Clock")
tabs.add(stopwatch_tab, text="Stopwatch")
tabs.add(timer_tab, text="Timer")
tabs.pack(expand=1, fill="both")


time_label = Label(
    clock_tab,
    font=(main_font, size_font_big, "bold"),
    foreground=fonts_big_color,
    background=main_background,
)
time_label.pack(anchor="center")

date_label = Label(
    clock_tab,
    font=(main_font, size_font_medium, "bold"),
    foreground="grey",
    background=main_background,
)
date_label.pack(anchor="s")


stopwatch_label = Label(
    stopwatch_tab,
    font=(main_font, size_font_big, "bold"),
    foreground=fonts_big_color,
    background=main_background,
)
set_stopwatch_default_label()
stopwatch_label.pack(anchor="center")

stopwatch_start_button = Button(
    stopwatch_tab,
    text="Start",
    font=(main_font, size_font_small, "bold"),
    command=lambda: stopwatch("start"),
)
stopwatch_start_button.pack(anchor="center")

stopwatch_pause_button = Button(
    stopwatch_tab,
    text="Pause",
    font=(main_font, 12),
    command=lambda: stopwatch("pause"),
)
stopwatch_pause_button.pack(anchor="s")

stopwatch_resume_button = Button(
    stopwatch_tab,
    text="Resume",
    font=(main_font, 12),
    command=lambda: stopwatch("resume"),
)
stopwatch_resume_button.pack(anchor="center")

stopwatch_reset_button = Button(
    stopwatch_tab,
    text="Reset",
    font=(main_font, 12),
    command=lambda: stopwatch("reset"),
)
stopwatch_reset_button.pack(anchor="center")


timer_label = Label(
    timer_tab,
    font=(main_font, size_font_big, "bold"),
    foreground=fonts_big_color,
    background=main_background,
)
timer_label.config(text="0:00:00")
timer_label.pack(anchor="center")

timer_label_hints = Label(
    timer_tab,
    font=(main_font, size_font_small),
    foreground=fonts_big_color,
    background=main_background,
)
timer_label_hints.config(text="hours:minutes:seconds")
timer_label_hints.pack(anchor="center")

entry_default_text = StringVar()
timer_entry = Entry(
    timer_tab, font=(main_font, size_font_small), textvariable=entry_default_text
)
entry_default_text.set("0:00:00")
timer_entry.pack(anchor="center")

timer_start_button = Button(
    timer_tab,
    text="Start",
    font=(main_font, size_font_small, "bold"),
    command=lambda: timer("start"),
)
timer_start_button.pack(anchor="center")


clock()
tk.mainloop()
