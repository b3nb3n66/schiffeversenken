import random                                                                                                           #random funtion is imported here
import sys
from NetCom import Communication

class Ship:                                                                                                        #Ship Class starts here

    def __init__(self, size):                                                                                           #init function to instantiate objects of that class
        self.row = random.choice([0,1,2,3,4,5,6,7,8,9])                                                                         #random number out of 0 - 5 as a starting point of the ship regaring the row (we come to this later again)
        self.col = random.choice([0,1,2,3,4,5,6,7,8,9])                                                                         #random number out of 0 - 5 as a starting point of the ship regaring the column (we come to this later again)
        self.size = size                                                                                                #size of the individual ship
        self.orientation = random.choice(["Horizontal", "Vertical"])                                                    #random choice between "horizontal" orientation and "vertical" orientation of the ships (we come to this later again)
        self.indexes = self.indexcalculation()                                                                      #storage of all indexes on the board the ship occupys, using another method to calculate the indexes

    def indexcalculation(self):                                                                                    #assistent method to calculate the indexes of the ship
        start_index = self.row * 10 + self.col                                                                           #the starting point of the ship are calculated here
        if self.orientation == "Horizontal":                                                                            #when the choice has been set to "horizontal"...
            return [start_index + i for i in range(self.size)]                                                          #... the ships index will be set from left to right, starting with the start_index with the length of the ship
        elif self.orientation == "Vertical":                                                                            #for the orientation choice of "vertical"...
            return [start_index + i * 10 for i in range(self.size)]                                                      #... the ships index will be set from top to bottom (multiplied by ten to be exactly on the field below the one before on the grid) with the length of the ship


class Player:                                                                                                      #Player Class starts here
    def __init__(self, placeships):                                                                                                 #init function to instantiate objects of that class
        self.ships = []                                                                                                 #every player has a list with ships in it
        self.search = ["Grid" for i in range(100)]                                                                       #search is a list of strings which represents the grids squares from 0 to 35 (top left to bottom right) / "Grid" as standard if no shot has been fired at field
        if placeships:
            self.placeships(sizes=[5, 4, 4, 3, 2])                                                                           #ship sizes and amount are stored in a list
            list_of_ships = [ship.indexes for ship in self.ships]                                                           #here the indexes of the ships are stored from the ship class, to make them accessable in the player class
            self.indexes = [index for sublist in list_of_ships for index in sublist]                                        #an actual property for the indexes of the ships is created in the player class. In the brackets we are accessing every index in each sublist (the different ships) in the list of ships -> the list of ships is now a flat list without any sublists

    def placeships(self, sizes):                                                                                   #function to place the ships
        for size in sizes:                                                                                              #we are going through all "ships" in the sizes list
            placed = False                                                                                              #var is set as False until all the ships have been placed
            while not placed:                                                                                           #as long as placed is still False enter the while loop

                ship = Ship(size)                                                                                  #create a new ship using the sizes from the list sizes starting with the first in the list
                                                                                                                        #the check if placement is possible starts here
                possible = True                                                                                         #var possible is set as possible as a standard

                for i in ship.indexes:                                                                                  #in this loop we are checking all possibilites for which the placment is NOT possible - looping through all indexes of the ship that wants to be placed
                    if i >= 100:                                                                                         #first check: when the ships index is higher than 35...
                        possible = False                                                                                #the placement is not possible as Grid reaches from 0 to 35
                        break
                                                                                                                        #we are checking now if the ship is set in a straight line, so that ships are not set with an angle or equaly
                    newrow = i // 10                                                                                     #new variable to compare the next row index with the index of the start row
                    newcol = i % 10                                                                                      #new variable to compare the next column index with the index of the start column
                    if newrow != ship.row and newcol != ship.col:                                                       #when the new row index is not equal to the start row index AND the new column index is not equal to the start column index...
                        possible = False                                                                                #... then something is wrong, and its not possible to place the ship
                        break

                    for othership in self.ships:                                                                        #check if ships collide with eachother
                        if i in othership.indexes:                                                                      #in case one index of the placed ship is already part of another placed ships index...
                            possible = False                                                                            #... var possible will be set to false and a new try need to be done
                            break

                if possible:                                                                                            #in case all prior checks are succesfully passed...
                    self.ships.append(ship)                                                                             #... the ship will be added to the list ships
                    placed = True                                                                                       #the ship is placed and var placed is set to true, so a new ship can be placed as long as there are still ships to be placed


class Game:                                                                                                        #Game Class starts here
                                                                                                                        #init function to instantiate objects of that class                                                                                            #player 1 is created                                                                                            #player 2 is created                                                                                                 #var for deciding which player is the active player                                                                                                      #var for Game over check                                                                                                    #var for result
    def __init__(self, player_instance):
        self.player = Player(True)
        if player_instance == 1:
            self.game_socket = Communication('server')
            self.player_turn = True  # player 1 start first
        else: # player_instance == 2
            self.game_socket = Communication('client')
            self.player_turn = False
        self.over = False
        self.result = None

    def make_move(self, i):                                                                                       #method to declare the active and inactive player plus the actual turn of a player


        if (int(sys.argv[1]) == 1):  # player 1 as server
                # send shot
            self.game_socket.send_message_to_client('shot', i)
                # receive response
            data = self.game_socket.get_message_from_client()

        if (int(sys.argv[1]) == 2):  # Player 2 as client
                # send shot
            self.game_socket.send_message_to_server('shot', i)
                # receive response
            data = self.game_socket.get_message_from_server()

        shot_result = data["content"]

        if shot_result == "Hit":
            self.player.search[i] = "Hit"

        else:
            self.player.search[i] = "Miss"
            self.player_turn = not self.player_turn
                #in the beginning of each players move there is no hit, as no shots were made

                                                                                                                        #now we are setting Hits, Misses and Sunk
    def remote_movesmall(self):
        # wait for getting the shot coordinates
        if (int(sys.argv[1])==1):
            data = self.game_socket.get_message_from_client()

        if (int(sys.argv[1])==2):
            data = self.game_socket.get_message_from_server()

        i = int(data["content"])

        # set hit "H" or miss "M"
        if i in self.player.indexes:
            shot_result = "Hit"
        else:
            shot_result = "Miss"
            self.player_turn = not self.player_turn
            # check if ship is sunk ("S")
            # not checked

            # check if game is over
            # not checked

        # send result
        if (int(sys.argv[1])==1):
            self.game_socket.send_message_to_client("Shot-impact", shot_result)
        if (int(sys.argv[1])==2):
            self.game_socket.send_message_to_server("Shot-impact", shot_result)