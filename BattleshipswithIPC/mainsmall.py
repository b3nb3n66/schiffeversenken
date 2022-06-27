from Schiffe_versenkensmall import Gamesmall                                                                            #the class Gamesmall is imported from the file schiffe versenkensmall
import sys
import pygame                                                                                                           #pygame is imported

pygame.init()                                                                                                           #initiate pygame
pygame.font.init()                                                                                                      #loading the ability to display fonts in pygame
pygame.display.set_caption("Schiffe versenken")                                                                         #the caption of the window will show "Schiffe versenken"
headline = pygame.font.SysFont("futura", 30)                                                                            #setting and saving the font for headlines in a variable
Playerturntext = pygame.font.SysFont("futura", 20)                                                                      #setting and saving another font plus size of the font in a var
continuequit = pygame.font.SysFont("futura", 20)                                                                        #setting and saving yet another font plus size of the font in a var

                                                                                                                        #setting some global variables for the grids and size of the window etc.
Square = 35                                                                                                             #square sizes will be 35
SmallerShips = 10                                                                                                       #ships will apear smaller in the grid

                                                                                                                        #Setting the opening Windows size
Width = Square * 6 * 2 + Square                                                                                         #the width will be wider than twice the grid (being 6 squares wide), so that there is still some distance between the grids and both grids are fully visable
Height = Square * 6 * 2 + Square                                                                                        #the height will be higher than twice the grid (being 6 squares high), so that there is still some distance between the grids and both grids are fully visable
Window = pygame.display.set_mode((Width, Height))                                                                       #the actual windowsize attributes are stored

                                                                                                                        #for visual differance
Black = (30, 30, 30)                                                                                                    #black is set up
Green = (40, 200, 50)                                                                                                   #green is set up
Grey = (90, 80, 80)                                                                                                     #a darker grey is set up
Blue = (50, 100, 200)                                                                                                   #blue is set up
Orange = (255, 120, 0)                                                                                                  #orange is set up
Red = (250, 50, 50)                                                                                                     #red is set up
AssignColors = {"Grid": Black, "Miss": Blue, "Hit": Orange, "Sunk": Red}                                                #in this list variables are attatche to strings


