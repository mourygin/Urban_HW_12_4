# coding UNF-8
import unittest
import runner_and_tournament
import  logging


def get_last_runner(a_dict):
    race_keys = list(a_dict.keys())
    last_runner_key = max(race_keys)
    last_runner_name = a_dict[last_runner_key]
    return last_runner_name
class TournamentTest(unittest.TestCase):
    is_frozen = True
    @classmethod
    def setUpClass(self):
        hussein = None
        andrew = None
        nick = None
        TournamentTest.all_results = []

    def setUp(self): # метод, где создаются 3 объекта:Усэйн (10), Андрей (9) и Ник (3)
        global hussein, andrew, nick, all_results
        hussein = runner_and_tournament.Runner('hussein',10)
        andrew = runner_and_tournament.Runner('andrew',9)
        nick = runner_and_tournament.Runner('nick',3)

    @classmethod
    def tearDownClass(self): # выводятся all_results по очереди в столбец
        global all_results
        for i in TournamentTest.all_results:
            print(i)
    @unittest.skipIf(is_frozen,'Соревнавания еще не начались. Этап регистрации участников.')
    def test_race_1(self):
        global hussein, andrew, nick, all_results, is_frozen
        print('is_frozen =', TournamentTest.is_frozen)
        race_h_n = runner_and_tournament.Tournament(90, hussein, nick)
        race_result = race_h_n.start()
        last_runner_name = get_last_runner(race_result)
        TournamentTest.all_results.append(race_result)
        self.assertTrue(race_h_n.turtle == last_runner_name)

    @unittest.skipIf(is_frozen, 'Соревнавания еще не начались. Этап регистрации участников.')
    def test_race_2(self):
        global hussein, andrew, nick, all_results
        race_a_n = runner_and_tournament.Tournament(90, andrew, nick)
        race_result = race_a_n.start()
        last_runner_name = get_last_runner(race_result)
        TournamentTest.all_results.append(race_result)
        self.assertTrue(race_a_n.turtle == last_runner_name)

    @unittest.skipIf(is_frozen, 'Соревнавания еще не начались. Этап регистрации участников.')
    def test_race_3(self):
        global hussein, andrew, nick, all_results
        race_h_a_n = runner_and_tournament.Tournament(90, hussein, andrew, nick)
        race_result = race_h_a_n.start()
        last_runner_name = get_last_runner(race_result)
        TournamentTest.all_results.append(race_result)
        self.assertTrue(race_h_a_n.turtle == last_runner_name)

class RunnerTest(unittest.TestCase):
    is_frozen = False
    @classmethod
    def setUpClass(self):
        RunnerTest.is_frozen = False
        logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_tests.log', encoding='utf-8', format="%(asctime)s | %(levelname)s, %(message)s")


    @unittest.skipIf(is_frozen, 'Соревнавания еще не начались. Этап регистрации участников.')
    def test_walker(self):
        # correct
        try:
            mr_walker = runner_and_tournament.Runner(name='jonnie_walker',speed=2)
            mr_walker.walk()
            mr_walker.walk()
            self.assertEqual(mr_walker.distance,4)
            logging.info('"test_walk" выполнен успешно')
        except Exception as exc:
            logging.warning('Неверная скорость для Walker', exc_info=True)
        # correct speed
        try:
            mr_walker_2 = runner_and_tournament.Runner(name='jonnie_walker', speed=-2)
            mr_walker_2.walk()
            mr_walker_2.walk()
            self.assertEqual(mr_walker_2.distance, 4)
            logging.info('"test_walk" выполнен успешно')
        except Exception as exc:
            logging.warning('Неверная скорость для Walker', exc_info=True)
        # correct name
        try:
            mr_walker_3 = runner_and_tournament.Runner(name=['jonnie_walker'], speed=2)
            mr_walker_3.walk()
            mr_walker_3.walk()
            self.assertEqual(mr_walker_3.distance, 4)
            logging.info('"test_walk" выполнен успешно')
        except Exception as exc:
            logging.warning('Неверная скорость для Walker', exc_info=True)

    @unittest.skipIf(is_frozen, 'Соревнавания еще не начались. Этап регистрации участников.')
    def test_runner(self):
        try:
            # mr_runner = runner_and_tournament.Runner(name='jonnie_runner', speed=2)
            mr_runner = runner_and_tournament.Runner(name='jonnie_runner', speed=2)
            mr_runner.run()
            mr_runner.run()
            self.assertEqual(mr_runner.distance, 8)
            logging.info('"test_run" выполнен успешно')
        except Exception as exc:
            logging.warning('Неверный тип данных для объекта Runner', exc_info=True)
            return