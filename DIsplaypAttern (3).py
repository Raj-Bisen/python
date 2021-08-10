# Accept number from user and print below pattern
#Input : 5
#Output : Marvellous    Marvellous   Marvellous   Marvellous   Marvellous
def Display(no):
    for i in range(no):
        print("Marvellous")
        
   

def main():
    print("Enter the number")
    value1 = int(input())
    
    Display(value1)
    

    

if __name__=="__main__":
    main()