# Домашняя работа по уроку "Специальные методы классов"
# Задача "Магические здания"


class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        int(new_floor)
        if new_floor > self.number_of_floors or new_floor <= 0: #or new_floor < 1:
            print('Такого этажа не существует')
        else:
            for i in range(1, new_floor + 1):
                print(i)

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'

h1 = House('ЖК Эльбрус', 30)
h2 = House('ЖК Горский', 18)
h3 = House('Домик в деревне', 2)

h1.go_to(2)
print(len(h1))
print()
h2.go_to(20)
print(len(h2))
print()
h3.go_to(1)
print(len(h3))
print()
print(str(h1))
print(str(h2))
print(str(h3))
print(len(h1))
print(len(h2))
print(len(h3))
