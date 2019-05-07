
#***************************************************************
#CREATORS NOTE!
#Created by William Ho
#objects that are labled with quotes won't be relabled again!
#Main Goal Of The Game:
#Using the ball on the buttom that you control stack it on the
#ball falling downwards failing to do so will result in losing the game
#You can also fail the game by colliding with the side of the game/walls
#so becareful!

#Game Controls!
# [Q] or [left Arrow] this moves the block to the left!
# [E] or [Right Arrow] this moves the block to the right!
# [M] goes to the main menu!
# [H] goes to the help menu
# [R] reloads the main game (*only in losing menu, winning menu*)
# [C] goes to the credit menu (*only in the hgelp menu*)
# [T] goes to the tutorial menu (*only in the help menu*)

#SPECIAL KEYS! Only in the main game!
#This is maded so ragers cant hit a key and end the game by accident! :D
#We got you covered! :D!
# Press [CONTROL AND -Key Below To Activate-]
# [Control] + [P] pause the game
# [Control] + [R] reloads the main game
# [Control] + [T] goes to the tutorial menu
# [Control] + [H] goes to the help menu
#Thank You All!
#© 2019 Enigma Arcade.inc
#© 2019 LL Productions 
#© 2019 Slap Or Stack
#All rights not reserved but please do not recreate and share unless you have
#the creators approval!
#*****************************************************************************
#This checks the user os to let the user use the right verison!
global os_check
os_check = 0
global deaths
deaths = 0
global wins
wins = 0
from tkinter import messagebox
msg = messagebox.showinfo("Slap Or Stack!", "Welcome Ladies And Gentlemen to the Slap Or Stack!")
msg = messagebox.showinfo("Slap Or Stack!", "Before you begin your journey! We must know what operating system (os) do you have! (*Please be accurate as some features are not cross plateform and may crash your game! If used on a different OS!*)")
msg = messagebox.askquestion("Slap Or Stack!", "Are you currently using any form of windows os? Examples >> (1.0,2.0,3.0,95,98,ME,2000,XP,VISTA,7,8,8.1,10)")
if msg == "yes":
    msg = messagebox.showinfo("Slap Or Stack!", "Thats awesome! Every module should work for you! And dont forget to have fun :D!")
if msg == "no":
    msg = messagebox.askquestion("Slap Or Stack!", "Ok, thats fine! Are you using any form of mac os? Examples >>*(Ex from os starting from 2011*)(OS X Mountain Lion – 10.8, OS X Mavericks – 10.9, OS X Yosemite – 10.10, OS X El Capitan – 10.11, MacOS Sierra – 10.12, macOS High Sierra – 10.13, Mojave – 10.14)")
    if msg == "yes":
        os_check = 5
        msg = messagebox.showinfo("Slap Or Stack!", "Thats awesome! Most module should work for you! But the pop up info will be in the python shell and you will have to manually open a game file and run it. But anyways don't forget to have fun :D!")
    if msg == "no":
        msg = messagebox.askquestion("Slap Or Stack!", "Are you running any form of linix os? (*Too many to name*)")
        if msg == "yes":
            print("nice")
            msg = messagebox.askquestion("Slap Or Stack!", "Your current os might or might not work?")
        if msg == "no":
            msg = messagebox.askquestion("Slap Or Stack!", "Hum?... Your current os might or might not work with enigma aracde and other games associated with enigma arcade")
