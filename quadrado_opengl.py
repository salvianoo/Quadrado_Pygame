import pygame

#Pygame 
pygame.init()

# Define the colors we will use in RGB format
cor_fundo = [238, 210, 238]# Set the height and width of the screen
hot_pink = [205,105,201]

size=[800,400]

screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("Elaine Aires - QUADRADO CG")

#Loop until the user clicks the close button.
done=False
clock = pygame.time.Clock()
rect_x = 50

while done==False:

	clock.tick(10)     

	for event in pygame.event.get(): # User did something
		if event.type == pygame.QUIT: # If user clicked close
			done=True # Flag that we are done so we exit this loop
	
	# Clear the screen and set the screen background
	screen.fill(cor_fundo)
	
	# Draw a rectangle
	pygame.draw.rect(screen,hot_pink,[rect_x, 50, 50, 50])
	rect_x += 3
	# Go ahead and update the screen with what we've drawn.
    # This MUST happen after all the other drawing commands.
	pygame.display.flip()
	
pygame.quit ()