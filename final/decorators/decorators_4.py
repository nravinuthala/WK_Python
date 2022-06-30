import datetime

def addtl_greeting(func):
    # hour = datetime.datetime.now().hour
    # if 1 <= hour < 22:
        func("Hasnain")
        print("What a Lovely evening It is")

# greeting() Is Passed as a Function to timed_greeting() automatically or internally
# timed_greeting is a decorator for greeting()
@addtl_greeting
def greeting(name):
    print(f"Greetings {name}")



