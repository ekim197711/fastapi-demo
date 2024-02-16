import unittest

from src.hero.hero import find_hero, find_real_hero, RealHero


class TestHeroWithSkill(unittest.TestCase):

    def setUp(self):
        self.main_hero = RealHero('Mike', 47)

    def tearDown(self):
        self.main_hero.say_goodbye()

    # @unittest.skip("Mike is prob wrong again")
    def test_hero_with_skill(self):
        hero: str = find_hero("shoot arrows")
        self.assertEqual('Robin Hood with skill shoot arrows', hero)

    def test_hero_is_not_uppercase(self):
        hero = find_hero("shoot arrows")
        self.assertFalse(hero.isupper())

    def test_real_hero(self):
        realhero = find_real_hero("Superman")
        realhero.introduce()
        self.assertIsNotNone(realhero)


if __name__ == '__main__':
    unittest.main()
