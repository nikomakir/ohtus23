class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.match_score1 = 0
        self.match_score2 = 0

    def won_point(self, player_name):
        if player_name == self.player1_name:
            self.match_score1 = self.match_score1 + 1
        else:
            self.match_score2 = self.match_score2 + 1

    def get_score(self):
        if self.match_score1 == self.match_score2:
            return self._tie()
        
        if self.match_score1 >= 4 or self.match_score2 >= 4:
            difference = abs(self.match_score1 - self.match_score2)
            return self._lead(difference)

        return self._early_game()
       
    def _tie(self):
        point = self.match_score1
        if point == 0:
            return "Love-All"
        elif point == 1:
            return "Fifteen-All"
        elif point == 2:
            return "Thirty-All"
        else:
            return "Deuce"
        
    def _lead(self, difference):
        if difference >= 2:
            if self.match_score1 > self.match_score2:
                return f"Win for {self.player1_name}"
            return f"Win for {self.player2_name}"
        
        if self.match_score1 > self.match_score2:
            return f"Advantage {self.player1_name}"
        return f"Advantage {self.player2_name}"

    def _early_game(self):
        score_names = {
        0 : "Love",
        1 : "Fifteen",
        2 : "Thirty",
        3 : "Forty"
        }

        return f"{score_names[self.match_score1]}-{score_names[self.match_score2]}"
