import time
def countdown(n):
    print(n)
    if n == 0:
        print("GO!!!")
    else:
        time.sleep(1)
        countdown(n-1)

countdown(int(input("Please enter how long your countdown should be: ")))