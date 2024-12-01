xmovenbi = ['a', 'e', 'i', 'o', 'u']
user = input('print something')
new_list = []
def xmovnebis_raodenobna(arr):
    for i in arr:
        for j in xmovenbi:
            if i == j:
                new_list.append(j)
    return len(new_list)
print(xmovnebis_raodenobna(user))