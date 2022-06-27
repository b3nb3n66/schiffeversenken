from Schiffe_versenken import Game                                                                                      #the class game is imported from the file schiffe versenken

import pygame                                                                                                           #pygame is imported

pygame.init()                                                                                                           #initiate pygame
pygame.font.init()                                                                                                      #loading the ability to display fonts in pygame
pygame.display.set_caption("Schiffe versenken")                                                                         #the caption of the window will show "Schiffe versenken"
headline = pygame.font.SysFont("futura", 50)                                                                            #setting and saving the font for headlines in a variable
Playerturntext = pygame.font.SysFont("futura", 30)                                                                      #setting and saving another font plus size of the font in a var
continuequit = pygame.font.SysFont("futura", 25)                                                                        #setting and saving yet another font plus size of the font in a var

                                                                                                                        #setting some global variables for the grids and size of the window etc.
Square = 35                                                                                                             #square sizes will be 35
SmallerShips = 10                                                                                                       #ships will apear smaller in the grid

                                                                                                                        #Setting the opening Windows size
Width = Square * 10 * 2 + Square                                                                                        #the width will be wider than twice the grid (being 10 squares wide), so that there is still some distance between the grids and both grids are fully visible
Height = Square * 10 * 2 + Square                                                                                       #the height will be higher than twice the grid (being 10 squares high), so that there is still some distance between the grids and both grids are fully visible
Window = pygame.display.set_mode((Width, Height))                                                                       #the actual windowsize attributes are stored

                                                                                                                        #for visual differance
Black = (30, 30, 30)                                                                                                    #black is set up
Green = (40, 200, 50)                                                                                                   #green is set up
Grey = (90, 80, 80)                                                                                                     #a darker grey is set up
Blue = (50, 100, 200)                                                                                                   #blue is set up
Orange = (255, 120, 0)                                                                                                  #orange is set up
Red = (250, 50, 50)                                                                                                     #red is set up
AssignColors = {"Grid": Black, "Miss": Blue, "Hit": Orange, "Sunk": Red}                                                #in this list variables are attatched to strings


