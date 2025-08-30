# functon arguments with "*"

# -------------AVERAGE FINDER-------------


def avg(*numbers):
    sum=0
    for i in range(0,len(numbers)):
        sum=sum+(numbers[i])
    return sum/len(numbers)

numbers=[]
i=1
while (i>0):
    num=int(input("Enter number: "))
    numbers.append(num)
    ask=input("do you want to enter more? (y/n): ")
    if(ask.lower()=="y"):
        continue
    else:
        data=tuple(numbers)
        result=avg(*data)
        print(result)
