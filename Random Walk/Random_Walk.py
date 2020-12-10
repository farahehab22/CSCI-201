import pygame
import random 
import math

pygame.init()
display_width = 600
display_height = 600

gameDisplay = pygame.display.set_mode((display_width,display_height))

#Robot
Robot_Image = pygame.image.load('Robot.png')
RobotX = 0
RobotY = (display_height/2) - (64/2)
RobotSpeed = (0.5)

#Wall
Wall_Image = pygame.image.load('Wall.png')
WallX = (display_width/2) - (64/2)
WallY = ((display_height/2) - (64/2)) + random.randrange(-100,100)

def calculateDistance(x1,y1,x2,y2):
    dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return dist

def Collision_Soon ():
    # Predicting next step of robot will be at coordinate of the Wall about A-Axis
    if ((RobotX+RobotSpeed) >= (WallX-64) and (RobotX+RobotSpeed) <= (WallX+64))   :
        # Checking the Wall at the same level of Robot according to Y-Axis
        if (RobotY >= (WallY-64) and RobotY <= (WallY+64)):
            # Mathmatics of going up the wall
            NearesetPostive = (WallY+64)
            # Mathmatics of going down the wall
            NearesetNegative = (WallY-64)
            # Distance of after going up
            Distance1 = calculateDistance(RobotX,RobotY,WallX,NearesetPostive)
            # Distance of after going down
            Distance2 = calculateDistance(RobotX,RobotY,WallX,NearesetNegative)
            #Checking if going up is better than going down
            if Distance1 <= Distance2 :
                # Return the going up position since he was the nearset
                return [NearesetPostive,"Up"]
            else:
                # Return the going down position since he was the nearset
                return [NearesetNegative,"Down"]

running = True
while running:
    #Screen Color (R,G,B)
    gameDisplay.fill((0, 0, 0))
    
    #Robot Image
    RobotX += RobotSpeed
    gameDisplay.blit(Robot_Image, (RobotX, RobotY))
    
    #Wall Image
    gameDisplay.blit(Wall_Image, (WallX, WallY))
    
    #Check if the robot had exited the screen
    if RobotX >= display_width :
        #Reset robot position
        RobotX = 0
        RobotY = (display_height/2) - (64/2)
        
        #Change wall position to different level according to Y-Axis
        WallY = ((display_height/2) - (64/2)) + random.randrange(-100,100)
    
    #Calling "Collision_Soon" function to predict if there is Collision to the wall
    if Collision_Soon():
        SoonCollsion,Place = Collision_Soon()
        if SoonCollsion and Place:
            #Check place if was up and makeing sure that Position is more than default value of Robot Y
            if (Place == "Up" and SoonCollsion >= RobotY):
                #Dynamically moveing robot up by his speed
                RobotY += RobotSpeed
            #Check place if was down and makeing sure that Position is less than default value of Robot Y
            elif (Place == "Down" and SoonCollsion <= RobotY):
                #Dynamically moveing robot down by his speed
                RobotY -= RobotSpeed
            else:
                RobotY = SoonCollsion              
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    #Update game screen
    pygame.display.update()