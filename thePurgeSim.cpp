#include <iostream>
#include <cstdlib>
#include <ctime>

using namespace std;

class Player {
private:
    int hp;
    int energy;
    int food;

public:
    Player(int hp, int energy, int food) : hp(hp), energy(energy), food(food) {}

    void status() const {
        cout << "\n[ Staatus ] HP: " << hp << " | Energia: " << energy << " | Toit: " << food << endl;
    }

    bool rest() {
        if (food > 0) {
            food--;
            energy += 3;
            cout << "Sa puhkasid. Energia taastatud (+3)." << endl;
            return true;
        } else {
            cout << "Pole piisavalt toitu puhkamiseks!" << endl;
            return false;
        }
    }

    void takeDamage(int dmg) {
        hp -= dmg;
        if (hp < 0) hp = 0;
        cout << "Said kahju: -" << dmg << " HP." << endl;
    }

    void useEnergy(int amount) {
        energy -= amount;
        if (energy < 0) energy = 0;
    }

    void addFood(int amount) {
        food += amount;
    }

    bool isAlive() const {
        return hp > 0 && energy > 0;
    }
};

string randomEvent() {
    int roll = rand() % 3;
    if (roll == 0) return "DANGER";
    else if (roll == 1) return "FOOD";
    else return "NONE";
}

void processEvent(Player& player) {
    string event = randomEvent();
    if (event == "DANGER") {
        cout << "Ohtlik sündmus! Sa sattusid rünnaku alla." << endl;
        player.takeDamage(3);
        player.useEnergy(1);
    } else if (event == "FOOD") {
        cout << "Leidsid toidutagavara! (+1 toidukord)" << endl;
        player.addFood(1);
    } else {
        cout << "Kõik on vaikne... midagi ei juhtunud." << endl;
    }
}

int main() {
    srand(static_cast<unsigned int>(time(0)));

    Player player(10, 5, 2);
    int day = 1;

    cout << "Tere tulemast mängu 'Sundöö: thePurgeSim'!" << endl;
    cout << "Eesmärk: jää ellu nii kaua kui võimalik, tehes strateegilisi otsuseid." << endl;

    while (player.isAlive()) {
        cout << "\n========== Päev " << day << " ==========" << endl;
        player.status();

        cout << "Valikud:\n";
        cout << "1. Puhka (kasutab toitu, taastab energiat)\n";
        cout << "2. Riskida sündmusega (võib leida toitu või saada kahju)\n";
        cout << "3. Mitte teha midagi (jätad päeva vahele)\n";

        string choice;
        cout << "Vali (1-3): ";
        cin >> choice;

        bool actionTaken = false;

        if (choice == "1") {
            actionTaken = player.rest();
        } else if (choice == "2") {
            processEvent(player);
            actionTaken = true;
        } else if (choice == "3") {
            cout << "Sa otsustasid mitte midagi teha..." << endl;
            actionTaken = true;
        } else {
            cout << "Vigane valik." << endl;
            continue;
        }

        if (actionTaken) {
            player.useEnergy(1);
        }

        day++;
    }

    cout << "\nMäng läbi. Sa ei jäänud ellu." << endl;
    cout << "Ellujäämispäevad: " << (day - 1) << endl;

    return 0;
}
