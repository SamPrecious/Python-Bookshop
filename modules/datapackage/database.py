from datetime import date
"""
This is a module that contains all of the functions that interact with the
database. It is used by all the modules in the first package
"""


def findBooks(bookName,address):
    """ This searches through the database and returns a list of books and their
    corresponding data using the name of the book, and address of the text file

    bookname = name of book (string)
    address = address of db file (string)
    """
    matchingBooks=[]
    """With Open acts similarly to a .open() and close() however it does
    it automatically I am using it for cleaner looking programming (and
    to avoid corrupting a file by forgetting .close
    """
    with open(address, "r") as file: 
        
        for i in file: #Loops through every element in the database
            n=i.strip() 
            currentBook = n.split(",")
            if(bookName == "all"):
                matchingBooks.append([int(currentBook[0]),   \
                int(currentBook[1]), currentBook[2], currentBook[3],   \
                currentBook[4], int(currentBook[5])])
            elif(currentBook[2] == bookName):
                matchingBooks = matchingBooks + currentBook

        return(matchingBooks)

def findDates(address):
    """This function searches through the logfile document and returns
    all of its elements

    address = current address of logfile(string)
    """
    matchingDates=[]
    with open(address, "r") as file: 
        
        for i in file: 
            n=i.strip() #Gets rid of the /n at the end of each line
            currentDate = n.split(",")
            matchingDates.append([int(currentDate[0]), currentDate[1],   \
                                  currentDate[2],currentDate[3]])
        return(matchingDates)

def findID(bookID,address):
    """Takes in an input bookID and checks for it in the database until found
    or until opened
    
    bookID = book ID (string)
    address = database text file (string)"""
    matchingID = []
    
    with open(address,"r") as file: 
        for i in file:
            n = i.strip()
            currentID = n.split(",")
            if(currentID[0] == str(bookID)):
                matchingID = matchingID + currentID
                break 
        return(matchingID)
#Returns the set containing the ID and its details (empty set if ID invalid)



def updateLine(bookID,memberID,address):
    """This is the function for checking out books, it takes a book of ID bookID
    and a members ID of memberID and pushes it through, updating the database
    accordingly

    bookID = book ID (int)
    memberID = members ID (int)
    address = db textfile address (string)
    """
    allBooks = findBooks("all",address)#Saves every val of DB to a temp list
    allBooks[bookID-1][5] = memberID
    
    with open(address, "w") as file: 
        for i in allBooks:
            line = str(i[0])+","+str(i[1])+","+i[2]+","+i[3]+","+i[4]+","   \
                   +str(i[5])+"\n" 
            file.write(line)
        

def updateDates(bookID,address): 
    """This function is used for the return feature. It takes a book ID and then
    replaces the logfile point with that ID with the current date in the 4th
    column

    bookID = book ID (int)
    address = logfile address (string)
    """
    allDates = findDates(address)
    x = 0
    for i in range(len(allDates)): 
        if(allDates[i][0] == bookID): 
            x = i
            break
    allDates[x][3] = str(date.today())
    with open(address, "w") as file: #Logfile
        for i in allDates:
            line = str(i[0])+","+i[1]+","+i[2]+","+i[3]+"\n" 
            file.write(line)



def newDate(bookID,logAddress,dbAddress):
    """This function is used for the checkout feature. It makes a new line at
    top of logfile with a the current date for checkingout associated with it

    bookID = book ID (int)
    logAddress = logfile address (string)
    dbAddress = database txt address (string)
    """
    allDates = findDates(logAddress)
    #Returns a list of lists containing lines of logfile
    IDStats = findID(bookID,dbAddress)
    #Returns a list of the book details (including the title)
    allDates = [[str(bookID)]+[IDStats[2]]+[str(date.today())]+[str(0)]]   \
               + allDates
    #updates the list putting the new checkout at the front with todays date
    #Return date is written as 0 to show it hasnt been returned yet
    
    
    
    with open(logAddress, "w") as file: #logfile
        for i in allDates:
            line = str(i[0])+","+i[1]+","+i[2]+","+i[3]+"\n" 
            file.write(line)
    

if __name__ == "__main__":
    """
    If called from within this module, this tests every single function.
    It returns some ugly to look at test data
    """
    dbAddress = "database.txt"
    logAddress = "logfile.txt"
    print("Find Books Test:")
    print(findBooks("Harry Pottery",dbAddress)) #Prints all books with that name
    print("\nFind Dates Test:")
    print(findDates(logAddress))
    print("\nFind ID Test:")
    print(findID(15,logAddress))
    print("\nUpdate Line test:")
    updateLine(15,1257,dbAddress)
    print("Successful")
    print("\nNew Date test:")
    newDate(15,logAddress,dbAddress)
    print("Successful")
    print("\nUpdate Dates test:")
    updateDates(15,logAddress)
    updateLine(15,'0',dbAddress)
    print("Successful")
    #The test will should end up updating the logfile with an extra row for ID
    #15 at the top :)











