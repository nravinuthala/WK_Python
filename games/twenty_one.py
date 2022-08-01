player_list = ['Player', 'Computer']
ans = input("DO you want to play first? (y/n)")
if ans in 'y':
    print('User to play first')
    current = player_list[0]
else:
    print('Computer to play first')
    current = player_list[1]




