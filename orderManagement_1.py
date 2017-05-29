# 첫 번째 줄에는 주문의 수 n이 주어집니다. 그 후 n개의 줄에 대하여 주문에 대한 정보가 주어집니다.
# 이는 3개의 숫자 a, b, c로 주어지며, aa는 고객이 방문하는 시간, b는 주문을 처리하기 위해 걸리는 시간,
# cc는 이 사람이 VIP인지에 대한 여부를 나타냅니다. 편의를 위하여 시간은 시/분/초 단위가 아닌, 초단위라고 가정합니다.
# 즉, 시간이 ‘2시 30분 41초’의 꼴로 주어지지 않고, 단순히 ‘1032초’의 꼴로 주어집니다.
# bb 역시 초단위이며, c=0 일 경우에는 일반주문, c=1일 경우에는 VIP주문을 나타냅니다.
# 편의상 aa 순으로 정렬되어 주어진다고 가정합니다.
# 입력 예시 :
# 4
# 1 3 0
# 4 3 0
# 7 3 0
# 10 3 0
# 출력 예시 : 1 2 3 4

from queue import *

class orderInfo:

    def __init__(self, i, t, d, v):
        self.idx = i
        self.time = t
        self.duration = d
        self.vip = v

def processOrder(orders) :


    result = []
    normal = Queue()
    vip = Queue()
    target = Queue()

    currTime = 1
    currIndex = 0

    while len(result) != len(orders):

        # print("len(result) = ", len(result), "; len(orders) = ", len(orders))

        while currIndex < len(orders) and orders[currIndex].time <= currTime :
            # print("currIndex before while: ", currIndex)

            if orders[currIndex].vip == 1 :
                vip.put(orders[currIndex])
            else :
                normal.put(orders[currIndex])
            currIndex = currIndex +1

        # print("currIndex after while: ", currIndex)

        if not vip.empty():
            target = vip.get()
        else :
            target = normal.get()

        # print("target.index: ", target.idx)


        currTime = currTime + target.duration
        result.append(target.idx)

        # print("result: ", result)

    return result

def main():


    p = int(input())

    orders = []

    for i in range(p) :
        myList = [int(v) for v in input().split()]

        orders.append(orderInfo(i+1, myList[0], myList[1], myList[2]))

    print(*processOrder(orders))

if __name__ == "__main__":
    main()