from gamelibwillh2 import*
import time
import webbrowser
import random
vid_true = 0
#The actual main game!
def mainGame():
    game = Game(800,600,"Slap Or Stack!")
    try:
        bk1 = Image("Slap_Or_Stack_Files\\Balls\\black.png",game)
    except pygame.error:        
        bk1 = Image("Slap_Or_Stack_Files//Balls//black.png",game)        
    bk1.resizeTo(game.width,game.height)
    game.setBackground(bk1)
    #main player
    try:
        ball = Image("Slap_Or_Stack_Files\\Balls\\Ball.jpg",game)
    except pygame.error: 
        ball = Image("Slap_Or_Stack_Files//Balls//Ball.jpg",game)
    ball.resizeTo(90,90)
    ball.moveTo(400,555)
    #collided with block or cwb
    try:
        cwb = Image("Slap_Or_Stack_Files\\Balls\\Ball.jpg",game)
    except pygame.error:
        cwb = Image("Slap_Or_Stack_Files//Balls//Ball.jpg",game)        
    cwb.resizeTo(90,90)
    cwb.moveTo(400,555)
    #collided with block_inside or cwb_inside
    try:
        cwb = Image("Slap_Or_Stack_Files\\Balls\\Ball.jpg",game)
    except pygame.error:     
        cwb = Image("Slap_Or_Stack_Files//Balls//Ball.jpg",game)        
    cwb.resizeTo(90,90)
    cwb.moveTo(400,555)
    #Stacking!
    try:
        balls = Image("Slap_Or_Stack_Files\\Balls\\Ball.jpg",game)
    except pygame.error: 
        balls = Image("Slap_Or_Stack_Files//Balls//Ball.jpg",game)
    balls.resizeTo(90,90)
    x = randint(90,620)
    balls.moveTo(x,45)
    #s is the speed!
    s = 3
    try:
        pong = Sound("Slap_Or_Stack_Files\\Songs\\Pong!.wav",3)
    except pygame.error:
        pong = Sound("Slap_Or_Stack_Files//Songs//Pong!.wav",3)       
    #borders, NO DONALD TRUMP!
    try:
        border_buttom = Image("Slap_Or_Stack_Files\\Balls\\Ball.jpg",game)
    except pygame.error: 
        border_buttom = Image("Slap_Or_Stack_Files//Balls//Ball.jpg",game)
    border_buttom.resizeTo(1000,1)
    border_buttom.moveTo(370,800)
    try:
        border_top = Image("Slap_Or_Stack_Files\\Balls\\Ball.jpg",game)
    except pygame.error: 
        border_top = Image("Slap_Or_Stack_Files//Balls//Ball.jpg",game)
    border_top.resizeTo(1000,1)
    border_top.moveTo(370,-200)
    try:
        border_left = Image("Slap_Or_Stack_Files\\Balls\\Ball.jpg",game)
    except pygame.error: 
        border_left = Image("Slap_Or_Stack_Files//Balls//Ball.jpg",game)
    border_left.resizeTo(1,1000)
    border_left.moveTo(-220,400)
    try:
        border_right = Image("Slap_Or_Stack_Files\\Balls\\Ball.jpg",game)
    except pygame.error: 
        border_right = Image("Slap_Or_Stack_Files//Balls//Ball.jpg",game)
    border_right.resizeTo(1,1000)
    
    border_right.moveTo(1010,400)
    game.stopMusic()
    try:
        game.setMusic("Slap_Or_Stack_Files\\Songs\\Beat_it.mp3")
    except pygame.error: 
        game.setMusic("Slap_Or_Stack_Files//Songs//Beat_it.mp3")
    game.playMusic()
    while not game.over:
        balls.y +=s
        game.processInput()
        bk1.move()
        border_buttom.move()
        if keys.Pressed[K_e]:
            ball.x +=10
            cwb.x +=10
        if keys.Pressed[K_q]:
            ball.x -=10
            cwb.x -=10
        if keys.Pressed[K_RIGHT]:
            ball.x +=10
            cwb.x +=10
        if keys.Pressed[K_LEFT]:
            ball.x -=10
            cwb.x -=10
        #Have to press control and what ever key to page switch!
        #This is to prevent misclick!
        def mainSwitch():
            if keys.Pressed[K_h]:
                game.over = True
                help_menu()
            if keys.Pressed[K_m]:
                game.over = True
                newstart()
            if keys.Pressed[K_t]:
                game.over = True
                Tutorial_Main()
            if keys.Pressed[K_r]:
                mainGame()
            #CHEAT CHEAT BELOW! LOL!
            if keys.Pressed[K_w]:
                balls.x = cwb.x
            if keys.Pressed[K_p]:
                game.drawText("Game is now paused!",0,0)
                game.drawText("Just press P again to unpause!",0,15)
                game.wait(K_p)
            if keys.Pressed[K_o]:
                game.stopMusic()
                game.drawText("Game is now muted and paused!",0,0)
                game.drawText("Just press o again to unmute and unpause!",0,15)
                game.wait(K_o)
                try:
                    game.setMusic("Slap_Or_Stack_Files\\Songs\\Beat_it.mp3")
                except pygame.error: 
                    game.setMusic("Slap_Or_Stack_Files//Songs//Beat_it.mp3")
                game.playMusic()
        if keys.Pressed[K_LCTRL]:
            mainSwitch()
        #Active collided with objects!
        if balls.collidedWith(cwb):
            pong.play()
            balls.moveTo(ball.x,ball.y)
            ball.height +=90
            x = randint(90,620)
            balls.moveTo(x,45)
            s +=1
            ball.height +=90
            cwb.y -=90
            game.score +=1
        if balls.collidedWith(border_buttom):
            balls.moveTo(ball.x,ball.y)
            x = randint(90,620)
            balls.moveTo(x,45)
            s +=5
            game.over = True
            if os_check <=0:
                from tkinter import messagebox
                global wins
                global deaths
                deaths+=1
                msg = messagebox.showinfo("Enigma Arcade!", "Looks like you Died: "+str(deaths)+" and Won: "+str(wins) +" this round!")
            if os_check >1:
                deaths+=1
                print("")
                print("************************************************************************")
                print("Looks like you Died: "+str(deaths)+" and Won: "+str(wins) +" this round!")
                print("************************************************************************")
            loses()
        if cwb.collidedWith(border_top):
            if os_check <=0:
                from tkinter import messagebox
                wins +=1
                msg = messagebox.showinfo("Enigma Arcade!", "Looks like you Died: "+str(deaths)+" and Won: "+str(wins)+" this round!")
            if os_check >1:
                wins +=1
                print("")
                print("************************************************************************")
                print("Looks like you Died: "+str(deaths)+" and Won: "+str(wins) +" this round!")
                print("************************************************************************")
            game.drawText("YOU WON!!",0,0)
            game.over = True
            winner()
        if cwb.collidedWith(border_left):
            game.drawText("touched left!",0,0)
            if os_check <=0:
                from tkinter import messagebox
                deaths+=1
                msg = messagebox.showinfo("Enigma Arcade!", "Looks like you Died: "+str(deaths)+" and Won: "+str(wins)+" this round!")
            if os_check >1:
                deaths+=1
                print("")
                print("************************************************************************")
                print("Looks like you Died: "+str(deaths)+" and Won: "+str(wins) +" this round!")
                print("************************************************************************")
            loses()
            game.over = True
            loses()
        if cwb.collidedWith(border_right):
            if os_check <=0:
                from tkinter import messagebox
                deaths+=1
                msg = messagebox.showinfo("Enigma Arcade!", "Looks like you Died: "+str(deaths)+" and Won: "+str(wins)+" this round!")
            if os_check >1:
                deaths+=1
                print("")
                print("************************************************************************")
                print("Looks like you Died: "+str(deaths)+" and Won: "+str(wins) +" this round!")
                print("************************************************************************")
            loses()
            game.over = True
            loses()
        ball.move()
        #Cool and all but learn to stop background images
        #after being drawn so it doesnt slow the game down!
        if game.score >=1:
            '''
            pinks = Image("pink.jpg",game)
            pinks.resizeTo(game.width,game.height)
            game.setBackground(pinks)
            pinks.draw()
            '''
            try:
                reds = Image("Slap_Or_Stack_Files\\Balls\\red.jpg",game)
            except pygame.error: 
                reds = Image("Slap_Or_Stack_Files//Balls//red.jpg",game)
            reds.resizeTo(ball.width,ball.height)
            reds.moveTo(ball.x,ball.y)
        if game.score >=2:
            '''
            reds = Image("red.jpg",game)
            reds.resizeTo(game.width,game.height)
            game.setBackground(reds)
            reds.move()
            '''
            try:
                blues = Image("Slap_Or_Stack_Files\\Balls\\blue.png",game)
            except pygame.error: 
                blues = Image("Slap_Or_Stack_Files//Balls//blue.png",game)               
            blues.resizeTo(ball.width,ball.height)
            blues.moveTo(ball.x,ball.y)
        if game.score >=3:
            '''
            greens = Image("green.png",game)
            greens.resizeTo(game.width,game.height)
            game.setBackground(greens)
            greens.draw()
            '''
            try:
                purples = Image("Slap_Or_Stack_Files\\Balls\\purples.png",game)
            except pygame.error: 
                purples = Image("Slap_Or_Stack_Files//Balls//purples.png",game)            
            purples.resizeTo(ball.width,ball.height)
            purples.moveTo(ball.x,ball.y)
        if game.score >=4:
            '''
            purples = Image("purples.png",game)
            purples.resizeTo(game.width,game.height)
            game.setBackground(purples)
            purples.draw()
            '''
            try:
                greens = Image("Slap_Or_Stack_Files\\Balls\\green.png",game)
            except pygame.error: 
                greens = Image("Slap_Or_Stack_Files//Balls//green.png",game)            
            greens.resizeTo(ball.width,ball.height)
            greens.moveTo(ball.x,ball.y)
        if game.score >=5:
            #Not the singer! :D
            '''
            bk1 = Image("black.png",game)
            bk1.resizeTo(game.width,game.height)
            bk1.draw()
            '''
            try:
                pinks = Image("Slap_Or_Stack_Files\\Balls\\pink.jpg",game)
            except pygame.error: 
                pinks = Image("Slap_Or_Stack_Files//Balls//pink.jpg",game)
            pinks.resizeTo(ball.width,ball.height)
            pinks.moveTo(ball.x,ball.y)
        balls.move()
        cwb.move()
        border_left.move()
        border_right.move()
        game.update(60)
    game.quit()
