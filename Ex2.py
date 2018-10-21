L = [-3,-2,-1,0,1, 2, 3]
S =  "Exp2"
def list_error(z):
    if type(z) == list:
        #Counts the number of positive integers in the list
        x = len([num for num in z if num > 0])
        print (x)
    else:
        #Gives out error if input is not a list
        raise TypeError
list_error(L)
list_error(S)
