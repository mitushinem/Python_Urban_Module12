from HumanMoveTest.runner_and_tournament import Runner, Tournament
from unittest import TestCase


class TournamentTest(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = []

    def setUp(self):
        self.runner_1 = Runner('Усэйн', 10)
        self.runner_2 = Runner('Андрей', 9)
        self.runner_3 = Runner('Ник', 3)

    def test_race_1(self):
        tournament = Tournament(90, self.runner_1, self.runner_3)
        self.all_results.append(tournament.start())
        self.assertTrue(self.all_results[-1][1] == 'Усэйн')

    def test_race_2(self):
        tournament = Tournament(90, self.runner_2, self.runner_3)
        self.all_results.append(tournament.start())
        self.assertTrue(self.all_results[-1][1] == 'Андрей')

    def test_race_3(self):
        tournament = Tournament(90, self.runner_1, self.runner_2, self.runner_3)
        self.all_results.append(tournament.start())
        self.assertTrue(self.all_results[-1][3] == 'Ник')

    @classmethod
    def tearDownClass(cls):
        for res in cls.all_results:
            print(res)
