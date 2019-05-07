
from tkinter import messagebox
msg = messagebox.showinfo("pong", "Welcome Ladies And Gentlemen to the Pong")
msg = messagebox.askquestion("pong", "Are you currently using any form of windows os?")
if msg == "yes":
    os_check = 0
if msg == "no":
    os_check = 5
from gamelibwillh2 import*
game = Game(900,650,"Pong")
try:
    bk = Image("Pong_Game_Files\\background\\background.png",game)
except pygame.error:    
    bk = Image("Pong_Game_Files//background//background.png",game)
bk.resizeTo(game.width,game.height)
game.setBackground(bk)
try:
    ball = Image("Pong_Game_Files\\ball\\goteem.png",game)
except pygame.error:
    ball = Image("Pong_Game_Files//ball//goteem.png",game)
ball.resizeBy(-90)
ball.setSpeed(20 ,60)
try:
    paddle = Image("Pong_Game_Files\\paddle\\smh.png",game)
except pygame.error:
    paddle = Image("Pong_Game_Files//paddle//smh.png",game)
paddle.resizeBy(-60)
paddle.moveTo(100,300)
try:
    paddles = Image("Pong_Game_Files\\paddle\\piskel.png",game)
except pygame.error:
    paddles = Image("Pong_Game_Files//paddle//piskel.png",game)
paddles.resizeBy(-60)
paddles.moveTo(800,300)
try:
    point = Image("Pong_Game_Files\\Goals\\yoink.png",game)
except pygame.error:
    point = Image("Pong_Game_Files//Goals//yoink.png",game)
point.moveTo(885,600)
point.resizeBy(-60)
try:
    point2 = Image("Pong_Game_Files\\Goals\\yoink2.png",game)
except pygame.error:
    point2 = Image("Pong_Game_Files//Goals//yoink2.png",game)
point2.moveTo(885,500)
point2.resizeBy(-60)
try:
    point3 = Image("Pong_Game_Files\\Goals\\yoink3.png",game)
except pygame.error:
    point3 = Image("Pong_Game_Files//Goals//yoink3.png",game)
point3.moveTo(885,400)
point3.resizeBy(-60)
try:
    point4 = Image("Pong_Game_Files\\Goals\\yoink4.png",game)
except pygame.error:
    point4 = Image("Pong_Game_Files//Goals//yoink4.png",game)
point4.moveTo(885,300)
point4.resizeBy(-60)
try:
    point5 = Image("Pong_Game_Files\\Goals\\yoink5.png",game)
except pygame.error:
    point5 = Image("Pong_Game_Files//Goals//yoink5.png",game)
point5.moveTo(885,200)
point5.resizeBy(-60)
try:
    point6 = Image("Pong_Game_Files\\Goals\\yoink6.png",game)
except pygame.error:
    point6 = Image("Pong_Game_Files//Goals//yoink6.png",game)
point6.moveTo(885,100)
point6.resizeBy(-60)
try:
    point7 = Image("Pong_Game_Files\\Goals\\yoink7.png",game)
except pygame.error:
    point7 = Image("Pong_Game_Files//Goals//yoink7.png",game)
point7.moveTo(885,0)

point7.resizeBy(-60)
global play1
global play2
play1 = 0
play2 = 0
#points #2
try:
    points = Image("Pong_Game_Files\\Goals\\images.png",game)
except pygame.error:
    points = Image("Pong_Game_Files//Goals//images.png",game)
points.resizeBy(-50)
points.moveTo(10,100)
try:
    points1 = Image("Pong_Game_Files\\Goals\\images1.png",game)
except pygame.error:
    points1 = Image("Pong_Game_Files//Goals//images1.png",game)
points1.resizeBy(-50)
points1.moveTo(10,200)
try:
    points3 = Image("Pong_Game_Files\\Goals\\images3.png",game)
except pygame.error:
    points3 = Image("Pong_Game_Files//Goals//images3.png",game)
points3.resizeBy(-50)
points3.moveTo(10,300)
try:
    points4 = Image("Pong_Game_Files\\Goals\\images4.png",game)
except pygame.error:
    points4 = Image("Pong_Game_Files//Goals//images4.png",game)
points4.resizeBy(-50)
points4.moveTo(10,400)
try:
    points5 = Image("Pong_Game_Files\\Goals\\images5.png",game)
except pygame.error:
    points5 = Image("Pong_Game_Files//Goals//images5.png",game)
