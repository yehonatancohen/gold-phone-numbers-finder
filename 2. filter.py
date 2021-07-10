from dataclasses import replace
from multiprocessing.dummy import Pool as ThreadPool
import multiprocessing 
from colorama import init, Fore
import os

init(autoreset=True)

def check_following(num):
    maxfollowing = 0
    curr = 1
    l = False
    amount = 0
    for i in range(0,len(num) - 1):
        if(num[i] == num[i + 1]):
            if l == False:
                amount += 1
                l = True
            curr += 1
            if curr > maxfollowing:
                maxfollowing = curr
        elif (l == True):
            curr = 1
            l = False
    return [maxfollowing, amount]

def ends_with_3_zeros(num):
    amount = 0
    for i in reversed(num):
        if amount > 2:
            return True
        if i != 0:
            amount = 0
        else:
            amount += 1
    if amount > 2:
        return True
    else:
        return False    

def zero_count(num):
    c = 0
    for i in num:
        if i == 0:
            c += 1
    return c

def palindrome(s):
    return s == s[::-1]

def num_cool(num):
    number = num.split()[0][3:] # Converts this "0586111111" to this "6111111"
    arr = list(map(int,number)) # Converts this "6111111" to this [6,1,1,1,1,1,1]
    
    diff = len(set([char for char in number])) # Converts this "6111111" to this [6,1] to this 2
    
    is_diff = diff < 3
    is_zero = zero_count(number) > 3
    is_ends_with_3_zeros = ends_with_3_zeros(number)
    is_max_following = check_following(number)[0] > 3
    is_following_amount = check_following(number)[1] > 1
    is_palindrome = palindrome(number)

    if is_diff:
        return f"{num.split()[0]}"
    return f"{num.split()[0]} no"

def mp_handler():
    p = multiprocessing.Pool(60)
    l = []
    for result in p.imap(num_cool, open('golant.txt', 'r').readlines()):
        l.append(result)
        if 'no' not in result:
            with open('goldengolant.txt', 'a+') as f:
                f.write(result + '\n')
            print(Fore.GREEN + result)
        else:
            print(Fore.RED + result)


if __name__=='__main__':
    os.system('cls')
    mp_handler()