class parent:   


    def relation(self):
        print("Father")
        print("Mother")


class child1(parent):  # inherited the function called relation from class parent
    def child1name(self):
        print("john")


class child2(parent):     # inherited the function called relation from class parent   
    def child2name(self):
        print("Robert")

obj1 = child1()

obj1.child1name()
obj1.relation()        

obj2 = child2()

obj2.relation()