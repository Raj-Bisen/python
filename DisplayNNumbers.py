"""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Accept  N number from user and display that N numbers on screen.
# input :    5          10,20,30,40,50
# output :  [10,20,30,40,50]                      
                                                  
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""
def DisplayNNum(List):
    print("Accepted data is : ",List)

def main():   
    arr = []
    print("Enter the number of elements : ")
    size = int(input())
    
    
    for i in range (size):
        print("enter the  element number : ",i+1)
        value = int(input())
        arr.append(value)
    
    DisplayNNum(arr)

if __name__=="__main__":
    main()