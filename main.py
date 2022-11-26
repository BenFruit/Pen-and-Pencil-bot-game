import random as r
import jackBot

        

def turn(pens,str):
    if pens == 0:
        print(str,"won!")
        return False
    else:
        return True

    

print("How many pencils you would like to use:")
while True:
    try:
        a = int(input())
        if(a < 1):
            raise Exception
        break
    except ValueError:
        print("The number of pencils should be numeric")
    except Exception:
        print("The number of pencils should be positive")
while True:
    try:
        str = input('Who will be the first (John, Jack):\n')
        if str != 'John' and str != 'Jack':
            raise Exception
        break
    except Exception:
        print("Choose between 'John' and 'Jack")
    
print('|'*a)
while turn(a,str):
    print(str+"'s",'turn!')
    if(str == 'Jack'):
        take = jackBot.choose(a)
        print(take)
        a -= take
        print('|'*a)
    else:
        while True:
            try:
                take = int(input())
                if take > 3 or take < 1:
                    raise ValueError
                if take > a:
                    raise Exception
                a -= take
                print('|'*a)
                break
            except ValueError:
                print("Possible values: '1', '2' or '3'")
            except Exception:
                print("Too many pencils were taken") 
    if str == 'John':
        str = 'Jack'
    else:
        str = 'John'
    
