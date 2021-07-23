def next_prime(n):    
    def is_prime(n):
        for j in range(2, n):
            if (n%j) == 0:
                pass
        else:
            pass

    for j in range(n+1, n+150):
        if j > 1:
            for i in range(2, j):
                if (j%i) == 0:
                    break
            else:
                print('The next prime number is:', j)
                num = input("Enter an Integer: ")
                if num.isdigit():
                    n = int(num)
                    next_prime(n)
                else:
                    print("program closed")
                    break
                return
    is_prime(n)

                

num = input("Enter an Integer: ")
if num.isdigit():
    n = int(num)
    next_prime(n)
else:
    print("program closed")





                
