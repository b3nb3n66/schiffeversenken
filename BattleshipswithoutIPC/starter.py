import pygame                                                                                                           #pygame is imported

pygame.init()                                                                                                           #initiate pygame
pygame.font.init()                                                                                                      #loading the ability to display fonts in pygame
pygame.display.set_caption("Schiffeversenken")                                                                          #the caption of the window will show "Schiffe versenken"
headline = pygame.font.SysFont("futura", 50)                                                                            #setting and saving the font for headlines in a variable
welcometexter = pygame.font.SysFont("brushscript", 80)                                                                  #setting and saving another font plus size of the font in a var
continuequit = pygame.font.SysFont("futura", 30)                                                                        #setting and saving another font plus size of the font in a var


                                                                                                                        #global variables
Square = 35                                                                                                             #square sizes will be 35

Width = Square * 10 * 2 + Square                                                                                        #the width will be wider than twice the grid (being 10 squares wide), so that there is still some distance between the grids and both grids are fully visible
Height = Square * 10 * 2 + Square                                                                                       #the height will be wider than twice the grid (being 10 squares wide), so that there is still some distance between the grids and both grids are fully visible
Window = pygame.display.set_mode((Width, Height))                                                                       #the actual windowsize attributes are stored

                                                                                                                        #colors
Black = (30, 30, 30)                                                                                                    #lightBlack is setup
Green = (40, 200, 50)                                                                                                   #Green is setup
Red = (250, 50, 50)                                                                                                     #Red is setup



def Startscreen():                                                                                                      #this function shows the Startingscreen to the Players, where they choose between small and normal Game
    starting = True                                                                                                     #variable starting is set to be True
    while starting:                                                                                                     #while starting is true
        for event in pygame.event.get():                                                                                #in case an user event is occuring capture that event
            if event.type == pygame.QUIT:                                                                               #if the event is the clicking on the close button...
                pygame.quit()                                                                                           #quit Pygame
                quit()                                                                                                  #quit the execution of the program
            if event.type == pygame.KEYDOWN:                                                                            #in case an key is pushed..
                if event.key == pygame.K_ESCAPE:                                                                        #...and the key is the "Esc" key...
                    pygame.quit()                                                                                       #quit Pygame
                    quit()                                                                                              #quit the execution of the program
                if event.key == pygame.K_s:                                                                             #...and the key is the "s" key...
                    from mainsmall import Gamesmall                                                                     #import the smaller game version
                    starting = False                                                                                    #set Starting to False
                    Gamesmall()                                                                                         #execute the smaller game version
                if event.key == pygame.K_n:                                                                             #...and the key is the "n" key...
                    from main import Game                                                                               #import the normal sized game version
                    starting = False                                                                                    #set starting to False
                    Game()                                                                                              #execute the nomal sized game version
        Window.fill(Black)                                                                                              #fill the Window Background in said Color

        welcometext = "Welcome to Battleships!"                                                                         #text is stored in variable
        welcometextbox = welcometexter.render(welcometext, False, Red)                                                  #the str stored in var welcometext is renderd
        Window.blit(welcometextbox, (Width // 2 - 300, Height // 2 - 200))                                              #the location is set and blitted to the screen

        textstart = "Get ready Player 1:"                                                                               #text is stored in variable
        textboxstart = headline.render(textstart, False, Green)                                                         #the str stored in var textstart is renderd
        Window.blit(textboxstart, (Width // 2 - 240, Height // 2 - 50))                                                 #the location is set and blitted to the screen

        textsmallnormal = "Press S to start Small or N to Start Normal"                                                 #text is stored in variable
        textboxcontinue = continuequit.render(textsmallnormal, False, Black, Green)                                     #the str stored in var textsmallnormal is renderd
        Window.blit(textboxcontinue, (Width // 2 - 290, Height // 2 + 50))                                              #the location is set and blitted to the screen
        pygame.display.update()                                                                                         #display is updated

Startscreen()                                                                                                           #method Startscreen is executed










