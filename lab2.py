#Yamel Hernandez
#80590552
#CS 2302
#Diego Aguirre
#Lab 2
#Purpose of this lab was to understand how to
#implement linked lists, their sorting algorithms
#and how dictionaries are used

#######################################################################################


    #solution a
    # Every time you read a password from the file, check (using a loop) if that
    #password has already been added to the linked list. That is, you need to traverse the
    #linked list to see if that password has been added already. If the password is already in
    #your linked list, update the number of times the password has been seen in the file.
    #Otherwise, add a the password to the linked list.

from Node import Node

def check1(x, psswrd):
    temp = x
    while temp is not None:
        if temp.password is psswrd:
            temp.count += 1
            return True
    return False

    #solution B
    #This is a variation of Solution A. Instead of traversing the linked list to check if
    #a password has been seen before, we will be using what is called a dictionary. Read the
    #following code snippet to understand how to use a dictionary in a similar context:
    
def check2(dct, psswrd):
    if psswrd in dct.keys():
        dct[psswrd] += 1
        return True
    return False
    
    
    #Sort the list (in descending order) using bubble sort, and print the 20 most
    #used passwords along with the number of times they appear in the file.
    
def linkedLength(x):
    i = 0
    while x is not None:
        i += 1
        x = x.next
    return i


def bubble(x):
    head = x
    temp = x
    lengthOfList = linkedLength(x)
    if temp != None:
        return temp
    for i in range(lengthOfList):
        temp = head #after every iteration returns to head to go thru list again
        for j in range(lengthOfList):
            if temp.password < temp.next.password:
                tempPass = temp.password
                temp.password = temp.next.password
                temp.next.password = tempPass
            temp = temp.next
    return temp
    
    #Sort the list (in descending order) using merge sort, and print the 20 most
    #used passwords along with the number of times they appear in the file.

def merge(x):
    temp = x
    if x == None or x.next == None:
        return x
    l = linkedLength(x)
    for i in range(int(l/2) - 1): #splits
        temp = temp.next
    start2 = temp.next
    temp.next = None
    start1 = x
    sorted1 = merge(start1)
    sorted2 = merge(start2)
    sortedList = None
    if sorted1.password > sorted2.password:
        sortedList = sorted1
        sorted1 = sorted1.next
    else:
        sortedList = sorted2
        sorted2 = sorted2.next
    root = sortedList
    while sorted1 != None and sorted2 != None:
        if sorted1.password > sorted2.password:
            sortedList.next = sorted1
            sorted1 = sorted1.next
        else:
            sortedList.next = sorted2
            sorted2 = sorted2.next
        sortedList = sortedList.next
    
    while sorted1 != None: #combining
        sortedList.next = sorted1
        sorted1 = sorted1.next
        sortedList = sortedList.next
        
    while sorted2 != None:
        sortedList.next = sorted2
        sorted2 = sorted2.next
        sortedList = sortedList.next
        
    return root

########################################################################################

def main():
    use = "/home/yamel/Desktop/CS3/lab2/10-million-combos.txt"
    x = None
    temp = x
    dictionary = {}
    f = open(use, 'r')
    try:
        with open(use) as f:
            for line in f:
                user_info = line.split('\t')
                password = user_info[1]
                if not check2(dictionary, password):
                    dictionary[password] = 1
                if not check1(temp, password):
                    x = Node(password, 1, x)
    except:
        pass
    
    sortedList = merge(x)
    #sortedList = bubble(x) #doesn't work???????
    
    temp = sortedList
    
    while temp is not None:
        print(temp.password)
        temp = temp.next
                
main()
