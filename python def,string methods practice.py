#!/usr/bin/env python
# coding: utf-8

# # def function
# 
# 

# In[56]:


def roshan(n):                 #n!-----4!-->4*3*2*1=24   recursion function call
    if n==1:
        return 1
    else:
        return n*n-1
n=int(input())
print(roshan(n))


# In[9]:


def tharun(*r):                #variable number of arguments
    return r
print(tharun(10,20,30,40))       #gives return in tuple 


# In[14]:


def sandeep(n):         #sandeep is a function name
    if n>0:
        sandeep(n-1)
        print(n)
n=int(input())            #integer input
sandeep(n)


# In[17]:


a=int(input())            #swapping the numbers by taking inputs from user
b=int(input())
temp1=a
temp2=b
a=temp2
b=temp1
print(a,b)


# In[24]:


'''i  j
   4  7
   3  11
   2  14
   1  16
   0  17
   return 17'''
def tharun(i,j):
    if i==0:
        return j
    else:
        return tharun(i-1,i+j)
i=int(input())
j=int(input())
print(tharun(i,j))


# In[26]:


#lambda--> anonymous function, doesn't having any name
#a,b are parameters passing
add = lambda a,b:a+b
add(3,5)


# In[29]:


#the variable passing inside the function called as 'local variable'
#the variable passing outside the function called as 'global variable'
def rupa(a):
    a=10           #local variable
    print(a)
a=5                #global variable
rupa(a)        #local variable is printed
print(a)       #global variable is printed


# In[41]:


#global keyword is used to make local variable to global variable
def chinni(a):
    global a
    a=10
print(a)


# In[36]:


x='awesome'
def sam():
    print('tharun is '+x)
sam()


# In[55]:


def tharun(n,k):
    for i in range(k):
        print(n,'*',i,'=', n*i)
        i+=1
n=10
k=10
tharun(n,k)


# # string methods

# In[63]:


list1=[1,3,4,5]          #append element is used to append one element--->at last
list1.append(2)
list1


# In[61]:


list1=[1,3,4,5]           #extend method is used to append a list of elements in another list
list1.extend([20,30])
list1


# In[65]:


list1=[1,3,4,5]           #insert method is used to insert sn element at perticular index number
list1.insert(1,50)        #paramets are-->(index number, element)
list1


# In[69]:


list1=[1,2,3,4,5]        #pop method is used to remove the last element from the last
list1.pop()
list1


# In[70]:


list1=[1,2,3,4,5]
list1.pop(2)          #pop(2)-->here 2 is the index number, and   is used to remove the 2nd index element from the list
list1


# In[72]:


list1=[10,20,30,40,50]     #clear method is used to clear all elements
list1.clear()
list1


# In[74]:


list1=[10,20,30,40,50]     #index  method is used print the index value of element
list1.index(10)


# In[80]:


list1=[10,20,20,20,30,40,50]      
a=list1.count(20)
b=list1.count(10)
print(a)
print(b)


# In[81]:


list1=[10,70,1,40,50]     #sort method is used to sort the list elements in ascending order
list1.sort()
list1


# In[83]:


list1=['tharun','roshan','sandeep','karthik']     #reverse method is used to print the list in the reverse order
list1.reverse()
list1


# In[89]:


list1=['tharun','roshan','sandeep','karthik']      
list1.pop()
list1


# In[91]:


list1=['tharun','roshan','sandeep','karthik']      
list1.pop(2)


# In[92]:


list1=['tharun','roshan','sandeep','karthik']      
list1.append('bunny')
list1


# In[94]:


list1=['tharun','roshan','sandeep','karthik']      
list1.extend(['bunny','rupa','reethu'])
list1


# In[95]:


list1=['tharun','roshan','sandeep','karthik']     #remove method is used to remove the element form the list using element name
list1.remove('tharun')
list1


# In[96]:


list1=['tharun','roshan','sandeep','karthik']     #clear method is used to remove all the element form the list using element name
list1.clear()
list1


# In[97]:


list1=['tharun','roshan','sandeep','karthik']      
list1.insert(0,'virat')
list1


