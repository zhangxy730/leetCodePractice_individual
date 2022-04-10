class daynames:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None

e1 = daynames('Mon')
e2 = daynames('Tue')
e3 = daynames('Wed')
print(e1.nextval)