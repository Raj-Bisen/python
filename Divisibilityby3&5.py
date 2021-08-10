# Accept number from user and check whether no is divisible by 3 & 5 or not.
# input : 15 
# output : true
#input : 4
#output : false

def ChckDivisible(no):
    if ((no % 3)==0)&((no % 5)== 0): 
        return True        
    else:
        return False

def main():
    print("Enter the number")
    value = int(input())
    
   
    
    bret = ChckDivisible(value)
    if (bret == True):
        print("Number is  divisible by 3 & 5")
    else:
        print("Number is not divisible by 3 & 5")
    
    

    

if __name__=="__main__":
    main()