#Sean Dehghani
#HW5


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        if self.items == []:
            return None
        else:
            peek=self.items.copy()
            return peek.pop(-1)

    def is_empty(self):
        return (self.items == [])

    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)


def html_checker(file):
    htmlStack = Stack()

#    htmlOpen = ['<title>', '<head>', '<h1>', '<body>', '<html>']
#    htmlClose = ['</title>', '</head>', '</h1>', '</body>', '</html>']
    #print(htmlOpen)
    htmlList=[]
    #set the len(htmlClose)=len(htmlOpen)
    
    htmlFile = open (file, "r")
    for lines in htmlFile:
        lines = lines.strip()
        htmlList.append(lines)
    #return htmlList
    #print(htmlList)
    


    htmlClose = []
    for item in htmlList:
        if item.startswith("</") and item.endswith(">"):
            htmlClose.append(item)
    #return(htmlClose)

    htmlOpen = []
    for item in htmlList:
        if item.startswith("<") and item.endswith(">") and item not in htmlClose:
            htmlOpen.append(item)
    #return(htmlOpen)
    
    htmlFile.close()
    
    itemslist=[]
    Stacklist=[]
    for item in htmlList:
        #print(item)
        if item in htmlOpen:
            htmlStack.push(item)
            #print(item)
        elif item in htmlClose:
            itemslist.append(item.replace('/','')) #item.replace(old,new)
            Stacklist.append(htmlStack.pop())
    #print(Stacklist)
    #print(itemslist)
    i=len(itemslist)
    j=len(htmlClose)
    #print(i)
    #print(j)  
    if int(j) - int(i) == 0 and htmlStack.is_empty():
        return True
        #print (" This is balanced")
    return False
    #print("This is unbalanced")

print('Balanced:', html_checker("balanced.txt"))
print('Unbalanced:', html_checker("unbalanced.txt"))


            
            

