#Capstone project 2
#Compulsory task


#This capstone project utilises pygame to creat a game with one player, three enemies and one award/prize collection
#if player collides with any of three enemies, the user loses and game ends
#if player collides with a prize/award the user wins and the game ends
#if the user avoids the collision with enemies until they disappear from the screen, the user wins and game ends
#to move the player, up,left,down and right arrow keys from the keyboard are used

#importing the packages to be used: pygama library and random package
import pygame # Imports a game library that lets you use specific functions in your program.
import random # Import to generate random numbers.


# Initialize the pygame modules to get everything started.

pygame.init() 

# The screen that will be created needs a width and a height.

screen_width = 1040
screen_height = 680
screen = pygame.display.set_mode((screen_width,screen_height)) # This creates the screen and gives it the width and height specified as a 2 item sequence.

# This creates the player and gives it the image found in this folder, same for enemy and prize. 

player = pygame.image.load("image.png")
enemy = pygame.image.load("enemy.png")

#these extra objects for the enemy allow for the 3 enemies to show on screen
enemy1 = pygame.image.load("enemy.png")         #second enemy
enemy2 = pygame.image.load("enemy.png")         #third enemy

#loading prize image
prize = pygame.image.load("award.png")

# Get the width and height of the images in order to do boundary detection (i.e. make sure the image stays within screen boundaries or know when the image is off the screen).

image_height = player.get_height()
image_width = player.get_width()
enemy_height = enemy.get_height()
enemy_width = enemy.get_width()

enemy1_height = enemy1.get_height()
enemy1_width = enemy1.get_width()

enemy2_height = enemy2.get_height()
enemy2_width = enemy2.get_width()

prize_height = prize.get_height()
prize_width = prize.get_width()


print("This is the height of the player image: " +str(image_height))
print("This is the width of the player image: " +str(image_width))

# Store the positions of the player and enemy as variables so that you can change them later. 

playerXPosition = 100
playerYPosition = 50

# Make all the enemies start off screen and at a random y position.

enemyXPosition =  screen_width
enemyYPosition =  random.randint(0, screen_height - enemy_height)

enemy1XPosition =  screen_width
enemy1YPosition =  random.randint(0, screen_height - enemy1_height)

enemy2XPosition =  screen_width
enemy2YPosition =  random.randint(0, screen_height - enemy2_height)

prizeXPosition = screen_width
prizeYPosition = random.randint(0, screen_height - prize_height)

# This checks if the up/left/down/right key is pressed.
# Right now they are not so make them equal to the boolean value (True or False) of False. 
 
keyUp= False
keyDown = False

keyLeft = False
keyRight = False

# This is the game loop.
#The game logic runs over and over again.
# You need to refresh/update the screen window and apply changes to 
# represent real time game play. 

