for x in range(0,101,1):
    print(x)
for x in range(5,1001,5):
    print(x)
for x  in range(101):
    print(x)
    if x%10 == 0:
        print("Coding Dojo") 
    elif x % 5 == 0:
        print("coding")

sum = 0
for x in range(0,500000):
       if x % 2==1:
           sum+= (x)
           print(sum)


for x in range(2018,0,-4):
    print(x)

def flexCount(lowNum, highNum, mult):
  for x in range(highNum, lowNum, -mult):
    print x