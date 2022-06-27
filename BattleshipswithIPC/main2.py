if i in self.player.indexes:
    shot_result = "Hit"
    for ship in self.player.ships:                                                                                      # now we are checking if the opponents ship has been hit totally or just partial, therefore if it is sunk or not
        shot_result = "Sunk"
        sunk = True                                                                                                     # first we set var sunk to true in case the ships has been hit totally
        for i in ship.indexes:                                                                                          # checking if there is still one or more positions of the ship is set as "Grid"
            if self.player.search[i] == "Grid":  # if so...
                shot_result = "Hit"
                sunk = False                                                                                            # ...var sunk will be set to False again
                break
        if sunk:                                                                                                        # but if there are no more positions of the ship indicating "Grid"...
            for i in ship.indexes:                                                                                      # every position of the ship on the grid...
                self.player.search[i] = "Sunk"

else:
    shot_result = "Miss"
    self.player_turn = not self.player_turn

    gameover = True                                                                                                     # here we check if the game is over / all ships of the inactive player have been sunk
    for i in self.player.indexes:                                                                                       # every index of the inactive players ships will be looked at
        if self.player.search[i] == "Grid":                                                                             # if there is one or more indexes of the ships stored as "Grid"...
            gameover = False                                                                                            # ... var game_over is set to False
    self.over = gameover


# send result
if (int(sys.argv[1]) == 1):
    self.game_socket.send_message_to_client("Shot-impact", shot_result)
if (int(sys.argv[1]) == 2):
    self.game_socket.send_message_to_server("Shot-impact", shot_result)