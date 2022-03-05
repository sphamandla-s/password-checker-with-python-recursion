def possible_password_comb(character_set, len_password):
    k = len(character_set)
    return possible_password_combRec(character_set, '', k, len_password)


def possible_password_combRec(character_set, prefix, k, n):
    if n == 0:
        return [prefix]
    elif not character_set or any(type(i) == int for i in character_set):
        return []
    else:
     new_list = [] 
     for i in range(k):
         new = prefix + character_set[i]
         new_list += possible_password_combRec(character_set, new, k , n - 1)
    return new_list


def password_character_set():
    numbers = ['1','2','3','4','5','6','7','8','9','0']
    specail_char = ['!','@','#','$','%','&','*','(',')','-','=','+',' ']
    joined = numbers +  specail_char
    return joined


def get_user_password():
    return input("Please Enter Your password: ")


def break_user_password(possible_comb,user_password):
    for i in range(len(possible_comb)):
        print("Checking for Password: " + possible_comb[i] + ": Not Password.")
        if possible_comb[i] == user_password:
            print(f'Your Password is: {user_password}')
            return True
    print("We can't find your password.")



if __name__ == '__main__':
    characters = password_character_set()
    password = get_user_password()
    possible_comb = possible_password_comb(characters, len(password))
    break_user_password(possible_comb,password)
