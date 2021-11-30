from tkinter import *

import modules.booksearch
import modules.bookcheckout
import modules.bookreturn
import modules.bookweed
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure


def searchCommand():
    """This creates a label + button and places an entry box"""
    
    booknameLabel = Label(window, text="Enter the book name: ")
    booknameLabel.grid(row=1, column=1)

    booknameEntry.grid(row=1,column=2)
    
    goBookname = Button(window, text="Go", background = 'orange',   \
                        command=goBooknameCommand)
    goBookname.grid(row=1, column=3)
    
def goBooknameCommand():
    """This function calls the search through the database with the input
    from the entry box as long as it isnt 'and' and then it takes all the
    books and their corresponding data, and displays it in a
    scroll(wheel)able text box
    
    """
    if(booknameEntry.get() != "all"):
        """This is to avoid error in the database
        function findBooks as "all" does something different"""
        matchedBooks = modules.booksearch.searchFunction(booknameEntry.get())
        bookLength = int(len(matchedBooks)/6)
        """
        This is the amount of actual books we have
        matchedBooks has given us a list with all the matching books and info,
        each line taking 6 elements. This is done slightly differently when
        we are looking for all books (e.g. the write function)
        I mainly did it differently this way to show list manipulation
        """
        
        allBooks = ""
        for i in range(bookLength): #We divide by 6 to get a list for each elem
            allBooks = allBooks + (" - ".join(matchedBooks[:6])+"\n")
            matchedBooks = matchedBooks[6:]

    
        #This next segment of code creats a scrollable textbox containing
        #the corresponding books and their associated values
        searchText = Text(height = 4, width = 75)
        searchText.grid(row = 1, column = 4, padx = 10, pady = 10)
        searchText.insert(END, allBooks)

    
def checkoutCommand():
    """This function places 2 entry boxes, creates 2 labels and also makes a
    button.
    """
    bookIDLabel = Label(window, text="Book ID : ")
    bookIDLabel.grid(row=2, column=1)
    userIDLabel = Label(window, text="User ID: ")
    userIDLabel.grid(row=2,column=3)

    bookIDEntry.grid(row=2,column=2,padx=50)
    userIDEntry.grid(row=2,column=4,padx=50)
    
    goCheckout= Button(window, text="Go", background = 'orange',   \
                       command=goCheckoutCommand)
    goCheckout.grid(row=2, column=5)
    

def goCheckoutCommand():
    """This function takes the inputs from the entry boxes, determines
    whether the inputted values match the correct case and then calls
    the checkout module to update the database and logfile. It then
    updates the user in a new label telling us if it was successful
    or not (and if not, why not)
    """
    bookID = bookIDEntry.get()
    userID = userIDEntry.get()
    x = 0
    #Returns 1 if user inputs int and 0 if else
    try:
        val = int(bookID)
        val = int(userID)
        x = 1
    except ValueError:
        error = "Input Error: Input must be string"

    #The next block of code checks for erronous inputs  
    if(userID == "" or bookID == ""):
        checkoutErrorIDLabel.configure   \
                        (text=" Sorry, both fields must contain text")
        checkoutErrorIDLabel.grid(row=2, column=6)
    elif(x == 0):
        checkoutErrorIDLabel.configure   \
                        (text=" Both values inputted must be integers")
        checkoutErrorIDLabel.grid(row=2, column=6)
    elif(len(userID)!=4):
        checkoutErrorIDLabel.configure   \
                        (text = "Sorry, your userID must be 4 digits long")
        checkoutErrorIDLabel.grid(row=2, column=6)
    else:
        bookIDInt = int(bookID)
        userIDInt = int(userID)
        correspondingInfo = modules.bookcheckout.isValid(bookIDInt,userIDInt)
        #Recieves list with 0 if its not available
        checkoutErrorIDLabel.grid_forget()
        if(correspondingInfo == ['0']):
            checkoutErrorIDLabel.configure   \
                    (text = "Sorry, this book does not exist ")
            checkoutErrorIDLabel.grid(row=2, column=6)
        elif(correspondingInfo[5] != '0'):
            #If the value isnt 0, another user ID is tied to the book
            checkoutErrorIDLabel.configure   \
                        (text = "The book is not available")
            checkoutErrorIDLabel.grid(row=2, column=6)
        else:
            modules.bookcheckout.updateTime(bookIDInt,userIDInt)
            #Updates the database & logfile accordingly
            checkoutErrorIDLabel.configure(text = "Checkout was successful ")
            checkoutErrorIDLabel.grid(row=2, column=6)

