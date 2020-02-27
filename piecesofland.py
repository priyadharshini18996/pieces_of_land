
def maximum_piece(no_of_input):
 
    for arbitary_point in range(1,no_of_input+1):
        lst[arbitary_point]=arbitary_point*(arbitary_point-1)/2 + arbitary_point*(arbitary_point-1)*(arbitary_point-2)*(arbitary_point-3)/24 + 1
        print "for" ,arbitary_point, "arbitary point maximum number pieces of land possible is",lst[arbitary_point]
    return lst[arbitary_point]

def user_input():
    pass
iteration=-1
while (iteration<1):
    
    for iteration_index in range(1):
        print "Enter number of test cases:"
        
        iteration=int(input())
        if(iteration<0):
            print "enter valid number"
    
    while(iteration_index<=iteration):
        no_of_input = int(raw_input("Enter the number: "))
        lst =[]
        for number in range(1,no_of_input+1):
            lst1=list(map(int,raw_input()))
            lst.append(lst1)
            lst.append(1)
            iteration_index+=1
               
        maximum_piece(no_of_input)
                  
user_input()      
    
            

    
    
    
   




# user_input()