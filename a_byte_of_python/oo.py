class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hi(self):
        print('Hello, my name is', self.name)


person = Person('Sun Jinbo', 20)
print(person)
person.say_hi()


class Robot:
    poplulation = 0

    def __init__(self, name):
        self.name = name
        print("(Initializing {})".format(self.name))
        Robot.poplulation += 1

    def die(self):
        print("({} is died!)".format(self.name))
        Robot.poplulation -= 1
        if (Robot.poplulation == 0):
            print("({} was the last one.)".format(self.name))
        else:
            print("There are still {:d} robots working.".format(Robot.poplulation))

    def say_hi(self):
        print("Greetings, my masters call me {}.".format(self.name))

    @classmethod
    def hom_many_robots(cls):
        print("We have {:d} robots.".format(cls.poplulation))


droid1 = Robot("R2-D2")
droid1.say_hi()
Robot.hom_many_robots()

droid2 = Robot("C1-3P")
droid2.say_hi()
Robot.hom_many_robots()

droid1.die()
droid2.die()

Robot.hom_many_robots()


class Teacher(Person):
    def __init__(self, name, age, salary):
        Person.__init__(self, name, age)
        self.salary = salary

    def tell(self):
        print('Salary: {:d}'.format(self.salary))


teacher = Teacher('Tom', 29, 15000)
teacher.say_hi()
teacher.tell()

