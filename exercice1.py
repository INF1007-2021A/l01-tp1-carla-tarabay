def fizzBuzz(n):
    if n%3==0 and n%5==0:
        print("fizzbuzz")


    elif n%3==0:
        print("fizz")

    elif n%5==0:
       print("buzz")

    else:
        print("n est ni multiple de 3 ni de 5")
    resultat= n
    return resultat




if __name__ == '__main__':
    n = int(input("indiquez le nombre: "))
    print(fizzBuzz(n))
