# Another answer to the orderMangement_1 challenge.
# Divided original processOrder method into two methods
# Not sure why orderMangement_2 is faster than orderMangement_1, but 2 passed while 1 didn't when submitted on elice.

class Queue:
    '''
    List를 이용하여 다음의 method들을 작성하세요.
    '''
    def __init__(self) :
        '''
        큐 myQueue을 만듭니다.
        '''
        self.myQueue = []

    def push(self, n) :
        '''
        queue에 정수 n을 넣습니다.
        '''
        self.myQueue.append(n)

    def pop(self) :
        '''
        queue에서 가장 앞에 있는 정수를 제거합니다. 만약 queue에 들어있는 값이 없을 경우에는 아무 일도 하지 않습니다.
        '''
        if len(self.myQueue) != 0 :
            self.myQueue.pop(0)

    def size(self) :
        '''
        queue에 들어 있는 정수의 개수를 return 합니다.
        '''
        return len(self.myQueue)

    def empty(self) :
        '''
        queue이 비어있다면 1, 아니면 0을 return 합니다.
        '''
        if len(self.myQueue) == 0 :
            return 1
        else :
            return 0

    def front(self) :
        '''
        queue의 가장 앞에 있는 정수를 return 합니다. 만약 queue에 들어있는 값이 없을 경우에는 -1을 return 합니다.
        '''
        if len(self.myQueue) == 0 :
            return -1
        else :
            return self.myQueue[0]

    def back(self) :
        '''
        queue의 가장 뒤에 있는 정수를 return 합니다. 만약 queue에 들어있는 값이 없을 경우에는 -1을 return 합니다.
        '''
        if len(self.myQueue) == 0 :
            return -1
        else :
            return self.myQueue[len(self.myQueue)-1]


class orderInfo:
    '''
    이 부분은 수정하지 마세요.
    '''
    def __init__(self, t, d, v):
        self.time = t
        self.duration = d
        self.vip = v

def selectQueue(orders,vipQ, normalQ, currTime):

    if normalQ.empty() :
        normalEle = orderInfo(-1,-1,-1)
    else :
        normalEle = orders[normalQ.front()]

    if vipQ.empty() :
        vipEle = orderInfo(-1,-1, -1)
    else :
        vipEle = orders[vipQ.front()]

    if currTime < normalEle.time and currTime < vipEle.time :
        if normalEle.time < vipEle.time :
            return normalQ
        else :
            return vipQ

    if vipEle.time != -1 and vipEle.time <= currTime :
        return vipQ
    else :
        return normalQ



def processOrder(orders) :
    '''
    주문 정보가 주어질 때, 주문이 처리되는 순서를 출력합니다.
    '''

    result = []
    vipQ = Queue()
    normalQ = Queue()
    currTime = 0

    for i in range(len(orders)):
        if orders[i].vip == 1:
            vipQ.push(i)
        else :
            normalQ.push(i)

    while not (vipQ.empty() and normalQ.empty()):
        targetQ = selectQueue(orders, vipQ, normalQ, currTime)
        resultIdx = targetQ.front()
        result.append(resultIdx+1)
        targetQ.pop()

        if currTime < orders[resultIdx].time :
            currTime = orders[resultIdx].time + orders[resultIdx].duration
        else :
            currTime = currTime+ orders[resultIdx].duration

    return result

def main():
    '''
    이 부분은 수정하지 마세요.
    '''

    p = int(input())

    orders = []

    for i in range(p) :
        myList = [int(v) for v in input().split()]

        orders.append(orderInfo(myList[0], myList[1], myList[2]))

    print(*processOrder(orders))

if __name__ == "__main__":
    main()