#losing menu :( but dont give up :D!
def loses():
    game = Game(800,600,"Slap Or Stack!_Try_Again_:O")
    try:
        bk1 = Image("Slap_Or_Stack_Files\\Background_Buttons\\JDI_7.jpg",game)
    except pygame.error: 
        bk1 = Image("Slap_Or_Stack_Files//Background_Buttons//JDI_7.jpg",game)
    bk1.resizeTo(game.width,game.height)
    #Button press to replay :D
    try:
        click_play = Image("Slap_Or_Stack_Files\\Background_Buttons\\CLICKME_v.2.png",game)
    except pygame.error: 
        click_play = Image("Slap_Or_Stack_Files//Background_Buttons//CLICKME_v.2.png",game)
    click_play.resizeBy(-40)
    click_play.moveTo(150,500)
    #Sad Emoji, PLEASE DON"T LEAVE MY GAME :(
    try:
        leave = Image("Slap_Or_Stack_Files\\Background_Buttons\\sads!.png",game)
    except pygame.error: 
        leave = Image("Slap_Or_Stack_Files//Background_Buttons//sads!.png",game)
    leave.resizeBy(-74)
    leave.moveTo(600,500)
    try:
        lose_audios = Sound("Slap_Or_Stack_Files\\Songs\\Fail.wav",1)
    except pygame.error: 
        lose_audios = Sound("Slap_Or_Stack_Files//Songs//Fail.wav",1)
    #I made custoum RGB values and assigned them to variables :D
    #ALL MY COLORS!
    grey = (192,192,192)
    creamblue = (204,255,255)
    lightgreen = (153,255,51)
    reds = (255,0,0)
    lightred = (204,0,0)
    lightgreen = (153,255,51)
    steelblue = (70,130,180)
    #ALL MY FONTS!
    if os_check <=0:
        f = Font(black,20,lightred,"Comic Sans MS")
    if os_check >0:
        f = Font(black,28,lightred,"Comic Sans MS")
    f1 = Font(grey,20,creamblue,"Comic Sans MS")
    f2 = Font(black,34,lightgreen,"Comic Sans MS")
    if os_check <=0:
        f3 = Font(black,34,reds,"Comic Sans MS")
    if os_check >0:
        f3 = Font(black,45,reds,"Comic Sans MS")
    f4 = Font(steelblue,25,steelblue,"Comic Sans MS")
    if os_check <=0:
        f5 = Font(black,20,cyan,"Comic Sans MS")
    if os_check >0:
        f5 = Font(black,28,cyan,"Comic Sans MS")
    lose_audios.play()
    game.stopMusic()
    try:
        game.setMusic("Slap_Or_Stack_Files\\Songs\\Stayin'_Alive.mp3")
    except pygame.error: 
        game.setMusic("Slap_Or_Stack_Files//Songs//Stayin'_Alive.mp3")        
        game.playMusic()
    while not game.over:
        bk1.move()
        click_play.draw()
        leave.draw()
        game.processInput()
        game.drawText("(Before you can succeed you most fail!)",90,10,f3)
        #LL productions hsould only be in the credit menu :D!
        game.drawText("Click Me Or Press R",50,380,f5)
        game.drawText("To Restart The Game!",38,400,f5)
        game.drawText("Click Me Or Press",510,380,f)
        game.drawText("ESC To Leave The Game :(",480,400,f)
        if mouse.collidedWith(leave) and mouse.LeftClick:
            game.quit()
            game.over = True
            quit()
        if keys.Pressed[K_ESCAPE]:
            game.quit()
            game.over = True
            quit()
        if mouse.collidedWith(click_play) and mouse.LeftClick:
            mainGame()
        if keys.Pressed[K_SPACE]:
            game.over = True
            mainGame()
        if keys.Pressed[K_r]:
            mainGame()
        if keys.Pressed[K_h]:
            game.over = True
            help_menu()
        if keys.Pressed[K_m]:
            game.over = True
            newstart()
        if keys.Pressed[K_t]:
            game.over = True
            Tutorial_Main()
        game.update(60)
    game.quit()
