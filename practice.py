class Node:
    """Creates a Node object that stores 1) data 2) pointer to next object."""
    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    def setdata(self, newdata):
        self.data = newdata

    def getdata(self):
        return self.data

    def setnext(self, nextnode):
        self.next = nextnode

    def getnext(self):
        return self.next


class UnorderedList:
    """Creates an linked list object that utilizes Nodes."""
    def __init__(self):
        self.head = None

    def add(self, newdata):
        """Adds a new Node at the end of linked list. Returns nothing."""
        temp = Node(newdata)  # make new temp Node to store new data
        temp.setnext(self.head)  # make new temp Node point toward OLD self.head
        self.head = temp  # update OLD self.head to point to new self.head (which is new temp Node)!

    def size(self):
        """Counts number of Nodes until final Node self.next is empty. Final Node has no pointer. Returns number of Nodes."""
        current = self.head  # start at head and traverse downward
        count = 0
        endoflinkedlist = False
        while self.next != None:
            count = count + 1  # increase count each loop
            current = current.getnext()  # traverse downward to next pointer each loop
        return count

    def search(self, existingdata):
        """Traverses linked list starting at self.head until self.data matches existingdata. Returns true or false. """
        current = self.head  # start at head object
        found = False  # flag for end condition in while loop

        # while not found and not at end of list
        while current != None and not found:  # why is current and not
            if self.data == existingdata:
                found = True  # end loop
            else:
                current = current.getnext()  # iterate to the next Node
        return found  # goes until end of list and returns the final state of found

    def remove(self, existingdata):
        """Removes a Node based on its data member self.data and reattaches the neighboring Nodes together. Returns nothing."""
        current = self.head  # start at self.head as always
        previous = None
        found = False

        # start loop that iterates through each Node
        while not found:
            if self.data == existingdata:  # first iteration will obviously not find
                found = True
                current = getnext()
                previous = current
                # remove the loop


            else:
                previous = current
                current = current.getnext()  # iterate to next Node if not found













