#HOMEWORK1
#PROBLEM1
#Introduction (all– total: 7- max points: 75)
#https://www.hackerrank.com/domains/python/py-introduction
# Name_Exercise_1
#Say "Hello, World!" With Python
if __name__ == '__main__':
    print("Hello, World!")


# Name_Exercise_2
#Python If-Else

#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    if n % 2 != 0:
        print("Weird")
    elif n >= 2 and n<= 5:
        print("Not Weird")
    elif n>= 6 and n<=20:
        print("Weird")
    elif n>20:
        print("Not Weird")



# Name_Exercise_3
#Arithmetic Operators

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    
    print(a+b)
    print(a-b)
    print(a*b)







# Name_Exercise_4
#Python: Division
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a//b)
    print(a/b)





# Name_Exercise_5
#Loops

if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        print(i*i)


# Name_Exercise_6
#Write a function

def is_leap(year):
    leap = False
    
    if(year%400==0):
        leap = True
    elif(year%100 != 0 and year%4==0):
        leap = True
    
    return leap




# Name_Exercise_7
#Print Function

if __name__ == '__main__':
    n = int(input())
    for i in range(1,n+1):
        print(i,end="")



# Data types (all– total: 6- max points: 60)
# https://www.hackerrank.com/domains/python/py-basic-data-types
# Name_Exercise_8
#List Comprehensions

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    a = []
    for i in range(x+1):
        for j in range(y+1):
            for k in range(z+1):
                if (i+j+k != n):
                    a.append([i,j,k])
    print(a)



# Name_Exercise_9
#Find the Runner-Up Score!

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr= list(arr)
    max1 = -100
    max2 = -100
    for i in range(n):
        
        if (arr[i]>max1):
            max1 = arr[i]
    for i in range(n):
        if(arr[i]>max2 and arr[i] < max1):
            max2 = arr[i]
    print(max2)
    



# Name_Exercise_10
#Nested Lists

from collections import OrderedDict
if __name__ == '__main__':
    d = OrderedDict()
    
    for _ in range(int(input())):
        n = input()
        s = float(input())
        d[n] = s
        
    
    d = dict(sorted(d.items(), key=lambda item: (item[1], item[0])))
    s = sorted(set(d.values()))
    for i,j in d.items():
        if j == s[1]:
            print(i)



# Name_Exercise_11
#Finding the percentage
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    
    for key, value in student_marks.items():
        if key == query_name:
            num = (value[0]+value[1]+value[2])/3
            print(f"{num:.2f}")

# Name_Exercise_12
#Lists

if __name__ == '__main__':
    N = int(input())
    a = []
    for i in range(N):
        s = input()
        s = s.split()
        if s[0] == "insert":
            a.insert(int(s[1]),int(s[2]))
        elif s[0] ==  "print":
            print(a)
        elif s[0] ==  "append":
            a.append(int(s[1]))
        elif s[0] ==  "sort":
            a=sorted(a)
        elif s[0] ==  "pop":
            a.pop()
        elif s[0] ==  "reverse":
            a.reverse()
        elif s[0] ==  "remove":
            a.remove(int(s[1]))
                    



# Name_Exercise_13
#Tuples



if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    t = tuple(integer_list)
    print(hash(t))


#  Strings (all– total: 14- max points: 220)
#  https://www.hackerrank.com/domains/python/py-strings
# Name_Exercise_14
#sWAP cASE
def swap_case(s):
    s2 = ""

    for i in s:
        if i.isupper():
            i = i.lower()
            s2 +=  i
        elif i.islower():
            i = i.upper()
            s2 += i
        else:
            s2 += i

    return s2
        



# Name_Exercise_15
#String Split and Join


def split_and_join(line):
    line = line.split(" ")
    line= "-".join(line)
    return(line)

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)


# Name_Exercise_16
#What's Your Name?
#
# Complete the 'print_full_name' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING first
#  2. STRING last
#

def print_full_name(first, last):
    print("Hello ",first," ",last,"! You just delved into python.",sep="")




# Name_Exercise_17
#Mutations
def mutate_string(string, position, character):
    s = list(string)
    s[position] = character
    s="".join(s)
    return s


# Name_Exercise_18
#Find a string
def count_substring(string, sub_string):
    s = list(string)
    b = list(sub_string)
    count = 0
    for i in range(len(s)):
        for j in range(len(b)):
            if i+j < len(s):
                if j == len(b)-1:
                    if (s[i+j] == b[j] ):
                        count = count + 1
                
                if (s[i+j] == b[j] ):
                    continue
                else:
                    break;
            
    return count



# Name_Exercise_19
#String Validators
if __name__ == '__main__':
    s = input()
    
    alnum = False
    c = False
    d = False
    l = False
    u = False
    for i in s:
        if(i.isalnum()):
            alnum = True
        if(i.isalpha()):
            c = True
        if(i.isdigit()):
            d = True
        if(i.islower()):
            l = True
        if(i.isupper()):
            u = True
    
    print(alnum)
    print(c)
    print(d)
    print(l)
    print(u)

