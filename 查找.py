# _*_coding:utf-8_*_

def linear_serch(li,val):
    for ind, v in enumerate(li):
        if v == val:
            return ind
    else:
        return None



def binary_search(li,val):
    left = 0
    right = len(li) - 1
    while left <= right: #候选区有值
        mid = (left + right) // 2
        if li[mid] == val:
            return mid
        elif li[mid] > val: #待查找的值在左侧
            right = mid - 1
        else:#待查找的值在mid右侧
            left = mid + 1
    else:
        return None


li = [1,2,3,4,5,6,7,8,9]

print(binary_search(li,3))
print()
print(linear_serch(li,3))

