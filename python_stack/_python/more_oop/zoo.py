
# Create Animal Class and three specific animal classes that inherit from Animal.


class Animal:
    def __init__(self, name, age, health=100, happiness=100):
        self.name = name
        self.age = age
        self.health = health
        self.happiness = happiness
        self.type = ''
        print("\n************************ New Animal *******************************\n")

    def display_info(self):
        # Show name, health and happiness
        print("{} is {}.".format(self.name, self.age))
        print("He is feeling {}".format(self.show_health().lower()))
        print("He is {} happy.".format(self.show_happiness().lower()))
        return self

    def speak(self):
        print("{} says hello!".format(self.name))
        return self

    def feed(self):
        self.health += 10
        self.happiness += 10
        return self

    def show_health(self):
        if self.health > 90:
            status = "Awesome!!!!"
        elif self.health > 80:
            status = "Great!"
        elif self.health > 70:
            status = "Pretty Good!"
        elif self.health > 60:
            status = "Normal"
        elif self.health > 50:
            status = "Not Well"
        elif self.health > 40:
            status = "Poor"
        elif self.health > 30:
            status = "Very Poor"
        elif self.health > 20:
            status = "Very Bad!"
        elif self.health > 10:
            status = "Horrible"
        else:
            status = "Dead!"

        return status

    def show_happiness(self):
        if self.happiness > 80:
            status = "Very"
        elif self.happiness > 60:
            status = "Mostly"
        elif self.happiness > 50:
            status = "Not So"
        elif self.happiness > 40:
            status = "Not Very"
        else:
            status = "Not at all"
        return status


class Lion(Animal):
    # Add at least one unique attribute
    def __init__(self, name, age, health=80, happiness=80):
        super().__init__(name, age, health, happiness)
        self.type = "lion"
        print("Created new {} named {}. He is {}.".format(
            self.type, self.name, self.age))

    # Child overwrites the parent. Roar!
    def speak(self):
        print("{} says RRRRRRRROAR!!!!!!".format(self.name))

    # Child overwrites the parent (eating makes Lions very healthy and Happy)
    def feed(self):
        self.health += 25
        self.happiness += 25
        return self


class Tiger(Animal):
    # Add at least one unique attribute
    def __init__(self, name, age, health=80, happiness=80):
        super().__init__(name, age, health, happiness)
        self.type = "tiger"
        print("Created new {} named {}. He is {}.".format(
            self.type, self.name, self.age))


class Bear(Animal):
    # Add at least one unique attribute.
    def __init__(self, name, age, health=80, happiness=80, IQ=120):
        super().__init__(name, age, health, happiness)
        self.type = "bear"
        print("Created new {} named {}. He is {}.".format(
            self.type, self.name, self.age))


larry = Lion('Lawrence Littleton', 10)
larry.speak()  # Larry Roars, because Lions don't say hello
larry.display_info()

terry = Tiger('Terrance Tyler', 5)
terry.speak()
terry.display_info()

barry = Bear('Bartholomew Benny', 2, 30, 60, 130)
barry.speak()
barry.display_info()
