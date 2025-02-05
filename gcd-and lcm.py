def gcd (a,b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
def lcm (a,b):
    return int((a * b) / gcd(a,b))
[a,b]=list(map(int,input("enter two numbers seperated by space : ").split()))
print("THE GCD OF NUMBERS IS ", gcd(a,b))
print("THE LCM OF NUMBERS IS ",lcm(a,b))