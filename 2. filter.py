from dataclasses import replace
from multiprocessing.dummy import Pool as ThreadPool
import multiprocessing 
from colorama import init, Fore
import os
import collections


init(autoreset=True)

# Checks the amount of digits exits in the number and the first digit to start counting
# 058-5880008 -> 3 digits starting at 0
# 058-5875887 -> 3 digits starting at 1
# 058-1871887 -> 3 digits starting at 2
def full_diff(num):
    diff = 0
    max = 10
    max_index = 0
    for i in range(0,3):
        number = num.split()[0][i:]
        diff = len(set([char for char in number]))
        if diff < max:
            max = diff
            max_index = i + 1
    return [max, max_index]

# Returns the number of the maximum digits in a row and the amount of digit rows
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

# Check if the number ends with 3 zeros (058-1234000)
# Originaly counted the amount of zeros from the end
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

# Counts the zero count
def zero_count(num):
    c = 0
    for i in num:
        if i == 0:
            c += 1
    return c

#058-1234321
def palindrome(s):
    return s == s[::-1]

# Check if the 2 or 3 first digits equals to the 2 or 3 last digits
# 058-1580158
def ryhmes(num):
    if num[6] == num[2] and num[5] == num[1]:
        if num[4] == num[0]:
            return 4
        return 3
    elif num[5] == num[1] and num[4] == num[0]:
        return 1
    return 0    

def num_cool(num):
    number = num.split()[0][2:] # Converts this "0586111111" to this "86111111"
    number2 = num.split()[0][3:] # Converts this "0586111111" to this "6111111"

    #arr = list(map(int,number)) # Converts this "6111111" to this [6,1,1,1,1,1,1]
    
    full_diff = len(set([char for char in num])) - 2
    #diff = len(set([char for char in number])) # Converts this "6111111" to this [6,1] to this 2
    
    # Check each function for additional explanation
    is_diff = full_diff < 5 # Good - 3 or less
    is_zero = zero_count(number) > 2  # Good - 3 or more
    is_ends_with_3_zeros = ends_with_3_zeros(number) # Good - yes
    is_max_following = check_following(number)[0] > 3 # Good - 3 or more
    is_following_amount = check_following(number)[1] > 1 # Good - 3 or more
    is_palindrome = palindrome(number) # Good - yes | No palindrome numbers exits
    is_ryhmes = ryhmes(number2) # Good - 4

    score = 0

    if(is_diff):
        score += (5 - full_diff)
    if(is_zero):
        score += zero_count(number) - 3
    if(is_ends_with_3_zeros):
        score += 0.5
    if(is_max_following):
        score += (check_following(number)[0] - 1)
    if(is_following_amount):
        score += check_following(number)[1]
    if(is_ryhmes):
        score += is_ryhmes

    if score >= 3:
        return f"{round(score,1)} {num.split()[0]}"
    return f"{round(score,1)} {num.split()[0]} no"

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
    numbers = []
    # Sort by score and cut the score
    with open('goldengolant.txt', 'r') as f:
        for line in sorted(f.readlines()):
            y = line.split()[1]
            numbers.append(y)
    # Write the sorted version to a new file
    with open('goldengolant_cut.txt', 'w') as r:
        for y in numbers:
            r.write(y + "\n")
        


if __name__=='__main__':
    os.system('cls')
    mp_handler()