import sys
input = sys.stdin.readline

class CustomSet:
    def __init__(self):
        self.obj = set()

    def add(self, element):
        self.obj.add(element)

    def remove(self, element):
        self.obj.discard(element)
    
    def toggle(self, element):
        if element in self.obj:
            self.obj.remove(element)
        else:
            self.obj.add(element)

    def check(self, element):
        print(1 if element in self.obj else 0)
    
    def all(self):
        self.obj = set(range(1, 21))

    def empty(self):
        self.obj.clear()

S = CustomSet()

for _ in range(int(input())):
    command = input().strip().split()
    cmd = command[0]

    if cmd == 'add':
        S.add(int(command[1]))
    elif cmd == 'remove':
        S.remove(int(command[1]))
    elif cmd == 'check':
        S.check(int(command[1]))
    elif cmd == 'toggle':
        S.toggle(int(command[1]))
    elif cmd == 'all':
        S.all()
    elif cmd == 'empty':
        S.empty()