from random import randint
from unittest import TestCase
from HumanMoveTest.runner import Runner


class RunnerTest(TestCase):
    def test_walk(self):
        runner = Runner(name='Вяся')
        for _ in range(10):
            runner.walk()

        self.assertEqual(runner.distance,50)

    def test_run(self):
        runner = Runner(name='Вяся')
        for _ in range(10):
            runner.run()

        self.assertEqual(runner.distance, 100)

    def test_challenge(self):
        runner_1 = Runner(name='Вяся')
        runner_2 = Runner(name='Петя')

        for _ in range(randint(10, 20)):
            runner_1.run()
            runner_1.walk()

        for _ in range(randint(10, 20)):
            runner_2.run()
            runner_2.walk()

        self.assertNotEqual(runner_1.distance, runner_2.distance)
