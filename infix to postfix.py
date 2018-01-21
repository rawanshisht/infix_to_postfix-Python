from pythonstack import stack
from Pythonqueue import Queue
def convertx (infix):
    ## Procedures, assigning a key to each operation
    prec = {}
    prec["^"]=4
    prec["*"]=3
    prec["/"]=3
    prec["+"]=2
    prec["-"]=2
    prec["("]=1
    ## Creating a stack, a queue and a list
    opstack = stack ()
    opqueue = Queue ()
    postfixlist =[]
    tokenlist = infix.split() ## Splitting the infix and storing it
    ## Loop on all charcaters
    for token in tokenlist:
        if token not in["^","*","/","+","-","(",")"]:## To avoid Upper/Lowercase and 2 digits problem.
            opqueue.enqueue(token) 
        elif token == '(':
            opstack.push(token)
        elif token ==')':
            toptoken=opstack.pop()
            while toptoken!= '(':
                opqueue.enqueue(toptoken)
                toptoken=opstack.pop()
        ## Procedures' comparison
        else:
            while (not opstack.isEmpty() and prec[opstack.peek()] >= prec[token]):
                opqueue.enqueue(opstack.pop())
            opstack.push(token)
            
    ## After the "tokenlist" is Empty, pop-ing all elements from the Stack into the queue
    while (not opstack.isEmpty()):
                opqueue.enqueue(opstack.pop())
    ## After the stack is Empty, enqueue-ing all elements from the queue into the list
    while (not opqueue.isEmpty()):
            postfixlist.append(opqueue.dequeue())
    return "".join(postfixlist)  ## Collecting all the elements of the list in one element
print(convertx ("2 + ( 3 * 10 ) "))  ## Calling the convert function and giving it's parameter
