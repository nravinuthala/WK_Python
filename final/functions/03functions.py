# function with positional arguments
def print_details(name, age, profession):
    print(f'{name} is {age} years old. {name} is a {profession}.')

# calling the function with positional arguments
# print_details("John", 50)

# calling the function with keyword arguments
# print_details(age=50, name="John")

print_details("John", 50, profession="Teacher")

# function with default parameters
def print_det_again(name, age = 20, profession = 'student'):
    print(f'{name} is {age} years old. {name} is a {profession}.')

print_det_again("Nag", 35, 'Trainer')

# function with variable number of parameters
def print_var_params(*args):
    print(args)
    for arg in args:
        print(arg)
    # if (params[3]):
    #     print(params[3])

print_var_params(1)
print_var_params(1, 2)
print_var_params(1, 2, 3)
print_var_params(1, 2, 3, 4)

def args_kwargs(*params, **named_params):
    print(params)
    print(named_params)

args_kwargs("hi", "I", "am", "an", "arbitrary", "arg", "list", kw1="while", kw2="this", kw3="is a keyword arg list")

args_kwargs()