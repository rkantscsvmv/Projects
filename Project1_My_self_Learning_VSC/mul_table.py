def mul_table(numm):
    # num=input("Enter number for mul table to be printed")
    for i in range(1,11):
        print(f"{numm}*{i} = ",numm*i)

n=int(input("Enter number for mul table to be printed : "))
print("\n")
mul_table(n)