#The starting menu!
def newstart():
    global os_check
    game = Game(640,640,"Slap Or Stack!_Main_Menu!")
    try:
        bk0 = Animation("Slap_Or_Stack_Files\\Background_Buttons\\flipstart.png",52,game,6400/10,3840/6)
    except pygame.error: 
        bk0 = Animation("Slap_Or_Stack_Files//Background_Buttons//flipstart.png",52,game,6400/10,3840/6)
    bk0.resizeBy(0)
    blueviolet = (138,43,226)
    if os_check<=0:
        f5 = Font(blueviolet,40,black,"Comic Sans MS")
    if os_check>0:
        f5 = Font(blueviolet,58,black,"Comic Sans MS")
    if os_check<=0:
        f4 = Font(blue,40,black,"Comic Sans MS")
    if os_check>0:
        f4 = Font(blue,58,black,"Comic Sans MS")
    creamblue = (204,255,255)
    if os_check<=0:
        f3 = Font(creamblue,40,cyan,"Comic Sans MS")
    if os_check>0:
        f3 = Font(creamblue,58,cyan,"Comic Sans MS")
    #MUSIC!
    game.stopMusic()
    try:
        game.setMusic("Slap_Or_Stack_Files\\Songs\\Heart_of_Gold.mp3")
    except pygame.error: 
        game.setMusic("Slap_Or_Stack_Files//Songs//Heart_of_Gold.mp3")
    game.playMusic()
    while not game.over:
        game.processInput()
        bk0.move()
        #RAINBOW!!!!
        '''
        color1 = randint(0,255)
        color2 = randint(0,255)
        color3 = randint(0,255)
        colors = (color1,color2,color3)
        color4 = randint(0,255)
        color5 = randint(0,255)
        color6 = randint(0,255)
        colorss = (color4,color5,color6)
        f2 = Font(colors,40,colors,"Comic Sans MS")
        f1 = Font(colorss,40,colorss,"Comic Sans MS")
        '''
        game.drawText("Slap Or Stack!",200,10,f4)
        game.drawText("Press H For Help Menu!",105,500,f5)
        game.drawText("Press SpaceBar To Play!",100,550,f5)
        if keys.Pressed[K_SPACE]:
            game.over = True
            mainGame()
        if keys.Pressed[K_h]:
            game.over = True
            help_menu()
        if keys.Pressed[K_w]:
            os_check = 0
            print("")
            print("*********&***********************************")
            print("Sucessfully converted to the windows verison!")
            print("*********************************************")
            print("*********************")
            print("Sucessfully reloaded!")
            print("*********************")
            print("")
            newstart()
        if keys.Pressed[K_m]:
            os_check = 5
            print("")
            print("*********&*********************************")
            print("Sucessfully converted to the mac verison!")
            print("*******************************************")
            print("*********************")
            print("Sucessfully reloaded!")
            print("*********************")
            print("")
            newstart()
        #******************
        #DELETE ME AFTER THIS IS FOR TESTING!
        '''
        if keys.Pressed[K_p]:
            game.over = True
            Tutorial_4()
        if keys.Pressed[K_y]:
            game.over = True
            credit_menu()
        if keys.Pressed[K_o]:
            game.over = True
            winner()
        '''
        game.update(25)
    game.quit()
