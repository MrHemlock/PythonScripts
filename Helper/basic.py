x=50
def func(x):
    print(f" X is {x}")
    x=200
    print(f"I just locally changed X to {x}")    
func(x)