def gridcreation(player, left=0, top=0, search=False):                                                                                #the grid is drawn in the following lines
    for i in range(36):                                                                                                 #every number from 0 to 35 will be called up in this for loop
        x = left + i % 6 * Square                                                                                       #the startpoint for the rectangle on the x axis is calculated
        y = top + i // 6 * Square                                                                                       #the startpoint for the rectangle on the y axis is calculated
        field = pygame.Rect(x, y, Square, Square)                                                                       #the individual field of the grid is stored with its startingpoints (x/y axis) and the lengst in x an y direction
        pygame.draw.rect(Window, Green, field, width=1)                                                                 #the individual rectangle is drawn on the window
        if search:
            x += Square // 2                                                                                                #the start location of the circles (Hit, Miss and Sunk) on the x axis is centered to the field it is supposed t be in
            y += Square // 2                                                                                                #the start location of the circles (Hit, Miss and Sunk) on the y axis is centered to the field it is supposed t be in
            pygame.draw.circle(Window, AssignColors[player.search[i]], (x, y), radius=Square // 2)                          #the circles are drawn with the pygame.draw function


def drawshipssmall(player, left=0, top=0):                                                                              #this is a function that draws the players ships on the grid
    for ship in player.ships:                                                                                           #every ship of the player is called
        x = left + ship.col * Square + SmallerShips                                                                     #start point on x axis + a deepening to let the ships be smaller than the flieds on the grid
        y = top + ship.row * Square + SmallerShips                                                                      #start point on y axis + deepening to let the ships be smaller than the flieds on the grid
        if ship.orientation == "Horizontal":                                                                            #for the horizontal orientation:
            width = ship.size * Square - 2 * SmallerShips                                                               #the width of the ship is indented by twice the smallerships to once cover the indet above and to indet this side of the ship too
            height = Square - 2 * SmallerShips                                                                          #the height is equal the Square Size minus again twice the smallerships (same reason as with the width)
        else:                                                                                                           #for the other orientation (vertical):
            width = Square - 2 * SmallerShips                                                                           #width and height is set the other way round as with the horizontal orientation
            height = ship.size * Square - 2 * SmallerShips
        rectangle = pygame.Rect(x, y, width, height)                                                                    #the actual rectangle attributes are stored
        pygame.draw.rect(Window, Grey, rectangle, border_radius=3)                                                      #the actual ship is drawn with the pygame.draw function in grey as an ectangle with rounded edges


                                                                                    #display is updated by pygame


gamesmall = Gamesmall(int(sys.argv[1]))                                                                                                 #the actual game starts here

animating = True
pausing = False
gamesmall.over = False
re_draw_done = False


while animating:                                                                                                        #the pygame loop starts
    # track user interaction                                                                                            #in case an user event is occuring capture that event
    for event in pygame.event.get():                                                                                    #if the event is the clicking on the close button...
        # user stops playing and closing the game                                                                       #..set animating to False
        if event.type == pygame.QUIT:                                                                                   #if the event is a click on the mouse
            animating = False                                                                                           #capture the accurate position on the window
                                                                                                                        #as long the game is not over and player one is the active player and the click was within the grid in the top left corner...
        # user clicks on mouse                                                                                          #...divide the row position by the var square so the position matches the grid in the range 0-35...
        if event.type == pygame.MOUSEBUTTONDOWN:                                                                        #...and divide the column position by the var square so the position matches the grid in the range 0-35...
            x, y = pygame.mouse.get_pos()                                                                               #...this is now stored as the actual index which represents the grid, we are working with in this programm
            # if player to shot .. he wil send the shot coordinate and  wait for the result                             #the position is now stored to the players index
            if not gamesmall.over and gamesmall.player_turn and x < 6 * Square and y < 6 * Square:                      #the switchplayer function is called
                row = y // Square                                                                                       #as long the game is not over and player two is the active player and the click was within the grid in the bottom right corner...
                col = x // Square                                                                                       #...divide the row position(in the bottom right grid) by the var square so the position matches the grid in the range 0-35...
                index = row * 6 + col                                                                                   #...and divide the column position(in the bottom right grid) by the var square so the position matches the grid in the range 0-35...
                gamesmall.make_movesmall(index)                                                                         #...this is now stored as the actual index which represents the grid, we are working with in this programm
                re_draw_done = False                                                                                    #the position is now stored to the players index
                                                                                                                        #the switchplayer function is called
        # if player to receive the shot ... he will wait for the shot coordinates and send the shot result back         #if the event is a pressed key...
        if not gamesmall.player_turn and re_draw_done:                                                                  #...and the key is the "Esc" key...
            # wait to receive the shot coordinates                                                                      #...set animating to False
            # send the response                                                                                         #if the "Enter" key is pressed...
            gamesmall.remote_movesmall()                                                                                #...restart game
                                                                                                                        #in case an event accured prior that set animating to false, the loop stops here and the pygame window closes
        # user presses key on keyboard                                                                                  #the background of the pygame window is filled with black color
        if event.type == pygame.KEYDOWN:                                                                                #the grid/Battlefield for player one is drawn with the indexes of the ships of player two (which are invisible at this point of time)
            # escape to close the animation                                                                             #the grid/Battlefield for player two is drawn with the indexes of the ships of player one (which are invisible at this point of time)
            if event.key == pygame.K_ESCAPE:
                animating = False
            # space to pause and unpause animation
            if event.key == pygame.K_SPACE:
                pausing = not pausing

            # return key to restart
            if event.key == pygame.K_RETURN:
                gamesmall = Gamesmall()


        # execution
        if not pausing:
            # draw background
            Window.fill(Black)

            # draw search grids
            gridcreation(gamesmall.player, search=True)
            gridcreation(gamesmall.player, left=(Width - Square) // 2 + Square, top=(Height - Square) // 2 + Square)
            drawshipssmall(gamesmall.player, left=(Width - Square) // 2 + Square, top=(Height - Square) // 2 + Square)

            if gamesmall.player_turn and not gamesmall.over:
                text = "<- your turn!"
                textbox = Playerturntext.render(text, False, Grey, Green)
                Window.blit(textbox, (Width // 2 + 10, Height // 2 - 200))

                text = "Your Ships ->"
                textbox = Playerturntext.render(text, False, Grey, Green)
                Window.blit(textbox, (Width // 2 - 100, Height // 2 + 100))

            elif not gamesmall.player_turn and not gamesmall.over:
                text = "Opponent will shoot now!"
                textbox = Playerturntext.render(text, False, Grey, Green)
                Window.blit(textbox, (Width // 2 - 10, Height // 2 - 200))
                text = "Your Ships -->"
                textbox = Playerturntext.render(text, False, Grey, Green)
                Window.blit(textbox, (Width // 2 - 100, Height // 2 + 100))

            re_draw_done = True

            # game over indication
            if gamesmall.over:
                # draw ships when game is over
                drawshipssmall(gamesmall.player1, left=(Width - Height) // 2 + Height,
                           top=(Height - Square) // 2 + Square)
                drawshipssmall(gamesmall.player2)

                text = "Player" + str(gamesmall.result) + " wins!"
                textbox = headline.render(text, False, Grey, Green)
                Window.blit(textbox, (Width // 2 - 200, Height // 2 - 50))

                textstartagain = "Press Enter to start again"
                textboxstartagain = continuequit.render(textstartagain, False, Grey, Green)
                Window.blit(textboxstartagain, (Width // 2 - 190, Height // 2 + 50))
                pygame.display.update()


            # update screen
            pygame.display.flip()