# Name_Exercise_20
#Text Alignment
# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
for i in range(n): #top pyramid 
    s="H"*(i*2+1)
    print(s.center(n*2," "))

for i in range(n+1): #two pillers || (top) 
    s="H"*n+"   "*n+"H"*n
    print(s.center(n*6," "))
    

for i in range((n+1)//2): #block of H
    s="H"*n*5      
    print(s.center(n*6," "))
    
for i in range(n + 1): #two pillers || (bottom) 
    s="H"*n+"   "*n+"H"*n
    print(s.center(n*6," "))
    
for i in range(n): #bottom pyramid after  
    s="H"*((n-i-1)*2+1)
    print(" "*n*4 +s.center(n*2," "))



# Name_Exercise_21
#Text Wrap

def wrap(string, m):
    s = ""
    ms = ""
    for i in string:
        s+=i
        if (len(s)==m):
            ms+=s+"\n"
            s = ""
            
        
    if (len(s) != 0):
        ms+= s+ "\n"
        
    return ms




# Name_Exercise_22
#Designer Door Mat
# Enter your code here. Read input from STDIN. Print output to STDOUT
n,m = map(int,input().split())
p = ".|."
for i in range(1,n,+2): #top for 7 ; i=1,3,5 
    print((p*i).center(m,'-'))
    
print("WELCOME".center(m,'-'))
    

for i in range(n-2,0,-2): #bottom for 7 ; i =5,3,1
    print((p*i).center(m,'-'))    



# Name_Exercise_23
#String Formatting

def print_formatted(number):
    # your code goes here
    for i in range(1,number+1):
        s = len(bin(number)[2:])
        
        d = str(i).rjust(s, ' ')     # decimal
        o = oct(i)[2:].rjust(s, ' ')    # octal
        h = hex(i).upper()[2:].rjust(s, ' ') # hexidecimal       
        b = bin(i)[2:].rjust(s, ' ')    # binary
        print(f"{d} {o} {h} {b}")








# Name_Exercise_24
#Alphabet Rangoli

def print_rangoli(size):
    # your code goes here
        s ="abcdefghijklmnopqrstuvwxyz"
        abc=""
        for i in range(size-1,-1,-1):
            abc+= s[i]
        #all the char in order c,b,a for 3
        
        mid = []
        for c in abc:
            bucket = ""    
            for i in range(size-1,s.index(c),-1):
                bucket += s[i]
            mid.append("-".join(bucket+c+bucket[::-1]))
        #mid has the middle pattern for 3
        #c
        #c-b-c
        #c-b-a-b-c
        
        
        fillsize = len(mid[-1]) #middle line (the last one)
        
        for i in mid: #top pyramid
            print(i.center(fillsize,"-"))
        
        for i in range(len(mid)-2,-1,-1): #bottom pyramid but without mid line as it repeats
            print(mid[i].center(fillsize,"-"))










# Name_Exercise_25
#Capitalize!

# Complete the solve function below.
def solve(s):
    n= s[0].upper()
    
    for i in range(1,len(s)):
        if(s[i-1]==" " and s[i] != " "):
            n+=s[i].upper()
        else:
            n+=s[i]
        
       
    return n 




# Name_Exercise_26
#The Minion Game
def minion_game(string):
    # when i take B, i also take BA,BAN,BANA,BANAN,BANANA(which makes claculation faster)
    s = 0
    k = 0
    v="AEIOU"
    for i in range(len(string)):
        if(string[i] in v):
            
            k += len(string)-i
        else:
            s += len(string)-i
    if(k>s):
        print("Kevin",k)
    elif(k<s):
        print("Stuart",s)
    else:
        print("Draw")







# Name_Exercise_27
#Merge the Tools!
def merge_the_tools(s, k):
    for i in range(0,len(s),k):
        
        s2 = ""
        for j in (s[i:i+k]):
            if j not in s2:
                s2+=j
        print(s2)





#  Sets (all– total: 13- max points: 170)
#  https://www.hackerrank.com/domains/python/py-sets
# Name_Exercise_28
#Introduction to Sets
def average(array):
    # your code goes here
    s = set(array)
    avg = round(sum(s) / len(s), 3)
    return avg






# Name_Exercise_29
#No Idea!
# Enter your code here. Read input from STDIN. Print output to STDOUT
l = input().split()
n = (l[0])
m = (l[1])
arr  = input().split()
a  = set(input().split())
b = set(input().split())

happiness= 0
for i in arr:
    if i in a:
        happiness += 1
    if i in b:
        happiness -= 1
print(happiness)
            







# Name_Exercise_30
#Symmetric Difference
# Enter your code here. Read input from STDIN. Print output to STDOUT


# best to use a^b but learnt it later
m = input()
a = list(input().split())
a=list(set(a)) # to remove duplicate values in a as remove deletes only one accurance 

n = input()
b = list(input().split())
b=list(set(b))  # to remove duplicate values in a as remove deletes only one accurance

same = []
for i in a:
    if i in b and i not in same:
        same.append(i)
        
# print(same)
a=list(set(a))

for i in same:
    a.remove(i)
    b.remove(i)


a = list(map(int,a))
# a = sorted(a)
b = list(map(int,b))
# b= sorted(b)
a.extend(b)
a = sorted(a)
a=set(a)        


for i in a:
    print(i)









# Name_Exercise_31
#Set .add()
# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
c = set()
for i in range(n):
    c.add(input())

print(len(list(c)))





# Name_Exercise_32
#Set .discard(), .remove() & .pop() 
n = int(input())
s = set(map(int, input().split()))

#i used python 3. there is issues in pop() as it is random, read the Note in question
N = int(input())
for i in range(N):
    c = list(input().split())
    if(c[0] == "pop"):
        if(s): 
            s.pop()

    elif(c[0] == "remove"):
        if (int(c[1]) in s):
            s.remove(int(c[1]))
        
    elif(c[0] == "discard"):
        s.discard(int(c[1]))
    # print(c[0],s)
        

sum = 0        
for i in s:
    sum+=int(i)
print(sum)    




# Name_Exercise_33
#Set .union() Operation
# Enter your code here. Read input from STDIN. Print output to STDOUT
a = input()
b = set(input().split())

c = input()
d = set(input().split())

b.update(d)
print(len(list(b)))








# Name_Exercise_34
#Set .intersection() Operation
# Enter your code here. Read input from STDIN. Print output to STDOUT
# Enter your code here. Read input from STDIN. Print output to STDOUT
a = input()
b = set(input().split())

c = input()
d = set(input().split())

e = b & d
print(len(list(e)))





# Name_Exercise_35
#Set .difference() Operation
# Enter your code here. Read input from STDIN. Print output to STDOUT
a = input()
b = set(input().split())

c = input()
d = set(input().split())

e = b - d
print(len(list(e)))






# Name_Exercise_36
#Set .symmetric_difference() Operation
# Enter your code here. Read input from STDIN. Print output to STDOUT
a = input()
b = set(input().split())

c = input()
d = set(input().split())

e = b ^ d
print(len(list(e)))







# Name_Exercise_37
#Set Mutations
# Enter your code here. Read input from STDIN. Print output to STDOUT
n1 = int(input())
a = set(input().split())

N = int(input())
for i in range(N):
    o = list(input().split())
    b = set(input().split())
    if(o[0] == "intersection_update"):
        a.intersection_update(b)
        
    if(o[0] == "update"):
        a.update(b)
    if(o[0] == "symmetric_difference_update"):
        a.symmetric_difference_update(b)
    if(o[0] == "difference_update"):
        a.difference_update(b)
sum = 0
for i in a:
    sum+= int(i)
print(sum)







# Name_Exercise_38
#The Captain's Room
#this same code is too slow for pypy 3 :) 
k = int(input())
s = list(input().split())
s2 = list(set(s)) #all unique values

for i in s2: # all unique value
    s.remove(i) # removing all unique value once so [1,1,2,2,3] => [1,2] //no 3 as it was one time present
    if i not in s: # if a unique value is missing from the after remove once list
        print(i)
        break


    





# Name_Exercise_39
#Check Subset
# Enter your code here. Read input from STDIN. Print output to STDOUT
t = int(input())
for i in range(t):
    nA = int(input())
    A = set(input().split())
    
    nB = int(input())
    B = set(input().split())
    union = ((A.union(B))) #everything all together in union. union == B if A is a subset. B=(1,2,3) A=(2), union = (1,2,3) 
    #else B=(1,2,3) A=(2,999), union = (1,2,3,999). union has an extra value taken from A
    
    if(union == B):
        print(True)
    else:
        print(False)




# Name_Exercise_40
#Check Strict Superset
# Enter your code here. Read input from STDIN. Print output to STDOUT
A = set(input().split())
n = int(input())

flag = True  
for i in range(n):
    B = set(input().split())
    if(flag):
        if (not A.issuperset(B)): #default function to check superset or not
            flag = False
        
if (flag):
    print(True)
else:
    print(False)







# Collections (all– total: 8- max points: 220)
# https://www.hackerrank.com/domains/python/py-collections
# Name_Exercise_41
#collections.Counter()
# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import defaultdict


A = defaultdict(list)

a, b = map(int, input().split())

B = []
for i in range(a):
    A[input()].append(i+1)

for i in range(b):
    s = input()
    if s in A:
        for j in A[s]:
            print(j,end=" ")
        print()
    else:
        print(-1)

   





# Name_Exercise_42
#DefaultDict Tutorial
# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
header = input().split()
i = header.index("MARKS")
t = 0
for j in range(n):
    r =  input().split()
    t += int(r[i])
print(t/n)




# Name_Exercise_43
#Collections.namedtuple()
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict
d = OrderedDict()
n = int(input())
for i in range(n):
    l = input().split()
    if len(l) == 3:
        if(l[0]+" "+l[1] in d):
            d[l[0]+" "+l[1]] = d[l[0]+" "+l[1]]+int(l[2])
        else:
            d[l[0]+" "+l[1]] = int(l[2])
            
    else:
        if(l[0] in d):
            d[l[0]] = d[l[0]]+int(l[1])
        else:
            d[l[0]] = int(l[1])
            
for i,j in d.items():
    print(i,j)
        





# Name_Exercise_44
#Collections.OrderedDict()
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict
d = OrderedDict()
n = int(input())

for i in range(n):
    s = input()
    if s in d:
        d[s] = d[s]+1
    else:
        d[s] = 1
print(len(d))
for i,j in d.items():
    print(j,end=" ")   







# Name_Exercise_45
#Word Order
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque
d = deque()
n = int(input())
for i in range(n):
    s = input().split()
    if(s[0]) == "append":
        d.append(s[1])
    elif(s[0] == "pop"):
        d.pop()
    elif(s[0] == "popleft"):
        
        d.popleft()
    elif(s[0] == "appendleft"):
        d.appendleft(s[1])

for i in d:
    print(i,end=" ")







# Name_Exercise_46
#Collections.deque()
#!/bin/python3

import math
import os
import random
import re
import sys
from collections import OrderedDict
d = OrderedDict()


if __name__ == '__main__':
    
    s = input()
   
    for i in s:
        if i in d:
            d[i] = d[i]+1
            
                
        else:
            d[i] = 1
    
    d = dict(sorted(d.items(), key=lambda item: (-item[1], item[0])))
    k = 0
    for i,j in d.items():
        print(i, j)
        k+=1
        if(k==3):
            break   
    
    









# Name_Exercise_47
#Company Logo
# Enter your code here. Read input from STDIN. Print output to STDOUT
import collections
t = int(input())
for i in range(t):
    r = "Yes"
        
    n = int(input())
    b = collections.deque((map(int, input().split())))
    p = [max(b[0], b[-1])]

    while len(b) != 0:
        m = max(b[0], b[-1])
        
        if m > p[-1]:
            r = "No"
            break
        
        else:
            p.append(m)
               
        if m == b[0]:
            b.popleft()
        else:
            b.pop()
    print(r)





# Name_Exercise_48
#Piling Up!
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter

x = int(input())    
s = Counter(list(map(int, input().split()))) #for each size as key and quatity as value
n = int(input())     
total = 0

for i in range(n):
    size, cost = map(int, input().split())
    
    if s[size]: #if exsist in collection
        s[size] -= 1 #quantity decrease
        total += cost
    

print(total)








# Date and Time (all– total: 2- max points: 40)
# https://www.hackerrank.com/domains/python/py-date-time
# Name_Exercise_49
#Calendar Module
# Enter your code here. Read input from STDIN. Print output to STDOUT

import calendar
m, d, y = map(int,input().split())
i = calendar.weekday(y, m, d)  #index of the week day
w = list(calendar.day_name) #list of days in week
print(w[i].upper())



# Name_Exercise_50
#Time Delta
#!/bin/python3

import math
import os
import random
import re
import sys
from datetime import datetime

# Complete the time_delta function below.
# Day dd Mon yyyy hh:mm:ss +xxxx
# %a  %d %b  %Y   %H:%M:%S %z 



def time_delta(t1, t2):
    f = "%a %d %b %Y %H:%M:%S %z"
    t1 = datetime.strptime(t1, f)
    t2 = datetime.strptime(t2, f)
    s = abs((t1-t2).total_seconds())
    return str(int(s))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()






# Exceptions (only 1- max points: 10)
# https://www.hackerrank.com/challenges/exceptions
# Name_Exercise_51
#Exceptions
# Enter your code here. Read input from STDIN. Print output to STDOUT
t=int(input())
for i in range(t):
    try:
        a,b= map(int,input().split())
        print(a//b)
    except ValueError as e:
        print("Error Code:",e)
    except ZeroDivisionError as e:
        print("Error Code:",e)




# Built-ins (only 3- max points: 80)
# https://www.hackerrank.com/challenges/zipped
# https://www.hackerrank.com/challenges/python-sort-sort
# https://www.hackerrank.com/challenges/ginorts
# Name_Exercise_52
#Zipped!
# Enter your code here. Read input from STDIN. Print output to STDOUT
n, x =map(int,input().split())
r=[]
for _ in range(x):
    r.append(list(map(float, input().split())))
    
t=(zip(*r))
for i in t:
    print(sum(i)/float(x))









# Name_Exercise_53
#Athlete Sort
#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input().strip())
    
    arr =sorted(arr,key=lambda x: x[k]) #each value of arr is sent to the lambda as x, and it returns x[k] the value. the sorted takes it as the key to order it
    for i in arr:
        print (" ".join(map(str,i))) #formating it to print
        








# Name_Exercise_54
#ginortS
# Enter your code here. Read input from STDIN. Print output to STDOUT
u = ""
l = ""
o = ""
e = ""
for i in input():
    if i.isupper():
        u+=i
    elif i.islower():
        l+=i
    elif int(i)%2 == 0:
        e += i
    else:
        o+=i
print("".join(sorted(l))+"".join(sorted(u))+"".join(sorted(o))+"".join(sorted(e)))






# Python Functionals (only 1- max points: 20)
# https://www.hackerrank.com/challenges/map-and-lambda-expression
# Name_Exercise_55
# Map and Lambda Function
cube = lambda x: x*x*x # complete the lambda function 

def fibonacci(n,a=0,b=1):
    if n == 0:
        return []
    return [a] + fibonacci(n-1,b,a+b)






#Regex and Parsing challenges (all– total: 17- max points: 560)
# https://www.hackerrank.com/domains/python/py-regex
# Name_Exercise_56
#Detect Floating Point Number
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
for i in range(int(input())):
    print(bool(re.match(r'^[+-]?\d*\.\d*$',input())))




# Name_Exercise_57
#Re.split()
regex_pattern = r"[/,,.]+"	# Do not delete 'r'.



# Name_Exercise_58
#Group(), Groups() & Groupdict()
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
s = input()
n = ""
m = re.findall(r'([a-zA-Z0-9])', s)
# print(m)
for i in m:
    # print(i)
    j = i+i
    m2 = len(re.findall(j,s))
    # print(m2)
    if m2>0:
        n = i
        break
if n != "":
    print(n)
else:
    print("-1")









# Name_Exercise_59
#Re.findall() & Re.finditer()
# Enter your code here. Read input from STDIN. Print output to STDOUT

# (?<=[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm]) looks for a conso behind
# [aeiouAEIOU]{2,} 2 or more vowel
# (?=[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm]) looks for a conso next

import re
s = input()
n = ""

m = re.findall(r'(?<=[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm])[aeiouAEIOU]{2,}(?=[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm])', s)

for i in m:
    print(i)
if(len(m)<1):
    print(-1)






# Name_Exercise_60
#Re.start() & Re.end()
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
s = input()
k = input()

m = re.search(k,s)
p = 0
while(p<len(s)):
    m = re.search(k,s[p:])
    if(m):
        # print(s[p:])
        print("(",p+m.start(),", ",p+m.end()-1,")",sep="")
        # print(s[p+m.start():p+m.end()])
        p+=m.start()+1
        
    else:
        break
if(p==0):
    print("(-1, -1)")
    
    

    


# Name_Exercise_61
#Regex Substitution
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
n = int(input())
def change(m):
    if m.group() == "&&":
        return "and"
    elif m.group() == "||":
        return "or"
for i in range(n):
    s = input()
    if(len(s)>0):
        if(s[0] == "#"):
            print(s)
        else:
            print(re.sub(r'(?<=\s)(&&|\|\|)(?=\s)', change, s))
    else:
        print()





# Name_Exercise_62
#Validating Roman Numerals
#I 1       1 V?I{0,3} IF NO V
#II 2      2 V?I{0,3} IF NO V
#III 3     3 V?I{0,3} IF NO V
#IV 4       
#V 5       0 V?I{0,3} IF there is V
#VI 6      1 V?I{0,3} IF there is V
#VII 7     2 V?I{0,3} IF there is V
#VIII 8    3 V?I{0,3}
#IX 9       
#X 10      1 L?X{0,3} if NO L
#XX 20     2 L?X{0,3} if NO L
#XXX 30    3 L?X{0,3} if NO L
#XL 40 
#L 50      0 L?X{0,3} if there is L
#LX 60     1 L?X{0,3} if there is L
#LXX 70    2 L?X{0,3} if there is L
#LXXX 80   3 L?X{0,3} if there is L

#XC 90  

#C 100     1 D?C{0,3} if no D
#CC 200    2 D?C{0,3} if no D
#CCC 300   3 D?C{0,3} if no D

#CD 400

#D 500     0 D?C{0,3} if is D   
#DC 600    1 D?C{0,3} if is D
#DCC 700   2 D?C{0,3} if is D
#DCCC 800  3 D?C{0,3} if is D
#CM 900

#M 1000    1
#MM 2000   2
#MMM 3000  3


# ^ start $ end
regex_pattern = r"^M{0,3}(CM|D?C{0,3}|CD)(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$"







# Name_Exercise_63
#Validating phone numbers
# Enter your code here. Read input from STDIN. Print output to STDOUT

import re

n = int(input())
for i in range(n):
    s = input()
    if re.match(r'^[789]\d{9}$', s):
        print("YES")
    else:
        print("NO")






# Name_Exercise_64
#Validating and Parsing Email Addresses
# 1st charecter should be letter, then can be alphanum/./_/- then it must be added with @ and again some alpha, then a fullstop again alpha from 1-4 (.tech is 4 letters )  
import re
n = int(input())
for i in range(n):
    s = input().split()
    temp = s[1][1:len(s[1])-1] #to remove <> 
    # print(temp)
    if re.match(r'^[a-zA-Z][\w._-]+@[a-zA-Z]+\.[a-zA-Z]{1,4}$', temp):
        print(s[0],s[1])
    




# Name_Exercise_65
#Hex Color Code
# Enter your code here. Read input from STDIN. Print output to STDOUT
#3 to 6 letters numbers, [a-f], [A-F]
import re
n = int(input())
for i in range(n):
    s = input()
    if(len(s)!=0):
        if(s[0]!="#"):
            m = re.findall(r'#[\da-fA-F]{3,6}',s)
            for i in m:
                print(i)
    



# Name_Exercise_66
#HTML Parser - Part 1
# Enter your code here. Read input from STDIN. Print output to STDOUT

from html.parser import HTMLParser #html.parser is for py3  HTMLParser shows error

# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Start :", tag)
        for i in attrs:
            print(f"-> {i[0]} > {i[1]}")
    def handle_endtag(self, tag):
        print("End   :", tag)
    def handle_startendtag(self, tag, attrs):
        print("Empty :", tag)
        for i in attrs:
            print(f"-> {i[0]} > {i[1]}")

# instantiate the parser and fed it some HTML
parser = MyHTMLParser()
for i in range(int(input())):
    parser.feed(input())



# Name_Exercise_67
#HTML Parser - Part 2
# Enter your code here. Read input from STDIN. Print output to STDOUT

from html.parser import HTMLParser #html.parser is for py3  HTMLParser shows error

# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):
    def handle_comment(self, data):
        if '\n' in data:
            print(">>> Multi-line Comment")
        else:
            print(">>> Single-line Comment")
        print(data)
        
    def handle_data(self, data):
        if '\n' not in data:
            print(">>> Data")
            print(data)
# instantiate the parser and fed it some HTML
parser = MyHTMLParser()
s = ""
for i in range(int(input())):
    s+=input()+"\n"    #comments can be multiline so parser must know all of the data instead of a single line, so the full data is passed
parser.feed(s)





# Name_Exercise_68
#Detect HTML Tags, Attributes and Attribute Values
# Enter your code here. Read input from STDIN. Print output to STDOUT

from html.parser import HTMLParser #html.parser is for py3  HTMLParser shows error

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        if attrs:
            for i in attrs:
                print(f'-> {i[0]} > {i[1]}')
    def handle_startendtag(self, tag, attrs):
        print(tag)
        for i in attrs:
            print(f'-> {i[0]} > {i[1]}')
  

parser = MyHTMLParser()
for i in range(int(input())):
    parser.feed(input())
    
    






# Name_Exercise_69
#Validating UID
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

n = int(input())
for i in range(n):
    s = input()
    uppercase_count = len(re.findall(r"[A-Z]", s))
    digit_count = len(re.findall(r"\d", s))
    Non_alnum_count = len(re.findall(r"[^\w]", s)) #must be == 0  (^ has 2 job. ^ in side a [^abc] is negation else "^abc" it is the 1st thing to find)
    
    #len(s)== len(set(s)) if s len is equal to set(s) len then no char repeats as set has no repeating char
    if  uppercase_count >= 2 and digit_count>=3 and  Non_alnum_count==0 and len(s)== len(set(s)) and(len(s) == 10)  :
        print("Valid")
    else:
        print("Invalid")








# Name_Exercise_70
#Validating Credit Card Numbers
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

n = int(input())
for i in range(n):
    s = input()
    s2 = "".join(s.split("-"))
    after_every_4_char = True
    if('-' in s):
       after_every_4_char =  bool(re.match(r"^(?!-)(?:\w{4}-?)*(?<!-)$", s))
       # ^(?!-) so - is not in begin ..... (?<!-)$ that - is not in end 
    
    # ?! looks next char 
    # .* any string
    # (.)(\1{3,}) here it checks for 3 same string as the same any string
    four_char_not_same = bool(re.match(r"^(?!.*(.)(\1{3,})).*$", s2))
    
        
    if re.match(r"^[456]", s)  and len(s2) == 16 and s2.isdigit() and after_every_4_char and four_char_not_same :
        print("Valid")
    else:
        print("Invalid")









# Name_Exercise_71
#Validating Postal Codes
regex_integer_in_range = r"^[1-9][0-9]{5}$"    # Do not delete 'r'.
regex_alternating_repetitive_digit_pair = r"(?=(\d)\d\1)"    # Do not delete 'r'.
#(\d) any digit
#?= looks next 
#\d finds another digit
#\1 mathes with 1st group 
# so it checks a digit exsists in next 12233 here it will take 2






# Name_Exercise_72
#Matrix Script
#!/bin/python3

import math
import os
import random
import re
import sys




first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

s = ""
for i in range(m):
    for j in range(n):
        s+=matrix[j][i]
# print(s) 
# s is just ordering the matrix into a string in order
#looks behind for a char(alpha num) (?<=\w)
# ([^\w]+) captures non alpha num 1 or more in a group 
#(?=\w) look next for a char (alpha num)

#

print( re.sub(r'(?<=\w)([^\w]+)(?=\w)', ' ', s))









# XML (all– total: 2- max points: 40)
# https://www.hackerrank.com/domains/python/xml
# Name_Exercise_73
#XML 1 - Find the Score


def get_attr_number(node):
    total = 0
    for i in node.iter(): #makeing it iterable
        total += len(i.attrib)  #each has attrib
    return total







# Name_Exercise_74
#XML2 - Find the Maximum Depth


maxdepth = 0
def depth(elem, level):
    global maxdepth
    # your code goes here
    if (level == maxdepth):
        maxdepth += 1
    for i in elem:
        depth(i, level + 1)





#  Closures and Decorations (all– total: 2- max points: 60)
#  https://www.hackerrank.com/domains/python/closures-and-decorators
# Name_Exercise_75
#Standardize Mobile Number Using Decorators
def wrapper(f): #f = sort_phone
    def fun(l):
        for i in range(len(l)):
            l[i] = '+91 '+l[i][-10:-5]+' '+l[i][-5:]
        return f(l)   #the function sort_phone is being called
    return fun




# Name_Exercise_76
#Decorators 2 - Name Directory


def person_lister(f): # f = name_format 
    def inner(people):
        people.sort(key=lambda x: int(x[2])) #sorting by age index 2
        
        
        for i in range(len(people)):
            people[i] = f(people[i]) #formating by the name_format function
            
            
        return people #returning the list to be printed  
    return inner





# Numpy (all– total: 15- max points: 300)
# https://www.hackerrank.com/domains/python/numpy
# Name_Exercise_77
#Arrays


def arrays(arr):
    arr.reverse()
    arr = numpy.array(arr, float)
    return arr 





# Name_Exercise_78
#Shape and Reshape


# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy as np
a = list(map(int,input().split()))
a = np.array(a)
print(np.reshape(a,(3,3)))





# Name_Exercise_79
#Transpose and Flatten
# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy as np
n = list(map(int,input().split()))
a = []
for i in range(n[0]):
    a.append(list(map(int,input().split())))
    

a = np.array(a)
print(np.transpose(a))

print(a.flatten())







# Name_Exercise_80
#Concatenate
# Enter your code here. Read input from STDIN. Print output to STDOUT

import numpy as np
n = list(map(int,input().split()))
a = []
for i in range(n[0]):
    a.append(list(map(int,input().split())))

for i in range(n[1]):
    a.append(list(map(int,input().split())))
a = np.array(a)
print(a)







# Name_Exercise_81
#Zeros and Ones
# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy as np
n = tuple(map(int,input().split())) 
#n[0] = size of array with 0
#n[1] = size of matrix with that array
#... goes on
print(np.zeros(n, dtype = np.int)) 
print(np.ones(n, dtype = np.int))







# Name_Exercise_82
#Eye and Identity
import numpy as np
np.set_printoptions(legacy = '1.13')
n = list(map(int,input().split()))

print (np.eye(n[0],n[1], k = 0))




# Name_Exercise_83
#Array Mathematics
# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy as np
n = list(map(int,input().split()))
a = []
b = []
for i in range(n[0]):
    a.append(list(map(int,input().split())))

for i in range(n[0]):
    b.append(list(map(int,input().split())))

a = np.array(a)
b = np.array(b)

print(np.add(a,b))
print(np.subtract(a,b))
print(np.multiply(a,b))
print(np.floor_divide(a,b))
print(np.mod(a,b))
print(np.power(a,b))








# Name_Exercise_84
#Floor, Ceil and Rint
# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy as np
np.set_printoptions(legacy = '1.13')
n = np.array(input().split(),dtype = np.float)

print(np.floor(n))
print(np.ceil(n))
print(np.rint(n))






# Name_Exercise_85
#Sum and Prod

# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy as np
np.set_printoptions(legacy = '1.13')
n = list(map(int,input().split()))
a = []
for i in range(n[0]):
    a.append(list(map(int,input().split())))
a = np.array(a)
a = np.sum(a, axis = 0)
a = np.prod(a,axis = 0)
print(a)
    





# Name_Exercise_86
#Min and Max
# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy as np
np.set_printoptions(legacy = '1.13')
n = list(map(int,input().split()))
a = []
for i in range(n[0]):
    a.append(list(map(int,input().split())))
a = np.array(a)
a = np.min(a, axis = 1)
a = np.max(a,axis = 0)
print(a)
    






# Name_Exercise_87
#Mean, Var, and Std
# Enter your code here. Read input from STDIN. Print output to STDOUT

import numpy as np
n = list(map(int,input().split()))
a = []
for i in range(n[0]):
    a.append(list(map(int,input().split())))
a = np.array(a)
print(np.mean(a, axis = 1))
print(np.var(a, axis = 0))
print(np.round(np.std(a, axis = None),11)) #round place 11




# Name_Exercise_88
#Dot and Cross
# Enter your code here. Read input from STDIN. Print output to STDOUT

import numpy as np
n = int(input())
a = []
for i in range(n):
    a.append(list(map(int,input().split())))
b = []
for i in range(n):
    b.append(list(map(int,input().split())))
a = np.array(a)
b = np.array(b)
print(np.dot(a, b))





# Name_Exercise_89
#Inner and Outer
# Enter your code here. Read input from STDIN. Print output to STDOUT
# Enter your code here. Read input from STDIN. Print output to STDOUT

import numpy as np

a = list(map(int,input().split()))
b = list(map(int,input().split()))
print(np.inner(a,b))
print(np.outer(a,b))



# Name_Exercise_90
#Polynomials

import numpy as np

p = list(map(float,input().split()))
x = int(input())
print(np.polyval(p,x))




# Name_Exercise_91
#Linear Algebra
# Enter your code here. Read input from STDIN. Print output to STDOUT

import numpy as np
n = int(input())
a = []
for i in range(n):
    a.append(list(map(float,input().split())))
print(np.round(np.linalg.det(a),2))











































#PROBLEM2
 # https://www.hackerrank.com/challenges/birthday-cake-candles
 # Name_Exercise_92
 #Birthday Cake Candles
 #!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#

def birthdayCakeCandles(candles):
    max1 = candles[0]
    count = 0
    for i in range(len(candles)):
        if (candles[i]>max1):
            max1 = candles[i]
            count = 1
        elif(candles[i]== max1):
            count+=1
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    fptr.write(str(result) + '\n')

    fptr.close()


 
 # https://www.hackerrank.com/challenges/kangaroo
 # Name_Exercise_93
 # Number Line Jumps
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'kangaroo' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER x1
#  2. INTEGER v1
#  3. INTEGER x2
#  4. INTEGER v2
#

def kangaroo(x1, v1, x2, v2):
    if (v1 == v2):
        if(x1 == x2):
            return "YES"
        else:
            return "NO"
            
    
    r1 = (x2 - x1)/(v1 - v2)
    r2 = (x2 - x1)//(v1 - v2)
    
    if r1 == r2 and r2>0:
        
        return "YES"
    else:
        return "NO"
    
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    x1 = int(first_multiple_input[0])

    v1 = int(first_multiple_input[1])

    x2 = int(first_multiple_input[2])

    v2 = int(first_multiple_input[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()
    
    
    
    
    
    
    
    

 # https://www.hackerrank.com/challenges/strange-advertising
 # Name_Exercise_94
 # Viral Advertising
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'viralAdvertising' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def viralAdvertising(n):
    
    share = 5
    like = 0
    total_like = 0
    for i in range(n):
        total_like += share//2
        like = share//2
        share = like * 3
    return total_like

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()




 
 # https://www.hackerrank.com/challenges/recursive-digit-sum
 # Name_Exercise_95
 # Recursive Digit Sum
 #!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
# return  n if(int(n) < 10) else superDigit(str(sum(int(i) for i in n*k )),1)

  
# here instead of making a larger string "123123123" = 18, i can just do sum("123") * 3 =which is also 18 but loops less T-T 

def superDigit(n, k):
    return  n if(int(n) < 10) else superDigit(str(sum(int(i) for i in n )*k),1)
    
    # flag = True
    # while(len(n) > 1):
    #     if(flag):
    #         n = str(sum(int(i) for i in n*k ))
    #         flag = False
    #     else:
    #         n = str(sum(int(i) for i in n ))
        
    # return n
        

if __name__ == '__main__':
    input_data = sys.stdin.read().strip().split()
    n = input_data[0]
    k = int(input_data[1])
    result = superDigit(n, k)
    sys.stdout.write(str(result) + '\n')




 
 
 
 
 
 
 # https://www.hackerrank.com/challenges/insertionsort1
 # Name_Exercise_96
 # Insertion Sort - Part 1
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    l = arr[-1]
    for i in range(n-2,-1,-1):
        # print(i)
        if (arr[i]>l):
            arr[i+1] = arr[i]
            
            for j in range(n):
                print(arr[j],end=" ")
            print()
        else:
            arr[i+1] = l
            for j in range(n):
                print(arr[j],end=" ")
            print()
            break
            
        
        
        
    # for j in range(n):
    #     print(arr[j],end=" ")
    # print()    
    if(l not in arr):
        arr[0] = l
        for j in range(n):
            print(arr[j],end=" ")
        print()
        
    
            

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)





 
 # https://www.hackerrank.com/challenges/insertionsort2
 # Name_Exercise_97
 # Insertion Sort - Part 2
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort2' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort2(n, arr):
    for i in range(1,n):
        for j in range(0,i):
            if(arr[i] < arr[j]):
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp
                
        # print(arr)
        for k in arr:
            print(k, end=" ")
        print()

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort2(n, arr)
