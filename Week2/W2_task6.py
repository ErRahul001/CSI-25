# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
stock = list(map(int,input().split(" ")))

from collections import Counter

dic =  Counter(stock)
x = int(input())

z=0
for i in range(x):
    size,price = map(int,input().split(" "))
    
    if dic[size]:
        dic[size]-=1
        z=z+price
        
print(z)