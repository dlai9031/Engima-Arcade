#Welcome to the Enigma Arcade!
#Contols will be listed below
#But i highly recommend to
#watch the full video to
#understand everything!
#Controls >>
#

# [>] Or Right Arrow keys will
#go to the next section
#
#[>] Or Left Arrow keys will bring
#you back to the previous section
#
# [Up Key] will go to the help menu if
#your in the menu menu
#
#{Down Key] will go to the main menu
#if your in help menu
#
#[S]
#Opens the Section finder!
#
#[1]
#Brings you to Section 1
#
#[2]
#Brings you to Section 2
#
#[M] Will bring you to the main menu
#
#[H] Will bring you to the help menu
#
#[Click on MIDDLE OF logo] will bring
#you to preprogrammed game or video...
#
#Learn more by going to the website link
#Link: https://who6907.wixsite.com/enigmaarcadeweb

#checks the users OS to output the right verison!
global os_check
os_check = 0
from tkinter import messagebox
msg = messagebox.showinfo("Enigma Arcade!", "Welcome Ladies And Gentlemen to the Enigma Arcade!")
msg = messagebox.showinfo("Enigma Arcade!", "Before you begin your journey! We must know what operating system (os) do you have! (*Please be accurate as some features are not cross plateform and may crash your game! If used on a different OS!*)")
msg = messagebox.askquestion("Enigma Arcade!", "Are you currently using any form of windows os? Examples >> (1.0,2.0,3.0,95,98,ME,2000,XP,VISTA,7,8,8.1,10)")
if msg == "yes":
    msg = messagebox.showinfo("Enigma Arcade!", "Thats awesome! Every module should work for you! And dont forget to have fun :D!")
if msg == "no":
    msg = messagebox.askquestion("Enigma Arcade!", "Ok, thats fine! Are you using any form of mac os? Examples >>*(Ex from os starting from 2011*)(OS X Mountain Lion – 10.8, OS X Mavericks – 10.9, OS X Yosemite – 10.10, OS X El Capitan – 10.11, MacOS Sierra – 10.12, macOS High Sierra – 10.13, Mojave – 10.14)")
    if msg == "yes":
        os_check = 5
        msg = messagebox.showinfo("Enigma Arcade!", "Thats awesome! Most module should work for you! But the pop up info will be in the python shell and you will have to manually open a game file and run it. But anyways don't forget to have fun :D!")
    if msg == "no":
        msg = messagebox.askquestion("Enigma Arcade!", "Are you running any form of linix os? (*Too many to name*)")
        if msg == "yes":
            
            print("nice")
            msg = messagebox.askquestion("Enigma Arcade!", "Your current os might or might not work?")
        if msg == "no":
            msg = messagebox.askquestion("Enigma Arcade!", "Hum?... Your current os might or might not work with enigma aracde and other games associated with enigma arcade")            
from gamelibwillh2 import*
try:
    import win32gui, win32con
except ModuleNotFoundError:
    pass
import webbrowser
import os
import tkinter as Tk
import ctypes
import time
import os
global music_value
music_value = 0
global music_values
music_values = 0
#This is the start of the game with the spinning coin in which users
#can also change there Verision that is best fitted for them
#[W] windows verison
#[m] mac verison
def enigma_start():
    game = Game(800,600,"Enigma Arcade! PRESS COIN TO START!")
    try:
        start = Image("Enigma_Arcade_Files\\arcade_start.png",game)
    except pygame.error:
        start = Image("Enigma_Arcade_Files//arcade_start.png",game)
    start.resizeTo(game.width,game.height)
    try:
        bk1 = Animation("Enigma_Arcade_Files\\coin_spin.png",6,game,1920/6,320)
    except pygame.error:
        bk1 = Animation("Enigma_Arcade_Files//coin_spin.png",6,game,1920/6,320)
    bk1.resizeTo(game.width,game.height)
    try:
         bk = Image("Enigma_Arcade_Files\\Enigma_logo.png",game)
    except pygame.error:
         bk = Image("Enigma_Arcade_Files//Enigma_logo.png",game) 
    bk.moveTo(400,70)
    try:
        game.setMusic("Enigma_Arcade_Files\\arcade_main_theme.mp3")
    except pygame.error:
        game.setMusic("Enigma_Arcade_Files//arcade_main_theme.mp3")
    game.playMusic()
    while not game.over:
        game.processInput()
        start.draw()
        bk1.move()
        bk.draw()
        if mouse.collidedWith(bk1) and mouse.LeftClick:
            enigma_move()
        if keys.Pressed[K_ESCAPE]:
            game.over = True
            game.quit()
            quit()
        if keys.Pressed[K_RIGHT]:
            game.over = True
            enigma_move()
        if keys.Pressed[K_m]:
            print("*****************************************")
            print("Sucessfully converted to the mac verison!")
            print("*****************************************")
            global os_check
            os_check = 5
        if keys.Pressed[K_w]:
            from tkinter import messagebox
            msg = messagebox.showinfo("Enigma Arcade!", "Sucessfully converted to the windows verison!")
            os_check = 0
        game.update(30)
    game.quit()
