'''
This is the return module, it takes the ID to return and puts them
through to the database while doing a few small extra things.
'''
def validID(bookID):
    """This function checks to see if the ID is valid. If it isnt it will return
    an error, if it is it will update the database and logfile with it
    """
    bookInfo = dataModule.findID(bookID,dbAddress)
    if(bookInfo == []): #no matching ID
        return("Error: ID not valid")
    elif(bookInfo[5] == '0'):
        #If the memberID is 0, the book is avaiable
        return("Error: This book is already available")
        
    else: 
        dataModule.updateLine(bookID,'0',dbAddress)
        #Resets ID value to 0 to show its empty
        dataModule.updateDates(bookID,logAddress)
        #Updates the logfile with the new checkout date
        return("Database Updated Successfully")
    
        


if __name__ == "__main__":
    """This test returns the book of ID 15 running the validID function. The
    function then prints off if it was successful or not. If the book isnt
    checked out yet it will return unsuccessful, otherwise, it should be 
    successful. Please run this AFTER running the test module in bookCheckout :)
    Extra proof of it working can be witnessed by the change in text files.
    """
    import datapackage.database as dataModule
    dbAddress = "datapackage/database.txt"
    logAddress = "datapackage/logfile.txt"
    validity = validID(15)
    print(validity)
else:
    import modules.datapackage.database as dataModule
    dbAddress = "modules/datapackage/database.txt"
    logAddress = "modules/datapackage/logfile.txt"
