import time
def countdown(n):
    print(n)
    if n == 0:
        print("End of Test")
    else:
        time.sleep(1)
        countdown(n-1)

