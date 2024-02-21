try:
    a = int(input("Enter Number: "))
    lis1 = [2,4]
    print(lis1[a])
except ValueError:
    print("Enter Valid Int")
except IndexError:
    print("index value not present")