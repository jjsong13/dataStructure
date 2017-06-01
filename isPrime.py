import math

# '''
# 다음의 함수들은 math 내의 함수들입니다. 참고하도록 합니다. 반드시 이 모든 함수를 써야한다는 의미는 아닙니다.
#
# math.sqrt(x) : 루트 x를 반환
# math.log(x) : 자연로그 x를 반환
# math.log10(x) : 상용로그 x를 반환
# '''

def isPrime(n):
    # '''
    # 숫자 n이 소수이면 True, 아니면 False를 반환하는 함수
    # '''
        if n%i == 0 :
            return False

    return True

    # My first attempt was code below but because this has  3 calculations for each for loop,
    # it's too slow and leads to error 
    # for i in range(2,int(math.sqrt(n))+1):
    #     j = 1
    #     while i * j <= n :
    #         if i * j == n:
    #             return False
    #         else :
    #             j = j + 1

def main():

    n = int(input())

    print(isPrime(n))

if __name__ == "__main__":
    main()
