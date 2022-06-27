from Schiffe_versenken import Game                                                                                      #the class Gamesmall is imported from the file schiffe versenkensmall
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
Width = Square * 10 * 2 + Square                                                                                         #the width will be wider than twice the grid (being 6 squares wide), so that there is still some distance between the grids and both grids are fully visable
Height = Square * 10 * 2 + Square                                                                                        #the height will be higher than twice the grid (being 6 squares high), so that there is still some distance between the grids and both grids are fully visable
Window = pygame.display.set_mode((Width, Height))                                                                       #the actual windowsize attributes are stored

                                                                                                                        #for visual differance
Black = (30, 30, 30)                                                                                                    #black is set up
Green = (40, 200, 50)                                                                                                   #green is set up
Grey = (90, 80, 80)                                                                                                     #a darker grey is set up
Blue = (50, 100, 200)                                                                                                   #blue is set up
Orange = (255, 120, 0)                                                                                                  #orange is set up
Red = (250, 50, 50)                                                                                                     #red is set up
AssignColors = {"Grid": Black, "Miss": Blue, "Hit": Orange, "Sunk": Red}                                                #in this list variables are attatche to strings


def gridcreation(player, left=0, top=0, search=False):                                                                  #the grid is drawn in the following lines
    for i in range(100):                                                                                                #every number from 0 to 35 will be called up in this for loop
        x = left + i % 10 * Square                                                                                      #the startpoint for the rectangle on the x axis is calculated
        y = top + i // 10 * Square                                                                                      #the startpoint for the rectangle on the y axis is calculated
        field = pygame.Rect(x, y, Square, Square)                                                                       #the individual field of the grid is stored with its startingpoints (x/y axis) and the lengst in x an y direction
        pygame.draw.rect(Window, Green, field, width=1)                                                                 #the individual rectangle is drawn on the window
        if search:
            x += Square // 2                                                                                            #the start location of the circles (Hit, Miss and Sunk) on the x axis is centered to the field it is supposed t be in
            y += Square // 2                                                                                            #the start location of the circles (Hit, Miss and Sunk) on the y axis is centered to the field it is supposed t be in
            pygame.draw.circle(Window, AssignColors[player.search[i]], (x, y), radius=Square // 2)                      #the circles are drawn with the pygame.draw function


def drawships(player, left=0, top=0):                                                                                   #this is a function that draws the players ships on the grid
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


game = Game(int(sys.argv[1]))                                                                                           #the actual game starts here

animating = True
pausing = False
game.over = False
re_draw_done = False


while animating:
    # track user interaction
    for event in pygame.event.get():
        # user stops playing and closing the game
        if event.type == pygame.QUIT:
            animating = False

        # user clicks on mouse
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            # if player to shot .. he wil send the shot coordinate and  wait for the result
            if not game.over and game.player_turn and x < 10 * Square and y < 10 * Square:
                row = y // Square
                col = x // Square
                index = row * 10 + col
                game.make_move(index)
                re_draw_done = False

        # if player to receive the shot ... he will wait for the shot coordinates and send the shot result back
        if not game.player_turn and re_draw_done:
            # wait to receive the shot coordinates
            # send the response
            game.remote_movesmall()

        # user presses key on keyboard
        if event.type == pygame.KEYDOWN:
            # escape to close the animation
            if event.key == pygame.K_ESCAPE:
                animating = False
            # space to pause and unpause animation
            if event.key == pygame.K_SPACE:
                pausing = not pausing

            # return key to restart
            if event.key == pygame.K_RETURN:
                game = Game()

        # execution
        if not pausing:
            # draw background
            Window.fill(Black)

            # draw search grids
            gridcreation(game.player, search=True)
            gridcreation(game.player, left=(Width - Square) // 2 + Square, top=(Height - Square) // 2 + Square)
            drawships(game.player, left=(Width - Square) // 2 + Square, top=(Height - Square) // 2 + Square)

            if game.player_turn and not game.over:
                text = "<- your turn!"
                textbox = Playerturntext.render(text, False, Grey, Green)
                Window.blit(textbox, (Width // 2 + 10, Height // 2 - 200))
                text = "Your Ships ->"
                textbox = Playerturntext.render(text, False, Grey, Green)
                Window.blit(textbox, (Width // 2 - 150, Height // 2 + 100))

            elif not game.player_turn and not game.over:
                text = "Opponent will shoot now!"
                textbox = Playerturntext.render(text, False, Grey, Green)
                Window.blit(textbox, (Width // 2 - 1, Height // 2 - 200))
                text = "Your Ships -->"
                textbox = Playerturntext.render(text, False, Grey, Green)
                Window.blit(textbox, (Width // 2 - 150, Height // 2 + 100))

            re_draw_done = True

            # game over indication
            if game.over:
                # draw ships when game is over
                drawships(game.player1, left=(Width - Height) // 2 + Height,
                          top=(Height - Square) // 2 + Square)
                drawships(game.player2)

                text = "Player" + str(game.result) + " wins!"
                textbox = headline.render(text, False, Grey, Green)
                Window.blit(textbox, (Width // 2 - 200, Height // 2 - 50))

                textstartagain = "Press Enter to start again"
                textboxstartagain = continuequit.render(textstartagain, False, Grey, Green)
                Window.blit(textboxstartagain, (Width // 2 - 190, Height // 2 + 50))
                pygame.display.update()


            # update screen
            pygame.display.flip()