while 1: # This is a looping structure that will loop the indented code until you tell it to stop(in the event where you exit the program by quitting). In Python the int 1 has the boolean value of 'true'.

    screen.fill(0) # Clears the screen.
    screen.blit(player, (playerXPosition, playerYPosition))# This draws the player image to the screen at the postion specfied. i.e. (100, 50).

    # The below draws the enemies and prize image to the screen at the retrieved postions
    screen.blit(enemy, (enemyXPosition, enemyYPosition))

    screen.blit(enemy1, (enemy1XPosition, enemy1YPosition))
    screen.blit(enemy2, (enemy2XPosition, enemy2YPosition))

    screen.blit(prize, (prizeXPosition, prizeYPosition))
    
    pygame.display.flip()# This updates the screen. 
    
    # This loops through events in the game.
    
    for event in pygame.event.get():
    
        # This event checks if the user quits the program, then if so it exits the program. 
        
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)

        # This event checks if the user press a key down.
        
        if event.type == pygame.KEYDOWN:
        
            # Test if the key pressed is the one we want: UP,DOWN,LEFT and RIGHT keys.
            
            if event.key == pygame.K_UP: # pygame.K_UP represents a keyboard key constant. 
                keyUp = True
            if event.key == pygame.K_DOWN:
                keyDown = True
                
            if event.key == pygame.K_LEFT:
                keyLeft = True
            if event.key == pygame.K_RIGHT:
                keyRight = True    
        

        # This event checks if the key is up(i.e. not pressed by the user).
        
        if event.type == pygame.KEYUP:
        
            # Test if the key released is the one we want.
            
            if event.key == pygame.K_UP:
                keyUp = False
            if event.key == pygame.K_DOWN:
                keyDown = False

            if event.key == pygame.K_RIGHT:
                keyRight = False
            if event.key == pygame.K_LEFT:
                keyLeft = False    

            
    # After events are checked in the for loop above and values are set,
    # check key pressed values and move player accordingly.
    
    # The coordinate system of the game window(screen) is that the top left corner is (0, 0).
    # This means that if you want the player to move down you will have to increase the y position. 
    
    if keyUp == True:
        if playerYPosition > 0 : # This makes sure that the user does not move the player above the window.
            playerYPosition -= 1
    if keyDown == True:
        if playerYPosition < screen_height - image_height:# This makes sure that the user does not move the player below the window.
            playerYPosition += 1



    if keyLeft == True:
        if playerXPosition < 0:# This makes sure that the user does not move the player below the left side of the window.
            playerXPosition += 1
        playerXPosition -= 1   
            

    if keyRight == True:
        if playerXPosition > screen_width - image_width:# This makes sure that the user does not move the player above the right side of the window.
            playerXPosition -= 1
        playerXPosition += 1    
    
    # Check for collision of the enemies with the player.
    # To do this we need bounding boxes around the images of the player and enemy.
    # We the need to test if these boxes intersect. If they do then there is a collision.
    
    # Bounding box for the player:
    
    playerBox = pygame.Rect(player.get_rect())
    
    # The following updates the playerBox position to the player's position,
    # in effect making the box stay around the player image. 
    
    playerBox.top = playerYPosition
    playerBox.left = playerXPosition
    
    # Bounding box for the enemies:
    
    enemyBox = pygame.Rect(enemy.get_rect())
    enemyBox.top = enemyYPosition
    enemyBox.left = enemyXPosition

    enemy1Box = pygame.Rect(enemy1.get_rect())
    enemy1Box.top = enemy1YPosition
    enemy1Box.left = enemy1XPosition

    enemy2Box = pygame.Rect(enemy2.get_rect())
    enemy2Box.top = enemy2YPosition
    enemy2Box.left = enemy2XPosition

    # Bounding box for the prize:
    
    prizeBox = pygame.Rect(prize.get_rect())
    prizeBox.top = prizeYPosition
    prizeBox.left = prizeXPosition
    
    
    # Test collision of the boxes:
    
    if playerBox.colliderect(enemyBox) or playerBox.colliderect(enemy1Box) or playerBox.colliderect(enemy2Box):  #check if player collides with either enemy 1/2/3
    
        # Display losing status to the user: 
        
        print("You lose!")
       
        # Quite game and exit window: 
        
        pygame.quit()
        exit(0)

    
    if playerBox.colliderect(prizeBox):         #check if the player collieds with the award/prize
    
        # Display winning status to the user: 
        
        print("You win!")
       
        # Quite game and exit window: 
        
        pygame.quit()
        exit(0)   
        
    # If the enemies are off the screen the user wins the game:
    
    if (enemyXPosition < (0 - enemy_width)) and (enemy1XPosition < (0 - enemy1_width)) and (enemy2XPosition < (0 - enemy2_width)):
    
        # Display wining status to the user: 
        
        print("You win!")
        
        # Quite game and exit window: 
        pygame.quit()
        
        exit(0)
    
 
    
    # Make enemies and prize approach the player at different speeds.
    #lower the number slower the object moves, higher the number - faster the object moves
    
    
    enemyXPosition -= 0.15      
    enemy1XPosition -= 0.30
    enemy2XPosition -= 0.35 
    prizeXPosition -= 0.10
    
    # ================The game loop logic ends here. =============
  
