#!/usr/bin/env python
#Find happy number
def HappyNumber(num):
    while num > 1:
        sum = 0
        for i in str(num):
            i = int(i)
            sum += i*i
    num = sum
    if num == 1:
        return True
    else:
        return False

print(HappyNumber(19))
