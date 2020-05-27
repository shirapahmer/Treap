import random
class Node(object):
    # create a binary tree node consisting of a key/data pair
    #code taken and modified from slides for binary tree
    def __init__(self, k, p):
        self.key  = k
        self.priority = p
        self.leftChild = None
        self.rightChild = None
        self.occurenceCount = 0 
        
    #taken from slides for binary tree
    def __str__(self):
        return "{" + str(self.key) + " , " + str(self.priority) + "}"

class Treap(object):
    def __init__(self):
        self.__root = None
        self.__nElems = 0


    ##modified from code given for BST
    #prints the nodes in readable format displaying tree-like node relationships
    def printTreap(self):
        self.pTreap(self.__root, "ROOT:  ", "")
        print()
    
    ##modified from code given for BST
    def pTreap(self, n, kind, indent):
        print("\n" + indent + kind, end="")
        if n: 
            print(n, end="")
            if n.leftChild:
                self.pTreap(n.leftChild,  "LEFT:   ",  indent + "    ")
            if n.rightChild:
                self.pTreap(n.rightChild, "RIGHT:  ", indent + "    ")
                
    ##code modified from code for AVL tree.
    #rotates cur node to the right. Its leftChild becomes its parent and cur 
    #takes on the rightChild of its previous leftChild. Cur's previous parent
    #now points to the leftChild node because it replaced cur
    def rotateRight(self, cur, insert = True):
        temp = cur.leftChild
        tempRight = temp.rightChild
        temp.rightChild = cur
        cur.leftChild = tempRight
        if not insert:
            parent = self.getParent(cur.key)                        
            if cur == self.__root: self.__root = temp
            elif cur.key < parent.key: parent.leftChild = temp
            elif cur.key > parent.key: parent.rightChild = temp
        return temp if insert else cur
    
    ##code modified from code for AVL tree
    #rotates cur node to the left. Its rightChild becomes its parent and cur 
    #takes on the leftChild of its previous rightChild. Cur's previous parent
    #now points to the leftChild node because it replaces cur
    def rotateLeft(self, cur, insert = True):
        temp = cur.rightChild
        tempLeft = temp.leftChild
        temp.leftChild = cur
        cur.rightChild = tempLeft
        if not insert:
            parent = self.getParent(cur.key)            
            if cur == self.__root: self.__root = temp
            if cur.key < parent.key: parent.leftChild = temp
            if cur.key > parent.key: parent.rightChild = temp
        return temp if insert else cur

    ##modified from code given for BST.
    #insert a new node. Calls the private insert function
    def insert(self, k):
        # remember nElems to see if it changed due to insert
        temp = self.__nElems
        
        #generate random number for priority
        randNum = random.random()      
        self.__root = self.__insert(self.__root, k, randNum)

        # if the insert failed, 
        # then nElems will not have changed
        return temp != self.__nElems    
    
    ##modified from code given for BST. 
    def __insert(self, cur, k, randNum):
        # empty tree, so just insert the node, increment the num of elements
        #in the tree, and increment amount of nodes with that key
        if not cur:  
            self.__nElems += 1 
            newNode = Node(k, randNum)
            newNode.occurenceCount += 1
            return newNode
        
        #if the key is already in the node, just increment tally of that node
        #increment the num of elems in the tree
        if cur.key == k: 
            cur.occurenceCount += 1
            self.__nElems += 1

        # insert k in the left or right branch as appropriate
        elif k < cur.key: 
            cur.leftChild  = self.__insert(cur.leftChild,  k, randNum)
            
            #make sure the priority of the new key is not bigger than its parent
            if cur.priority < cur.leftChild.priority:
                cur = self.rotateRight(cur)
                
        elif k > cur.key: 
            cur.rightChild = self.__insert(cur.rightChild, k, randNum)
            
            #make sure the priority of the new key is not bigger than its parent
            if cur.priority < cur.rightChild.priority:
                cur = self.rotateLeft(cur)
            
        # at this point, k was inserted into the correct branch,
        # or it wasn't inserted since the key k was already there
        return cur        
    
    #the calling function to find if theres node with the given key in the tree
    def find(self, k):
        key = self.__find(k)
        if key:
            occurs = self.getOccurenceCount(k)
            print("Found node with key:", k,"\nOccurs ",occurs, "times.")
            return True
        else: 
            print("No node found with key: "+ k)
            return False
        
    ##modified from code given for BST
    #recursively find the node with the given key k. returns the node if found.
    #if the key is the root node, return the root node itself
    def __find(self, k, cur = "start"):
        if cur == "start": cur = self.__root
        #if node isn't found, return None
        if not cur: return None
        if k == cur.key: return cur
        elif k  < cur.key: return self.__find(k, cur.leftChild)
        else:              return self.__find(k, cur.rightChild)
        
    #get the number of times a key appears in the tree
    def getOccurenceCount(self, k):
        k = self.__find(k)
        return k.occurenceCount
    
    #get the parent node of a node with a given key
    def getParent(self, k, cur = "start"):
        
        if cur == "start": cur = self.__root
        if cur.key == k: return cur
        #if cur's right child exists and it is the key, return cur. Same with 
        #the left node
        if (cur.rightChild and cur.rightChild.key == k) or \
           (cur.leftChild and cur.leftChild.key == k):return cur
        
        #if not, move on to the next key in the correct side of the tree
        elif k  < cur.key: return self.getParent(k, cur.leftChild)
        else:              return self.getParent(k, cur.rightChild)        

    #remove a node with given key
    def remove(self, k, cur = "start"):
        if cur == "start": cur = self.__find(k)
        
        #if the node doesn't exist, return none
        if not cur: return False
        
        #if there is more than one of the key, just decrement the count 
        if self.getOccurenceCount(cur.key) >1: 
            cur.occurenceCount -= 1
            return
        
        #if its a leaf node
        if not cur.rightChild and not cur.leftChild: 
            #if it is the root node, set root to none
            if cur == self.__root:
                self.__root = None
            
            #find the parent node of cur, set it to None
            else: 
                parent = self.getParent(cur.key)
                if parent.rightChild == cur: parent.rightChild = None
                elif parent.leftChild == cur: parent.leftChild = None
                self.__nElems -= 1
            return True
        #if cur is not a leaf node
        else: 
            #if it has two children, rotate with the child who has a higher 
            #priority of the two nodes
            if cur.leftChild and cur.rightChild:
                if cur.leftChild.priority > cur.rightChild.priority: 
                    self.rotateRight(cur, insert = False)
                else: self.rotateLeft(cur, insert = False)
            
            #if it only has one child node, rotate with that node
            elif not cur.leftChild and cur.rightChild: self.rotateLeft(cur, insert = False)
            else: self.rotateRight(cur, insert = False)
        
        #keep going until it is a leaf node and deleted
        cur = self.remove(k, cur)
        
