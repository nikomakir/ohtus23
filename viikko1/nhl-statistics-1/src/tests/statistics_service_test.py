import unittest
from statistics_service import StatisticsService
from player import Player
from enum import Enum


class SortBy(Enum):
    POINTS = 1
    GOALS = 2
    ASSISTS = 3

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_search_returns_player(self):
        result = self.stats.search("Kurri")
        self.assertEqual(result, self.stats._players[2])

    def test_search_returns_nothing_if_player_not_found(self):
        self.assertIsNone(self.stats.search("Paavo"))

    def test_team_returns_correct_list_of_players(self):
        players_in_team = self.stats.team("PIT")
        self.assertEqual(players_in_team[0], self.stats._players[1])

    def test_top_points_returns_correct_list(self):
        self.assertEqual(self.stats.top(1)[0], self.stats._players[4])

    def test_top_goals_returns_correct_list(self):
        top_player = self.stats.top(1, SortBy.GOALS)
        self.assertEqual(top_player[0], self.stats._players[1])

    def test_top_assists_returns_correct_list(self):
        top_player = self.stats.top(1, SortBy.ASSISTS)
        self.assertEqual(top_player[0], self.stats._players[4])
