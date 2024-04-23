class Enemy:
    # Abstraction - basically talks about implementing code such that the user does not need to understand what happens behind the scenes in implementation
    # Generated automatically when the class is created. This is the constructor
    def __init__(self, type_of_enemy, health_points=10, attack_damage=1):
        # pass
        # type_of_enemy now becomes inaccessible and can only be gotten by getters and setters.
        self.__type_of_enemy = type_of_enemy
        self.health_points = health_points
        self.attack_damage = attack_damage
        # The above are instance values which are created when the object is created
        print("New enemy created with no starting values")

    def talk(self):
        print(f"I am a {self.__type_of_enemy}. Be prepared to fight!")

    def walk_forward(self):
        print(f"{self.__type_of_enemy} moves closer to you")

    def attack(self):
        print(f"{self.__type_of_enemy} attacks for {
              self.attack_damage} damage")

    def get_type_of_enemy(self):
        return self.__type_of_enemy

    def special_attack(self):
        print(f"{self.get_type_of_enemy()} has no special attack")
