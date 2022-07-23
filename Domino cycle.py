

list_of_tuples =input(' Enetr your list of tuples: ')

string_without_brackets = list_of_tuples.replace("[","").replace("]","")

string_without_parantes = string_without_brackets.replace("(","").replace(")","")

string_without_camas = string_without_parantes.replace(",","")

string_without_space = string_without_camas.replace(" ","")


list1= list(string_without_space)
lenlist = len(list1)-2
flag = 0

if not lenlist == -2:

    if list1[0] == list1[-1]:
        for i in range (1,lenlist,2):
           
            if not list1[i] == list1[i+1]:
                print('False')
                flag = 1
                break
            
        if flag == 0:
            print('True')
    else:
        print('False')
else:
    print('True')
               
        




    
    

                                           
    
    
      
    

    

    





    
        
