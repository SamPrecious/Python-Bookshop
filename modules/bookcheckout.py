'''
This is the checkout module, it takes the bookID and memberID
to checkout and puts them through to the database while doing
a few small extra things.
'''

def isValid(bookID,memberID):
    """This function takes an input and returns a list representing either
    error values (e.g. 1) or success if it returns the correct values.

    bookID = book ID(int)
    memberID = member ID(int)
    """
    bookInfo = dataModule.findID(bookID,dbAddress)
    if(bookInfo == []): #Checks if there was no book with that ID
        return(['0'])#Returns a list with 1 in it to signify no matching ID
    else:
        return(bookInfo)


def updateTime(bookID,memberID):
    """This function updates the database and logfile with the new details (by
    calling updateLine and newDate in the database module

    bookID = book ID(int)
    memberID = member ID(int)
    """
    dataModule.updateLine(bookID,memberID,dbAddress) #Updates the main database
    dataModule.newDate(bookID,logAddress,dbAddress) #Updates the logfile



if __name__ == "__main__":
    """This test checks out a set book to make sure its working fine. The
    textfile contains information on this test (and using return to undo).
    This current test updates the database value and logfile value.
    If the book isnt taken out it will update the checkout txt with
    the users ID who took it out (4423 in this case)
    Extra proof of it working can be witnessed by the change in text files.
    """
    
    import datapackage.database as dataModule
    dbAddress = "datapackage/database.txt"
    logAddress = "datapackage/logfile.txt"


    validity = isValid(15,4423)
    if(validity[5] != '0'):
        print("This book has already been taken out, please try return test ")
    else:
        updateTime(15,4423)
        print("Checkout was a success, please use the return test next")
    
    
else:
    import modules.datapackage.database as dataModule
    dbAddress = "modules/datapackage/database.txt"
    logAddress = "modules/datapackage/logfile.txt"
