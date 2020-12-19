import random


# 4个最简单的结构
# 栈 Stack  队列 Queue 双端队列 Deque  列表 List
# ---------------------------------------------
"""抽象数据类型：栈Stack"""
class Stack:
    """模拟栈"""
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        if not self.isEmpty():
            return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


def parChecker(symbolString):
    """
    括号匹配
    :param symbolString:
    :return:
    """
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol in "([{":
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                top = s.pop()
                if not matches(top, symbol):
                    balanced = False
        index += 1
    if balanced and s.isEmpty():
        return True
    else:
        return False


def matches(open, close):
    opens = "([{"
    closers = ")]}"
    return opens.index(open) == closers.index(close)


def divideBy2(decNumber):
    """
    二进制换算
    :param decNumber:
    :return:
    """
    remstack = Stack()
    while decNumber > 0:
        rem = decNumber % 2
        remstack.push(rem)
        decNumber = decNumber // 2
    binString = ""
    while not remstack.isEmpty():
        binString = binString + str(remstack.pop())
    return binString


def baseConverter(decNumber, base):
    """
    十进制转换为十六以下任意进制
    :param decNumber:
    :return:
    """
    digits = "0123456789ABCDEF"
    remstack = Stack()
    while decNumber > 0:
        rem = decNumber % base
        remstack.push(rem)
        decNumber = decNumber // base
    binString = ""
    while not remstack.isEmpty():
        binString = binString + digits[remstack.pop()]
    return binString


def infixToPostfix(infixexpr):
    """
    中缀转后缀
    :param infixexpr:
    :return:
    """
    prec = {}
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1  # 记录操作符优先级
    opStack = Stack()
    postfixList = []
    tokenList = infixexpr.split()  # 解析表达式到单词列表
    for token in tokenList:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            postfixList.append(token)
        elif token == "(":
            opStack.push(token)
        elif token == ')':
            topToken = opStack.pop()
            while topToken != '(':
                postfixList.append(topToken)
                topToken = opStack.pop()
        else:
            while (not opStack.isEmpty()) and \
                    (prec[opStack.peek()] >= prec[token]):
                postfixList.append(opStack.pop())
            opStack.push(token)
    #  打印
    while not opStack.isEmpty():
        postfixList.append(opStack.pop())
    return " ".join(postfixList)


# ---------------------------------------------
"""抽象数据类型：队列Queue"""
class Queue:
    """模拟队列"""
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.item == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


# 约瑟夫问题
def hotPotato(namelist, num):
    simqueue = Queue()
    for name in namelist:
        simqueue.enqueue(name)
    while simqueue.size() > 1:
        for i in range(num):
            simqueue.enqueue(simqueue.dequeue())  # 一次传递
        simqueue.dequeue()  # 踢出被点到的人
    return simqueue.dequeue()


# 打印机问题
class Printer:
    def __init__(self, ppm):
        self.pagerate = ppm  # 打印速度
        self.current_task = None  # 打印任务
        self.time_remaining = 0  # 任务倒计时

    def tick(self):  # 打印1秒
        if self.current_task != None:
            self.time_remaining -= 1
            if self.time_remaining <= 0:
                self.current_task = None

    def busy(self):  # 打印繁忙?
        if self.current_task != None:
            return True
        else:
            return False

    def startNext(self, newtask):  # 打印新作业
        self.current_task = newtask
        self.time_remaining = newtask.getPages() \
                              * 60/self.pagerate


class Task:
    def __init__(self, time):
        self.timestamp = time  # 生成时间戳
        self.pages = random.randrange(1, 21)  # 打印页数

    def getStamp(self):
        return self.timestamp

    def getPages(self):
        return self.pagespages

    def waitTime(self, currnttime):
        return currnttime - self.timestamp


def newPrintTask():  # 1/180 概率生成作业
    num = random.randrange(1, 181)
    if num == 180:
        return True
    else:
        return False


def simulation(numSeconds, pagesPerMinute):  # 主体函数 模拟
    labprinter = Printer(pagesPerMinute)
    printQuene = Queue()
    waitingtimes = []

    for currentSecond in range(numSeconds):  # 时间流逝
        if newPrintTask():
            task = Task(currentSecond)
            printQuene.enqueue(task)
        if (not labprinter.busy()) and \
                (not printQuene.isEmpty()):
            nexttask = printQuene.dequeue()
            waitingtimes.append(
                nexttask.waitTime(currentSecond))
            labprinter.startNext(nexttask)
        labprinter.tick()

    averageWait = sum(waitingtimes) / len(waitingtimes)
    print("Average Wait %6.2f secs %3d tasks remaining."
          % (averageWait, printQuene.size()))


# ---------------------------------------------
"""抽象数据类型:双端队列Deque"""
class Deque:
    """
    List下标0作为deque的尾端
    list下标-1作为deque的首端
    """
    def __init__(self):
        self.items = []

    def iSEmpty(self):
        return self.items == []

    def addFront(self, item):
        self.items.append(item)

    def addRear(self, item):
        self.items.insert(0, item)

    def removeFront(self):
        return self.items.pop()

    def removeRear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)


# 回文词判定
def palchecker(aString):
    """
    先将需要判定的词从队首加入deque
    再从两端同时移除字符判定是否相同，
    直到deque中剩下0个或1个字符
    """
    chardeque = Deque()
    for ch in aString:
        chardeque.addFront(ch)
    stillEqual = True
    while chardeque.size() > 1 and stillEqual:
        first = chardeque.removeRear()
        last = chardeque.removeFront()
        if first != last:
            stillEqual = False
    return stillEqual


# ---------------------------------------------
# 链表

"""链表实现：节点Node"""
class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newdata):
        self.data = newdata

    def setNext(self, newnext):
        self.next = newnext


"""抽象数据类型:无序表Unorderedlist（链表实现）"""
class Unorderedlist:

    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def size(self):
        """
        链表实现:size
        :return:
        """
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.getNext()
        return count

    def search(self, item):
        """链表实现：查找"""
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
        return found

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()
        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())


"""抽象数据类型:有序表OrderedList"""
"""
OrderedList(): 创建一个空的有序表
add(item): 在表中添加一个数据项，并保持整体顺序，此项原不存在

search(item): 在有序表中查找数据项，返回是否存在
isEmpty(): 是否空表
index(item): 返回数据项在表中的位置，此项应存在
pop(): 移除并返回有序表中最后一项，表中应至少存在一项
pop(pos): 移除并返回有序表中指定位置的数据项，此位置应存在
"""
class OrderedList:
    def __init__(self):
        self.head = None

    def iSEmpty(self):
        return self.head == None

    def size(self):  # 返回表中数据项的个数
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.getNext()
        return count

    def remove(self, item):
        # remove(item): 从有序表中移除一个数据项，此项应存在，在有序表被修改
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()
        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())


if __name__ == "__main__":
    X = infixToPostfix("A + B * C")
    print(X)






