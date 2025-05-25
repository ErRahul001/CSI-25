def print_formatted(number):
    # your code goes here
    width = len(bin(number)[2:])
    for i in range(1,number+1):
        print("{:{}d}".format(i,width),end=" ")
        print("{:{}o}".format(i,width),end=" ")
        print("{:{}X}".format(i,width),end=" ")
        print("{:{}b}".format(i,width))
    return ""
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)