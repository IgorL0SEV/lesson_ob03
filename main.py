


# 1. Создайте базовый класс `Animal`, который будет содержать общие атрибуты
# (например, `name`, `age`) и методы (`make_sound()`, `eat()`) для всех животных.

class Animal():
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def make_sound(self):
    return f"{self.name} - издаёт звуки"

  def eat(self):
    return f"{self.name} - кушает"

# 2. Реализуйте наследование, создав подклассы `Bird`, `Mammal`, и `Reptile`,
# которые наследуют от класса `Animal`. # Добавьте специфические атрибуты и
# переопределите методы, если требуется (например, различный звук для `make_sound()`).

class Bird(Animal):
  def __init__(self, name, age):
    super().__init__(name, age)

  def make_sound(self):
    return f"{self.name} - чирикает"

  def eat(self):
    return f"{self.name} - клюёт корм"

class Mammal(Animal):
  def __init__(self, name, age):
    super().__init__(name,age)

  def make_sound(self):
    return f"{self.name} - ревёт"

  def eat(self):
    return f"{self.name} - жуёт корм"

class Reptile(Animal):
  def __init__(self, name, age):
    super().__init__(name, age)

  def make_sound(self):
    return f"{self.name} - шипит"

  def eat(self):
    return f"{self.name} - заглатывает корм"


# 3. Продемонстрируйте полиморфизм: создайте функцию `animal_sound(animals)`,
# которая принимает список животных и вызывает метод `make_sound()` для каждого животного

def animal_sound(animals):
  for animal in animals:
    print (f"{animal.make_sound()}")

parrot = Bird("Gosha", "5") # создали объект класса - птичка
giraffe = Mammal("Stepa", "3") # создали объект класса - млекопитающее
varan = Reptile("Petya", "9") # создали объект класса - рептилию


# 4. Используйте композицию для создания класса `Zoo`, который будет содержать
# информацию о животных и сотрудниках. Должны быть методы для добавления животных и сотрудников в зоопарк.

class Zoo():
  def __init__(self):
    self.animals = [] # список животных Zoo
    self.personnel = [] # список персонала Zoo

  def add_animal (self, animals): # добавление в Zoo животных
    self.animals.append(animals)

  def add_personell (self, personel): # добавление в Zoo персонала
    self.personnel.append(personel)

  def show_animals_sound (self): # перечень звуков животных
    for animal in self.animals:
      print (f"{animal.make_sound()}")

  def show_animals (self): # перечень животных
    for animal in self.animals:
      print (f"{animal.name}\n{animal.age} лет\n{animal.make_sound()}\n{animal.eat()}\n")

  def show_personell (self): # перечень персонала
    for person in self.personnel:
      print (f"{person.name}\n{person.age} лет\n{person.profession}\n")

  def save_to_file(self, filename):
    with open(filename, 'wb') as file:
        pickle.dump(self, file)
    print(f"Данные зоопарка сохранены в файл: {filename}")

  @staticmethod
  def load_from_file(filename):
    with open(filename, 'rb') as file:
        zoo = pickle.load(file)
    print(f"Данные зоопарка загружены из файла: {filename}")
    return zoo

# 5. Создайте классы для сотрудников, например, `ZooKeeper`, `Veterinarian`,
# которые могут иметь специфические методы (например, `feed_animal()` для `ZooKeeper` и
# `heal_animal()` для `Veterinarian`).

class ZooKeeper():
  def __init__(self, name, age, profession):
    self.name = name
    self.age = age
    self.profession = profession

  def feed_animal(self):
    return f"животное покормлено"

class Veterinarian():
  def __init__(self, name, age, profession):
    self.name = name
    self.age = age
    self.profession = profession

  def heal_animal(self):
    return f"животному сделан профилактический осмотр"

zookeeper = ZooKeeper("Сидоров", "29 лет", "Уход за животными")
veterinarian = Veterinarian("Петров", "35 лет", "Лечение животных")


# добавление объектов класса и примеры вывода
zoo = Zoo()
zoo.add_animal(parrot)
zoo.add_animal(giraffe)
zoo.add_animal(varan)
zoo.add_personell(zookeeper)
zoo.add_personell(veterinarian)

print("Список животных с описанием")
zoo.show_animals()  # список животных с характеристиками
print()

print("Список только звуков")
zoo.show_animals_sound()  # список только звуков
print()

print("Список звуков через полиморфизм")
animal_sound(zoo.animals)  # список звуков полиморфизм
print()

print("Список персонала.")
zoo.show_personell()

# 6. Попробуйте добавить дополнительные функции в вашу программу,
# такие как сохранение информации о зоопарке в файл и возможность её загрузки,
# чтобы у вашего зоопарка было "постоянное состояние" между запусками программы.


# Сохранение состояния зоопарка в файл
zoo.save_to_file('zoo_data.pkl')

# Загрузка состояния зоопарка из файла
loaded_zoo = Zoo.load_from_file('zoo_data.pkl')