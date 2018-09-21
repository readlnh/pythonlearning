#reference(引用)只是一种别名不会代表变量本身
print('Simple Assignment')
shoplist = ['apple', 'mango', 'carrot', 'banana']
#mylist只是指向同一对象的另一种名称
mylist = shoplist

del shoplist[0]
#可见两者指的是同一个对象

print('shoplist is ', shoplist)
print('mylist is ', mylist)

print('Copy by making a full slice')
#通过生成一份完整的切片制作一份列表的副本
mylist = shoplist[:]

del mylist[0]

print('shoplist is', shoplist)
print('mylist is', mylist)