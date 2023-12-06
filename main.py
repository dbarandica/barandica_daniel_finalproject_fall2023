# This file was created by: Daniel Barandica


'''
# Sources: 
https://www.youtube.com/watch?v=7fqQt2Bwobo

'''



'''
Passions/Interests: 
- Food - In N Out

Project Title:
- Hamgurger Herder

Goals: 
- be able to herd as many items from In N Out menu as possible
- have entire menu available
- be able to import images of food 
- have a counter to count how much food is collected, one for each item, one for total
'''



import pygame
pygame.init()

background_img = pygame.image.load('menu.png')

window_length = 1000
window_height = 600
window = pygame.display.set_mode((window_length, window_height))

def draw():
    # Draw background
    window.blit(background_img,(0,0))
    
    pygame.display.update()

main = True
while main == True:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            main = False

pygame.quit()