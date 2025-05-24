def minion_game(string):
    # your code goes here
    n = len(string)
    vowels = 'AEIOU'
    stuart = 0
    kevin = 0
    for i in range(n):
        if string[i] in vowels:
            kevin += n - i
        else:
            stuart += n - i

    if stuart > kevin:
        print(f"Stuart {stuart}")
    elif kevin > stuart:
        print(f"Kevin {kevin}")
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)