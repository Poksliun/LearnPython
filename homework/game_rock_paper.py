class game():

    def start_screen(self):
        print("камень ножницы бумага\n"
              "существует 3 оружия: камень, ножницы и бумага\n"
              "бумага бьет камень, камень бьет ножницы, ножницы бьют бумагу\n"
              "если хотите закончить игру напишите /end")

    def check_weapon(self, weapon,weapons):
        for weap in weapons.table_of_combinations:
            if weap == weapon:
                return True
        return False
    def choise_weapon(self,User):
        weapon_user = input('fвведите в'
                            'аше оружие: ')
        print('\033[F\033[K',end="")
        print(" " * 0, end='\r')

        if weapon_user=="/end":
            return False
        if not self.check_weapon(weapon_user,weapons):
            print('такого оружия нет, введите оружие повторно')
            self.choise_weapon(User)
            return True
        else:
            print(User._name+" выбрал оружие")
        User.chouce_weapon(weapon_user)
        return True
class user():
    def __init__(self,name):
        self._name=name
    def chouce_weapon(self, weapon):
        self._weapon = weapon


class weapons():
    table_of_combinations = {'камень': 'ножницы',
                             "ножницы": "бумага",
                             "бумага": "камень"}

    def fight(self, User_1, User_2):
        if User_1._weapon == User_2._weapon:
            print('ничья')
        elif self.table_of_combinations[User_2._weapon] == User_1._weapon:
            print('победил игрок 2')
        else:
            print('победил игрок 1')

User1 = user('игрок 1')
User2 = user('игрок 2')
Game = game()
all_weapons=weapons()
Game.start_screen()
while True:
    Game.choise_weapon(User1)
    Game.choise_weapon(User2)
    all_weapons.fight(User1,User2)