#made global variable so i can excess the value anywhere :D!
global vid_true_value
vid_true_value = 0
#This is the main menu which will either go to section one or help menu!
def enigma_in_stay_start():
    game = Game(750,600,"Enigma Arcade_Main Menu!")
    try:
         start = Image("Enigma_Arcade_Files\\arcades_outs.png",game)
    except pygame.error:
         start = Image("Enigma_Arcade_Files//arcades_outs.png",game) 
    start.resizeTo(game.width,game.height)
    try:
         bk = Image("Enigma_Arcade_Files\\Enigma_logo.png",game)
    except pygame.error:
         bk = Image("Enigma_Arcade_Files//Enigma_logo.png",game)
    bk.moveTo(378,100)
    if os_check <=0:
        f7 = Font(blue,40,black,"Comic Sans MS")
    if os_check >0:
        f7 = Font(blue,58,black,"Comic Sans MS")
    time.sleep(1)
    try:
        game.setMusic("Enigma_Arcade_Files\\blue1.mp3")
        game.playMusic()
    except pygame.error:
        game.setMusic("Enigma_Arcade_Files//blue1.mp3")
        game.playMusic()
    while not game.over:
        game.processInput()
        start.draw()
        bk.draw()
        game.drawText("Press H For Help Menu",170,420,f7)
        game.drawText("Press Space To Start Adventure",66,470,f7)
        if keys.Pressed[K_UP]:
            game.over = True
            enigma_in_stay_help()
        if keys.Pressed[K_h]:
            enigma_in_stay_help()
        if keys.Pressed[K_SPACE]:
            if os_check >0:
                if vid_true_value <1:
                    print("")
                    print("*************************************************************************")
                    print("Hey looks you didn't look at the help menu, We high advise you to do so!")
                    print("*************************************************************************")
                    game.over = True
                    enigma_screen_1()
                if vid_true_value >=1:
                    print("********************************************************")
                    print("Thanks for watching the tutorial!, Now its time to play!")
                    print("********************************************************")
                    print("")
                    game.over = True
                    enigma_screen_1()
            if os_check <=0:
                if vid_true_value <1:
                    from tkinter import messagebox
                    msg = messagebox.showinfo("Enigma Arcade!", "Hey looks you didn't look at the help menu, We high advise you to do so!")
                    if msg == "ok":
                        game.over = True
                        enigma_screen_1()
                if vid_true_value >=1:
                    game.over = True
                    enigma_screen_1()
        if keys.Pressed[K_ESCAPE]:
            game.over = True
            game.quit()
            quit()
        if keys.Pressed[K_m]:
            enigma_start()
        if keys.Pressed[K_LEFT]:
            enigma_start()
        if keys.Pressed[K_RIGHT]:
            game.over = True
            if os_check >0:
                if vid_true_value <1:
                    print("")
                    print("*************************************************************************")
                    print("Hey looks you didn't look at the help menu, We high advise you to do so!")
                    print("*************************************************************************")
                    game.over = True
                    enigma_screen_1()
                if vid_true_value >=1:
                    print("********************************************************")
                    print("Thanks for watching the tutorial!, Now its time to play!")
                    print("********************************************************")
                    print("")
                    game.over = True
                    enigma_screen_1()
            if os_check <=0:
                if vid_true_value <1:
                    from tkinter import messagebox
                    msg = messagebox.showinfo("Enigma Arcade!", "Hey looks you didn't look at the help menu, We high advise you to do so!")
                    if msg == "ok":
                        game.over = True
                        enigma_screen_1()
                if vid_true_value >=1:
                    game.over = True
                    enigma_screen_1()
        game.update(60)
    game.quit()
#The help menu which will answer many questions beginners may have!
def enigma_in_stay_help():
    game = Game(750,600,"Enigma Arcade_Help Menu!")
    try:
        game.setMusic("Enigma_Arcade_Files\\Megalovania_piano_edition.mp3")
    except pygame.error:       
        game.setMusic("Enigma_Arcade_Files//Megalovania_piano_edition.mp3")
    game.playMusic()
    try:
        bk = Image("Enigma_Arcade_Files\\Enigma_logo.png",game)
    except pygame.error:
        bk = Image("Enigma_Arcade_Files//Enigma_logo.png",game)
    try:
        start = Image("Enigma_Arcade_Files\\arcades_outs.png",game)
    except pygame.error:
        start = Image("Enigma_Arcade_Files//arcades_outs.png",game)
    start.resizeTo(game.width,game.height)
    bk.moveTo(378,100)
    if os_check <=0:
        f7 = Font(blue,40,black,"Comic Sans MS")
    if os_check >0:
        f7 = Font(blue,58,black,"Comic Sans MS")
    if os_check <=0:
        f9 = Font(blue,28,black,"Comic Sans MS")
    if os_check >0:
        f9 = Font(blue,38,black,"Comic Sans MS")
    try:
        play_button_move = Animation("Slap_Or_Stack_Files\\Background_Buttons\\play_button_move.png",110,game,8000/10,6600/11)
    except pygame.error:
        play_button_move = Animation("Slap_Or_Stack_Files//Background_Buttons//play_button_move.png",110,game,8000/10,6600/11)
    play_button_move.resizeBy(-65)
    play_button_move.moveTo(375,250)
    try:
        play_button = Image("Slap_Or_Stack_Files\\Background_Buttons\\play_button_main.png",game)
    except pygame.error:
        play_button = Image("Slap_Or_Stack_Files//Background_Buttons//play_button_main.png",game)
    play_button.resizeBy(-65)
    play_button.moveTo(375,250)
    while not game.over:
        game.processInput()
        start.draw()
        bk.draw()
        play_button.draw()
        game.drawText("Press 1 for problem 1, How do i upload a game?",70,440,f9)
        game.drawText("Press 2 for problem 2, Why is it called Enigma? ",70,412,f9)
        game.drawText("Press 3 for problem 3, What is Game Controls?",70,384,f9)
        game.drawText("Press play button to understand all questions!",70,356,f9)
        game.drawText("Press M For Main Menu",170,470,f7)
        if keys.Pressed[K_DOWN]:
            game.over = True
            enigma_in_stay_start()
        if keys.Pressed[K_h]:
            game.over = True
            enigma_screen_1()
        if keys.Pressed[K_m]:
            game.over = True
            enigma_in_stay_start()
        if keys.Pressed[K_1]:
            game.over = True
            GAME_Rule()
        if keys.Pressed[K_3]:
            game.over = True
            enigma_screen_test()
        if keys.Pressed[K_2]:
            game.over = True
            credit_ea_explaination_screen()
        if keys.Pressed[K_ESCAPE]:
            game.over = True
            game.quit()
            quit()
        if mouse.collidedWith(play_button):
            play_button_move.move()
        if mouse.collidedWith(play_button) and mouse.LeftClick:
            global vid_true_value
            vid_true_value = 4
            
            if os_check <=0:
                from tkinter import messagebox
                msg = messagebox.showinfo("Enigma Arcade!", "Scroll down until you see the watch tutorial video! and click it! :D!, You are also welcome to look around the website :D!")
                webbrowser.open("https://who6907.wixsite.com/enigmaarcadeweb/informationmenu")
            if os_check >0:
                print("************************************************************************************************************************************************************")
                print("Sorry your os can not view the website link via button :(, But you can go to the link (https://who6907.wixsite.com/enigmaarcadeweb/informationmenu)!")
                print("After entering the website please scroll down until you see the watch tutorial video! and click it! :D!, You are also welcome to look around the website :D!")
                print("************************************************************************************************************************************************************")                
        if keys.Pressed[K_RIGHT]:
            game.over = True
            GAME_Rule()
        if keys.Pressed[K_LEFT]:
            game.over = True
            enigma_in_stay_start()
        game.update(60)
    game.quit()
