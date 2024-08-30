from random import randint

from HumanMoveTest.rt_with_exceptions import Runner
import logging
from unittest import TestCase


class RunnerTest(TestCase):

    def test_walk(self):
        try:
            runner = Runner(name='Вяся', speed=-5)
            logging.info('"test_walk" выполнен успешно!')
        except ValueError:
            logging.warning('Неверная скорость для Runner', exc_info=True)
        else:
            for _ in range(10):
                runner.walk()

            self.assertEqual(runner.distance, 50)

    def test_run(self):
        try:
            runner = Runner(name='123')
            logging.info('"test_run" выполнен успешно')
        except ValueError as e:
            logging.warning('Неверный тип данных для объекта Runner', exc_info=True)
        else:
            for _ in range(10):
                runner.run()

            self.assertEqual(runner.distance, 100)

    def test_challenge(self):
        runner_1 = Runner(name='Вяся', speed=5)
        runner_2 = Runner(name='Петя', speed=10)

        for _ in range(randint(10, 20)):
            runner_1.run()
            runner_1.walk()

        for _ in range(randint(10, 20)):
            runner_2.run()
            runner_2.walk()

        self.assertNotEqual(runner_1.distance, runner_2.distance)


# if '__main__' == __name__:
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    filename='runner_tests.log', filemode='a', encoding='utf-8')
