import collections

command = input()
 
pets = {1:{"Мухтар": {"Вид питомца": "Собака","Возраст питомца": 9,"Имя владельца": "Павел"},},2:{"Каа": {"Вид питомца": "желторотый питон","Возраст питомца": 19,"Имя владельца": "Саша"},},}

def create(command):
    last = collections.deque(pets, maxlen=1)[0]
    last += 1
    a = input("Введите вид питомца:")
    b = input("Введите возраст питомца:")
    c = input("Введите кличку питомца:")
    d = input("Введите имя владельца:")
    pets[last] = {c: {'Вид питомца': a, 'Возраст питомца': b, 'Имя владельца': d}}
    return pets
    print(get_suffix(b))


def get_pet(ID):
    return pets[ID] if ID in pets.keys() else False

def get_suffix(b):
  for b in create(command):
    if int(b[-1]) == 1:
      print("Это", a, "по кличке", c,". Возраст питомца:", b, "год.", "Имя владельца:", d)
    elif int(b[-1]) == 2 or int(b[-1]) == 3 or int(b[-1]) == 4 and int(b) != 12 and int(b) != 13 and int(b) != 14:
      print("Это", a, "по кличке", c,". Возраст питомца:", b, "года.", "Имя владельца:", d)
    else:
      print("Это", a, "по кличке", c,". Возраст питомца:", b, "лет.", "Имя владельца:", d)


def pets_all(command):
    if command == 'all':
        return pets

while command:
    if command == 'create':
        print(create(command))
        continue
    elif command == 'all':
        print(pets_all(command))
        break
    elif command == 'stop':
        print('Работа с базой данных завершена')
        break
    elif command == 'search':
        ID = int(input())
        if ID in pets:
            print(get_pet(ID))
        else:
            print('Данный номер отсутствует в базе данных')
            continue
    else:
        break