#This is the spinning start which will go to the main menu at the end
def enigma_move():
    game = Game(800,600,"Enigma_Arcade!")
    try:
        start = Animation("Enigma_Arcade_Files\\arcade_in.png",11,game,4000/5,1800/3)
    except pygame.error:
        start = Animation("Enigma_Arcade_Files//arcade_in.png",11,game,4000/5,1800/3)
    global music_values
    music_values = 1
    game.stopMusic()
    try:
        game.setMusic("Enigma_Arcade_Files\\insert_coin_effects.mp3")
    except pygame.error:
        game.setMusic("Enigma_Arcade_Files//insert_coin_effects.mp3")
    game.playMusic()
    while not game.over:
        game.score +=10
        game.processInput()
        start.move()
        if game.score >=110:
            enigma_in_stay_start()
        game.update(10)
    game.quit()
#this is section one which holds SOS and Pong
def enigma_screen_1():
    game = Game(750,600,"Enigma Arcade Section_1!")
    #This allows users to play the song stay on the song with out restarting
    #said song! But if you want to restart the music you will have to press R
    try:
        start = Image("Enigma_Arcade_Files\\arcades_outs.png",game)
    except pygame.error:
        start = Image("Enigma_Arcade_Files//arcades_outs.png",game)
    start.resizeTo(game.width,game.height)
    try:
        bk = Image("Enigma_Arcade_Files\\Enigma_logo.png",game)
    except pygame.error:
        bk = Image("Enigma_Arcade_Files//Enigma_logo.png",game)

    bk.moveTo(378,100)
    try:
        sos_logo = Image("Slap_Or_Stack_Files\\Background_Buttons\\Slap Or Stack_logo_offical.png",game)
    except pygame.error:
        sos_logo = Image("Slap_Or_Stack_Files//Background_Buttons//Slap Or Stack_logo_offical.png",game)
    sos_logo.resizeBy(-85)
    sos_logo.moveTo(240,350)
    try:
        plogo = Image("Pong_Game_Files\\background\\pong_logo_main.png",game)
    except pygame.error:
        plogo = Image("Pong_Game_Files//background//pong_logo_main.png",game)
    plogo.resizeBy(-30)
    plogo.moveTo(550,350)
    if os_check <=0:
        f7 = Font(blue,40,black,"Comic Sans MS")
    if os_check >0:
        f7 = Font(blue,58,black,"Comic Sans MS") 
    while not game.over:
        game.processInput()
        start.draw()
        bk.draw()
        sos_logo.draw()
        plogo.draw()
        game.drawText("Section One",270,150,f7)
        game.drawText("Slap Or Stack!",100,450,f7)
        game.drawText("Pong!",500,450,f7)
        game.drawText("LL Productions Game!",180,184,f7)
        if keys.Pressed[K_ESCAPE]:
            game.over = True
            game.quit()
            quit()
        if keys.Pressed[K_r]:
            try:
                game.setMusic("Enigma_Arcade_Files\\blue1.mp3")
                game.playMusic()
            except pygame.error:
                game.setMusic("Enigma_Arcade_Files//blue1.mp3")
                game.playMusic()
        if keys.Pressed[K_p]:
            if os_check <=0:
                from tkinter import messagebox
                msg = messagebox.askquestion("Enigma Arcade!", "Do you feel the rush?")
                if msg == "no":
                    pass
                if msg == "yes":
                    game.stopMusic()
                    try:
                        game.setMusic("Enigma_Arcade_Files\\blue_1-2.mp3")
                    except pygame.error:
                        game.setMusic("Enigma_Arcade_Files//blue_1-2.mp3")
                    game.playMusic()
                    from tkinter import messagebox
                    msg = messagebox.askquestion("Enigma Arcade!", "Do you feel the rush?")
                    if msg == "no":
                        pass
                    if msg == "yes":
                        game.stopMusic()
                        try:
                            game.setMusic("Enigma_Arcade_Files\\blue_1.5.mp3")
                        except pygame.error:
                            game.setMusic("Enigma_Arcade_Files//blue_1.5.mp3")
                        from tkinter import messagebox
                        msg = messagebox.showinfo("Enigma Arcade!", "Hang on tight! Get ready for your heart to explode!")
                        game.playMusic()
        if keys.Pressed[K_LEFT]:
            game.over = True
            enigma_in_stay_start()
        if keys.Pressed[K_RIGHT]:
            game.over = True
            enigma_screen_2()
        if keys.Pressed[K_s]:
            game.over = True
            section_finder()
        if keys.Pressed[K_2]:
            game.over = True
            enigma_screen_2() 
        if keys.Pressed[K_0]:
            game.over = True
            enigma_screen_test()
        if keys.Pressed[K_m]:
            game.over = True
            enigma_in_stay_start()
        if keys.Pressed[K_h]:
            game.over = True
            enigma_in_stay_help()
        if mouse.collidedWith(sos_logo) and mouse.LeftClick:
            try:
                Minimize = win32gui.GetForegroundWindow()
                win32gui.ShowWindow(Minimize, win32con.SW_MINIMIZE)
            except NameError:
                pass
            if os_check <=0:
                from tkinter import messagebox
                msg = messagebox.askquestion("Enigma Arcade!", "Would you like to close Enigma Arcade?")
                if msg == "no":
                    pass
                if msg == "yes":
                    game.over = True
                    game.quit()
            webbrowser.open('ball_game_main.py')
            if os_check <=0:
                time.sleep(5)
                from tkinter import messagebox
                msg = messagebox.askquestion("Enigma Arcade!", "Now that you have tried Slap Or Stack? Was it enjoyable?")
                if msg == "no":
                    msg = messagebox.showinfo("Enigma Arcade!", "Sorry to hear that :(, If you would like contact us at who6907@baysidehighschool.org and our team will be glad to change that! :D!")
                if msg == "yes":
                    msg = messagebox.showinfo("Enigma Arcade!", "Thats great to hear! Well then you have to check out LL Productions game i will be sure you like! :D")
            if os_check >0:
                print("***************************************************************************")
                reply = str(input("Now that you will start [Slap or stack] Would you like to close Enigma Arcade?"+' (y/n) Type Here >>: ')).lower().strip()
                print("***************************************************************************")
                print("")
                if reply[0] == 'y':
                    print("****************************************************************************************************")
                    print("OK closing Enigma Arcade")
                    print("****************************************************************************************************")
                    game.over = True
                    game.quit()
                if reply[0] == 'n':
                    print("**********************************************************************************************************************************")
                    print("OK Enigma Arcade will be still open!")
                    print("**********************************************************************************************************************************")
            if os_check >0:
                print("")
                print("*****************************************************************************************************")
                print("In order to play [Slap Or Stack] you will have to go to {ball_game_main.py} and run the file with a IDLE!")
                print("*****************************************************************************************************")
                time.sleep(5)
                print("********************************************************************************")
                reply = str(input("Now that you have tried Slap Or Stack? Was it enjoyable?"+' (y/n) Type Here >>: ')).lower().strip()
                print("********************************************************************************")
                if reply[0] == 'y':
                    print("****************************************************************************************************")
                    print("Thats great to hear! Well then you have to check out LL Productions game i will be sure you like! :D")
                    print("****************************************************************************************************")
                if reply[0] == 'n':
                    print("**********************************************************************************************************************************")
                    print("Sorry to hear that :(, If you would like contact us at who6907@baysidehighschool.org and our team will be glad to change that! :D!")
                    print("**********************************************************************************************************************************")
        if mouse.collidedWith(plogo) and mouse.LeftClick:
            try:
                Minimize = win32gui.GetForegroundWindow()
                win32gui.ShowWindow(Minimize, win32con.SW_MINIMIZE)
            except NameError:
                pass
            if os_check >0:
                print("***************************************************************************")
                reply = str(input("Now that you will start [Pong] Would you like to close Enigma Arcade?"+' (y/n) Type Here >>: ')).lower().strip()
                print("***************************************************************************")
                print("")
                if reply[0] == 'y':
                    print("****************************************************************************************************")
                    print("OK closing Enigma Arcade")
                    print("****************************************************************************************************")
                    game.over = True
                    game.quit()
                if reply[0] == 'n':
                    print("**********************************************************************************************************************************")
                    print("OK Enigma Arcade will be still open!")
                    print("**********************************************************************************************************************************")
            if os_check <=0:
                from tkinter import messagebox
                msg = messagebox.askquestion("Enigma Arcade!", "Would you like to close Enigma Arcade?")
                if msg == "no":
                    pass
                if msg == "yes":
                    game.over = True
                    game.quit()
            webbrowser.open('pong_game_main.py')
            if os_check <=0:
                time.sleep(5)
                from tkinter import messagebox
                msg = messagebox.askquestion("Enigma Arcade!", "Now that you have tried Pong? Was it enjoyable?")
                if msg == "no":
                    msg = messagebox.showinfo("Enigma Arcade!", "Sorry to hear that :(, If you would like contact us at who6907@baysidehighschool.org and our team will be glad to change that! :D!")
                if msg == "yes":
                    msg = messagebox.showinfo("Enigma Arcade!", "Thats great to hear! Well then you have to check out LL Productions game i will be sure you like! :D")
            if os_check >0:
                print("")
                print("*****************************************************************************************************")
                print("In order to play [pong game] you will have to go to {pong_game_main.py} and run the file with a IDLE!")
                print("*****************************************************************************************************")
                time.sleep(5)
                print("***************************************************************************")
                reply = str(input("Now that you have tried pong game? Was it enjoyable?"+' (y/n) Type Here >>: ')).lower().strip()
                print("***************************************************************************")
                print("")
                if reply[0] == 'y':
                    print("****************************************************************************************************")
                    print("Thats great to hear! Well then you have to check out LL Productions game i will be sure you like! :D")
                    print("****************************************************************************************************")
                if reply[0] == 'n':
                    print("**********************************************************************************************************************************")
                    print("Sorry to hear that :(, If you would like contact us at who6907@baysidehighschool.org and our team will be glad to change that! :D!")
                    print("**********************************************************************************************************************************")
        game.update(60)
    game.quit()
