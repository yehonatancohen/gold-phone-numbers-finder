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

def ryhmes(num):
    index = 0
    curr = 0
    max = 0
    end = ((len(num) - 1) // 2) 
    for i in range(0, end):
        if num[i] == num[i + 4]:
            curr += 1
    return curr  

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

def palindrome(s):
    return s == s[::-1]

        
#print(palindrome('1220321'))
#print(check_following(list(map(int,'1166333'))))
print(ryhmes(list(map(int,'2031203'))))