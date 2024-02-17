def binario(num):
    if(num == 0):
        return ""
    else:
        return binario(num//2) + str(num%2)

print(binario(100))    

    
