''' Classes for Event Manager '''

class Player(object):
    def __init__(self, name, username):
        self.name = name
        self.username = username
    def __str__(self):
        return self.username


class Table(object): 
    def __init__(self, seats):
        self.seats = seats
        self.players = []
    def add_player(self, player):
        if len(self.players) < self.seats:
            if player not in self.players:
                self.players.append(player)
            else:
                print("Player {} already at table".format(str(player))
        else:
            print("This table is full.")
            #raise FullTable
    def remove_player(self, player):
        if player in self.players:
            self.players.remove(player)
        else:
            print("Player {} not at table".format(str(player))
    def remaining_seats(self):
        return self.seats - len(self.players)
    def print_players(self):
        return [str(x) for x in self.players]
