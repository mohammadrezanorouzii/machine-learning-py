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