#this is section two which holds breakout and pacman!
def enigma_screen_2():
    game = Game(750,600,"Enigma Arcade Section_1!")
    try:
        start = Image("Enigma_Arcade_Files\\arcades_outs.png",game)
    except pygame.error:
        start = Image("Enigma_Arcade_Files//arcades_outs.png",game)
    start.resizeTo(game.width,game.height)
    try:
        bk = Image("Enigma_Arcade_Files\\Enigma_logo.png",game)
    except pygame.error:
        bk = Image("Enigma_Arcade_Files//Enigma_logo.png",game)

    bk.moveTo(378,100)
    try:
        b_logo = Image("Breakout_Files\\breakout_logo.jpg",game)
    except pygame.error:
        b_logo = Image("Breakout_Files//breakout_logo.jpg",game)
    b_logo.resizeTo(300,150)
    b_logo.moveTo(220,380)
    if os_check <=0:
        f7 = Font(blue,40,black,"Comic Sans MS")
    if os_check >0:
        f7 = Font(blue,58,black,"Comic Sans MS")
    try:
        p_logo = Image("PacMan_Files\\cover.png",game)
    except pygame.error:       
        p_logo = Image("PacMan_Files//cover.png",game)
    p_logo.resizeTo(250,150)
    p_logo.moveTo(550,380)
    while not game.over:
        game.processInput()
        start.draw()
        bk.draw()
        b_logo.draw()
        p_logo.draw()
        game.drawText("Section Two",270,150,f7)
        game.drawText("Breakout!",135,450,f7)
        game.drawText("PacMan",555-75,450,f7)
        game.drawText("LL Productions Game!",180,184,f7)
        if keys.Pressed[K_ESCAPE]:
            game.over = True
            game.quit()
            quit()
        if keys.Pressed[K_LEFT]:
            game.over = True
            enigma_screen_1()
        if keys.Pressed[K_RIGHT]:
            game.over = True
            enigma_screen_test()
        if keys.Pressed[K_s]:
            game.over = True
            section_finder()
        if keys.Pressed[K_0]:
            game.over = True
            enigma_screen_test()
        if keys.Pressed[K_1]:
            game.over = True
            enigma_screen_1()
        if keys.Pressed[K_m]:
            game.over = True
            enigma_in_stay_start()
        if keys.Pressed[K_h]:
            game.over = True
            enigma_in_stay_help()
        if mouse.collidedWith(b_logo) and mouse.LeftClick:
            try:
                Minimize = win32gui.GetForegroundWindow()
                win32gui.ShowWindow(Minimize, win32con.SW_MINIMIZE)
            except NameError:
                pass
            if os_check >0:
                print("***************************************************************************")
                reply = str(input("Now that you will start [Breakout] Would you like to close Enigma Arcade?"+' (y/n) Type Here >>: ')).lower().strip()
                print("***************************************************************************")
                print("")
                if reply[0] == 'y':
                    print("****************************************************************************************************")
                    print("OK closing Enigma Arcade")
                    print("****************************************************************************************************")
                    game.over = True
                    game.quit()
                if reply[0] == 'n':
                    print("**********************************************************************************************************************************")
                    print("OK Enigma Arcade will be still open!")
                    print("**********************************************************************************************************************************")
            if os_check <=0:
                from tkinter import messagebox
                msg = messagebox.askquestion("Enigma Arcade!", "Would you like to close Enigma Arcade?")
                if msg == "no":
                    pass
                if msg == "yes":
                    game.over = True
                    game.quit()
            #Minimize = win32gui.GetForegroundWindow()
            #win32gui.ShowWindow(Minimize, win32con.SW_MINIMIZE)
            webbrowser.open('breakout_game_main.py')
            if os_check <=0:
                time.sleep(5)
                from tkinter import messagebox
                msg = messagebox.askquestion("Enigma Arcade!", "Now that you have tried Breakout? Was it enjoyable?")
                if msg == "no":
                    msg = messagebox.showinfo("Enigma Arcade!", "Sorry to hear that :(, If you would like contact us at who6907@baysidehighschool.org and our team will be glad to change that! :D!")
                if msg == "yes":
                    msg = messagebox.showinfo("Enigma Arcade!", "Thats great to hear! Well then you have to check out LL Productions game i will be sure you like! :D")
            if os_check >0:
                print("")
                print("*****************************************************************************************************")
                print("In order to play [Breakout] you will have to go to {breakout_game_main.py} and run the file with a IDLE!")
                print("*****************************************************************************************************")
                time.sleep(5)
                print("********************************************************************************")
                reply = str(input("Now that you have tried Breakout? Was it enjoyable?"+' (y/n) Type Here >>: ')).lower().strip()
                print("********************************************************************************")
                if reply[0] == 'y':
                    print("****************************************************************************************************")
                    print("Thats great to hear! Well then you have to check out LL Productions game i will be sure you like! :D")
                    print("****************************************************************************************************")
                if reply[0] == 'n':
                    print("**********************************************************************************************************************************")
                    print("Sorry to hear that :(, If you would like contact us at who6907@baysidehighschool.org and our team will be glad to change that! :D!")
                    print("**********************************************************************************************************************************")
        if mouse.collidedWith(p_logo) and mouse.LeftClick:
            try:
                Minimize = win32gui.GetForegroundWindow()
                win32gui.ShowWindow(Minimize, win32con.SW_MINIMIZE)
            except NameError:
                pass
            if os_check >0:
                print("***************************************************************************")
                reply = str(input("Now that you will start [PacMan] Would you like to close Enigma Arcade?"+' (y/n) Type Here >>: ')).lower().strip()
                print("***************************************************************************")
                print("")
                if reply[0] == 'y':
                    print("****************************************************************************************************")
                    print("OK closing Enigma Arcade")
                    print("****************************************************************************************************")
                    game.over = True
                    game.quit()
                if reply[0] == 'n':
                    print("**********************************************************************************************************************************")
                    print("OK Enigma Arcade will be still open!")
                    print("**********************************************************************************************************************************")
            if os_check <=0:
                from tkinter import messagebox
                msg = messagebox.askquestion("Enigma Arcade!", "Would you like to close Enigma Arcade?")
                if msg == "no":
                    pass
                if msg == "yes":
                    game.over = True
                    game.quit()
            webbrowser.open('Pacman_main.py')
            if os_check <=0:
                time.sleep(5)
                from tkinter import messagebox

                msg = messagebox.askquestion("Enigma Arcade!", "Now that you have tried PacMan? Was it enjoyable?")
                if msg == "no":
                    msg = messagebox.showinfo("Enigma Arcade!", "Sorry to hear that :(, If you would like contact us at who6907@baysidehighschool.org and our team will be glad to change that! :D!")
                if msg == "yes":
                    msg = messagebox.showinfo("Enigma Arcade!", "Thats great to hear! Well then you have to check out LL Productions game i will be sure you like! :D")
            if os_check >0:
                print("")
                print("*****************************************************************************************************")
                print("In order to play [PacMan] you will have to go to {Pacman_main.py} and run the file with a IDLE!")
                print("*****************************************************************************************************")
                time.sleep(5)
                print("********************************************************************************")
                reply = str(input("Now that you have tried PacMan? Was it enjoyable?"+' (y/n) Type Here >>: ')).lower().strip()
                print("********************************************************************************")
                if reply[0] == 'y':
                    print("****************************************************************************************************")
                    print("Thats great to hear! Well then you have to check out LL Productions game i will be sure you like! :D")
                    print("****************************************************************************************************")
                if reply[0] == 'n':
                    print("**********************************************************************************************************************************")
                    print("Sorry to hear that :(, If you would like contact us at who6907@baysidehighschool.org and our team will be glad to change that! :D!")
                    print("**********************************************************************************************************************************")

        game.update(60)
    game.quit()
