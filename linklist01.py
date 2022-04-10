class Node:
  def __init__(self, data, next=None):
    self.data = data
    self.next = next
s = Node(5)
print(s.data)
print(s.next)