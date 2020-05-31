### This code is written from help of this tutorial: https://www.youtube.com/watch?v=ujOTNg17LjI&list=PLQVvvaa0QuDdLkP8MrOXLe_rKuf6r80KO



import pygame                                                                   #Import pygame
import time
import random

pygame.init()                                                                   #After importing we need to initiate pygame.

display_width = 900                                                             #Setting up the total display weidth and height of the game display.
display_height = 650
                                                                                #Defining the colors.
black = (0, 0, 0)                                                               #Black means absence of any color and white means all colos
white = (255, 255, 255)                                                         #Colors are written here in (R,G,B) format. ie. (Red,Green,Blue) Maximum 256 choices starting from 0
red = (255, 0, 0)                                                               #Maximum 256 choices starting from 0.
green = (0, 255, 0)
blue = (0, 0, 255)
block_color= (25, 100, 130)                                                     #Defining the color of the block

car_width = 74                                                                  #Defining the height and with of our object of the game.
car_height = 82                                                                 # Object means the image we will import..

game_display = pygame.display.set_mode((display_width, display_height))         #Setting up the display enviournment.
pygame.display.set_caption("CAR CRASH 2D")                                              #Giving a name to the enviournment.
clock = pygame.time.Clock()                                                     #Defining the clock of the game.
car_image = pygame.image.load('car_paint_transparent.png')                      #Importing the image and assigning it to a variable called car_image.

def dodged_things(count) :                                                      #Here we want to enter a counter that says how many blocks we have dodged.
    font= pygame.font.SysFont(None,25)
    text= font.render(("Dodged: " + str(count)),True, black)
    game_display.blit(text,(0,0))

def things(thingx,thingy,thingw,thingh,color):                                  #Defining things as those will come up and  we have to go away from it.
    pygame.draw.rect(game_display,block_color,[thingx,thingy,thingw,thingh])          #Drawing rectangles.


def car(x, y):                                                                  #Defing a function for the image i.e. the car at coordinates (x,y).
    game_display.blit(car_image, (int(x), int(y)))

def text_objects(text,font):                                                    #We want to show some text if something happens in the game.
    text_surface = font.render(text, True, black)                               #Thus we define a function text_objects() which takes the text and font as inputs
    return text_surface, text_surface.get_rect()                                #and returns the text confined in a rectangle->get_rect()

def message_display(text):                                                      #Defining a function for displaying the message.
    largeText= pygame.font.Font('freesansbold.ttf', 80)                         #Stating the font and size of the text.
    text_surface, text_rectangle = text_objects(text, largeText)
    text_rectangle.center = (int((display_width/2)), int((display_height/2)))      #Stating where the text will be. Here at the middle of the screen of the game.
    game_display.blit(text_surface, text_rectangle)                              #This is the code for text to generate. Without this thext would not generate.
    pygame.display.update()                                                     #This is the code for the text to pop up at the front after generating.
    time.sleep(2)                                                               #Stating the time (i.e. 2 sec) after which the text will pop up.
    game_loop()                                                                 #After the text is shown, the game will restart.

def crash():                                                                    #Defining a function called crash which will actually show the text.
    message_display("You Crashed")                                              #This is the message we want to display.


def game_loop():                                                                #Here the main code for the  game starts.
    x = (display_width * 0.45)                                                  # Initializing the position of the  object.
    y = (display_height * 0.75)
    x_change = 0                                                                #Initializing the change in position as 0 initially.

    thing_startx= random.randrange(0,display_width)
    thing_starty= -600
    thing_speed= 7
    thing_width= 50
    thing_height= 50

    dodged=0

    gameExit = False
    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:                                      #This is the code for if we click on the cross button on the game screen,
                pygame.quit()                                                  #the game will close. Otherwise the game will close automatically.
                quit()
            if event.type == pygame.KEYDOWN:                                   #From here we defined if we press right-aroow/left-arrow/up/down keys
                if event.key == pygame.K_LEFT:                                 #The x_change and the y_change variables
                    x_change = -7                                              #will be upgraded as we wish.
                if event.key == pygame.K_RIGHT:
                    x_change = +7


            if event.type == pygame.KEYUP:                                      #Codes here states that if we don't press the keys
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:   #or stop pressing the keys,
                    x_change = 0                                                #the object will stop moving,#That means x_change  will be 0.


        x += x_change                                                           #Upgrading the coordinates of the object by x_change and y_change


        game_display.fill(white)                                                #Game display is stated as white

        things(thing_startx,thing_starty,thing_width,thing_height,block_color)
        thing_starty += thing_speed                                             #This means the initial y coordinate of the block is equal to its initial speed.
        car(x, y)
        dodged_things(dodged)
        if x > display_width - car_width or x < 0:                              #Here we state a boundary for the car i.e the edges of the game display.
            crash()                                                             # We further state that if the car goes to the boundary,the message is poped up i.e "You Crushed".
        if thing_starty > display_height:
            thing_starty=0-thing_height
            thing_startx= random.randrange(0,display_width)                     #This generates the blocks randomly.
            dodged += 1                                                         #This increases the number of counts of the dodged blocks.
            thing_speed += 1                                                  #This increases the speed of the block over time.

        if y< thing_starty+thing_height:                                        #Code for the conditions of the car to crash.

            if x> thing_startx and x< thing_startx + thing_width or x+car_width>thing_startx and x+car_width< thing_startx+thing_width:

                crash()

        pygame.display.update()                                                 #This is again to update the display. Otherwise we would not see anything.
        clock.tick(100)                                                         #This is to specify how fast I want to change the dispaly frame.
                                                                                #Here it is 100 frames/sec.

game_loop()                                                                     #This code actually runs the game. The prev one was just defining it. :)
pygame.quit()                                                                   #To quit pygame.
quit()                                                                          #To quit python.
