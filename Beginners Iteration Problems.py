print ("---Check Password---")
password = False
flag = 1
while not password:
    if flag > 3:
        print ("Locked.")
        break
    ans = input("Enter password.\n>>")
    if ans == ("hello"):
        password = True
        print ("Correct password.")
    flag += 1
print ("---Name Loop---")
num = int(input("Enter a number\n>>"))
name = input("Enter your name\n>>")
for i in range(num):
    print (name)
print ("---Multiplication---")
num = int(input("Enter a positive integer\n>>"))
while num<0:
    print ("Not a positive integer.")
    num = int(input("Enter a positive integer\n>>"))
for i in range (1, num+1):
    for j in range (i, num+1):
        print (f"{i}*{j}={i*j}", end =" ")
    print ()
print ("---Prime Number---")
prime = True
num =int(input("Input an integer.\n>>"))
for i in range (2, num):
    if num % i == 0:
        prime = False
if prime :
    print (num,"is a prime number.")
else:
    print(num,"isn't a prime number.")
print ("---FizzBuzz---")
for i in range (1,101):
    print (i,end =" ")
    if i % 3 == 0:
        print ("Fizz", end =" ")
    if i % 5 == 0:
        print ("Buzz", end =" ")
    print ()
