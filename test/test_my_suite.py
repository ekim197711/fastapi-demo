import unittest

from test.hero.test_hero import TestHeroWithSkill


def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestHeroWithSkill))
    # Add more test cases to the suite here
    return suite


if __name__ == "__main__":
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite())
