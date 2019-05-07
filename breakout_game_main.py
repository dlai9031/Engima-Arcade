#*****************************************************************************
#Goal of the game! Make the ball collided with the color blocks
#And try not to make the ball touch the buttom of the screen!
#If all the color blcoks are gone then you win!
#If the ball collides with the buttom of the screen then you lose :(
#Game Controls
#[Q] or [Left Arrow] makes the buttom paddle go left
#[E] or [Right Arrow] makes the buttom paddle go left
#Thank You All!
#© 2019 Enigma Arcade.inc
#© 2019 LL Productions 
#© 2019 Slap Or Stack
#All rights not reserved but please do not recreate and share unless you have
#the creators approval!
#*****************************************************************************
from gamelibwillh2 import*
def main_game():
    game = Game(800,600,"BreakOut!")
    #Thing to collided with ball
    try:
        bk = Image("Breakout_Files\\black.png",game)        
    except pygame.error:    
        bk = Image("Breakout_Files//black.png",game)
    bk.resizeTo(game.width,game.height)
    try:
        plate = Image("Breakout_Files\\Ball.jpg",game)
    except pygame.error:
        plate = Image("Breakout_Files//Ball.jpg",game)
    plate.resizeTo(90,10)
    plate.moveTo(400,570)
    #ball
    try:
        ball = Image("Breakout_Files\\goteem.png",game)
    except pygame.error:    
        ball = Image("Breakout_Files//goteem.png",game)
    ball.resizeBy(-90)
    ball.moveTo(400,500)
    ball.moveTowards(plate,5)
    #layer one
#Lay1_1 is the middle block
#lay1_1 - lay1_4 is to the left side
#Lay1_1 - l
    try:
        lay1_1 = Image("Breakout_Files\\green.png",game)
    except pygame.error:
        lay1_1 = Image("Breakout_Files//green.png",game)
    lay1_1.resizeTo(90,20)
    lay1_1.moveTo(400,10)
    try:
        lay1_2 = Image("Breakout_Files\\green.png",game)
    except pygame.error:
        lay1_2 = Image("Breakout_Files//green.png",game)
    lay1_2.resizeTo(90,20)
    lay1_2.moveTo(305,10)
    try:
        lay1_3 = Image("Breakout_Files\\green.png",game)
    except pygame.error:
        lay1_3 = Image("Breakout_Files//green.png",game)
    lay1_3.resizeTo(90,20)
    lay1_3.moveTo(210,10)
    try:
        lay1_4 = Image("Breakout_Files\\green.png",game)
    except pygame.error:
        lay1_4 = Image("Breakout_Files//green.png",game)
    lay1_4.resizeTo(90,20)
    lay1_4.moveTo(115,10)
    try:
        lay1_5 = Image("Breakout_Files\\green.png",game)
    except pygame.error:
        lay1_5 = Image("Breakout_Files//green.png",game)
    lay1_5.resizeTo(90,20)
    lay1_5.moveTo(495,10)
    try:
        lay1_6 = Image("Breakout_Files\\green.png",game)
    except pygame.error:
        lay1_6 = Image("Breakout_Files//green.png",game)
    lay1_6.resizeTo(90,20)
    lay1_6.moveTo(590,10)
    try:
        lay1_7 = Image("Breakout_Files\\green.png",game)
    except pygame.error:
        lay1_7 = Image("Breakout_Files//green.png",game)
    lay1_7.resizeTo(90,20)
    lay1_7.moveTo(685,10)
#layer 2
    try:
        lay1_1s = Image("Breakout_Files\\blue.png",game)
    except pygame.error:
        lay1_1s = Image("Breakout_Files//blue.png",game)
    lay1_1s.resizeTo(90,20)
    lay1_1s.moveTo(400,40)
    try:
        lay1_2s = Image("Breakout_Files\\blue.png",game)
    except pygame.error:
        lay1_2s = Image("Breakout_Files//blue.png",game)
    lay1_2s.resizeTo(90,20)
    lay1_2s.moveTo(305,40)
    try:
        lay1_3s = Image("Breakout_Files\\blue.png",game)
    except pygame.error:
        lay1_3s = Image("Breakout_Files//blue.png",game)
    lay1_3s.resizeTo(90,20)
    lay1_3s.moveTo(210,40)
    try:
        lay1_4s = Image("Breakout_Files\\blue.png",game)
    except pygame.error:
        lay1_4s = Image("Breakout_Files//blue.png",game)
    lay1_4s.resizeTo(90,20)
    lay1_4s.moveTo(115,40)
    try:
        lay1_5s = Image("Breakout_Files\\blue.png",game)
    except pygame.error:
        lay1_5s = Image("Breakout_Files//blue.png",game)
    lay1_5s.resizeTo(90,20)
    lay1_5s.moveTo(495,40)
    try:
        lay1_6s = Image("Breakout_Files\\blue.png",game)
    except pygame.error:
        lay1_6s = Image("Breakout_Files//blue.png",game)
    lay1_6s.resizeTo(90,20)
    lay1_6s.moveTo(590,40)
    try:
        lay1_7s = Image("Breakout_Files\\blue.png",game)
    except pygame.error:
        lay1_7s = Image("Breakout_Files//blue.png",game)
    lay1_7s.resizeTo(90,20)
    lay1_7s.moveTo(685,40)
