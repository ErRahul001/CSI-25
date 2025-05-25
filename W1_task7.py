# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations

# Input
n = int(input())                 
letters = input().split()       
k = int(input())                
combs = list(combinations(letters, k))

countwitha=sum([1 for comb in combs if "a" in comb])
ratio=countwitha/len(combs)
print(f"{ratio:.3f}")