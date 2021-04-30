# ----------------------------------------------------
# StudentNode class, EnrollTable class, Priority Queue class
# Author: Deepak Paudel
# Collaborators/references:
#https://www.geeksforgeeks.org/priority-queue-using-doubly-linked-list/
# ----------------------------------------------------

class StudentNode:
    """
    A class to represent a Student Node.
    ...
    Attributes
    ----------
    id : int
        the student id
    faculty : str
        the student faculty
    first: str
        the student first name
    last: str
        the student last name
    """

    def __init__(self, id, faculty, first, last):
        """
        Constructs all the necessary attributes for the StudentNode object.
        Parameters
        ----------
        id : str
        the student id
        faculty : str
            the student faculty
        first: str
            the student first name
        last: str
            the student last name
        """
        # check to see if the parameters are valid
        assert len(id) == 6, ("Error: not a valid id")
        assert faculty == "SCI" or faculty == "ENG" or faculty == "BUS" or faculty == "ART" or faculty == "EDU", ("Error: not valid faculty")
        assert isinstance(first, str), ("Error: not a valid first name")
        assert isinstance(last, str), ("Error: not a valid last name")
        
        self.__id = id
        self.__faculty = faculty
        self.__first = first
        self.__last = last
        self.__next = None
        self.__previous = None

    def setID(self,id):
        """
        sets the student id to the given id.
        Parameters
        ----------
        id : int
        the student id
        """
        # check for valid id
        assert len(id) == 6, ("Error: not a valid id")
        
        self.__id = id

    def setFac(self,faculty):
        """
        sets the faculty abbreviation to the given faculty.
        Parameters
        ----------
        faculty : str
            the student faculty
        """
        # check for valid faculty
        assert faculty == "SCI" or faculty == "ENG" or faculty == "BUS" or faculty == "ART" or faculty == "EDU", ("Error: not valid faculty")
        
        self.__faculty = faculty

    def setFirstName(self,first):
        """
        sets the student’s first name to the given first name.
        Parameters
        ----------
        first: str
            the student first name
        """
        # check for valid first name
        assert isinstance(first, str), ("Error: not a valid first name")
        
        self.__first = first

    def setLastName(self,last):
        """
        sets the student’s last nam e to the given last name.
        Parameters
        ----------
        last: str
            the student last name
        """
        # check for valid last name
        assert isinstance(last, str), ("Error: not a valid last name")
        
        self.__last = last
    
    def setNext(self, next):
        """
        sets next as the next node.
        Parameters
        ----------
        next: StudentNode
            the next node
        """
        self.__next = next

    def setPrev(self, previous):
        """
        sets previous as the previous node.
        Parameters
        ----------
        previous : StudentNode
            the previous node
        """
        self.__previous = previous

    def getID(self):
        """
        returns the student id as a string.
        Parameters
        ----------
        N\A
        """
        return str(self.__id)

    def getFac(self):
        """
        returns the faculty abbreviation as a string.
        Parameters
        ----------
        N\A
        """
        return self.__faculty
    
    def getFirstName(self):
        """
        returns first name as a string.
        Parameters
        ----------
        N\A
        """
        return str(self.__first)

    def getLastName(self):
        """
        returns the last name as a string.
        Parameters
        ----------
        N\A
        """
        return str(self.__last)

    def getNext(self):
        """
        returns the next node.
        Parameters
        ----------
        N\A
        """
        return self.__next

    def getPrev(self):
        """
        returns the previous node.
        Parameters
        ----------
        N\A
        """
        return  self.__previous
    
