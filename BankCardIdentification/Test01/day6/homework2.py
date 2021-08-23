
hjc_list=['19990902','hejaichen','CharlesHe']
print(hjc_list[2])
print(len(hjc_list))

print(hjc_list[1:5])

alist=[10,20,'a','bcd',[1,2,3]]
print(alist[-1])
print(alist[4][-2])
print(alist[0])
print(alist[5])
print(len(alist))
alist.remove(10)
print(alist)

x=3
x+=6
print(x)

_test=1
print(_test)

x=[1,2,3,2,3]
x.pop()
print(x)

path = r'c:\test.html'
print(path[:-4]+'htm')

name = ['F', 'i', 'h', 'w']
name.insert(2,'s')
print(name)

#编程题1
alist=[1,2,3,'abc','def',3,5]
print(alist[::-1])

#编程题2
#方法一
member = ['金鱼', '黑夜', '迷途', '怡静', '太阳']
member.insert(1,88)
member.insert(3,90)
member.insert(5,85)
member.insert(7,90)
member.insert(9,88)
print(member)

#方法二
member = ['金鱼', '黑夜', '迷途', '怡静', '太阳']
member[1:1]=[88]
member[3:3]=[90]
member[5:5]=[85]
member[7:7]=[90]
member[9:9]=[88]
print(member)


#编程题3
list1 = [1, [1, 2, ['小金鱼']], 3, 5, 8, 13, 18]
list1[1][2]=['章鱼保罗']
print(list1[1][2])

#编程题4
list2 = [1, 8, 2, 3, 5, 8, 13, 18]
list2.sort()
print(list2)

#编程题5
dict1={1:'tony',2:'tom',3:'john',4:'tony'}
list1=['a','b','c','d']
list2=['aaaa','cccc','dddd','eeee']
dict2={}
for key,value in zip(list1,list2):
    dict2[key]=value
print(dict2)
print(dict1[3])
print(dict2['b'])
for key, value in dict2.items():
    if key == 'b':
        dict2['b'] = "ffff"
print(dict2)


#编程题6
lista=[2,2,3,4,5,6,2,6,7,8]
seta=set()
seta=set(lista)
print(seta)