def gridcreation(player, left=0, top=0):                                                                                #the grid is drawn in the following lines
    for i in range(100):                                                                                                #every number from 0 to 99 will be called up in this for loop
        x = left + i % 10 * Square                                                                                      #the startpoint for the rectangle on the x axis is calculated
        y = top + i // 10 * Square                                                                                      #the startpoint for the rectangle on the y axis is calculated
        field = pygame.Rect(x, y, Square, Square)                                                                       #the individual field of the grid is stored with its startingpoints (x/y axis) and the length in x and y direction
        pygame.draw.rect(Window, Green, field, width=1)                                                                 #the individual rectangle is drawn on the window
        x += Square // 2                                                                                                #the start location of the circles (Hit, Miss and Sunk) on the x axis is centered to the field it is supposed t be in
        y += Square // 2                                                                                                #the start location of the circles (Hit, Miss and Sunk) on the y axis is centered to the field it is supposed t be in
        pygame.draw.circle(Window, AssignColors[player.search[i]], (x, y), radius=Square // 2)                          #the circles are drawn with the pygame.draw function


def drawships(player, left=0, top=0):                                                                                   #this is a function that draws the players ships on the grid
    for ship in player.ships:                                                                                           #every ship of the player is called
        x = left + ship.col * Square + SmallerShips                                                                     #start point on x axis + a deepening to let the ships be smaller than the fields on the grid
        y = top + ship.row * Square + SmallerShips                                                                      #start point on y axis + deepening to let the ships be smaller than the fieldss on the grid
        if ship.orientation == "Horizontal":                                                                            #for the horizontal orientation:
            width = ship.size * Square - 2 * SmallerShips                                                               #the width of the ship is indented by twice the smallership to once cover the indent above and to indent this side of the ship too
            height = Square - 2 * SmallerShips                                                                          #the height is equal the Square Size minus again twice the smallership (same reason as with the width)
        else:                                                                                                           #for the other orientation (vertical):
            width = Square - 2 * SmallerShips                                                                           #width and height is set the other way round as with the horizontal orientation
            height = ship.size * Square - 2 * SmallerShips                                                              #"
        rectangle = pygame.Rect(x, y, width, height)                                                                    #the actual rectangle attributes are stored
        pygame.draw.rect(Window, Grey, rectangle, border_radius=3)                                                      #the actual ship is drawn with the pygame.draw function in grey as an rectangle with rounded edges


def switchplayer():                                                                                                     #the switchplayer fuction starts here
    playerswitch = True                                                                                                 #playerswitch
    while playerswitch:                                                                                                 #as long playerswitch is true enter while loop
        for event in pygame.event.get():                                                                                #in case an user event is occuring capture that event
            if event.type == pygame.QUIT:                                                                               #if the event is the clicking on the close button...
                pygame.quit()                                                                                           #...quit pygame...
                quit()                                                                                                  #...and quit the excecution of the programm
            if event.type == pygame.KEYDOWN:                                                                            #in case an key is pushed
                if event.key == pygame.K_c:                                                                             #If the pushed key is the "c" key...
                    playerswitch = False                                                                                #...set the var playerswitch to false
                elif event.key == pygame.K_q:                                                                           #otherwise if the pushed key is the "q" key...
                    pygame.quit()                                                                                       #...quit pygame...
                    quit()                                                                                              #...and quit the excecution of the programm

        if game.player1turn:                                                                                            #when player 1 is the active player
            Window.fill(Black)                                                                                          #the screen will be covered in black
            textmissed = "You missed!"                                                                                  #text is stored in a variable
            textplayer1turn = "Hand over to Player 1:"                                                                  #text is stored in a variable
            textboxplayer1turn = headline.render(textplayer1turn, False, Green, Black)                                  #the str stored in var textplayer1turn is rendered
            Window.blit(textboxplayer1turn, (Width // 2 - 300, Height // 2 - 50))                                       #the location is set and blitted to the screen
            textboxmissed = headline.render(textmissed, False, Red)                                                     #the str stored in var textboxmissed is rendered
            Window.blit(textboxmissed, (Width // 2 - 150, Height // 2 - 200))                                           #the location is set and blitted to the screen

            textnextplayercq = "Press C to continue or Q to quit"                                                       #text is stored in a variable
            textboxcontinue = continuequit.render(textnextplayercq, False, Black, Green)                                #the str stored in var textboxcontinue is rendered
            Window.blit(textboxcontinue, (Width // 2 - 200, Height // 2 + 50))                                          #the location is set and blitted to the screen
            pygame.display.update()                                                                                     #display is updated by pygame


        if not game.player1turn:                                                                                        #when player 2 is the active player
            Window.fill(Black)                                                                                          #the screen will be covered in black
            textmissed = "You missed!"                                                                                  #text is stored in a variable
            textplayer2turn = "Hand over to Player 2:"                                                                  #text is stored in a variable
            textboxplayer2turn = headline.render(textplayer2turn, False, Green, Black)                                  #the str stored in var textplayer2turn is rendered
            Window.blit(textboxplayer2turn, (Width // 2 - 300, Height // 2 - 50))                                       #the location is set and blitted to the screen
            textboxmissed = headline.render(textmissed, False, Red)                                                     #the str stored in var textboxmissed is rendered
            Window.blit(textboxmissed, (Width // 2 - 150, Height // 2 - 200))                                           #the location is set and blitted to the screen

            textpausecontinue = "Press C to continue or Q to quit"                                                      #text is stored in a variable
            textboxcontinue = continuequit.render(textpausecontinue, False, Black, Green)                               #the str stored in var textboxcontinue is rendered
            Window.blit(textboxcontinue, (Width // 2 - 200, Height // 2 + 50))                                          #the location is set and blitted to the screen
            pygame.display.update()                                                                                     #display is updated by pygame


game = Game()                                                                                                           #the actual game starts here

animating = True                                                                                                        #animating is set to true so the following loop can start
while animating:                                                                                                        #the pygame loop starts

    for event in pygame.event.get():                                                                                    #in case an user event is occuring capture that event
        if event.type == pygame.QUIT:                                                                                   #if the event is the clicking on the close button...
            animating = False                                                                                           #..set animating to False

        if event.type == pygame.MOUSEBUTTONDOWN:                                                                        #if the event is a click on the mouse
            x, y = pygame.mouse.get_pos()                                                                               #capture the accurate position on the window
            if not game.over and game.player1turn and x < 10 * Square and y < 10 * Square:                              #as long the game is not over and player one is the active player and the click was within the grid in the top left corner...
                row = y // Square                                                                                       #...divide the row position by the var square so the position matches the grid in the range 0-99...
                col = x // Square                                                                                       #...and divide the column position by the var square so the position matches the grid in the range 0-99...
                index = row * 10 + col                                                                                  #...this is now stored as the actual index which represents the grid, we are working with in this programm
                game.playerturn(index)                                                                                  #the position is now stored to the players index
                if not game.player1turn:
                    switchplayer()                                                                                      #the switchplayer function is called
            elif not game.over and not game.player1turn and x > Width - 10 * Square and y > 10 * Square + Square:       #as long the game is not over and player two is the active player and the click was within the grid in the bottom right corner...
                row = (y - Square * 10 - Square) // Square                                                              #...divide the row position(in the bottom right grid) by the var square so the position matches the grid in the range 0-99...
                col = (x - Square * 10 - Square) // Square                                                              #...and divide the column position(in the bottom right grid) by the var square so the position matches the grid in the range 0-99...
                index = row * 10 + col                                                                                  #...this is now stored as the actual index which represents the grid, we are working with in this programm
                game.playerturn(index)                                                                                  #the position is now stored to the players index
                if game.player1turn:
                    switchplayer()                                                                                      #the switchplayer function is called


        if event.type == pygame.KEYDOWN:                                                                                #if the event is a pressed key...

            if event.key == pygame.K_ESCAPE:                                                                            #...and the key is the "Esc" key...
                animating = False                                                                                       #...set animating to False

            if event.key == pygame.K_RETURN:                                                                            #if the "Enter" key is pressed...
                game = Game()                                                                                           #...restart game


        if animating:                                                                                                   #in case an event accured prior that set animating to false, the loop stops here and the pygame window closes

            Window.fill(Black)                                                                                          #the background of the pygame window is filled with black color

            gridcreation(game.player1)                                                                                  #the grid/Battlefield for player one is drawn with the indexes of the ships of player two (which are invisible at this point of time)
            gridcreation(game.player2, left=(Width - Square) // 2 + Square,                                             #the grid/Battlefield for player two is drawn with the indexes of the ships of player one (which are invisible at this point of time)
                         top=(Height - Square) // 2 + Square)

            if game.player1turn:                                                                                        #in case player one is the active player the following happens

                drawships(game.player1, left=(Width - Square) // 2 + Square,                                            #the ships of player one are drawn on the grid in the bottom right corner of the window
                          top=(Height - Square) // 2 + Square)
                textplayer1turn = "<- Player 1, your turn!"                                                             #text is stored in var
                textbox = Playerturntext.render(textplayer1turn, False, Green, Black)                                   #the str stored in var textplayer1turn is rendered
                Window.blit(textbox, (Width // 2 - 0, Height // 2 - 300))                                               #the location is set and blitted to the screen
                textyourships = "Your Ships ->"                                                                         #text is stored in var
                textbox = Playerturntext.render(textyourships, False, Green, Black)                                     #the str stored in var textyourships is rendered
                Window.blit(textbox, (Width // 2 - 200, Height // 2 + 150))                                             #the location is set and blitted to the screen


            elif not game.player1turn:                                                                                  #in case player two is the active player the following happens

                drawships(game.player2)                                                                                 #the ships of player one are drawn on the grid in the top left corner of the window
                textplayer2turn = "Player 2, your turn! ->"                                                             #text is stored in var
                textbox = Playerturntext.render(textplayer2turn, False, Green, Black)                                   #the str stored in var textplayer2turn is rendered
                Window.blit(textbox, (Width // 2 - 350, Height // 2 + 150))                                             #the location is set and blitted to the screen
                textyourships = "<- Your Ships"                                                                         #text is stored in var
                textbox = Playerturntext.render(textyourships, False, Green, Black)                                     #the str stored in var textyourships is rendered
                Window.blit(textbox, (Width // 2 - 0, Height // 2 - 300))                                               #the location is set and blitted to the screen


            if game.over:                                                                                               #in the case game.over is set true the following is happening

                drawships(game.player1, left=(Width - Square) // 2 + Square,                                            #all ships are drawn on both grids when game is over...
                          top=(Height - Square) // 2 + Square)                                                          #...first the ships of player one in the bottom right grid...
                drawships(game.player2)                                                                                 #...and now the ships of player two in the top left grid

                finalresult = "Player " + str(game.result) + " wins!"                                                   #the str with the result is stored in the var "finalresult" including the int from game.result as a string
                textbox = headline.render(finalresult, False, Red, Black)                                               #the str stored in var finalresult is rendered
                Window.blit(textbox, (Width // 2 - 200, Height // 2 - 50))                                              #the location is set and blitted to the screen

                textstartagain = "Press Enter to start again"                                                           #text is stored in var
                textboxstartagain = continuequit.render(textstartagain, False, Green, Black)                            #the str stored in var textstartagain is rendered
                Window.blit(textboxstartagain, (Width // 2 - 190, Height // 2 + 50))                                    #the location is set and blitted to the screen
                pygame.display.update()                                                                                 #display is updated

            pygame.display.flip()