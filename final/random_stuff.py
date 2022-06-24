# # print("Hello world", "How are you doing today?", sep='*', end='thats all folks')
# print("Hello world", "How are you doing today?", sep='\n',  end='thats all folks')
# print()
# # print('This is Python')
#
# name = 'Nagaraj'
#
# print(f'Hi {name}. How are you?')
# age = 30.0
# print('Hi {}. You are {} years old.'.format(name, age))
#
# print(type(age))
# print(type(name))
#
#
# cars = ['audi', 'bmw', 'merc', 5, [1, [3]], 5.0]
#
# print(cars)
#
# cars[2] = 'maruti'
#
# print(cars)
#
# tuple1 = ('audi', 'bmw', 'merc', 5, [1, [3]], 5.0)
# print(tuple1)
#
# # tuple1[2] = 'maruti'
#
# print(tuple1)
#
# print(range(5, 9, 2))
#
# player = ["John", 20, 6.1, "Basket Ball"]
#
# player = {
#     "name": "John",
#     "age": 20,
#     "height": 6.1,
#     "game": "Basket Ball"
# }
#
# print(player)
#
# set1 = {1, 3, 4, 5, 5, 5, 5}
# print(set1[0])
#
# canbeanything = {1}
# print(type(canbeanything))
#
# lang = "0123456789"
# print(len(lang))
# print(lang[2:5])
# print(lang[5:])
#
# num = '10'
# num = int(num)
# print(num + num)
#
# height = 6.3
# print(int(height))
#
# list1 = [1, 2, 3]
# print(tuple(list1))
# print(list1)
#
#
# player = {
#     "name": "John",
#     "age": 20,
#     "height": 6.1,
#     "game": "Basket Ball"
# }
#
# print(player["name"])
# print(player.get("name"))

# blank = (1)
# if (0):
#     print('hi')
# elif (blank):
#     print('something else')
# else:
#     print('hello')

# counter = 0
# while (counter < 10):
#     print("You don't have to terminate me.")
#     counter += 1
# else:
#     print('Fnally I am out of while loop.')


# for _ in range(0, 10):
#     print("I will be printed 9 times")
#
# cars = ['audi', 'bmw']
# for car in cars:
#     print(car)

player = {
    "name": "John",
    "age": 20,
    "height": 6.1,
    "game": "Basket Ball"
}

# print(player.keys())
# print(player.values())
#
# for key in player.keys():
#     print(f'{key}: {player[key]}')
#
# print(player.items())

for _, y in player.items():
    print(y)
