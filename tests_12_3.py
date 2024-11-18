import runner
import unittest
import Runner_2 as runner


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_walk(self):
        name1 = runner.Runner('Lada')
        for i in range(10):
            name1.walk()
        self.assertEqual(name1.distance, 50)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_run(self):
        name2 = runner.Runner('Nikolai')
        for i in range(10):
            name2.run()
        self.assertEqual(name2.distance, 100)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_challenge(self):
        name3 = runner.Runner('Varvara')
        name4 = runner.Runner('Vladislav')
        for i in range(10):
            name3.walk()
            name4.run()
        self.assertNotEqual(name3.distance, name4.distance)

class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def setUp(self):
        self.first = runner.Runner('Усэйн', 10)
        self.second = runner.Runner('Андрей', 9)
        self.third = runner.Runner('Ник', 3)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_first_tournament(self):
        tournament = runner.Tournament(90, self.first, self.third)
        results = tournament.start()
        self.assertTrue(results[list(results.keys())[-1]] == 'Ник')
        self.all_results['1'] = results

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_second_tournament(self):
        tournament_2 = runner.Tournament(90, self.second, self.third)
        results = tournament_2.start()
        self.assertTrue(results[list(results.keys())[-1]] == 'Ник')
        self.all_results['2'] = results

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_third_tournament(self):
        tournament_3 = runner.Tournament(90, self.first, self.second, self.third)
        results = tournament_3.start()
        self.assertTrue(results[list(results.keys())[-1]] == 'Ник')
        self.all_results['3'] = results

    @classmethod
    def tearDownClass(cls):
        for test_key, test_value in cls.all_results.items():
            print(f'Test {test_key}:')
            for key, value in test_value.items():
                print(f'\t{key}: {value}')


if __name__ == "__main__":
    unittest.main()