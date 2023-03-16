def hello():
    print("Hello User")

def pack(arg1, arg2, arg3):
    return print([arg1, arg2, arg3])

def eat_lunch(list):
    
    if len(list) != 0:
        print(f"First, I eat {list[0]}")
        i = 1
        while i< len(list):
            print(f"Next, I will eat {list[i]}")
            i+=1
    else: print("My lunchbox is empty!")

hello()
pack("phone", "glasses", "book")
eat_lunch(["sandwhich", "apple", "grapes", "chocolate"])
eat_lunch([])
eat_lunch([])