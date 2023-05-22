#code for question 4

var = [1,[1,2],'abc',(1,2),{1,2},{1:'a',2:'b'},1.4,1j,True,None]
for i in range(len(var)):
    print(var[i],end='=')
    print(type(var[i]))
    ++i
    
#code for question 5
A = int(input("Enter number A: "))
B = int(input("Enter number B: "))

count = 0  # Initialize the count to 0

while A % B == 0:
    A = A / B
    count += 1

if count > 0:
    print(f"{A} is divisible by {B} and can be divided {count} times.")
else:
    print(f"{A} is not divisible by {B}.")   
    
    
#code for question 6

numbers = [2, 9, 12, 15, 21, 30, 33, 36, 40, 45, 50, 55, 60, 63, 70, 75, 80, 81, 85, 90, 95, 99, 105, 110, 120]

for num in numbers:
    if num % 3 == 0:
        print(f"{num} is divisible by 3.")
    else:
        print(f"{num} is not divisible by 3.")    
