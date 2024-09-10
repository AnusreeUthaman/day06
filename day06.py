#Data structures
#LIST,DICTIONARY,TUPLE

#LIST []-handling one or more data
>Ordered
>indexing
>slicing
>duplicates are allowed
>changable
>List methods-apppend,insert,remove,pop,sort,reverse,count,index,clear,copy


Mark = [30,25,35,45,48]
      # 0  1  2  3  4  =indexing - left to right , starting from 0 to infinity
      #-5  -4 -3 -2 -1  =negative indexing- right to left, starting from -1 to infinity
print(mark)
# ordered-unique positions
# Items,elememts
# indexing
#negative indexing

sample_list=[1,2,"hello",45.50,True,"codeme"]
print(sample_list[3])
print(sample_list[3]="vitez")
print(len(sample_list))


#SLICING [start:end:steps]

data=[10,20,30,40,50,60]
     #0  1  2  3  4  5
     #-6 -5 -4 -3 -2 -1

print(data[1:4])
print(data[1:])
print(data[:5])
print(data[-4:-2])
print(data[-2:-4])
print(data[:-2])
print(data[-5:])

print(data[0:5:2])
print(data[::3])
print(data[::-1])
print(data[-2:-5:-1]

print(data[1:3:4])

print(data[1:3:5])


a=[1,2,3,4,5,6]

print(a[2:4])#[3,4]
print(a[4:5])#[5]
print(a[2])#3
print(a[-2:-4:-1])#[5,4]
print(a[1::2])#[2,4,6]
print(a[::-1])#[6,5,4,3,2,1]
print(a[-2::-1])#[5,4,3,2,1]
'''

'''
#LIST METHODS()

#append
mark=[30,25,35,45,30]
mark.append(55)
print("list.append(item)",mark)

mark1=[30,25,35,45,30]
mark1.append(45)
print("list.append(item)",mark1)

#insert
mark2=[30,25,35,45,30]
mark2.insert(1,22)
print("list.insert(position,item)",mark2)


#remove
mark3=[11,22,33,44,55]
mark3.remove(22)
print("list.remove(item)",mark3)

#pop
mark4=[12,13,14,15,16]
mark4.pop()
print("list.pop()",mark4)

mark5=[44,55,66,77,88]
mark5.pop(3)
print("list.pop(position)",mark5)

#sort
mark6=[45,23,34,54]
mark6.sort(reverse=True)
print(mark6)




#append(item),insert(index,item),remove(item),pop(),pop(index)
#extend(),count(),sort(),sort(reverse=True),reverse()
#sum,min,max
#extend()
#append(item)
x=[3,4,5,2,1,4]
x.append(6)
print(x)#[3,4,5,2,1,4,6]

#insert(index,item)
x=[3,4,5,2,1,4]
x.insert(3,7)
print(x)#[3, 4, 5, 7, 2, 1, 4]

#remove(item)
x=[3,4,5,2,1,4]
x.remove(2)
print(x)#[3, 4, 5, 1, 4]

#pop()
x=[3,4,5,2,1,4]
x.pop(3)
print(x)#[3, 4, 5, 1, 4]

#pop(index)
x=[3,4,5,2,1,4]
x.pop(1)
print(x)#[3, 5, 2, 1, 4]


#extend()
a=[1,2,3]
b=[4,5]
print(a+b)#[1,2,3,4,5]
b.extend(a)
print(b)#[4,5,1,2,3]

#count()
x=[3,4,5,2,1,4,4]
print(x.count(4))#3(4 appers 3 times in a list)


#sort()-ascending
x=[3,4,5,2,1,4]
x.sort()
print(x)#[1, 2, 3, 4, 4, 5]

#sort(reverse=True)descending
x=[3,4,5,2,1,4]
x.sort(reverse=True)
print(x)#[5, 4, 4, 3, 2, 1]


#reverse
x=[3,4,5,2,1,4]
x.reverse()
print(x)#[4, 1, 2, 5, 4, 3]


#index
x=[3,4,5,2,1,4]
print(x.index(4))#1



      




