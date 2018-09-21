#python从0开始，切片左闭右开
shoplist = ['apple', 'mango', 'carrot', 'banana']
name = 'swaroop'

#索引(Indexing)或下标(Subscription)
print('Item 0 is', shoplist[0])
print('Item 0 is', shoplist[1])
print('Item 0 is', shoplist[2])
print('Item 0 is', shoplist[3])
print('Item 0 is', shoplist[-1])
print('Item 0 is', shoplist[-2])
print('Item 0 is', name[0])

#list的切片(Slicing)
print('Item 1 to 3 is', shoplist[1:3])
print('Item 2 to end is', shoplist[2:])
print('Item 1 to -1 is', shoplist[1:-1])
print('Item start to end is', shoplist[:])

#字符串的切片
print('characters 1 to 3 is', name[1:3])
print('characters 2 to end is', name[2:])
print('characters 1 to -1 is', name[1:-1])
print('characters start to end is', name[:])