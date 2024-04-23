from Enemy import Enemy
import random


class Zombie(Enemy):
    def __init__(self, health_points, attack_damage):
        super().__init__(type_of_enemy="Zombie",
                         health_points=health_points, attack_damage=attack_damage)

    def talk(self):  # Method overriding
        print("*Grumbling....*")

    def spread_disease(self):
        print("The Zombie is trying to spread the virus")

    def special_attack(self):
        did_special_attack_work = random.random() < 0.5
        if did_special_attack_work == True:
            self.health_points += 2
            print("Zombie regenerated 2 HP")
