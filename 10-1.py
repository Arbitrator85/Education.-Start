import collections

last = collections.deque(pets, maxlen=1)[0]
last += 1

a = input("Введите вид питомца:")

b = int(input("Введите возраст питомца:"))

c = input("Введите кличку питомца:")

d = input("Введите имя владельца:")

pets[last] = {c:{'Это':a, 'Возраст питомца':b, 'Имя владельца':d}}

if ID in pets.keys():
  if int(b[-1]) == 1:
    print("Это", a, "по кличке", c,". Возраст питомца:", b, "год.", "Имя владельца:", d)

elif int(b[-1]) == 2 or int(b[-1]) == 3 or int(b[-1]) == 4 and int(b) != 12 and int(b) != 13 and int(b) != 14:

    print("Это", a, "по кличке", c,". Возраст питомца:", b, "года.", "Имя владельца:", d)

else:

    print("Это", a, "по кличке", c,". Возраст питомца:", b, "лет.", "Имя владельца:", d)