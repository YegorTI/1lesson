# s = 'sfghgfefdcgxhxhhfrhzrgzdfg'
# for sym in set(s):
#     count = 0
#     for sub_sym in s:
#         if sym == sub_sym:
#             count+=1
#     print(sym, count)


# s = ('abcccc')
# syms_counter = {}
# for sym in s:
#     syms_counter[sym] = syms_counter.get(sym, 0) + 1
# print(syms_counter)

#Д/З


palindrom = str(input('Enter: '))

for i in range(len(palindrom)):
    if palindrom[i] != palindrom[-(i+1)]:
        print('False')
        break
    elif palindrom[i-1] == palindrom[-i]:
        if i+1 == len(palindrom):
            print('True')