#layer 3
    try:
        lay1_1z = Image("Breakout_Files\\purples.png",game)
    except pygame.error:
        lay1_1z = Image("Breakout_Files//purples.png",game)
    lay1_1z.resizeTo(90,20)
    lay1_1z.moveTo(400,70)
    try:
        lay1_2z = Image("Breakout_Files\\purples.png",game)
    except pygame.error:
        lay1_2z = Image("Breakout_Files//purples.png",game)
    lay1_2z.resizeTo(90,20)
    lay1_2z.moveTo(305,70)
    try:
        lay1_3z = Image("Breakout_Files\\purples.png",game)
    except pygame.error:
        lay1_3z = Image("Breakout_Files//purples.png",game)
    lay1_3z.resizeTo(90,20)
    lay1_3z.moveTo(210,70)
    try:
        lay1_4z = Image("Breakout_Files\\purples.png",game)
    except pygame.error:
        lay1_4z = Image("Breakout_Files//purples.png",game)
    lay1_4z.resizeTo(90,20)
    lay1_4z.moveTo(115,70)
    try:
        lay1_5z = Image("Breakout_Files\\purples.png",game)
    except pygame.error:
        lay1_5z = Image("Breakout_Files//purples.png",game)
    lay1_5z.resizeTo(90,20)
    lay1_5z.moveTo(495,70)
    try:
        lay1_6z = Image("Breakout_Files\\purples.png",game)
    except pygame.error:
        lay1_6z = Image("Breakout_Files//purples.png",game)
    lay1_6z.resizeTo(90,20)
    lay1_6z.moveTo(590,70)
    try:
        lay1_7z = Image("Breakout_Files\\purples.png",game)
    except pygame.error:
        lay1_7z = Image("Breakout_Files//purples.png",game)
    lay1_7z.resizeTo(90,20)
    lay1_7z.moveTo(685,70)
#code to lose
    try:
        lay1_1q = Image("Breakout_Files\\green.png",game)
    except pygame.error:
        lay1_1q = Image("Breakout_Files//green.png",game)
    lay1_1q.resizeTo(90,20)
    lay1_1q.moveTo(400,625)
    try:
        lay1_2q = Image("Breakout_Files\\purples.png",game)
    except pygame.error:
        lay1_2q = Image("Breakout_Files//purples.png",game)
    lay1_2q.resizeTo(90,20)
    lay1_2q.moveTo(310,625)
    try:
        lay1_3q = Image("Breakout_Files\\purples.png",game)
    except pygame.error:
        lay1_3q = Image("Breakout_Files//purples.png",game)
    lay1_3q.resizeTo(90,20)
    lay1_3q.moveTo(200,625)
    try:
        lay1_4q = Image("Breakout_Files\\purples.png",game)
    except pygame.error:
        lay1_4q = Image("Breakout_Files//purples.png",game)
    lay1_4q.resizeTo(90,20)
    lay1_4q.moveTo(80,625)
    try:
        lay1_5q = Image("Breakout_Files\\purples.png",game)
    except pygame.error:
        lay1_5q = Image("Breakout_Files//purples.png",game)
    lay1_5q.resizeTo(90,20)
    lay1_5q.moveTo(500,625)
    try:
        lay1_6q = Image("Breakout_Files\\purples.png",game)
    except pygame.error:
        lay1_6q = Image("Breakout_Files//purples.png",game)
    lay1_6q.resizeTo(90,20)
    lay1_6q.moveTo(595,625)
    try:
        lay1_7q = Image("Breakout_Files\\purples.png",game)
    except pygame.error:
        lay1_7q = Image("Breakout_Files//purples.png",game)
    lay1_7q.resizeTo(90,20)
    lay1_7q.moveTo(690,625)
    while not game.over:
        game.processInput()
        bk.draw()
        ball.move(True)
        plate.draw()
        #ball.move(True)
        lay1_1.draw()
        lay1_2.draw()
        lay1_3.draw()
        lay1_4.draw()
        lay1_5.draw()
        lay1_6.draw()
        lay1_7.draw()
        #layer 2
        lay1_1s.draw()
        lay1_2s.draw()
        lay1_3s.draw()
        lay1_4s.draw()
        lay1_5s.draw()
        lay1_6s.draw()
        lay1_7s.draw()
        #layer 3
        lay1_1z.draw()
        lay1_2z.draw()
        lay1_3z.draw()
        lay1_4z.draw()
        lay1_5z.draw()
        lay1_6z.draw()
        lay1_7z.draw()
        #code to lose
        lay1_1q.draw()
        lay1_2q.draw()
        lay1_3q.draw()
        lay1_4q.draw()
        lay1_5q.draw()
        lay1_6q.draw()
        lay1_7q.draw()
        if ball.collidedWith(lay1_1):
            lay1_1.visible = False
            ball.setSpeed(20,25)    
            game.score +=1
        if ball.collidedWith(lay1_2):
            lay1_2.visible = False
            ball.setSpeed(20,45)
            game.score +=1
        if ball.collidedWith(lay1_3):
            lay1_3.visible = False
            ball.setSpeed(20,25)
            game.score +=1
        if ball.collidedWith(lay1_4):
            lay1_4.visible = False
            ball.setSpeed(20,45)
            game.score +=1
        if ball.collidedWith(lay1_5):
            lay1_5.visible = False
            ball.setSpeed(20,25)
            game.score +=1
        if ball.collidedWith(lay1_6):
            lay1_6.visible = False
            ball.setSpeed(20,-45)
            game.score +=1
        if ball.collidedWith(lay1_7):
            lay1_7.visible = False
            ball.setSpeed(20,-25)
            game.score +=1
