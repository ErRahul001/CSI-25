import textwrap

def wrap(string, max_width):
    lst =[]
    for i in range(0,len(string),max_width):
        lst.append(string[i:i+max_width])
    return "\n".join(lst)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)