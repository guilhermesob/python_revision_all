# Python program for the above approach
 
from collections import deque
 
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
 
def levelOrder(root, n):
    queue = deque([None, root, None] + [None]*(2*n - 2))
    top = 2
    front = 1
    prevFront = 0
    count = 1
    while True:
        curr = queue[front]
        if curr == None:
            if front == top:
                break
            else:
                if count % 2 == 0:
                    for i in range(prevFront + 1, front):
                        print(queue[i].data, end=' ')
                else:
                    for i in range(front - 1, prevFront, -1):
                        print(queue[i].data, end=' ')
                prevFront = front
                count += 1
                front += 1
                queue[top+1] = None
                top += 1
                continue
        if curr.left != None:
            queue[top+1] = curr.left
            top += 1
        if curr.right != None:
            queue[top+1] = curr.right
            top += 1
        front += 1
 
    if count % 2 == 0:
        for i in range(prevFront + 1, top):
            print(queue[i].data, end=' ')
    else:
        for i in range(top - 1, prevFront, -1):
            print(queue[i].data, end=' ')
 
# Driver code
if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(7)
    root.left.right = Node(6)
    root.right.left = Node(5)
    root.right.right = Node(4)
    levelOrder(root, 7)
