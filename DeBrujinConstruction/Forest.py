from TreeNode import *
from In_Out_matrix import *


#case of leaf not done

import math

class Forest:

    maxTreeHeight = 1
    nodeDict = {}
    treeRoots = list()
    treeLeafs = list()
    countNumberofNodes = 0

    def __init__(self,inOutMatrix,k, alphabetSize):


        maxTreeHeight = 3*k*math*.log(alphabetSize,2)

        initialNode = TreeNode(id(initialNode),str[0:k-1],0,None,True)
        treeRoots.append(initialRootNode)
        dict.update(initialRoot:[(str[0:k-1],0)])


        #condition to know when to stop
        #i will be iterated everytime we encounter a node that is marked as  visited
        while countNumberofNodes <= inOutMatrix.size:
            #if tree is full
            if treeRoots[treeNum].level == maxTreeHeight:
                newRootNode = TreeNode(id(newRootNode),str[i:i+k-1],0,None,True)
                treeRoots.append(newRootNode)
                ++countNumberofNodes
                ++treeNum


            #else do a regular insert
            else:
                insert_init(newRootNode,newRootNode.value)


    def insert_init(Node, Node.value, count):

        kmerList = list(Node.val)
        newLevel = Node.level + 1

        if Node.visited == True:
            return

        elif newLevel > maxTreeHeight:
            treeLeafs.append(Node)
            return

        else:
            arrayOut = inOutMatrix.getOut(Node.value)
            for index in range(0, len(arrayOut)):
                #get header columns marked as 1
                #put it to a chracter
                #get value prev  from in-out matrix
                valueDeque = deque(kmerList)
                valueDeque = parent.rotate(-1)
                valueList = list(collections.deque(valueDeque))
                valueList[-1] = prevVal
                #check the hash of the value = hashValue
                newNode = TreeNode(id(newNode), hashValue, newLevel, Node, False)
                kmer_string = ''.join(valueList)
                dict.update(newNode:hashValue)
                ++countNumberofNodes
                #insert recursively
                insert_init(newNode, kmer_string)