class EnrollTable:
    """
    A class to represent a EnrollTable.
    ...
    Attributes
    ----------
    capacity : int
        the maximum capacity of given capacity
    """

    def __init__(self,capacity):
        """
        Constructs all the necessary attributes for the StudentNode object.
        Parameters
        ----------
        capacity : int
            the maximum capacity of given capacity
        """
        assert capacity<=51, ("The max capacity has been reached")

        self.__capacity = capacity
        self.__table = []
        # initialize the table with none using capacity
        for index in range(self.__capacity):
            self.__table.append(None)

        self.__tableSize = 0

    def cmputIndex(self,studentID):
        """
        a method takes in a given student id and returns an
        integer that will represent the index
        Parameters
        ----------
        studentID: str
            id of the student
        Returns
        ----------
        int that will represent the index of student
        """
        
        # separate the ID 
        start = int(studentID[:2])
        middle = int(studentID[2:4])
        end = int(studentID[4:])
        
        # cmput
        index = (start+middle+(end**2))%self.__capacity

        return index

    def insert(self,item):
        """
        this method inserts a given item, in the enrollment table.
        Parameters
        ----------
        item: StudentNode
            a Student Node
        Returns
        ----------
        N/A
        """
        # only student node can be inserted
        assert isinstance(item, StudentNode), ("Cannot enqueue: invalid argument provided.")
        
        # get id of item
        studentID = item.getID()
        
        # find the index
        index = self.cmputIndex(studentID)
        
        # check if table is empty
        if self.__table[index] == None:
            self.__table[index] = item
        else:
            current = self.__table[index] # Start the traversal
            # instert at the beginning
            if studentID < current.getID():
                item.setNext(current)
            else:
                # loop till end of linked list chain and ID is less than item studentID
                while current.getNext() != None and current.getNext().getID() < studentID:
                    current = current.getNext()
                # change the links
                item.setNext(current.getNext())
                current.setNext(item)

        self.__tableSize += 1

    def remove(self,studentID):
        """
        this method removes from the enrollment table the node for the relevant
        student corresponding with the given student id.
        Parameters
        ----------
        Student ID: int
            id of the student
        Returns
        ----------
        True if the student has been successfully dropped from the course or False otherwise
        """
        if  self.__tableSize == 0:
            raise Exception('can not remove from a empty table')

        index = self.cmputIndex(studentID)
        current = self.__table[index] # Start the traversal
        previous = None
        found = False
        # loop until student ID is found and end of linked list chain
        while current != None and not found:
            if current.getID() == studentID:
                found = True
            else:
                previous = current
                current = current.getNext()
        if not found:
            return False
        else:
            if previous == None:  # the item is in the first node of the list
                self.__table[index] = current.getNext()
            else:  # item is not in the first node
                previous.setNext(current.getNext())
            self.__tableSize -= 1
            return True

    def isEnrolled(self,studentID):
        """
        this method searches the enrollment table given a student id
        Parameters
        ----------
        Student ID: int
            id of the student
        Returns
        ----------
        True if the corresponding student is found in the table, and False otherwise
        """

        index = self.cmputIndex(studentID)
        current = self.__table[index] # Start the traversal
        found = False
        
        # loop till the end of the linked list chain and when the ID is not found
        while current != None and not found:
            if current.getID() == studentID:
                found = True
            else:
                current = current.getNext()
        return found

    def size(self):
        """
        this method returns the size of the enrollment table.
        Parameters
        ----------
        N/A
        """
        return self.__tableSize

    def isEmpty(self):
        """
        this method returns True if the table is empty, i.e., size is 0, and False otherwise.
        Parameters
        ----------
        N/A
        """
        return self.__tableSize == 0

    def __str__(self):
        """
        returns the string representation of the EnrollTable instance
        Parameters
        ----------
        N/A
        """
        string ="["
        currentPosition = 0
        for index in range(self.__capacity):
            if self.__table[index] != None:
                current = self.__table[index] # Start the traversal
                # loop till the end of the linked list chain
                while current != None:
                    if currentPosition+1 == self.size():
                        string =  string +"{}{}".format(str(index),": ")+str(current.getID())+ " "+ str(current.getFac()) + " "+str(current.getFirstName()) + " "+str(current.getLastName())+ "]"
                    else:
                        string = string +"{}{}".format(str(index),": ")+str(current.getID())+ " "+ str(current.getFac()) + " "+str(current.getFirstName()) + " "+str(current.getLastName())+ ","
                        string = string + " "
                    current = current.getNext()
                    currentPosition = currentPosition+1
                string = string + "\n"
        return string