#This is N/A!
def enigma_screen_control_menu():
    game = Game(750,600,"Enigma Arcade_control menu!")
    try:
        start = Image("Enigma_Arcade_Files\\arcades_outs.png",game)
    except pygame.error:
        start = Image("Enigma_Arcade_Files//arcades_outs.png",game)
    start.resizeTo(game.width,game.height)
    try:
        bk = Image("Enigma_Arcade_Files\\Enigma_logo.png",game)
    except pygame.error:
        bk = Image("Enigma_Arcade_Files//Enigma_logo.png",game)
    bk.moveTo(378,100)
    f7 = Font(blue,40,black,"Comic Sans MS")
    while not game.over:
        game.processInput()
        start.draw()
        bk.draw()
        game.drawText("Control Tutorial!",220,150,f7)
        game.drawText("Press Spacebar To Start!",150,450,f7)
        if keys.Pressed[K_ESCAPE]:
            game.over = True
            game.quit()
            quit()
        if keys.Pressed[K_SPACE]:
            game.over = True
            enigma_screen_test()
        if keys.Pressed[K_m]:
            game.over = True
            enigma_in_stay_start()
        game.update(60)
    game.quit()
#This is the control menu! It shows how everything is structured
#and the mostly for the controls!
def enigma_screen_test():
    game = Game(750,600,"Enigma Arcade_Creator Layout!")
    try:
        start = Image("Enigma_Arcade_Files\\arcades_outs.png",game)
    except pygame.error:
        start = Image("Enigma_Arcade_Files//arcades_outs.png",game)
    start.resizeTo(game.width,game.height)
    try:
        bk = Image("Enigma_Arcade_Files\\Enigma_logo.png",game)
    except pygame.error:
        bk = Image("Enigma_Arcade_Files//Enigma_logo.png",game)
    bk.moveTo(378,100)
    try:
        test = Image("Enigma_Arcade_Files\\working!.jpg",game)
    except pygame.error:    
        test = Image("Enigma_Arcade_Files//working!.jpg",game)
    test.resizeBy(-10)
    test.moveTo(220,350)
    try:
        click_me = Image("Enigma_Arcade_Files\\click_me_logo.png",game)
    except pygame.error:
        click_me = Image("Enigma_Arcade_Files//click_me_logo.png",game)
    click_me.resizeBy(-40)
    click_me.moveTo(220,350)
    if os_check <=0:
        f7 = Font(blue,40,black,"Comic Sans MS")
    if os_check >0:
        f7 = Font(blue,54,black,"Comic Sans MS")
    if os_check <=0:
        f9 = Font(blue,25,black,"Comic Sans MS")
    if os_check >0:

        f9 = Font(blue,30,black,"Comic Sans MS")
    while not game.over:
        game.processInput()
        start.draw()
        bk.draw()
        test.draw()
        game.drawText("Section N/A",270,150,f7)
        game.drawText("Game Name!",120,450,f7)
        game.drawText("<< Click on logo to play game!",350,350,f9)
        game.drawText("<Tip>! Number key = section #!",320,372,f9)
        game.drawText("<Tip>! Press 1 To Goto Section 1!",320,400,f9)
        game.drawText("<Tip>! Press H For Help Menu!",320,428,f9)
        game.drawText("Expression/slogan/company name!",56,184,f7)
        if keys.Pressed[K_ESCAPE]:
            game.over = True
            game.quit()
            quit()
        if mouse.collidedWith(click_me):
            click_me.draw()
        if keys.Pressed[K_m]:
            game.over = True
            enigma_in_stay_start()
        if keys.Pressed[K_h]:
            game.over = True
            enigma_in_stay_help()
        if keys.Pressed[K_LEFT]:
            game.over = True
            enigma_in_stay_help()
        if keys.Pressed[K_RIGHT]:
            game.over = True
            enigma_screen_1()
        #add more here!
        if keys.Pressed[K_1]:
            if os_check <=0:
                from tkinter import messagebox
                msg = messagebox.showinfo("Enigma Arcade!", "GET READY TO EXPERIENCE TRUE GAMING! (*Most the keys are kind of obvious but whatever :D*)")
                if msg == "ok":
                    game.over = True
                    enigma_screen_1()
            if os_check >0:
                print("")
                print("******************************************************************************************")
                print("GET READY TO EXPERIENCE TRUE GAMING! (*Most the keys are kind of obvious but whatever :D*)")
                print("******************************************************************************************")
                time.sleep(1)
                game.over = True
                enigma_screen_1()
        if mouse.collidedWith(test) and mouse.LeftClick:
            if os_check <=0:
                from tkinter import messagebox
                msg = messagebox.showinfo("Enigma Arcade!", "No game here :(, But you can play real ones by clicking on the middle of the logo on different sections! :D!")
            if os_check >0:
                print("")
                print("*******************************************************************************************")
                print("No game here :(, But you can play real ones by clicking on the middle of the logo on different sections! :D!")
                print("*******************************************************************************************")
        game.update(60)
    game.quit()
