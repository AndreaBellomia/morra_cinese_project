


class GameApp():
    ''' Class to determine victory in a game of "Morra Cinese" '''

    # definition of winning conditions
    winn_condition = [
        ['Paper', 'Rock'],
        ['Rock', 'Scissor'],
        ['Scissor', 'Paper'],
    ]

    # definition of lost conditions
    lost_condition = [
        ['Rock', 'Paper'],
        ['Scissor', 'Rock'],
        ['Paper', 'Scissor'],
    ]

    # definition of break-even conditions
    tie_condition = [
        ['Rock', 'Rock'],
        ['Paper', 'Paper'],
        ['Scissor', 'Scissor'],
    ]


    def __init__(self, player, computer, conversion):
        self.player = player
        self.computer = computer
        self.conversion = conversion

        """
        Templater for convert a input in programm variable

        conversion = {
            'player': 'Rock',
            'player': 'Paper',
            'player': 'Scissor',
            'computer': 'Rock',
            'computer': 'Paper',
            'computer': 'Scissor',
        }
        """
    
    def get_win(self):
        """  Script to determine the result """
        
        #Winn
        for item in self.winn_condition:
            if self.conversion[self.player] == item[0] and self.conversion[self.computer] == item[1]:
                return 1
        #Lost
        for item in self.lost_condition:
            if self.conversion[self.player] == item[0] and self.conversion[self.computer] == item[1]:
                return 0

        #Tie  
        for item in self.tie_condition:
            if self.conversion[self.player] == item[0] and self.conversion[self.computer] == item[1]:
                return 2
    
