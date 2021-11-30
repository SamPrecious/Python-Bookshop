'''
This is the checkout module, it takes the values to checkout and puts them
through to the database while doing a few small extra things.
'''

def searchFunction(nameOfBook):
    """Returns a list where ever 6 elements contains a book matching
       nameOfBook and its related data
       

        nameOfBook: Book name (String)"""
    matchedBooks = dataModule.findBooks(nameOfBook,dbAddress)
    
    return(matchedBooks)

 

if __name__ == "__main__":
    """This test returns all values in the database file corresponding to
    harry pottery and prints them all"""
    
    import datapackage.database as dataModule
    dbAddress = "datapackage/database.txt"
    print(searchFunction("Harry Pottery"))

    
else: #If called externally use different database address
    import modules.datapackage.database as dataModule
    dbAddress = "modules/datapackage/database.txt"
    