#Enigma Arcade Explained!
def credit_ea_explaination_screen():
    game = Game(750,600,"Enigma Arcade_History!")
    try:
        start = Image("Enigma_Arcade_Files\\arcades_outs.png",game)
    except pygame.error:
        start = Image("Enigma_Arcade_Files//arcades_outs.png",game)        
    start.resizeTo(game.width,game.height)
    try:
        bk = Image("Enigma_Arcade_Files\\Enigma_logo.png",game)
    except pygame.error:
        bk = Image("Enigma_Arcade_Files//Enigma_logo.png",game)
    bk.moveTo(375,100)
    #enigma machine = em
    try:
        em = Image("Enigma_Arcade_Files\\Enigma_Machine_main.jpg",game)
    except pygame.error:
        em = Image("Enigma_Arcade_Files//Enigma_Machine_main.jpg",game)
    em.resizeBy(-75)
    em.moveTo(200,472)
    if os_check <=0:
        f9 = Font(blue,25,black,"Comic Sans MS")
    if os_check >0:
        f9 = Font(blue,30,black,"Comic Sans MS")
    while not game.over:
        game.processInput()
        start.draw()
        bk.draw()
        em.draw()
        if keys.Pressed[K_ESCAPE]:
            game.over = True
            game.quit()
            quit()
        if keys.Pressed[K_m]:
            game.over = True
            enigma_in_stay_start()
        if keys.Pressed[K_h]:
            game.over = True
            enigma_in_stay_help()
        if mouse.collidedWith(em) and mouse.LeftClick:
            game.over = True
            LL_credit_menu()
        if keys.Pressed[K_LEFT]:
            game.over = True
            enigma_in_stay_help()
        if keys.Pressed[K_RIGHT]:
            game.over = True
            enigma_in_stay_start()
        game.drawText("If the word enigma reminds you of something",100,160,f9)
        game.drawText("maybe back in ww2 then you are right!",100,190,f9)
        game.drawText("The enigma machine was used to encrypt or",100,220,f9)
        game.drawText("scramble nazi morse code messages and is",100,250,f9)
        game.drawText("really hard to crack and this is a simile",100,280,f9)
        game.drawText("to how the games are as hard to win when",100,310,f9)
        game.drawText("compared to breaking enigma code. So the",100,340,f9)
        game.drawText("challenge is do you have what it takes?",100,370,f9)
        game.drawText("<<-- <Tip>! Enigma Machine!",320,458,f9)
        game.drawText("<Tip>! Press H For Help Menu!",320,428,f9)
        game.update(60)
    game.quit()