class PriorityQueue:
    """
    A class to represent a Priority Queue.
    ...
    Attributes
    ----------
    head: 
        reference to the head of the queue
    tail: 
        reference to the tail of the queue
    size:
        size of the priority queue
    """
    def __init__(self):
        """
        Constructs all the necessary attributes for the PriorityQueue object.
        Parameters
        ----------
        N/A
        """
        # creates an empty doubly linked chain with both head and tail having references to None
        self.__head = None
        self.__tail = None
        self.__size = 0
        self.__priority = {"SCI":4,"ENG":3,"BUS":2,"ART":1,"EDU":0}

    def enqueue(self,item):
        """
        enqueues a new student node to the rear of the queue or traverses the queue to
        determine the position in which the new node will be inserted based on the faculty priority of the given
        item
        Parameters
        ----------
        item: StudentNode
            a Student Node
        Returns
        ----------
        N/A
        """
        # only student node can be enqueued
        assert isinstance(item, StudentNode), ("Cannot enqueue: invalid argument provided.")

        # get the priority of the new item
        priority = self.__priority[item.getFac()]
        
        # if the Queue is empty
        if self.__head == None:
            self.__head = item
            self.__tail = item
            item.setNext(None)
        else:
            # if priority is greater than priority of first item, insert at the start
            if priority > self.__priority[self.__head.getFac()]:
                item.setNext(self.__head)
                self.__head.setPrev(item)
                self.__head = item
            # if priority is less than or equal to the priority of last item, insert at the end
            elif priority <= self.__priority[self.__tail.getFac()]:
                item.setNext(None)
                self.__tail.setNext(item)
                item.setPrev(self.__tail)
                self.__tail = item
            # insert inbetween 
            else:
                current = self.__head # Start the traversal
                # loop until the current next priority greater than or equal to the priority of new item
                while (self.__priority[current.getNext().getFac()] >= priority):
                    current = current.getNext()
                # update the linked list 
                current.getNext().setPrev(item)
                item.setNext(current.getNext())
                item.setPrev(current)
                current.setNext(item)
        
        self.__size = self.__size + 1
    
    def dequeue(self):
        """
        dequeues and returns the highest priority student node from the front of the queue and
        updates the size of the priority
        Parameters
        ----------
        N/A
        Returns
        ----------
        returns the highest priority student node from the front of the queue
        """
        # check if there is a student node to dequeue
        if self.isEmpty():
            raise Exception("Queue is empty: cannot dequeue from a empty queue")
        else:
            priorityStudent = self.__head # get the node thats at the start 
            self.__head = self.__head.getNext()  # update the node
            self.__size = self.__size -1
            return priorityStudent

    def size(self):
        """
        this method returns the number of students in the priority queue.
        Parameters
        ----------
        N/A
        """
        return self.__size

    def isEmpty(self):
        """
        this method returns True if the priority queue is empty, if its size is 0, or False otherwise.
        Parameters
        ----------
        N/A
        """
        return self.__size == 0

    def __str__(self):
        """
        returns the string representation of the PriorityQueue instance
        Parameters
        ----------
        N/A
        """
        string ="["
        current = self.__head # Start the traversal
        if self.isEmpty():
            string = string + "] "
        else:
        # loop till the end
            while current != None:
                # add each node info to the string
                if current.getNext() == None:
                    string = string +str(current.getID())+ " "+ str(current.getFac()) + " "+str(current.getFirstName()) + " "+str(current.getLastName())+ ']'
                else:
                    string = string +str(current.getID())+ " "+ str(current.getFac()) + " "+str(current.getFirstName()) + " "+str(current.getLastName())+ ',\n'
                    string = string + " "
                current = current.getNext()  
        return string

if __name__ == "__main__":