def returnCommand():
    """This creates a label and a button while placing an Entry box
    """
    
    returnIDLabel = Label(window, text="Book ID: ")
    returnIDLabel.grid(row=3, column=1)

    returnIDEntry.grid(row=3,column=2)

    returnButton = Button(window, text="Return", background = 'orange',   \
                          command=goReturnCommand)
    returnButton.grid(row=3, column=3)



def goReturnCommand():
    """This takes the inputted bookID and then runs it through the checkout
    module if z is a string and is not empty (if it is it will make an error
    message appear). The checkout will then return a string saying if it worked5
    or not
    """
    z = 0
    try:
        val = int(returnIDEntry.get())
        z = 1
    except ValueError:
        error = "Input Error: Input must be string"
        
    if(returnIDEntry.get() == "" or z == 0):
        checkoutErrorIDLabel.configure(text = "Please enter a valid input")
        checkoutErrorIDLabel.grid(row=3, column=4)
    else:
        verif = returnIDEntry.get()
        VerifyMessage = modules.bookreturn.validID(int(verif))

        checkoutErrorIDLabel.configure(text = VerifyMessage)
        checkoutErrorIDLabel.grid(row=3, column=4)


def weedCommand():
    """
    This function requests data from the weeding module and then puts it into
    a graph to represent it whilst also creating a textbox to display any
    other useful weeding information to the user.
    """
    weedValues = modules.bookweed.weed()
    moreThan60 = weedValues[0]
    neverOut = weedValues[1]
    

    weedingInfo = ["These books have never been checked out: "]+neverOut+ \
    ["\n\nThese books havent been checked out for at least 60 days: "] + \
    moreThan60 + ["\nit is suggested you remove some of these books"]
    #Above creates a textbox of suggestions with the data
    
    weedData = Text(height = 24, width = 60)
    weedData.grid(row = 5, column = 2, padx = 10, pady = 10)
    weedData.insert(END, ("\n".join(weedingInfo)))
    #Above creates a multi-line string containing all the weeding data


    #The next part of this code creates a graph to represent the weeding data
    x = ['Never Checked Out', '>60 Days']
    y = [len(neverOut), len(moreThan60)]
    
    fig = plt.figure(figsize=(3, 4))
    plt.bar(x=x, height=y)

    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas.draw()
    canvas.get_tk_widget().grid(row=5, column=1)
    
window = Tk()
window.geometry("1920x1080") #Sets window size





#Global variable for the definitions to tell the user if they have a bad input
checkoutErrorIDLabel = Label(window, text="")
checkoutErrorIDLabel.grid_forget()

returnErrorIDLabel = Label(window, text="")
returnErrorIDLabel.grid_forget()

searchButton = Button(window, text="   Search   ", background = 'orange',   \
                      height = 6, width = 10,command=searchCommand)
searchButton.grid(row=1, column=0)
#searchButton.grid_forget()


booknameEntry = Entry(window)
booknameEntry.grid_forget()
#This creates a global input box that is hidden until other code refrences it
#I did this because i planned on making them disappear on other button presses
#but didnt get round to it

returnIDEntry = Entry(window)
returnIDEntry.grid_forget()

bookIDEntry = Entry(window)
bookIDEntry.grid_forget()

userIDEntry = Entry(window)
userIDEntry.grid_forget()

checkoutButton = Button(window, text="Checkout", height = 6, width = 10,   \
                        background = 'orange',command=checkoutCommand)
checkoutButton.grid(row=2, column=0)

returnButton = Button(window, text="Return", height = 6, width = 10,   \
                      background = 'orange',command=returnCommand)
returnButton.grid(row=3, column=0)

weedButton = Button(window, text="Weed", height = 6, width = 10,   \
                    background = 'orange',command=weedCommand)
weedButton.grid(row=4, column=0)




window.mainloop()






