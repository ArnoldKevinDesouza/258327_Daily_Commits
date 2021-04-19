if __name__ == '__main__':
    n = int(input())
   
    list= list(set(map(int, input().split())))

list.sort(reverse=True)

print(list[1])
