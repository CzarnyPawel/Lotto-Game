from random import shuffle
"""Lotto game application. User selects 6 digits. After then computer does it one more time.
    Digits are compared. User win if thre is 3, 4, 5 or 6 same digits."""


def user():
    user_numbers = []
    i = 1

    while i <= 6:
        number = input('Wprowadź ' + str(i) + ' liczbę: ')
        try:
            u_num = int(number)
        except ValueError:
            print('Należy wprowadzić liczbę!')
            continue
        if u_num <= 0 or u_num > 49:
            print('Należy wprowadzić liczbę z zakresu od 1 do 49!')
            continue
        if u_num in user_numbers:
            print(f'Wprowadzono już liczbę {u_num}!')
            continue
        user_numbers.append(u_num)
        i += 1
    return user_numbers


def lotto():
    lotto_nums = list(range(1, 50))
    shuffle(lotto_nums)
    return lotto_nums[:6]


user_n = user()
print(sorted(user_n))
lotto_numbers = lotto()
print(sorted(lotto_numbers))

win_nums = []
for one_num in user_n:
    if one_num in lotto_numbers:
        win_nums.append(one_num)
if len(win_nums) == 1:
    print(f'Trafiłeś {len(win_nums)} liczbę.')
elif len(win_nums) == 0 or len(win_nums) == 5 or len(win_nums) == 6:
    print(f'Trafiłeś {len(win_nums)} liczb.')
else:
    print(f'Trafiłeś {len(win_nums)} liczby.')
