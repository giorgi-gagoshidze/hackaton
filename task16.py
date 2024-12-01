list = [1,5,3,6,3,7,354,3435,3]
def sashualo_aretmitekuli(arr):
    a = 0
    for i in arr:
        a += i
    return a / len(list)
print(sashualo_aretmitekuli(list))