#set
bri = set(['brazil', 'russia', 'india'])
print('india' in bri)

bric = bri.copy()
bric.add('china')
#是否是超集
print(bric.issuperset(bri))

bri.remove('russia')
print(bri & bric)
print(bri | bric)