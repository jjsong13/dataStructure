# 첫 번째 줄에 n개의 정수들이 오름차순으로 주어집니다.
# n의 값은 따로 주어지지 않습니다. (1≤n≤100,000,000)
# 합이 0에 가장 가까운 숫자쌍을 빈 칸으로 구분하여 출력합니다. 숫자쌍은 오름차순으로 정렬하여 출력하며, 정답이 여러개일 경우 그 중 하나만 출력하면 됩니다.
# Second attmept was two slow as time complexity was at least O(n^2)
# First attempt was just wrong as the loop stopped if the first evaluation was bigger than diff
# Final attempt is  O(n) 
def sum_0(data):
    # Implement here

    minDiff = 100000000
    i = 0
    j = len(data)-1

    while i < j :
        if minDiff > abs(data[i] + data[j]) :
            minDiff = abs(data[i] + data[j])
            return_pair = [data[i], data[j]]

        if abs(data[i] + data[j-1]) < abs(data[i+1] + data[j]) :
            j = j -1
        else :
            i = i + 1

    return return_pair



#  <--- SECOND ATTEMPT --->
#     final_return_pair = [0, 0]
#     local_return_pair = [0, 0]


#     final_diff = data[-1]

#     for i in range(len(data)):

#         local_diff = data[-1]
#         j = -1

#         while local_diff > abs(data[i]+ data[j]) and data[i] < data[j]:
#             local_return_pair = [data[i], data[j]]
#             local_diff = abs(data[i]+ data[j])
#             j = j-1

#             # print("this is local_return_pair: ", local_return_pair)

#         if final_diff > local_diff:
#             final_diff = local_diff
#             final_return_pair  = local_return_pair

#     return final_return_pair

#     <--- FIRST ATTEMPT --->
#     left_idx = 0
#     right_idx = -1

#     diff = data[right_idx]

#     while data[left_idx] <= 0 :
#         while data[right_idx] >= 0 :
#             # print("this is left, right, diff: ", data[left_idx]," , ", data[right_idx], " , ", abs(data[left_idx] + data[right_idx]))
#             if diff > abs(data[left_idx] + data[right_idx]):
#                 return_pair = [data[left_idx], data[right_idx]]
#                 diff = abs(data[left_idx] + data[right_idx])

#             right_idx = right_idx -1

#         left_idx = left_idx +1
#         right_idx = -1



    # return return_pair

def main():
    '''
    이 부분은 수정하지 마세요.
    '''

    given_data = input()

    data = [int(v.strip()) for v in given_data.split()]

    print (*sum_0(data))

if __name__ == "__main__":
    main()
