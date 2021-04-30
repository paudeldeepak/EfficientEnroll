# ----------------------------------------------------
# main program
# Author: Deepak Paudel
# Collaborators/references:
# ----------------------------------------------------

from enrollStudent import StudentNode, EnrollTable, PriorityQueue

def main():
    # get user input
    userInput = getInput() 
    # initialize table and queue
    table = EnrollTable(51)
    queue = PriorityQueue()
    validFile = True
    # loop until user wants to end the program
    while userInput != "Q" and validFile:
        studentRecords = []
        # check if the file info was valid
        validFile = openFile(studentRecords)
        if validFile:
            # rregister
            if userInput == "R":
                # loop through the studentRecords
                for student in studentRecords:
                    newStudent = StudentNode(student[0], student[1], student[2], student[3])
                    # insert if thre is space
                    if table.size() < 50:
                        table.insert(newStudent)
                    else:
                        # add to wait list if there is no space
                        queue.enqueue(newStudent)
                writeEnrolled(table)
                writeWaitList(queue)
            # drop
            elif userInput == "D":
                for student in studentRecords:
                    idStudent = student[0]
                    # if table is not empty and id is found remove 
                    if not table.isEmpty():
                        if table.remove(idStudent) == False:
                            print("WARNING: {} {} (ID: {}) is not currently enrolled and cannot be dropped".format(student[2], student[3],student[0]))
                    # insert if thre is space
                    if table.size() < 50:
                        newStudent = queue.dequeue()
                        table.insert(newStudent)
                writeWaitList(queue)
            userInput = getInput()
    
    print("Thank you for using the program. Goodbye...")

def writeWaitList(queue):
    """
    function to write PriorityQueue into a file and print it
    Parameters
    ----------
    queue is the PriorityQueue
    Returns
    ----------
    N/A
    """
    # open a file to write to 
    enrolledFile = open("waitlist.txt", "w")
    # write the table content
    enrolledFile.write(str(queue))
    enrolledFile.close()

    print("Sample outputs in waitlist.txt:\n")
    # open the file to read
    inFile = open('waitlist.txt', 'r')
    print(inFile.read()) # print each line
    inFile.close()
    print()

def writeEnrolled(table):
    """
    function to write EnrollTable into a file and print it
    Parameters
    ----------
    table is the EnrollTable
    Returns
    ----------
    N/A
    """
    # open a file to write to 
    enrolledFile = open("enrolled.txt", "w")
    # write the table content
    enrolledFile.write(str(table))
    enrolledFile.close()

    print("Sample outputs in enrolled.txt:\n")
    # open the file to read
    inFile = open('enrolled.txt', 'r')
    print(inFile.read()) # print each line
    inFile.close()

def openFile(studentRecords):
    """
    prompt for the filename of the file containing the
    students to be registered and will read this file
    Parameters
    ----------
    N/A
    Returns
    ----------
    true if each line info is valid, false otherwise
    """

    valid = False
         # loop until a valid file name has been inputed
    while not valid:
        fileInput = input("Please enter a filename for student records: ")
        print()
        try:
            inFile = open(fileInput, 'r')
         # catch error for input of non existing file
        except IOError:
            print("Cannot read from {}.".format(fileInput))
        else:
            valid = True

    # keep track of line number
    lineNumber = 0
    validInfo = True
    # go through the file to get info for each student
    for line in inFile:
        line = line.strip() # remove '\n' 
        line = line.split(" ") # seperate the info
        # add each line number
        lineNumber = lineNumber+1
        # add the info for each student to the list if the information is valid
        if len(line[0]) == 6 and (line[1] == "SCI" or line[1] == "ENG" or line[1] == "BUS" or line[1] == "ART" or line[1] == "EDU") and isinstance(line[2], str) and isinstance(line[3], str):
            studentRecords.append(line)
        else:
            print("Invalid Data on Line:{} {} {} {} {}".format(lineNumber,line[0], line[1], line[2], line[3]))
            validInfo = False
    inFile.close()

    return validInfo

def getInput():
    """
    get user choice from the menu option
    Parameters
    ----------
    N/A
    Returns
    ----------
    user choice
    """
    inValid = True
    # loop until the user choice is valid
    while inValid:
        userChoice = input("Would you like to register or drop students [R/D]: ")
        print()
        # the user choice has to R , D or Q
        if userChoice == "R" or userChoice == "D" or userChoice == "Q":
            inValid = False
        else:
            inValid = True

    return userChoice

if __name__ == "__main__":
    main()