#offical game rule to help users add there games to the enigma arcade!
def GAME_Rule():
    game = Game(750,600,"Enigma_Arcade_How_To_Add_A_Game!")
    try:
        start = Image("Enigma_Arcade_Files\\arcades_outs.png",game)
    except pygame.error:
        start = Image("Enigma_Arcade_Files//arcades_outs.png",game)        
    start.resizeTo(game.width,game.height)
    try:
        bk = Image("Enigma_Arcade_Files\\Enigma_logo.png",game)
    except pygame.error:
        bk = Image("Enigma_Arcade_Files//Enigma_logo.png",game)        
    bk.moveTo(375,100)
    if os_check <=0:
        f7 = Font(blue,40,black,"Comic Sans MS")
    if os_check >0:
        f7 = Font(blue,58,black,"Comic Sans MS")
    if os_check <=0:
        f9 = Font(blue,25,black,"Comic Sans MS")
    if os_check >0:
        f9 = Font(blue,30,black,"Comic Sans MS")
    if os_check <=0:
        f8 = Font(blue,30,black,"Comic Sans MS")
    if os_check >0:
        f8 = Font(blue,40,black,"Comic Sans MS")            
    while not game.over:
        game.processInput()
        start.draw()
        bk.draw()
        if keys.Pressed[K_0]:
            if os_check <=0:
                from tkinter import messagebox
                msg = messagebox.showinfo("Enigma Arcade!", "Remember the game rule and see the structure to understand how to add your game to the Enigma Aracde, or watch the tutorial video :D! ")
                if msg == "ok":
                    game.over = True
                    enigma_screen_test()
            if os_check >0:
                print("")
                print("*************************************************************************************************************************************")
                print("Remember the game rule and see the structure to understand how to add your game to the Enigma Aracde, or watch the tutorial video :D!")
                print("*************************************************************************************************************************************")
                time.sleep(1)
                game.over = True
                enigma_screen_test()
        if keys.Pressed[K_ESCAPE]:
            game.over = True
            game.quit()
            quit()
        if keys.Pressed[K_m]:
            game.over = True
            enigma_in_stay_start()
        if keys.Pressed[K_h]:
            game.over = True
            enigma_in_stay_help()
        if keys.Pressed[K_LEFT]:
            game.over = True
            enigma_in_stay_help()
        if keys.Pressed[K_RIGHT]:
            game.over = True
            if os_check <=0:
                from tkinter import messagebox
                msg = messagebox.showinfo("Enigma Arcade!", "Remember the game rule and see the structure to understand how to add your game to the Enigma Aracde, or watch the tutorial video :D! ")
                if msg == "ok":
                    game.over = True
                    enigma_screen_test()
            if os_check >0:
                print("")
                print("*************************************************************************************************************************************")
                print("Remember the game rule and see the structure to understand how to add your game to the Enigma Aracde, or watch the tutorial video :D!")
                print("*************************************************************************************************************************************")
                time.sleep(1)
                game.over = True
                enigma_screen_test()           
        game.drawText("How To Upload A Game!",150,160,f7)
        game.drawText("Offical GAME Rule",200,200,f7)
        game.drawText("How To Upload A Game!",150,160,f7)
        game.drawText("Game Title",100,250,f9)
        game.drawText("Add all game resources in a folder!",100,280,f9)
        game.drawText("Make a nice logo!",100,305,f9)
        game.drawText("Expression/slogan or company name or even both",100,335,f9)
        game.drawText("Press 0 To See The Structure!",160,420,f8)
        game.drawText("Or Watch The Tutorial Video!",160,450,f8)
        game.update(60)
    game.quit()
