from functools import wraps
 
def Outer(func):
    @wraps(func)
    def inner(*args, **kwargs):
        print("F")
        result = func(*args,**kwargs)
        print("---- After the Function ----")
        return result
    return inner

@Outer
def myorder(greet,tea):
    print(f"You {greet} order {tea}")       

myorder("Harsh","Masala Chai")    