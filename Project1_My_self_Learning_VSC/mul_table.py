def mul_table(num):
    # num=input("Enter number for mul table to be printed")
    for i in range(1,11):
        print(f"{num}*{i} = ",num*i)

n=int(input("Enter number for mul table to be printed : "))
mul_table(n)