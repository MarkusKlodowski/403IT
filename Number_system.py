#import timeit

def BinaryToDecimal (binary):
    binary = str(binary)
    decimal = 0
    for i in range(len(binary)):
        decimal += int(binary[i]) * 2**(len(binary)-i-1)
    return decimal

def BinaryToHex (binary: int):
    hex = ""
    padding = 4 - (len(str(binary)) % 4)
    if padding != 4:
        binary = '0' * padding + str(binary)
    for i in range(0, len(binary), 4):
        decimalValue = int(binary[i:i+4], 2)
        if decimalValue > 10:
            decimalValue = chr(ord('A') + decimalValue - 10)#chr(ord('A') genrated by github copilot I just didnt know how to itrate through the alphabet
        hex += str(decimalValue)  
    return hex, 
#time_taken = timeit.timeit(lambda: BinaryToHex(110110), number=1000000)
#print(f"Elapsed Time: {time_taken:.6f} seconds") (this was ment to test the speed of the function)

def DecimalToBinary (decimal):
    binary = ""
    while decimal > 0:
        binary = str(decimal % 2) + binary
        decimal = decimal // 2
    return binary  

def DecimalToHex (decimal: int):
    hex = ""
    while decimal > 0:
        decimalValue = int(decimal%16)
        if decimalValue > 10:
            decimalValue = chr(ord('A') + decimalValue - 10)#chr(ord('A') genrated by github copilot I just didnt know how to itrate through the alphabet
        decimal = decimal//16
        hex = str(decimalValue) +hex      
    return hex
def HexToBinary (hex: str):
    bianry = 0
    for i in range(len(hex)):
        if hex[i].isnumeric() == True:
            binaryValue = int(hex[i])
        else:
            binaryValue = (ord(hex[i]) - 65) + 10
        bianry += binaryValue * 16**(len(hex)-i-1)
    bianry = DecimalToBinary(bianry)    
    return bianry
#technically works but I dont like it

def HexToDecimal(hex: str):
    decimal = 0
    for i in range(len(hex)):
        if hex[i].isnumeric() == True:
            decimalValue = int(hex[i])
        else:
            decimalValue = (ord(hex[i]) - 65) + 10
        decimal += decimalValue * 16**(len(hex)-i-1)
    return decimal
