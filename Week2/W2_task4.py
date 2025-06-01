def print_rangoli(size):
    # your code goes here
    alp = [chr(i) for i in range(97,123)]
    alp = alp[:size]
    indices = list(range(size))
    indices = indices[:-1]+indices[::-1]
    for i in indices:
        start_ind = i + 1
        orig = alp[-start_ind:]
        rev = orig[::-1]
        row = rev + orig[1:]
        row = "-".join(row)
        width = size*4-3
        row = row.center(width,"-")
        print(row)
        

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)