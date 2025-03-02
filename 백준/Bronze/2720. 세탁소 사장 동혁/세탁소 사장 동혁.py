a=int(input())

for i in range(a):
    c=int(input())
    quarter=c//25
    c%=25
    dime=c//10
    c%=10
    nickel=c//5
    c%=5
    penny=c
    
    print(quarter, dime, nickel, penny)

