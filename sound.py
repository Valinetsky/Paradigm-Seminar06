def play_sound():
    import platform
    import os
    import winsound

    if platform.system() == "Windows":
        winsound.Beep(1000, 200)
        winsound.Beep(1000, 400)
        winsound.Beep(1000, 800)
    elif platform.system() == "Linux":
        os.system("beep -f 5000")

play_sound()