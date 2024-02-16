class RealHero:
    def __init__(self, name: str, age: int):
        print("Real hero constructor")
        self.name = name
        self.age = age

    def introduce(self):
        print("I am {name} and I am {age} years".format(name=self.name, age=self.age))

    def say_goodbye(self):
        print("Goodbye my friend! My name is {}".format(self.name))


def find_hero(skill: str) -> str:
    return "Robin Hood with skill " + skill


def find_real_hero(name: str) -> RealHero:
    return RealHero(name, 40)