points5.resizeBy(-50)
points5.moveTo(10,550)
if os_check <=0:
    f = Font(white,20,red,"Comic Sans MS")
if os_check >0:
    f = Font(white,28,red,"Comic Sans MS")
if os_check <=0:
    e = Font(white,20,red,"Comic Sans MS")
if os_check >0:
    e = Font(white,28,red,"Comic Sans MS")
if os_check <=0:
    g = Font(white,30,red,"Comic Sans MS")
if os_check >0:
    g = Font(white,40,red,"Comic Sans MS")
import webbrowser
def regular():
    play1 = 0
    play2 = 0
    while not game.over:
        game.processInput()
        bk.draw()
        ball.draw()
        paddle.draw()
        paddles.draw()
        point.draw()
        point2.draw()
        point3.draw()
        point4.draw()
        point5.draw()
        point6.draw()
        point7.draw()
        points.draw()
        points1.draw()
        points3.draw()
        points4.draw()
        points5.draw()
        if keys.Pressed[K_w]:
            paddle.y-=10
        if keys.Pressed[K_s]:
            paddle.y+=10
        if keys.Pressed[K_UP]:
            paddles.y-=10
        if keys.Pressed[K_DOWN]:
            paddles.y+=10
        #VHEAT

        if keys.Pressed[K_ESCAPE]:
            game.over = True
            game.quit()
            quit()
        if keys.Pressed[K_p]:
            ball.moveTowards(paddle,5) 

        if ball.collidedWith(point):
            ball.moveTo(450,350)
            play1+=1
        if ball.collidedWith(point2):
            ball.moveTo(450,350)
            play1+=1
        if ball.collidedWith(point3):
            ball.moveTo(450,350)
            play1+=1
        if ball.collidedWith(point4):
            ball.moveTo(450,350)
            play1+=1
        if ball.collidedWith(point5):
            ball.moveTo(450,350)
            play1+=1
        if ball.collidedWith(point6):
            ball.moveTo(450,350)
            play1+=1
        if ball.collidedWith(point7):
            ball.moveTo(450,350)
            play1+=1

        #collide check
        if ball.collidedWith(paddle):
            ball.setSpeed(20,258)
        if ball.collidedWith(paddles):
            ball.setSpeed(20,96) and (20,90)
        game.drawText("Red's Score:" + str(play1),points.x+50,points.y-30)
        if paddle.y > 600:
            paddle.y -=10
        if paddles.y > 600:
            paddles.y -=10
        if paddle.y < 50:
            paddle.y +=10
        if paddles.y < 50:
            paddles.y +=10
        #text
        #if statements for points

        if ball.collidedWith(points):
            ball.moveTo(450,450)
            play2 +=1
        if ball.collidedWith(points1):
            ball.moveTo(450,450)
            play2 +=1
        if ball.collidedWith(points3):
            ball.moveTo(450,450)
            play2 +=1
        if ball.collidedWith(points4):
            ball.moveTo(450,450)
            play2 +=1
        if ball.collidedWith(points5):
            ball.moveTo(450,450)
            play2 +=1
        game.drawText("Blue's score:" + str(play2),point.x-150,points.y-30)




    
        ball.move(True)
        paddle.move()
        game.update(30)
    game.quit()
