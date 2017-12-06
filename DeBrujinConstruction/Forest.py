from TreeNode import *
from In_Out_matrix import *


#case of leaf not done

import math

class Forest:

    maxTreeHeight = 1


    #key is address of node and value is list typle in <value, visited>
    nodeDict = {}
    #list of all the tree roots for deletition and insertion purposes
    treeRoots = list()
    #list of all the leafs (may not be needed anymore)
    treeLeafs = list()
    #number of kmers to compare and see if we have have added all of the kmers from the in-out matrix
    countNumberofKmers = 0

    def __init__(self,inOutMatrix,k):
        if not inOutMatrix:
            print("No in and out matrix")
            return

        maxTreeHeight = 3*k*math.log(5,2)

        #definition of a node: def __init__(val, level, parent, isRoot):

        #may not need id(initialNode)
        initialNode = TreeNode(str[0:k-1],0,None,True)
        treeRoots.append(initialRootNode)

        curr = initialNode


        dict.update({curr:[(str[0:k-1],1)]})

        #start at index 0
        #while not all kmers from inoutMatrix have been visited
        while countNumberofKmers <= inOutMatrix.size:
            #if tree is full and we are at an overflow
            #we make a new root
            if curr.level > maxTreeHeight:
                #reset the level of the root
                curr.level = 0
                #initialize new root with string value

                ##!!!!!! still need pre value and kmer value from hash function
                ##!!!!!! we can get this from insert
                newRootNode = TreeNode(curr.val,0,None,True)

                #append to roots list
                treeRoots.append(newRootNode)

                #the number of kmers we have visited has increased
                ++countNumberofKmers

                #update current
                curr = newRootNode


            #else do a regular insert
            else:
                #is called recursively and returns the "overflow node"
                curr = insert_init(curr,curr.val)


    #recursive function to build tree
    def insert_init(self, node, kmer):

        #initialize current node
        curr = node

        #turn Node value to a list in order to rotate and update the value
        kmerList = list(node.val)
        #update the node level that we are going to add
        newLevel = node.level + 1

        #if the new level is the max height we have a leaf
        if newLevel == maxTreeHeight:
            #put into leaf list
            treeLeafs.append(Node)


        #if we already visited the Node we return
        if node.visited == True:
            return node

        #else we are not full and we have not visited the node
        else:
            #{
            #get all the headers which return true for the out matrix
            # Ayush
            #function : I/p : string of a node (kmer)
            #            o/p : List of column headers
            arrayOut = inOutMatrix.getOut(node.value)

            #exit if no outgoing edges
            if not arrayOut:
                return curr


            #if the new height is overflown (above the max tree height we return and get that node)
            if newLevel > maxTreeHeight:
                return curr
            #loop through all the true values to add to the forest
            for index in range(0, len(arrayOut)):

                #get header columns marked as 1
                #prevalue is the value in the header of the out matrix: e.g. a,t,c,g
                #put it to a chracter (variable preVal)
                preVal = arrayOut[index]
                #put it into a deque in order to manipulate the list (rotate the list)
                valueDeque = deque(kmerList)
                #rotate the list left (kmer)
                valueDeque = parent.rotate(-1)
                #convert back to list (kmer)
                valueList = list(collections.deque(valueDeque))
                #add column header to the end of the kmer value
                valueList[-1] = prevVal
                #check the hash of the value = hashValue
                #!!!!!still need to do

                #create a new node (internal node)with hash value in value
                newNode = TreeNode(hashValue, newLevel, node, False)
                #convert list back to a string
                kmer_string = ''.join(valueList)
                #mark the kmer as visited
                newNode.visit = True
                #add the node to the dictionary with the hashvalue
                dict.update({newNode:hashValue})
                #increase the number of kmers for the check above (that is, cehcking if we have visited all the kmers)
                ++countNumberofKmers
                #insert recursively
                #update curr pointer
                curr = newNode
                #call recursively until we either reach max height or reach all the nodes visited
                curr = insert_init(curr, kmer_string)
                #}
            return curr