#Help menu! For those who are new!
def help_menu():
    game = Game(800,600,"Slap Or Stack!_Help_Menu!")
    try:
        bk0 = Animation("Slap_Or_Stack_Files\\Background_Buttons\\mountain.png",21,game,7110/10,4000/10)
    except pygame.error: 
        bk0 = Animation("Slap_Or_Stack_Files//Background_Buttons//mountain.png",21,game,7110/10,4000/10)
    bk0.resizeTo(game.width,game.height)
    springgreen = (0,255,127)
    green = (0,128,0)
    if os_check <=0:
        f7 = Font(blue,40,black,"Comic Sans MS")
    if os_check >0:
        f7 = Font(blue,58,black,"Comic Sans MS")
    creamblue = (204,255,255)
    if os_check <=0:
        f3 = Font(creamblue,40,cyan,"Comic Sans MS")
    if os_check >0:
        f3 = Font(creamblue,58,cyan,"Comic Sans MS")
    f2 = Font(cyan,40,cyan,"Comic Sans MS")
    if os_check <=0:
        f8 = Font(springgreen,30,green,"Comic Sans MS")
    if os_check >0:
        f8 = Font(springgreen,40,green,"Comic Sans MS")    
    game.stopMusic()
    try:
        game.setMusic("Slap_Or_Stack_Files\\Songs\\Take_Me_Home_Country_Roads.mp3")      
    except pygame.error: 
        game.setMusic("Slap_Or_Stack_Files//Songs//Take_Me_Home_Country_Roads.mp3")
    game.playMusic()
    while not game.over:
        game.processInput()
        bk0.move()
        #RAINBOW COLORS!
        '''
        color1 = randint(0,255)
        color2 = randint(0,255)
        color3 = randint(0,255)
        colors = (color1,color2,color3)
        f1 = Font(colors,40,colors,"Comic Sans MS")
        color4 = randint(0,255)
        color5 = randint(0,255)
        color6 = randint(0,255)
        colorss = (color4,color5,color6)
        f2 = Font(colorss,40,colorss,"Comic Sans MS")
        color7 = randint(0,255)
        color8 = randint(0,255)
        color9 = randint(0,255)
        colorsss = (color7,color8,color9)
        f4 = Font(colorsss,40,colorsss,"Comic Sans MS")
        f5 = Font(red,40,blue,"Comic Sans MS")
        '''
        game.drawText("The idea of Slap Or Stack comes from the old game pong",5,100,f8)
        game.drawText("and stacker. Which is why the games UI and Music",40,130,f8)
        game.drawText("is somewhat related around the time of 1970s!",80,160,f8)
        game.drawText("Press C For Credit Menu!",160,350,f3)
        game.drawText("Press T For Tutorial!",195,400,f3)
        game.drawText("Press SpaceBar To Play!",171,450,f3)
        game.drawText("Press M For Main Menu!",170,500,f3)
        game.drawText("Slap Or Stack!",250,40,f7)
        if keys.Pressed[K_SPACE]:
            game.over = True
            mainGame()
        if keys.Pressed[K_m]:
            game.over = True
            newstart()
        if keys.Pressed[K_t]:
            game.over = True
            Tutorial_Main()
        if keys.Pressed[K_c]:
            game.over = True
            credit_menu()
        game.update(60)
    game.quit()
#tutorial start screen!
def Tutorial_Main():
    game = Game(640,640,"Slap Or Stack!_Tutorial_Main!")
    try:
        bk1 = Animation("Slap_Or_Stack_Files\\Background_Buttons\\flipstart.png",52,game,6400/10,3840/6)
    except pygame.error: 
        bk1 = Animation("Slap_Or_Stack_Files//Background_Buttons//flipstart.png",52,game,6400/10,3840/6)
    bk1.resizeBy(0)
    if os_check <=0:
        f7 = Font(blue,40,black,"Comic Sans MS")
    if os_check >0:
        f7 = Font(blue,58,black,"Comic Sans MS")
    blueviolet = (138,43,226)
    if os_check <=0:
        f6 = Font(blueviolet,40,black,"Comic Sans MS")
    if os_check >0:
        f6 = Font(blueviolet,58,black,"Comic Sans MS")
    f4 = Font(black,40,black,"Comic Sans MS")
    f5 = Font(white,40,white,"Comic Sans MS")
    creamblue = (204,255,255)
    f3 = Font(creamblue,40,cyan,"Comic Sans MS")
    game.stopMusic()
    try:
        game.setMusic("Slap_Or_Stack_Files\\Songs\\YMCA.mp3")
    except pygame.error: 
        game.setMusic("Slap_Or_Stack_Files//Songs//YMCA.mp3")
    game.playMusic()
    while not game.over:
        game.processInput()
        bk1.move()
        '''
        color1 = randint(0,255)
        color2 = randint(0,255)
        color3 = randint(0,255)
        colors = (color1,color2,color3)
        f1 = Font(colors,40,colors,"Comic Sans MS")
        color4 = randint(0,255)
        color5 = randint(0,255)
        color6 = randint(0,255)
        colorss = (color4,color5,color6)
        f2 = Font(colorss,40,colorss,"Comic Sans MS")
        color7 = randint(0,255)
        color8 = randint(0,255)
        color9 = randint(0,255)
        colorsss = (color7,color8,color9)
        #game.clearBackground(colorsss)
        '''
        game.drawText("Slap Or Stack!",200,10,f7)
        game.drawText("Press SpaceBar To Begin!",75,550,f6)
        game.drawText("Welcome To The Tutorial!",90,70,f6)
        if keys.Pressed[K_m]:
            game.over = True
            newstart()
        if keys.Pressed[K_SPACE]:
            game.over = True
            Tutorial_1()
        if keys.Pressed[K_h]:
            game.over = True
            help_menu()
        if keys.Pressed[K_m]:
            game.over = True
            newstart()
        game.update(25)
    game.quit()
