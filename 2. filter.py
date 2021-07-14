from dataclasses import replace
from multiprocessing.dummy import Pool as ThreadPool
import multiprocessing 
from colorama import init, Fore
import os

init(autoreset=True)

def ryhmes(num):
    index = 0
    curr = 0
    max = 0
    for i in range(0, len(num) - 1):
        j = i
        k = 0
        while num[j] == num[len(num) - k] and j < k:
            curr += 1
            j += 1
            k += 1
            if curr > max:
                max = curr
    return max  

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
    
    is_diff = diff < 6 # Good - 3 or less
    is_zero = zero_count(number) > 2  # Good - 3 or more
    is_ends_with_3_zeros = ends_with_3_zeros(number) # Good - yes
    is_max_following = check_following(number)[0] > 1 # Good - 3 or more
    is_following_amount = check_following(number)[1] > 1 # Good - 3 or more
    is_palindrome = palindrome(number) # Good - yes
    score = 0
    if(is_diff):
        score += (5 - diff)
    if(is_zero):
        score += (zero_count(number) - 2)
    if(is_ends_with_3_zeros):
        score += 2
    if(is_max_following):
        score += (check_following(number)[0] - 2)
    if(is_following_amount):
        score += check_following(number)[1] - 1
    if(is_palindrome):
        score += 5

    if score >= 3:
        return f"{score} {num.split()[0]}"
    return f"{score} {num.split()[0]} no"

def mp_handler():
    p = multiprocessing.Pool(60)
    l = []
    for result in p.imap(num_cool, open('golant.txt', 'r').readlines()):
        l.append(result)
        if 'no' not in result:
            with open('goldengolant2.txt', 'a+') as f:
                f.write(result + '\n')
            print(Fore.GREEN + result)
        else:
            print(Fore.RED + result)


if __name__=='__main__':
    os.system('cls')
    mp_handler()