import os
import pathlib
import subprocess,io
import shutil
import glob

browser = int(input(
"""
Which browser are you using?
1- Opera
2- Firefox
3- Google Chrome
"""))

ffplay_main = r'{}/ffplay.exe'.format(os.getcwd())

if browser == 1:
    home = str(pathlib.Path.home())+"\\AppData\\Local\\Opera Software\Opera Stable\Cache"
    ffplay_copy = home + "/ffplay.exe"
    shutil.copyfile(ffplay_main, ffplay_copy)
    os.chdir(f"{home}\\")

    while True:
        os.system("for /f %f in ('dir /b .') do ffplay %f")

if browser == 2:
    home = str(pathlib.Path.home())+"\\AppData\\Local\\Mozilla\\Firefox\\Profiles\\"
    lenght_home = len(home)
    firefox_default_profile = home + "*default*"
    firefox_default_profile_id = glob.glob(firefox_default_profile)[0][lenght_home:lenght_home+28]
    main = f"{home}{firefox_default_profile_id}\\cache2\\entries"


    ffplay_copy = home + "/ffplay.exe"
    shutil.copyfile(ffplay_main, ffplay_copy)
    os.chdir(f"{main}\\")
    while True:
        os.system("for /F %f in ('dir /b .') do ffplay %f")

if browser == 3:
    home = str(pathlib.Path.home())+"\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\Cache"
    ffplay_copy = home + "/ffplay.exe"
    shutil.copyfile(ffplay_main, ffplay_copy)
    os.chdir(f"{home}\\")
    while True:
        os.system("for /f %f in ('dir /b .') do ffplay %f")
