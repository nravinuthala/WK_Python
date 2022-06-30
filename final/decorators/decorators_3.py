# import datetime
#
#
# def timed_greeting(func, *args, **kwargs):
#     hour = datetime.datetime.now().hour
#     if (hour >= 18 and hour < 22):
#         func(*args, **kwargs)
#         print('What a lovely evening it is.')
#     else:
#         func(*args, **kwargs)
#         print("In else")
#
# @timed_greeting
# def greeting(name):
#     print(f"Hello {name}")

# greeting("Nagaraj")

# timed_greeting(greeting, "Nagaraj")

# def greeting(*msg, )