def AI_LEVEL():
    switch = 0
    switch_1 = 0
    global play1
    global play2
    while not game.over:
        game.processInput()
        bk.draw()
        ball.draw()
        paddle.draw()
        paddles.draw()
        point.draw()
        point2.draw()
        point3.draw()
        point4.draw()
        point5.draw()
        point6.draw()
        point7.draw()
        points.draw()
        points1.draw()
        points3.draw()
        points4.draw()
        points5.draw()
        if keys.Pressed[K_w]:
            paddle.y-=10
        if keys.Pressed[K_s]:
            paddle.y+=10
        if keys.Pressed[K_UP]:
            paddles.y-=10
        if keys.Pressed[K_DOWN]:
            paddles.y+=10
        #VHEAT

        if keys.Pressed[K_ESCAPE]:
            game.over = True
            game.quit()
            quit()
        if keys.Pressed[K_p]:
            ball.moveTowards(paddle,5) 

        if ball.collidedWith(point):
            ball.moveTo(450,350)
            play1+=1
            switch_1 +=1
        if ball.collidedWith(point2):
            ball.moveTo(450,350)
            play1+=1
            switch_1 +=1
        if ball.collidedWith(point3):
            ball.moveTo(450,350)
            play1+=1
            switch_1 +=1
        if ball.collidedWith(point4):
            ball.moveTo(450,350)
            play1+=1
            switch_1 +=1
        if ball.collidedWith(point5):
            ball.moveTo(450,350)
            play1+=1
            switch_1 +=1
        if ball.collidedWith(point6):
            ball.moveTo(450,350)
            play1+=1
            switch_1 +=1
        if ball.collidedWith(point7):
            ball.moveTo(450,350)
            play1+=1
            switch_1 +=1
    

    #collide check
        if ball.collidedWith(paddle):
            ball.setSpeed(20,258)
            switch = 0
            switch_1 = 0
        if ball.collidedWith(paddles):
            ball.setSpeed(20,96) and (20,90)
        game.drawText("Red's Score:" + str(play1),points.x+50,points.y-30)
        if paddle.y > 550:
            paddle.y -=50
        if paddles.y > 600:
            paddles.y -=10
        if paddle.y < 50:
            paddle.y +=50
        if paddles.y < 50:
            paddles.y +=10
    #dumb AI
        def ai():
            if not game.over:
                if ball.y >300:
                    paddle.y+=15
                if ball.y <290: #or ball.x <200:
                    paddle.y-=10
                #if paddle.isOffScreen("top"):
                    #paddle.y+=100
                   # print("top")
                
        ai()
        if ball.collidedWith(points):
            paddle.y+=300
        if ball.collidedWith(points1):
            paddle.y+=300
        if ball.collidedWith(points3):
            paddle.y+=300
        if ball.collidedWith(points4):
            paddle.y+=300
        if ball.collidedWith(points5):
            paddle.y-=300
        if switch >=1:
            paddle.y = ball.y
        if switch_1 >=10:
            ball.moveTo(450,325)
            if os_check <=0:
                msg = messagebox.showinfo("pong", "Looks like your game broke :(, Press ok to reload!")
                if msg == "ok":
                    #game.over = True
                    #game.quit()
                    #webbrowser.open('pong_game_main.py')
                    #quit()
                    #game.over = True
                    #MAKE THIS WHOLE THING DEF AI():
                    #AND THEN RUN IT
                    AI_LEVEL()
                
            if os_check >1:
                print("************************************************************************")
                print("Looks like your game broke :(, Sadly you will have to reload the game :(")
                print("************************************************************************")
        #text
    #if statements for points
        if ball.collidedWith(points):
            ball.moveTo(450,450)
            play2 +=1
            switch +=1
        if ball.collidedWith(points1):
            ball.moveTo(450,450)
            play2 +=1
            switch +=1
        if ball.collidedWith(points3):
            ball.moveTo(450,450)
            play2 +=1
            switch +=1
        if ball.collidedWith(points4):
            ball.moveTo(450,450)
            play2 +=1
            switch +=1
        if ball.collidedWith(points5):
            ball.moveTo(450,450)
            play2 +=1
            switch +=1
        game.drawText("Blue's score:" + str(play2),point.x-150,points.y-30)


    
        ball.move(True)
        paddle.move()
        game.update(30)
    game.quit()
while not game.over:
    game.processInput()
    paddle.draw()
    paddles.draw()
    game.drawText("Player 1 is RED. Controls is the ARROW keys. (UP and DOWN) " ,game.width-750,game.height-600,f)
    if os_check <=0:
        game.drawText("Player 2 is BLUE. Controls is W and S bar.(W to go UP, S to go DOWN) " ,game.width-740,game.height-550,e)
    if os_check >0:
        game.drawText("Player 2 is BLUE. Controls is W and S bar.(W to go UP, S to go DOWN) " ,game.width-800,game.height-550,e)
    game.drawText("Press R to do the two player level. Be FAST and Have FUN",game.width-870,game.height-50,g)
    game.drawText("Press SPACE bar to start AI Level. Be FAST and Have FUN " ,game.width-880,game.height-75,g)
    if keys.Pressed[K_SPACE]:
        AI_LEVEL()
    if keys.Pressed[K_r]:
        regular()
    if keys.Pressed[K_p]:
        game.over = True
        AI_Level()
    if keys.Pressed[K_ESCAPE]:
        game.over = True
        game.quit()
        quit()
    game.update(30)
game.quit()
