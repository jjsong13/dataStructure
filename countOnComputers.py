# 첫 번째 줄에는 컴퓨터 대수와 사람의 수 N(1 ≤ N ≤ 2,100,000,000)이 주어집니다.
# first line of input is N, i.e. number of people (1 <= N <= 2,100,000,000)
# output is the number of computers on at the end
# 1st person turns the switch (i.e. off if on, on if off) for all the computers that are its multiples, i.e. all
# 2nd person does the same for its multiple, i.e. 2nd, 4th, 6th, etc

# first attempt is the commented out section. It worked but time complexity is too bad so gave error when submitted.
# After working through 1-> 9 people by hand, I noticed that the pattern was that the result was actually the number of square number <= n. 

def getAnswer(n):
    '''
    마지막에 켜져 있는 컴퓨터의 대수를 반환하는 함수입니다.
    '''

#     # testArr[0] is just placeholder, so always 0
#     testArr = [1]*(n+1)
#     testArr[0] = 0

#     for i in range(2,n+1):
#         j = 1
#         while (i*j) <= n :
#             if testArr[i*j] == 0 :
#                 testArr[i*j] = 1
#             else :
#                 testArr[i*j] = 0
#             j = j+1

#     sum = 0
#     # print("this is testArr: ", testArr)
#     for k in testArr:
#         sum = sum + k

    i = 1
    sum = 0
    while i*i <= n :
        sum = sum + 1
        i = i+1

    return sum

def main():
    '''
        이 부분은 수정하지 마세요.
        '''
    print(getAnswer(int(input())))

if __name__ == "__main__":
    main()
