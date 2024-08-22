


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


