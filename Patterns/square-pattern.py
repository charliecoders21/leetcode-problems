def square_pattern(n):
    num=1
    for item in range(n):
        for j in range(n):
            print(num,end="")
            num+=1
            
        print()
print(square_pattern(3))