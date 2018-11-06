#Yamel Hernandez
#80590552
#CS 2302
#Diego Aguirre
#Anindita Nath
#Lab 3 Ver A
#Purpose of this lab was to understand how to use
#Binary Trees, AVL and REd-Black Trees and how to
#how to write files
####################################################################

from RBTNode import RBTNode
from RedBlackTree import RedBlackTree
from AVLTree import AVLTree
from AVL_Node import AVL_Node
import math


#2 SImilarity with embeddings & word mag

	#dot product
def dotProduct(x, y):
    sum = 0
    for i in range(len(x.embeddings)):
        sum += (float(x.embeddings[i]) * float(y.embeddings[i]))
    return sum

	#finds word magnitude of its embedding
def wordMagnitude(x):
    sum = 0
    for i in range(len(x.embeddings)):
        sum += (math.pow(float(x.embeddings[i]), 2))
    return math.sqrt(sum)

	#finds similarity
def similarTo(x, y):
        if x is None:
            print('x')
        if y is None:
            print('y')
        mag1 = wordMagnitude(x)
        mag2 = wordMagnitude(y)
        dotPro = dotProduct(x, y)
        similar = (dotPro) / (mag1 * mag2)
        return similar
    
#3 Finish the following to finish lab   

#Compute number of nodes in the tree
def countNodes(x):
    if x == None:
        return 0
    return 1 + countNodes(x.left) + countNodes(x.right)


#Compute tree Height
def height(x):
    if x != None:
        left = height(x.left)
        right = height(x.right)
        if left > right:
            return 1 + left
        return 1 + right
    return -1


#Generate a file containing all the words stored in the tree in
#ascending order, one per line
def gen_A(x, fName):
    f = open(fName, "a")
    if x == None: return
    gen_A(x.left, fName)
    f.write(str(x.key))
    gen_A(x.right, fName)

#Given desired depth generate a file with all the keys that
#have that depth in ascending order
def gen_DA(x, d, fName):
    f = open(fName, "a")
    if x == None: return
    while x != None:
        if d == 0:
            f.write(str(x.key))
        else:
            gen_DA(x.left, d-1, fName)
            gen_DA(x.right, d-1, fName)



#extra credit implement using a btree
def count_BtreeNodes(T):
    count = 1 #current node
    if T.isLeaf:
        return 1
    for i in range(T.n):
        count += count_BtreeNodes(T.c[i])
    return count

def height_Btree(T):
    if T == None:
        return -1
    if T.isLeaf:
        return 0
    return 1 + height_Btree(T.c[0])



####################################################################

def main():
    print('hello')
    use = "/home/yamel/Desktop/CS3/lab3/glove.6B.50d.txt"
    while True:
        choice = input("how would you like to store the glove file?\nAVL, a or Red-Black Tree, r")
        if choice is 'a' or choice is 'r':
            break
        print('Invalid choice')
    if choice is 'a':
        tree = AVLTree()
    elif choice is 'r':
        tree = RedBlackTree()
#try:
    with open(use) as f:
        for line in f:
            info = line.split(' ')
            if info[0][0].isalpha():
                if choice is 'a':
                    node = AVL_Node(info[0], info[1:])
                    tree.insert(node)
                elif choice is 'r':
                    tree.insert(info[0], info[1:])
    use2 = "/home/yamel/Desktop/CS3/lab3/similarities.txt"
    with open(use2) as f:
        for line in f:
            words = line.split(' ')
            word1 = words[0]
            word2 = words[1].rstrip('\n')
            node1 = tree.search(word1)
            node2 = tree.search(word2)
            if node1 and node2:
                print(word1 + ' ' + word2 + ' ' + str(similarTo(node1, node2)))
    temp = tree.root
    gen_A(temp, "printA.txt")
    gen_DA(temp, 3, "printAtDepth.txt")

#except:
    #print('error')
    pass
    
    
main()