#if the q key is pressed go to the next screen!
def Tutorial_1():
    game = Game(800,600,"Slap Or Stack!_Tutorial_Screen_1!")
    creamblue = (204,255,255)
    if os_check <=0:
        f3 = Font(creamblue,40,cyan,"Comic Sans MS")
    if os_check >0:
        f3 = Font(creamblue,58,cyan,"Comic Sans MS")
    try:
        bk1 = Image("Slap_Or_Stack_Files\\Balls\\black.png",game)
    except pygame.error: 
        bk1 = Image("Slap_Or_Stack_Files//Balls//black.png",game)
    bk1.resizeTo(game.width,game.height)
    try:
        ball = Image("Slap_Or_Stack_Files\\Balls\\Ball.jpg",game)
    except pygame.error: 
        ball = Image("Slap_Or_Stack_Files//Balls//Ball.jpg",game)
    ball.resizeTo(90,90)
    ball.moveTo(400,555)
    while not game.over:
        game.processInput()
        bk1.draw()
        game.drawText("The Block Below Is You!",171,40,f3)
        game.drawText("Press Q or Left Arrow to move Left!",45,75,f3)
        if keys.Pressed[K_q]:
            ball.x -=10
        if keys.Pressed[K_LEFT]:
            ball.x -=10
        if ball.x < 300:
            Tutorial_2()
        if keys.Pressed[K_h]:
            game.over = True
            help_menu()
        if keys.Pressed[K_m]:
            game.over = True
            newstart()
        if keys.Pressed[K_t]:
            game.over = True
            Tutorial_Main()
        ball.draw()
        game.update(60)
    game.quit()
#if the e key is pressed go to the next screen!
def Tutorial_2():
    game = Game(800,600,"Slap Or Stack!_Tutorial_Screen_2!")
    creamblue = (204,255,255)
    if os_check <=0:
        f3 = Font(creamblue,40,cyan,"Comic Sans MS")
    if os_check >0:
        f3 = Font(creamblue,58,cyan,"Comic Sans MS")
    try:
        bk1 = Image("Slap_Or_Stack_Files\\Balls\\black.png",game)
    except pygame.error: 
        bk1 = Image("Slap_Or_Stack_Files//Balls//black.png",game)
    bk1.resizeTo(game.width,game.height)
    try:
        ball = Image("Slap_Or_Stack_Files\\Balls\\Ball.jpg",game)
    except pygame.error: 
        ball = Image("Slap_Or_Stack_Files//Balls//Ball.jpg",game)
    ball.resizeTo(90,90)
    ball.moveTo(300,555)
    while not game.over:
        game.processInput()
        bk1.draw()
        game.drawText("The Block Below Is You!",171,40,f3)
        game.drawText("Press E or Right Arrow to move Right",45,75,f3)
        if keys.Pressed[K_e]:
            ball.x +=10
        if keys.Pressed[K_RIGHT]:
            ball.x +=10
        if ball.x > 400:
            Tutorial_3()
        if keys.Pressed[K_h]:
            game.over = True
            help_menu()
        if keys.Pressed[K_m]:
            game.over = True
            newstart()
        if keys.Pressed[K_t]:
            game.over = True
            Tutorial_Main()
        ball.draw()
        game.update(60)
    game.quit()
#if the player collides with the test blocl go to the next screen!
def Tutorial_3():
    game = Game(800,600,"Slap Or Stack!_Tutorial_Screen_3!")
    creamblue = (204,255,255)
    if os_check <=0:
        f3 = Font(creamblue,40,cyan,"Comic Sans MS")
    if os_check >0:
        f3 = Font(creamblue,55,cyan,"Comic Sans MS")
    if os_check <=0:
        f1 = Font(red,40,red,"Comic Sans MS")
    if os_check >0:
        f1 = Font(red,58,red,"Comic Sans MS")
    try:
        bk1 = Image("Slap_Or_Stack_Files\\Balls\\black.png",game)
    except pygame.error: 
        bk1 = Image("Slap_Or_Stack_Files//Balls//black.png",game)
    bk1.resizeTo(game.width,game.height)
    
    try:
        ball = Image("Slap_Or_Stack_Files\\Balls\\Ball.jpg",game)       
    except pygame.error: 
        ball = Image("Slap_Or_Stack_Files//Balls//Ball.jpg",game)
    ball.resizeTo(90,90)
    ball.moveTo(400,555)
    try:
        balls = Image("Slap_Or_Stack_Files\\Balls\\Ball.jpg",game)
    except pygame.error: 
        balls = Image("Slap_Or_Stack_Files//Balls//Ball.jpg",game)
    balls.resizeTo(90,90)
    x = randint(90,620)
    balls.moveTo(x,45)
    #s is the speed!
    s = 1
    try:
        border_buttom = Image("Slap_Or_Stack_Files\\Balls\\Ball.jpg",game)
    except pygame.error: 
        border_buttom = Image("Slap_Or_Stack_Files//Balls//Ball.jpg",game)
    border_buttom.resizeTo(1000,1)
    border_buttom.moveTo(370,800)

    try:
        border_left = Image("Slap_Or_Stack_Files\\Balls\\Ball.jpg",game)    
    except pygame.error: 
        border_left = Image("Slap_Or_Stack_Files//Balls//Ball.jpg",game)
    border_left.resizeTo(1,1000)
    border_left.moveTo(-220,400)

    try:
        border_right = Image("Slap_Or_Stack_Files\\Balls\\Ball.jpg",game)        
    except pygame.error: 
        border_right = Image("Slap_Or_Stack_Files//Balls//Ball.jpg",game)
    border_right.resizeTo(1,1000)
    border_right.moveTo(1010,400)
    while not game.over:
        game.processInput()
        bk1.draw()
        balls.y +=s
        balls.draw()
        game.drawText("The Block Below Is You!",171,40,f3)
        game.drawText("The Block Above Is Not You!",140,75,f3)
        game.drawText("Your Goal! Is to stack or collide with the!",10,110,f3)
        game.drawText("top block above and avoid side walls! and",35,150,f3)
        game.drawText("if your top block goes off screen you lose!",10,185,f3)
        if keys.Pressed[K_e]:
            ball.x +=10
        if keys.Pressed[K_RIGHT]:
            ball.x +=10
        if keys.Pressed[K_q]:
            ball.x -=10
        if keys.Pressed[K_LEFT]:
            ball.x -=10
        if keys.Pressed[K_h]:
            game.over = True
            help_menu()
        if keys.Pressed[K_m]:
            game.over = True
            newstart()
        if keys.Pressed[K_t]:
            game.over = True
            Tutorial_Main()
        if ball.collidedWith(border_left):
            game.drawText("Don't do that or you will lose the game!",25,220,f1)
        if ball.collidedWith(border_right):
            game.drawText("Don't do that or you will lose the game!",25,220,f1)
        if ball.collidedWith(balls):
            game.over = True
            Tutorial_4()
        if balls.collidedWith(border_buttom):
            game.drawText("Don't do that or you will lose the game!",25,220,f1)
            #The msg box only works on windows!
            #So any other os will crash when runned!
            from tkinter import messagebox
            msg = messagebox.showinfo("Slap Or Stack!", "In a real game you would of lost, so try not to do that a again!, lets retry :D")
            if msg == "ok":
                x = randint(90,620)
                balls.moveTo(x,45)
        ball.draw()
        border_left.move()
        border_right.move()
        border_buttom.move()
        game.update(60)
    game.quit()
