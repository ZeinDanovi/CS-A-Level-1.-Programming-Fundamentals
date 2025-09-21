# Create a named tuple to represent a product record with fields like product ID, name, category, and price.
# Implement functions to add new products, remove productsloops, update product details, and search for products by ID or name.


def create_inventory():
    stored_items = [("9960A","pen","crafts","10"),("9342A","pencil","crafts","12")]         #create sample inventory 
    return stored_items                                                                     #returns the inventory 

NewInventory = create_inventory()                                 #stores the result of the inventory creation in a function 


def add_products():
    while True:                                     #sets a loop that keeps prompting for input data until the input is "stop"
        testdata = input("enter products")             #prompts user for a product 
        if testdata == "stop":                      #checks user input isn't "stop"
            break                                      #breaks out of the loop if the user wants to stop adding products 
        else:
            NewInventory.append(testdata)               #adds the new product to the existing inventory 

    return NewInventory                               #returns the final  inventory after any product editions 



def search_products_ID(SearchID):             
    for i in range(len(NewInventory)):            # through all the indexes of tuples in the inventory 
        if NewInventory[i][0] == SearchID:           #if the ID of the current product is == to the SearchID entered 
            return NewInventory[i]                      #the products details are returned 
        
    return "no item found"                        #otherwise the function returns that the product wasn't found 

def search_products_name(SearchName):            
    for i in range(len(NewInventory)):                        #loops through all the indexes of tuples in the inventory 
        if NewInventory[i][1] == SearchName:                    #if the current product's name == the entered search name
            return NewInventory[i]                                    #the product's details are returned 
        
    return "no item found"                             #otherwise the function returns that the product wasn't found 
        
def remove_product_by_name(ProductName):                    
    for i in range(len(NewInventory)):                                       #loops through all the indexes of tuples in the inventory 
        if ProductName == NewInventory[i][1]:                             #if the current product's name == the entered search name
            NewInventory.pop(i)                                           #the product is removed from the list 
            return NewInventory                                            #the new list is removed 
        
    return "no item found"                                                     #if no item is found, the function says product wasn't found 
            


def update_details_by_ID(ProductID,DetailType,NewDetail):                   
    if DetailType == "ID":                                
        for i in range(len(NewInventory)): 
            if ProductID == NewInventory[i][0]:
                NewInventory[i][0] = NewDetail
                return NewInventory

    elif DetailType == "name":
        for i in range(len(NewInventory)): 
            if ProductID == NewInventory[i][1]:
                NewInventory[i][1] = NewDetail
                return NewInventory

    elif DetailType == "category":
        for i in range(len(NewInventory)): 
            if ProductID == NewInventory[i][1]:
                NewInventory[i][2] = NewDetail
                return NewInventory
    
    elif DetailType == "price":
        for i in range(len(NewInventory)): 
            if ProductID == NewInventory[i][1]:
                NewInventory[i][3] = NewDetail
                return NewInventory 

test_data1 = ("9960A","pen","crafts","10")
test_data2 = ("9342A","pencil","crafts","12")

print(NewInventory)
        
    

