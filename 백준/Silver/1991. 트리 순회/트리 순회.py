import sys

input = sys.stdin.readline

class Node:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right
  
def pre_order(node: Node):
    if node:
        print(node.data, end='')
        pre_order(tree.get(node.left))
        pre_order(tree.get(node.right))
        
def in_order(node: Node):
    if node:
        in_order(tree.get(node.left))
        print(node.data, end='')
        in_order(tree.get(node.right))
        
def post_order(node: Node):
    if node:
        post_order(tree.get(node.left))
        post_order(tree.get(node.right))
        print(node.data, end='')
      
n = int(input())
tree = {}

for _ in range(n):
    data, left, right = input().split()
    tree[data] = Node(data, left if left != '.' else None, right if right != '.' else None)
    
root = tree['A']
pre_order(root)
print()
in_order(root)
print()
post_order(root)
