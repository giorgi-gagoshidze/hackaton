list = [234234,434334,3434,3434,34,34,34,34,12,21]
new_list = []
def square(arr):
    for i in list:
        new_list.append(i**2)
    return new_list
print(square(list))
