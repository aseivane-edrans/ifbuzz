FIZZ = 1
BUZZ = 2
FIZZBUZZ = 3

def init():
    for i in range(1,100):
        j=0
        if(i%3 == 0): j=FIZZ
        if(i%5 == 0): j=BUZZ
        if(i%3 == 0 and i%5 == 0): j=FIZZBUZZ

        match j:
            case 0: print(i)
            case 1: print("Fizz")
            case 2: print("Buzz")
            case 3: print("FizzBuzz") 

init()