# list enumeration
vals_list = [i for i in range(1, 10)]
print(vals_list)

def give_single_val(vals):
    n = 10
    for val in vals:
        n += 10
        print(n)
        yield val

sing_val_gen = give_single_val(vals_list)

print(next(sing_val_gen))
print(next(sing_val_gen))
print(next(sing_val_gen))


# single_val_generator = give_single_val(vals_list)

# print(next(single_val_generator))
# print(next(single_val_generator))
# print(next(single_val_generator))
# print(next(single_val_generator))
#
# while True:
#     try:
#         print(next(single_val_generator))
#     except StopIteration:
#         break