# In[101]:


list1=[10,1,3,50,16]      #sort(reverse = True) method is used to sort the element in descending order in the list
list1.sort(reverse=True)
list1


# In[102]:


list1=[10,1,3,50,16]     #sort(reverse = False) method is used to sort the element in ascending order in the list
list1.sort(reverse=False)
list1


# In[107]:


list2=list1.copy()       #copy method is used to copy all elements of one list in another list
print(list1,list2)


# In[10]:


n=int(input())
words=[input().split("/n") for i in range(n)]
t=count(words)
list3=[]
for i in words:
    list3.append(words.count(i))
print(t)
print(list3) 


# In[15]:


from collections import Counter
n=int(input()); 
words=[input().split('\n') for i in range(n)]
n_words=Counter(list(map(tuple,words)))
print(len(n_words))
for i in n_words:
    print(n_words[i],end=" ")


# In[14]:


from collections import Counter
n=int(input()); words=[input().split('\n') for i in range(n)]
n_words=Counter(list(map(str,words)))
print(n_words)


# In[ ]:





# In[26]:


n = int(input())
def tharun(n):
    if n%2==0 and n<21:
        if n in range(2,6):
            print('Not Weird')
        if n in range(6,21):
            print('Weird')
    elif n%2==0 and n>20:
        print('Not Weird')
    elif n%2!=0:
        print('Weird')
tharun(n)


# In[47]:


s=input()
list1=[]
for j in s:
    list1.append(s.count(j))
print(list1)


# In[29]:


s='tharun'
s.count('t')


# In[40]:


t=('1122334')
t.('1')


# In[68]:


n,m = map(int,input().split())
array = list(map(int,input().split()))
A={*input().split(',')} 
B={*input().split(',')}
happiness=0
for i in array:
    if i in A:
        happiness+=1
    elif i in B:
        happiness-=1
print(happiness)


# In[65]:


n,m = map(int,input().split())
array = list(map(int,input().split()))
A = set(map(int,input().split()))
B = set(map(int,input().split()))
happy=len(A.intersection(array))
sad=len(B.intersection(array))
happiness=happy-sad
print(happiness)


# In[60]:


n, m = map(int, input().split())
arr = list(map(int, input().split()))
a = set(map(int, input().split()))
b = set(map(int, input().split()))

happ = len(a.intersection(arr))
sad = len(b.intersection(arr))
print(happ-sad)


# In[67]:


n,m=map(int,input().split())
c=list(map(int,input().split()))
a=set(map(int,input().split()))
b=set(map(int,input().split()))
happiness=0
for i in c:
    if i in a:
        happiness+=1
    elif i in b:
        happiness-=1
        
print(happiness)


# In[74]:


n = int(input())
list1=[]
for i in range(1,n+1):
    list1.append(i)
list2=(map(str,list1))
print(''.join(list2))


# In[ ]:


dictionary1=dict(map())


# In[101]:


from collections import OrderedDict
n=int(input())
d=OrderedDict()
for _ in range(n):
    key,value=(input().split())
if d[key] in d:
    d[key]+=int(value)
else:
    d[key]=int(value)
for key,value in d.items():
    print(key,value)


# >>> ordered_dictionary = OrderedDict()
#  ordered_dictionary['a'] = 1
#  ordered_dictionary['b'] = 2
# ordered_dictionary['c'] = 3
# ordered_dictionary['d'] = 4
# ordered_dictionary['e'] = 5

# In[79]:


ordered_dictionary =dict()
ordered_dictionary['a'] = 1
ordered_dictionary['b'] = 2
ordered_dictionary['c'] = 3
ordered_dictionary['d'] = 4
ordered_dictionary['e'] = 5
print(ordered_dictionary)


# In[96]:


from collections import OrderedDict

N = int(input())
item_log = OrderedDict()

for _ in range(N):
    item_name, item_price =input().split()
    if item_name in item_log:
        item_log[item_name] += int(item_price)
    else:
        item_log[item_name] = int(item_price)
        
for item_name, net_price in item_log.items():
    print(item_name, net_price)


# In[102]:


from collections import OrderedDict

