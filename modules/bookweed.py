import datetime
import matplotlib.pyplot as plt
'''
This is the weeding module, it doesnt take inputs but just suggests
box to get rid of. It will suggest books over 60 days since last
checkout and books that have never been checked out
'''



def weed():
    """This takes no extra parameters. It starts off looking through the
    database and logfile and taking all entries before comparing them against
    a set of criteria where it will determine books that havent ever been
    checked out and books that are older than 60 days old before returning them
    all. 
    """
    allBooks = dataModule.findBooks("all",dbAddress)
    allDates = dataModule.findDates(logAddress)
    bookAmount = len(allBooks)#This value is the amount of books in the Database
    idUnused = []
    booksUnused = []
    for i in range(len(allBooks)): #Creates a list of all book titles
        booksUnused.append(allBooks[i][2])

    noDupeTitle=[]
    [noDupeTitle.append(x) for x in booksUnused if x not in noDupeTitle]
    #Above removes all duplicate values from the list
    
    for f in range(len(allDates)):
        if allDates[f][1] in noDupeTitle:
            noDupeTitle.remove(str(allDates[f][1]))
        
    for i in range(len(allBooks)):
        idUnused = idUnused + [i+1] #Creates a list of all book IDs
        
    for f in range(len(allDates)):
        #This makes idUsed a list of books that have never been checked out
        if allDates[f][0] in idUnused: 
            idUnused.remove(allDates[f][0])
        #for g in range(len(allDates)-1):
    dateLeng = len(allDates)
    y = 0
                
    IDAllDates = []
    for g in range(len(allDates)):
        IDAllDates.append(allDates[g][1])
 
    noDupes = []
    [noDupes.append(x) for x in IDAllDates if x not in noDupes] 
    trueAllDates = []
    for x in range(len(noDupes)):
        #This forloop creates a list of all books most recent checkout 
        for z in range(len(allDates)):
            if(noDupes[x] == allDates[z][1]):
                
                checkedOut = allDates[z][2]
                checkFormat = checkedOut.split("-")
                date = datetime.datetime.now()
                dateFormat = ((str(date.today()).split(" ")[0]).split("-"))
                dComp1 = datetime.date(int(dateFormat[0]),   \
                                    int(dateFormat[1]),int(dateFormat[2]))
                dComp2 = datetime.date(int(checkFormat[0]),   \
                                    int(checkFormat[1]),int(checkFormat[2]))
                timeDiff = dComp1 - dComp2

                if(timeDiff.days > 60):
                    #Makes a list of books that were checked out >60 days ago
                    trueAllDates.append(allDates[z][1])
                break
      
    return(trueAllDates,noDupeTitle)
'''
    fruit_names = ['>60 days ','Never Taken Out']
    sold_numbers = [len(trueAllDates),len(idUnused)]
    plt.bar(fruit_names,sold_numbers)
    plt.show()
    
    print(len(allDates))
'''


if __name__ == "__main__":
    """This test module runs the weed function and returns the lists given,
    before suggesting to remove them and why.
    """
    import datapackage.database as dataModule
    dbAddress = "datapackage/database.txt"
    logAddress = "datapackage/logfile.txt"

    #This is the weeding test, it will return what should be weeded from the
    #program. Graph and GUI representation is available in menu.py
    weedVals = weed()
    

    print("These books are more than 60 days since last checkout: ",weedVals[0])
    print("")
    print("These are the books that have never been checked out: ",weedVals[1])
    print("\nThese books are recommended to be considered for removal")
else:
    import modules.datapackage.database as dataModule
    dbAddress = "modules/datapackage/database.txt"
    logAddress = "modules/datapackage/logfile.txt"
    
