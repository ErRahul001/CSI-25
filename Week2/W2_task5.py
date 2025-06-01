def merge_the_tools(string, k):
    # your code goes here
    x=0
    s=""
    for i in string:
        if i not in s:
            s=s+i
        x+=1
        if(x==k):
            print(s)
            x=0
            s=""

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)