#layer 2 for if statements
        if ball.collidedWith(lay1_1s):
            lay1_1s.visible = False
            ball.setSpeed(20,25)    
            game.score +=1
        if ball.collidedWith(lay1_2s):
            lay1_2s.visible = False
            ball.setSpeed(20,45)
            game.score +=1
        if ball.collidedWith(lay1_3s):
            lay1_3s.visible = False
            ball.setSpeed(20,25)
            game.score +=1
        if ball.collidedWith(lay1_4s):
            lay1_4s.visible = False
            ball.setSpeed(20,45)
            game.score +=1
        if ball.collidedWith(lay1_5s):
            lay1_5s.visible = False
            ball.setSpeed(20,25)
            game.score +=1
        if ball.collidedWith(lay1_6s):
            lay1_6s.visible = False
            ball.setSpeed(20,-45)
            game.score +=1
        if ball.collidedWith(lay1_7s):
            lay1_7s.visible = False
            ball.setSpeed(20,-25)
            game.score +=1
#layer 3
        if ball.collidedWith(lay1_1z):
            lay1_1z.visible = False
            ball.setSpeed(20,25)    
            game.score +=1
        if ball.collidedWith(lay1_2z):
            lay1_2z.visible = False
            ball.setSpeed(20,45)
            game.score +=1
        if ball.collidedWith(lay1_3z):
            lay1_3z.visible = False
            ball.setSpeed(20,25)
            game.score +=1
        if ball.collidedWith(lay1_4z):
            lay1_4z.visible = False
            ball.setSpeed(20,45)
            game.score +=1
        if ball.collidedWith(lay1_5z):
            lay1_5z.visible = False
            ball.setSpeed(20,25)
            game.score +=1
        if ball.collidedWith(lay1_6z):
            lay1_6z.visible = False
            ball.setSpeed(20,-45)
            game.score +=1
        if ball.collidedWith(lay1_7z):
            lay1_7z.visible = False
            ball.setSpeed(20,-25)
            game.score +=1
# code to lose
        if ball.collidedWith(lay1_1q):
            game.quit()
        if ball.collidedWith(lay1_2q):
            game.quit()
        if ball.collidedWith(lay1_3q):
            game.quit()
        if ball.collidedWith(lay1_4q):
            game.quit()
        if ball.collidedWith(lay1_5q):
            game.quit()
        if ball.collidedWith(lay1_6q):
            game.quit()
        if ball.collidedWith(lay1_7q):
            game.quit()
#controls
        if keys.Pressed[K_ESCAPE]:
            game.over = True
            game.quit()
            quit()
        if keys.Pressed[K_LEFT]:
            plate.x -=20
        if keys.Pressed[K_RIGHT]:
            plate.x +=20
        if keys.Pressed[K_q]:
            plate.x -=20
        if keys.Pressed[K_e]:
            plate.x +=20
        if plate.x >770:
            plate.moveTo(770,570)
        if plate.x <5:
            plate.moveTo(5,570)
        if ball.collidedWith(plate):
            A = randint(145,180)
            S = 20
            ball.setSpeed(S,A)

        plate.draw()
        game.displayScore()
        game.update(30)
    game.quit()
main_game()
