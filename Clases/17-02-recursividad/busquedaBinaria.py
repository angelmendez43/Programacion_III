#dos decimales son un problema para hacer las busqueda binaria, por el motivo que no podemos bucar en un arreglo un numero decimal.
# solucion
#print(9//2) aproximado en la division. 

def binario(arr,x,inicio=0,fin= None):  #fin sera igual a una variable es nuestra primera interacion.
    if(fin == None):
        fin = len(arr)-1

    mid =(inicio + fin) //2
    if(x == arr[mid] ):
        print("Numero encontrado")
        return mid        

    elif(x< arr[mid]):
        return binario(arr,x,inicio,mid-1)
    else: 
        return binario(arr,x,mid+1,fin)


arr = [2,5,8,10,13,20,23,50,90]
x = 23

print(binario(arr,x))