N = int(input())
item_log = OrderedDict()
for _ in range(N):
    item_name, item_price =input().rsplit(' ',1)
    if item_name in item_log:
        item_log[item_name] += int(item_price)
    else:
        item_log[item_name] = int(item_price)
        
for item_name, net_price in item_log.items():
    print(item_name, net_price)


# In[2]:


t='tharunvirat'
t.upper()


# In[3]:


t='tharun THARUNVIRAT virat'
t.lower()


# In[5]:


t='THARUNVIRAT1234'
t.isalpha()


# In[6]:


t='THARUNVIRAT1234'
t.isdigit()


# In[9]:


t='tharun VIRAT 1234'
t.swapcase()


# In[11]:


t='THARUNVIRAT1234'
t.count('T')


# In[12]:


t='THARUNVIRAT1234'
t.isdecimal()


# In[13]:


t='THARUNVIRAT1234'
t.isnumeric()


# In[14]:


t='THARUNVIRAT1234'
t.endswith()


# In[12]:


'''7
3573579
k'''



n=int(input())  #7                          
array=list(map(int,input().split())) #3,5,7,3,5,7,9
k=int(input())  #3
array2=array[:k]
if k==0:
    print('duplicates not found within range of k')
for i in range(k):
    if array2[i] in array[k:n]:
        print('duplicates found within range of k at index ',array[k:n].index(array2[i])+k)
    elif array2 != array[k:n]:
        print('duplicates not found within range of k')
        break


# In[13]:


n=int(input())  #7                          
array=list(map(int,input().split())) #3,5,7,3,5,7,9
k=int(input())  #3
array2=array[:k]
if k==0:
    print('duplicates not found within range of k')
for i in range(k):
    if array2[i] in array[k:n]:
        print('duplicates found within range of k at index ',array[k:n].index(array2[i])+k)
    elif array2 != array[k:n]:
        print('duplicates not found within range of k')
        break


# In[1]:


n=int(input())  #7                          
array=list(map(int,input().split())) #3,5,7,3,5,7,9
k=int(input())  #3
array2=array[:k]
if k==0:
    print('duplicates not found within range of k')
for i in range(k):
    if array2[i] in array[k:n]:
        print('duplicates found within range of k at index ',array[k:n].index(array2[i])+k)
    elif array2 != array[k:n]:
        print('duplicates not found within range of k')
        break


# In[4]:


n=int(input())  #7                          
array=list(map(int,input().split())) #3,5,7,3,5,7,9
k=int(input())  #3
array2=array[:k]
if k==0:
    print('duplicates not found within range of k')
for i in range(k):
    if array2[i] in array[k:n]:
        print('duplicates found within range of k at index ',array[k:n].index(array2[i])+k)
    if array2[i] not in array[k:n]:
        print('duplicates not found within range of k')
        break


# In[7]:


head=list(map(int,input().split()))
list2=[]
for i in range(len(head)):
    if head[i] not in list2:
        list2.append(head[i])
print(list2)


# In[12]:


num1=int(input())
num2=int(input())
n1=str(num1)
n2=str(num2)
count=0
for i in range(len(n1)):
    for j in range()


print(type(n1))


# In[3]:


try:
    print(f"{:.2f} 5/1")
except:
    print('error')
finally:
    print('tharun')


# In[17]:


s='tharun'
loopcounter=6
for i in range(len(s)):
    loopcounter=loopcounter - 1
    print(s[loopcounter])


# In[20]:


c='f'
a='s'
b='x'
sum=int(a)+(b)+(c)
print(sum)


# In[15]:


def sorting(arr):
    low=0
    mid=0
    high=len(arr)-1
    while(mid<=high):
        if(arr[mid]==1):
            mid+=1
        elif(arr[mid]==0):
            temp=arr[low]
            arr[low]=arr[mid]
            arr[mid]=temp
            low+=1
            mid+=1
        elif(arr[mid]==2):
            temp=arr[high]
            arr[high]=arr[mid]
            arr[mid]=temp
            high-=1
    return arr

arr=list(map(int,input().split()))
print(sorting(arr))


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




