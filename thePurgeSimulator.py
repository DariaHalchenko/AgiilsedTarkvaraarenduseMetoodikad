import random


class Player:
    def __init__(self, hp, energy, food):
        self.hp = hp
        self.energy = energy
        self.food = food

    def status(self):
        print(f"\n[ Staatus ] HP: {self.hp} | Energia: {self.energy} | Toit: {self.food}")

    def rest(self):
        if self.food > 0:
            self.food -= 1
            self.energy += 3
            print("Sa puhkasid. Energia taastatud (+3).")
            return True
        else:
            print("Pole piisavalt toitu puhkamiseks!")
            return False

    def heal(self):
        if self.food >= 2:
            self.food -= 2
            self.hp += 2
            if self.hp > 10:
                self.hp = 10
            print("Sa ravisid end. HP +2.")
            return True
        else:
            print("Pole piisavalt toitu ravimiseks! (vaja 2)")
            return False
#
    def take_damage(self, dmg):
        self.hp -= dmg
        if self.hp < 0:
            self.hp = 0
        print(f"Said kahju: -{dmg} HP.")
#
    def use_energy(self, amount):
        self.energy -= amount
        if self.energy < 0:
            self.energy = 0

    def add_food(self, amount):
        self.food += amount

    def lose_food(self, amount):
        self.food -= amount
        if self.food < 0:
            self.food = 0
        print(f"Kaotasid toitu: -{amount}")

    def is_alive(self):
        return self.hp > 0 and self.energy > 0


def random_event():
    roll = random.randint(0, 4)
    if roll == 0:
        return "DANGER"
    elif roll == 1:
        return "FOOD"
    elif roll == 2:
        return "NOTHING"
    elif roll == 3:
        return "HEAL"
    else:
        return "LOSE_FOOD" 


def process_event(player):
    event = random_event()
    if event == "DANGER":
        print("Ohtlik sündmus! Rünnak!")
        player.take_damage(3)
        player.use_energy(1)
    elif event == "FOOD":
        print("Leidsid toitu! (+1)")
        player.add_food(1)
    elif event == "HEAL":
        print("Leidsid esmaabikomplekti! (+2 HP)")
        player.hp += 2
        if player.hp > 10:
            player.hp = 10
    elif event == "LOSE_FOOD":
        print("Rööviti! Kaotasid osa toidust.")
        player.lose_food(1)
    else:
        print("Mitte midagi ei juhtunud.")


def main():
    player = Player(hp=10, energy=5, food=3)
    day = 1
    max_days = 15  

    print("Tere tulemast mängu 'Sundöö'!")
    print(f"Eesmärk: jää ellu {max_days} päeva.")

    while player.is_alive() and day <= max_days:
        print(f"\n========== Päev {day} / {max_days} ==========")
        player.status()

        print("Valikud:")
        print("1. Puhka (kasutab toitu, taastab energiat)")
        print("2. Riskida sündmusega")
        print("3. Mitte teha midagi")
        print("4. Ravida (kasutab 2 toitu, taastab 2 HP)")
        print("5. Sündmus (võib anda või võtta midagi)")  
        print("6. Koguda ressursse (otsid ainult toitu)")  

        choice = input("Vali (1-6): ").strip()
        action_taken = False

        if choice == "1":
            action_taken = player.rest()
        elif choice == "2":
            process_event(player)
            action_taken = True
        elif choice == "3":
            print("Sa ei teinud midagi täna.")
            action_taken = True
        elif choice == "4":
            action_taken = player.heal()
        elif choice == "5":
            print("Toimus juhuslik sündmus...")
            process_event(player)
            action_taken = True
        elif choice == "6":
            print("Sa läksid koguma toitu...")
            success = random.randint(0, 1)
            if success:
                print("Leidsid 1 toidu!")
                player.add_food(1)
            else:
                print("Ei leidnud midagi...")
            action_taken = True
        else:
            print("Vigane valik.")
            continue

        if action_taken:
            player.use_energy(1)
            day += 1

    if player.is_alive():
        print(f"\nPalju õnne! Sa jäid ellu {max_days} päeva!")
    else:
        print("\nMäng läbi. Sa ei jäänud ellu.")
    print(f"Ellujäämispäevad: {day - 1}")


if __name__ == "__main__":
    main()