#Tutorial end screen!
def Tutorial_4():
    game = Game(800,600,"Slap Or Stack!_Tutorial_Screen_4!")
    creamblue = (204,255,255)
    if os_check <=0:
        f3 = Font(creamblue,35,cyan,"Comic Sans MS")
    if os_check >0:
        f3 = Font(creamblue,45,cyan,"Comic Sans MS")
    try:
        bk1 = Image("Slap_Or_Stack_Files\\Balls\\black.png",game)
    except pygame.error: 
        bk1 = Image("Slap_Or_Stack_Files//Balls//black.png",game)
    bk1.resizeTo(game.width,game.height)
    try:
        ball = Image("Slap_Or_Stack_Files\\Balls\\Ball.jpg",game)
    except pygame.error: 
        ball = Image("Slap_Or_Stack_Files//Balls//Ball.jpg",game)
    ball.resizeTo(90,270)
    ball.moveTo(400,555)
    try:
        reds = Image("Slap_Or_Stack_Files\\Balls\\red.jpg",game)
    except pygame.error: 
        reds = Image("Slap_Or_Stack_Files//Balls//red.jpg",game)
    try:
        border_left = Image("Slap_Or_Stack_Files\\Balls\\Ball.jpg",game)
    except pygame.error: 
        border_left = Image("Slap_Or_Stack_Files//Balls//Ball.jpg",game)
    border_left.resizeTo(1,1000)
    border_left.moveTo(-220,400)

    try:
        border_right = Image("Slap_Or_Stack_Files\\Balls\\Ball.jpg",game)
    except pygame.error: 
        border_right = Image("Slap_Or_Stack_Files//Balls//Ball.jpg",game)
    border_right.resizeTo(1,1000)
    border_right.moveTo(1010,400)
    while not game.over:
        game.processInput()
        bk1.draw()
        ball.draw()
        reds.draw()
        reds.resizeTo(ball.width,90)
        reds.moveTo(ball.x,ball.y)
        game.drawText("Congrats!, You Passed!!",220,10,f3)
        game.drawText("Quick Tip before you play!",180,52,f3)
        game.drawText("All Hot Keys Below Mostly In All Screens!",55,90,f3)
        game.drawText("Switch Too much = No More Memory :(",90,130,f3)
        game.drawText("(*Press LCTRL In Main Game! For Access!*)",50,170,f3)
        game.drawText("Press T For Tutorial!",220,210,f3)
        game.drawText("Press H For Help Menu!",220,250,f3)
        game.drawText("Press M For Main Menu!",220,290,f3)
        game.drawText("Press P To Pause Game!",220,330,f3)
        game.drawText("Press SPACE To Start (*What ever*)!",100,370,f3)
        if keys.Pressed[K_e]:
            ball.x +=10
        if keys.Pressed[K_RIGHT]:
            ball.x +=10
        if keys.Pressed[K_q]:
            ball.x -=10
        if keys.Pressed[K_LEFT]:
            ball.x -=10
        if keys.Pressed[K_SPACE]:
            mainGame()
        #Universial Page! Switcher for M,T,H
        if keys.Pressed[K_h]:
            game.over = True
            help_menu()
        if keys.Pressed[K_m]:
            game.over = True
            newstart()
        if keys.Pressed[K_t]:
            game.over = True
            Tutorial_Main()
        if ball.collidedWith(border_left):
            ball.moveTo(400,555)
        if ball.collidedWith(border_right):
            ball.moveTo(400,555)
        game.update(60)
        '''
        #Add key instrucions like how to use the keys and how to play!/ the objective!
        '''
    game.quit()
