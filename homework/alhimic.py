from enum import Enum
class Elements(Enum):
    fire = 1
    earth = 2
    water = 3
    air = 4
    energy = 5
    lava=6
    cloud=7
    pressure=8

class alchemist:
    def __init__(self):
        self.all_elements_data = {
            (Elements.fire.value, Elements.air.value): Elements.energy,
            (Elements.fire.value, Elements.water.value): Elements.lava,
            (Elements.water.value, Elements.air.value): Elements.cloud,
            (Elements.earth.value, Elements.earth.value): Elements.pressure
        }
        self.elements = [Elements.fire, Elements.earth,Elements.water,Elements.air]
        self.elements_for_crossing =[]

    def choose_element(self,n):
        try:
            element = int(input(f'id {n} элемента: '))
            if len(self.elements)>=element and element>0:
                self.elements_for_crossing.append(element)
            else:
                print('элемента с таким id не существуют')
                self.choose_element(n)
        except:
            print('введите число')
            self.choose_element(n)

    def crossing_elements(self):
        print('выберите id элементов для скрещевания')
        number_elements_crossed=2
        for i in range(1,number_elements_crossed+1):
            self.choose_element(i)
        key = tuple(sorted(self.elements_for_crossing))
        if key in self.all_elements_data:
            if self.all_elements_data[key] not in self.elements:
                self.elements.append(self.all_elements_data[key])
                print(f'вы создали новый элемент {self.all_elements_data[key].name}')
                self.elements_for_crossing = []
            else:
                print('такой элемент уже создан')
                self.elements_for_crossing = []
        else:
            print('такого элемента нет, попробуйте еще раз')
            self.elements_for_crossing = []

    def look_all_elements(self):
        print('ваши элементы')
        for i, element in enumerate(self.elements):
            print(f'{i+1}: {element.name}')

alchemist_game =alchemist()
game = True

while game:

    alchemist_game.look_all_elements()
    alchemist_game.crossing_elements()




















