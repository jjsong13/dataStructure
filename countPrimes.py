def countPrimes(t):
    # '''
    # 1부터 t까지의 수 중에서 소수의 개수를 반환합니다.
    # '''

    testArr = [1]*(t+1)
    testArr[0],testArr[1] = 0,0
    count = 0

    for i in range(2, t+1):
        # print("this is testArr[",i,"]:",testArr[i])
        if testArr[i] == 1:
            j = 2
            count = count + 1
            while i*j <= t:
                testArr[i*j] = 0
                j = j+1


    return count

def main():
    # '''
    # 이 부분은 수정하지 마세요.
    # '''

    t = int(input())

    print(countPrimes(t))

if __name__ == "__main__":
    main()
