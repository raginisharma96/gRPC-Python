def validatePrime(num:int) -> bool:
    count = 0
    for i in range(1,num+1):
        if num%i == 0:
            count+=1
        
    if count>2:
        return False
    else:
        return True