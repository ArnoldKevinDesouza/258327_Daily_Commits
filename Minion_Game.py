def minion_game(st):
    vowels = 'AEIOU'

    kevsc = 0
    stusc = 0
    for i in range(len(st)):
        if s[i] in vowels:
            kevsc += (len(st)-i)
        else:
            stusc += (len(st)-i)

    if kevsc > stusc:
        print ("Kevin", kevsc)
    elif kevsc < stusc:
        print ("Stuart", stusc)
    else:
        print ("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)