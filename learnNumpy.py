from ctypes.wintypes import PINT
import numpy as np

arr = np.array([1, 2, 3, 4])
# not same
arr2 = [1, 2, 3, 4]

print(type(arr))
print(arr)

# 0-D arrays :
print(np.array(42))


# [1,2,3],[1,2] is impossible
arr3 = np.array([[2, 13, 13, 122], [7, 8, 9, 11]])
print(arr3)

print(arr[-3:-1])
# [2,3]
# arr[start, end, steps]

arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
arr[0] = 42

print(arr)
print(x)

# BUT :

arr = np.array([1, 2, 3, 4, 5])
x = arr.view()
arr[0] = 42

print(arr)
print(x)

print("-------------------------------------")

arr4 = np.array([[1, 2, 3], [4, 5, 6]])
print(arr4.shape)

arr5 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
arr6 = arr5.reshape(3, 4)
print(arr6)

arr7 = np.array([1, 2, 3, 4, 4, 2])
arr8 = np.array([0, 1, 8, 0])
arr9 = np.concatenate((arr7, arr8))
print(arr9)

print("=====================================")

arr10 = np.array([1, 2, 3, 4, 5, 6])
newarr = np.array_split(arr10, 3)

print(newarr[0])
print(newarr[1])
print(newarr[2])

print("____________________________________")

arr11 = np.array([1, 2, 3, 4, 5, 4, 4])
x1 = np.where(arr == 2)
print(x1)

# returns indexes which have 4 value

arr12 = np.array([6, 7, 8, 9])
x2 = np.searchsorted(arr, 7, side='right')
print(x2)

print("...................................")

arr13 = np.array([1, 2, 18, 0, 5, 6])
arr14 = np.array(['chery', 'apple',  'banana'])
print(np.sort(arr13))
print(np.sort(arr14))

# filter arrays

arr = np.array([1, 2, 3, 4, 5, 6, 7])
filter_arr = arr % 2 == 0
newarr = arr[filter_arr]

print(filter_arr)
print(newarr)

print("-------------------------------------")

print(np.random.randint(2))
print(np.random.rand())
print(np.random.randint(100, size=(3, 5)))
print(np.random.choice([3, 5, 7, 9]))

x10 = np.random.choice([0,1] , p=[0.2, 0.8] , size=100)
print(x10)

x15 = np.array([1,2,3,4,5,6,7])
print(x15[::2])