#WINNING SCREEN!
def winner():
    game = Game(800,600,"Slap Or Stack! YOU WON!!!!")
    try:
        work = Image("Slap_Or_Stack_Files\\Background_Buttons\\Musk.jpeg",game)
    except pygame.error: 
        work = Image("Slap_Or_Stack_Files//Background_Buttons//Musk.jpeg",game)
    work.resizeTo(game.width,game.height)
    try:
        black = Image("Slap_Or_Stack_Files\\Balls\\black.png",game)
    except pygame.error: 
        black = Image("Slap_Or_Stack_Files//Balls//black.png",game)
    black.resizeTo(80,80)
    black.moveTo(770,40)
    try:
        win = Sound("Slap_Or_Stack_Files\\Songs\\win!.wav",1)
    except pygame.error: 
        win = Sound("Slap_Or_Stack_Files//Songs//win!.wav",1)
    win.play()
    try:
        click_play = Image("Slap_Or_Stack_Files\\Background_Buttons\\CLICKME_v.2.png",game)        
    except pygame.error: 
        click_play = Image("Slap_Or_Stack_Files//Background_Buttons//CLICKME_v.2.png",game)
    click_play.resizeBy(-40)
    click_play.moveTo(150,500)
    #Sad Emoji, PLEASE DON"T LEAVE MY GAME :(
    try:
        leave = Image("Slap_Or_Stack_Files\\Background_Buttons\\sads!.png",game)       
    except pygame.error: 
        leave = Image("Slap_Or_Stack_Files//Background_Buttons//sads!.png",game)
    leave.resizeBy(-74)
    leave.moveTo(600,500)
    try:
        lose = Sound("Slap_Or_Stack_Files\\Songs\\Fail.wav",2)
    except pygame.error: 
        lose = Sound("Slap_Or_Stack_Files//Songs//Fail.wav",2)
    creamblue = (204,255,255)
    if os_check <=0:
        f1 = Font(cyan,40,cyan,"Comic Sans MS")
    if os_check >0:
        f1 = Font(cyan,58,cyan,"Comic Sans MS")
    if os_check <=0:
        f5 = Font(creamblue,20,cyan,"Comic Sans MS")
    if os_check >0:
        f5 = Font(creamblue,28,cyan,"Comic Sans MS")
    if os_check <=0:
        f4 = Font(red,20,red,"Comic Sans MS")
    if os_check >0:
        f4 = Font(red,28,red,"Comic Sans MS")
    game.stopMusic()
    try:
        game.setMusic("Slap_Or_Stack_Files\\Songs\\I_Will_Survive.mp3")
    except pygame.error: 
        game.setMusic("Slap_Or_Stack_Files//Songs//I_Will_Survive.mp3")
    game.playMusic()
    while not game.over:
        game.processInput()
        work.draw()
        leave.draw()
        click_play.draw()
        black.draw()
        game.drawText("OMG! WHAT A LEGEND YOU WON!",50,0,f1)
        game.drawText("Click Me Or Press R",50,380,f5)
        game.drawText("To Restart The Game!",38,400,f5)
        game.drawText("Click Me Or Press",510,380,f4)
        game.drawText("ESC To Leave The Game :(",480,400,f4)
        if mouse.collidedWith(leave) and mouse.LeftClick:
            game.quit()
            game.over = True
            quit()
        if keys.Pressed[K_ESCAPE]:
            game.quit()
            game.over = True
            quit()
        if keys.Pressed[K_SPACE]:
            game.over = True
            #Go back to the engima arcade!
            #only leave the game when in the arcade menu
            #to keep players interested and play more :D
            #and of course i have to make that!
            mainGame()
        if mouse.collidedWith(click_play) and mouse.LeftClick:
            mainGame()
            print("Elon Musk Thanks You!, Play Again Winner :D") 
        if keys.Pressed[K_r]:
            mainGame()
        if keys.Pressed[K_h]:
            game.over = True
            help_menu()
        if keys.Pressed[K_m]:
            game.over = True
            newstart()
        if keys.Pressed[K_t]:
            game.over = True
            Tutorial_Main()
        game.update(60)
    game.quit()
#AYE THE CREATOR MENU!
def credit_menu():
    game = Game(800,600,"Slap Or Stack!Credit_Menu!")
    try:
        bk0 = Animation("Slap_Or_Stack_Files\\Background_Buttons\\mountain.png",21,game,7110/10,4000/10)       
    except pygame.error: 
        bk0 = Animation("Slap_Or_Stack_Files//Background_Buttons//mountain.png",21,game,7110/10,4000/10)
    bk0.resizeTo(game.width,game.height)
    if os_check <=0:
        f7 = Font(blue,40,black,"Comic Sans MS")
    if os_check >0:
        f7 = Font(blue,58,black,"Comic Sans MS")
    game.stopMusic()
    try:
        game.setMusic("Slap_Or_Stack_Files\\Songs\\Dancing_Queen.mp3")
    except pygame.error: 
        game.setMusic("Slap_Or_Stack_Files//Songs//Dancing_Queen.mp3")
    game.playMusic()
    #HOlA, Its me :D!
    try:
        creator = Image("Slap_Or_Stack_Files\\Background_Buttons\\William1.jpg",game)
    except pygame.error: 
        creator = Image("Slap_Or_Stack_Files//Background_Buttons//William1.jpg",game)
    creator.resizeBy(-70)
    if os_check <=0:
        creator.moveTo(400,400)
    if os_check >0:
        creator.moveTo(400,360)
    while not game.over:
        game.processInput()
        bk0.draw()
        game.drawText("Slap Or Stack!",250,40,f7)
        game.drawText("LL Productions Association",150,80,f7)
        game.drawText("Game Made By William Ho!",150,120,f7)
        game.drawText("Thank You For Looking! :D",150,160,f7)
        game.drawText("Press H For Help Menu!",170,540,f7)
        creator.draw()
        if keys.Pressed[K_SPACE]:
            game.over = True
            mainGame()
        if keys.Pressed[K_m]:
            game.over = True
            newstart()
        if keys.Pressed[K_t]:
            game.over = True
            Tutorial_Main()
        if keys.Pressed[K_h]:
            game.over = True
            help_menu()
        game.update(60)
    game.quit()
newstart()