#Credit menu! You can delete this its a troll!
def LL_credit_menu():
    game = Game(750,600,"Enigma_Arcade_Creator_Menu!")
    start = Image("Enigma_Arcade_Files\\arcades_outs.png",game)
    start.resizeTo(game.width,game.height)
    bk = Image("Enigma_Arcade_Files\\Enigma_logo.png",game)
    bk.moveTo(375,100)
    f7 = Font(blue,40,black,"Comic Sans MS")
    f9 = Font(blue,25,black,"Comic Sans MS")
    f8 = Font(blue,24,black,"Comic Sans MS")
    while not game.over:
        game.processInput()
        start.draw()
        bk.draw()
        game.drawText("LL Productions Group!",180,184,f7)
        game.drawText("Wow Congrats You Found The Creator Menu!",132,230,f9)
        game.drawText("Game Director: William Ho, Creator of the game",100,280,f9)
        game.drawText("Slap Or Stack and the developer of the Enigma Arcade!",58,300,f8)
        game.drawText("Creator of pong game: Michael Leung",170,350,f9)
        game.drawText("Creator of pac man: Anthony Zheng",170,400,f9)
        game.drawText("(*Played a lot of games instead of coding!*)",140,420,f9)
        game.drawText("Creator of Life: David Lai",170,460,f9)
        game.drawText("(*Goes on phone of the time and talks a lot!*)",123,480,f9)
        if keys.Pressed[K_m]:
            game.over = True
            enigma_in_stay_start()
        if keys.Pressed[K_h]:
            game.over = True
            enigma_in_stay_help()
        if keys.Pressed[K_0]:
            game.over = True
            enigma_screen_test()
        if keys.Pressed[K_ESCAPE]:
            game.over = True
            game.quit()
            quit()
        if keys.Pressed[K_1]:
            game.over = True
            enigma_screen_1()
        if keys.Pressed[K_p]:
            from tkinter import messagebox
            msg = messagebox.askquestion("Enigma Arcade!", "Are you sure you want to continue?")
            if msg == "no":
                print("ok")
            if msg == "yes":
                webbrowser.open('secret.py')
                from tkinter import messagebox
                msg = messagebox.showinfo("Enigma Arcade!", "Congrats! You played yourself! :P")
                game.over = True
                game.quit()
        game.update(60)
    game.quit()
#Quick select for a section!
def section_finder():
    game = Game(750,600,"Enigma_Arcade_How_To_Add_A_Game!")
    try:
        start = Image("Enigma_Arcade_Files\\arcades_outs.png",game)
    except pygame.error:
        start = Image("Enigma_Arcade_Files//arcades_outs.png",game)        
    start.resizeTo(game.width,game.height)
    try:
        bk = Image("Enigma_Arcade_Files\\Enigma_logo.png",game)
    except pygame.error:
        bk = Image("Enigma_Arcade_Files//Enigma_logo.png",game)        
    bk.moveTo(375,100)
    #this is the top text or logo!
    try:
        main_logo = Image("Enigma_Arcade_Files\\Enigma_Section_Logos\\section_info_logo.png",game)
    except pygame.error:
        main_logo = Image("Enigma_Arcade_Files//Enigma_Section_Logos//section_info_logo.png",game)
    main_logo.resizeBy(-40)
    main_logo.moveTo(375,100)
    try:
        s1 = Image("Enigma_Arcade_Files\\Enigma_Section_Logos\\section_one_logo.png",game)
    except pygame.error:
        s1 = Image("Enigma_Arcade_Files//Enigma_Section_Logos//section_one_logo.png",game)
    s1.resizeBy(-40)
    s1.moveTo(200,200)
    try:
        s2 = Image("Enigma_Arcade_Files\\Enigma_Section_Logos\\section_two_logo.png",game)
    except pygame.error:
        s2 = Image("Enigma_Arcade_Files//Enigma_Section_Logos//section_two_logo.png",game)
    s2.resizeBy(-40)
    s2.moveTo(200,250)
    if os_check <=0:
        f7 = Font(blue,40,black,"Comic Sans MS")
    if os_check >0:
        f7 = Font(blue,58,black,"Comic Sans MS")
    while not game.over:
        game.processInput()
        bk.draw()
        start.draw()
        main_logo.draw()
        s1.draw()
        s2.draw()
        if mouse.collidedWith(s1) and mouse.LeftClick:
            game.over = True
            enigma_screen_1()
        if mouse.collidedWith(s2) and mouse.LeftClick:
            game.over = True
            enigma_screen_2()
        if keys.Pressed[K_m]:
            game.over = True
            enigma_in_stay_start()
        if keys.Pressed[K_h]:
            game.over = True
            enigma_in_stay_help()
        if keys.Pressed[K_0]:
            game.over = True
            enigma_screen_test()
        if keys.Pressed[K_ESCAPE]:
            game.over = True
            game.quit()
            quit()
        if keys.Pressed[K_RIGHT]:
            if os_check <=0:
                from tkinter import messagebox
                msg = messagebox.showinfo("Enigma Arcade!", "There is not a another screen! So i will bring you to the main menu?")
            if os_check >0:
                print("")
                print("********************************************************************")
                print("There is not a another screen! So i will bring you to the main menu?")
                print("********************************************************************")
            game.over = True
            enigma_in_stay_start()
        game.drawText("Press {>} to go to the next slide!",80,462,f7)
        if keys.Pressed[K_LEFT]:
           if os_check <=0:
                from tkinter import messagebox
                msg = messagebox.showinfo("Enigma Arcade!", "There is not a another screen! So i will bring you to the section one?")
                if os_check >0:
                    print("")
                    print("********************************************************************")
                    print("There is not a another screen! So i will bring you to the section one?")
                    print("********************************************************************")
                game.over = True
                enigma_screen_1()
 
        game.update(60)
    game.quit()
enigma_start()
