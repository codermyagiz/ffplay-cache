from tkinter import *
import tkinter as tk
import os
import pathlib
import subprocess,io
import shutil
import glob

root = tk.Tk()
root.title('ffplay')
root.geometry('340x200')
root.maxsize(340,200)
root.minsize(340,200)
root.configure(bg="DeepSkyBlue3")

ffplay_main = r'{}/ffplay.exe'.format(os.getcwd())

def cache():
    browser = browser_entry.get()

    if browser == "Opera":
        home = str(pathlib.Path.home())+"\\AppData\\Local\\Opera Software\Opera Stable\Cache"
        ffplay_copy = home + "/ffplay.exe"
        shutil.copyfile(ffplay_main, ffplay_copy)
        os.chdir(f"{home}\\")

        while True:
            os.system("for /f %f in ('dir /b .') do ffplay %f")
    elif browser == "Firefox":
        home = str(pathlib.Path.home())+"\\AppData\\Local\\Mozilla\\Firefox\\Profiles\\"
        lenght_home = len(home)
        firefox_default_profile = home + "*default*"
        firefox_default_profile_id = glob.glob(firefox_default_profile)[0][lenght_home:lenght_home+28]
        main = f"{home}{firefox_default_profile_id}\\cache2\\entries"


        ffplay_copy = main + "/ffplay.exe"
        shutil.copyfile(ffplay_main, ffplay_copy)
        os.chdir(f"{main}\\")
        while True:
            os.system("for /F %f in ('dir /b .') do ffplay %f")
    elif browser == "Google Chrome":
        home = str(pathlib.Path.home())+"\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\Cache"
        ffplay_copy = home + "/ffplay.exe"
        shutil.copyfile(ffplay_main, ffplay_copy)
        os.chdir(f"{home}\\")
        while True:
            os.system("for /f %f in ('dir /b .') do ffplay %f")

def cache_path():
    browser = browser_entry.get()

    if browser == "Opera":
        home = str(pathlib.Path.home())+"\\AppData\\Local\\Opera Software\Opera Stable\Cache"
        path = os.path.realpath(home)
        subprocess.Popen(f'explorer {os.path.realpath(path)}')
    elif browser == "Firefox":
        home = str(pathlib.Path.home())+"\\AppData\\Local\\Mozilla\\Firefox\\Profiles\\"
        lenght_home = len(home)
        firefox_default_profile = home + "*default*"
        firefox_default_profile_id = glob.glob(firefox_default_profile)[0][lenght_home:lenght_home+28]
        main = f"{home}{firefox_default_profile_id}\\cache2\\entries"

        path = os.path.realpath(main)
        subprocess.Popen(f'explorer {os.path.realpath(path)}')
    elif browser == "Google Chrome":
        home = str(pathlib.Path.home())+"\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\Cache"
        path = os.path.realpath(home)
        subprocess.Popen(f'explorer {os.path.realpath(path)}')

title_label = tk.Label(root, text="View Cache With ffplay", fg="white", bg="DeepSkyBlue3", font=('verdana',13,'bold')).place(x=1, y=10)

browser_label = tk.Label(root, text="Browser:", fg="white", bg="DeepSkyBlue3", font=('verdana',11,'bold')).place(x=1, y=40)
browser_entry = tk.Entry(root)
browser_entry.place(x=80, y=45)

find_cache = tk.Button(root, text="Search", command=cache)
find_cache.place(x=210, y=43)

cache_path_label = tk.Label(root, text="Cache Path:", fg="white", bg="DeepSkyBlue3", font=('verdana',11,'bold'))
cache_path_label.place(x=1, y=90)

cache_path = tk.Button(root, text="Go Path", command=cache_path)
cache_path.place(x=110, y=90)

root.mainloop()
