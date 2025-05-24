# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import *
S = input()

for c,X in groupby(S):
    # it is important to convert c to int implocitly or it'll print "c"
    print(tuple([len(list(X)), int(c)]), end=" ")