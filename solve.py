# # li = [1,2,3,4]

# # # summation
# # for i in li:
# #     value = 0
# #     value += i 

# # print(value)

# # # max value
# # for i in li:
# #     max = li[0]
# #     if i > max:
# #         max= i

# # print(max)

# # #  Write a Python program to count the number of strings from a given list of strings when
# # #  The string length is 2 or more and the first and last characters are the same.
# # a= ['abc', 'xyz', 'aba', '1221']
# # counti =0
# # for i in a:
   
# #     if len(i) >= 2 and i[0]==i[-1]:
# #         counti+=1

# # print(counti)

# # # Write a Python program to remove duplicates from a list

# # li1 = [1,2,3,4,2,6,3]
# # li2=[]

# # for i in li1:
# #     if i not in li2:
# #         li2.append(i)

# # print(li2)

# # # Write a Python program to check if a list is empty or not.
# # if len(li)==0:
# #     print("empy")
# # else:
# #     print("not empty")

# # # copy a list
# # li3 = [1,2,34,4]
# # copy = []
# # for i in li3:
# #     copy.append(i)
# # print(copy)

# # # Write a Python program to find the list of words that are longer than n from a given list of words.
# # n= 3
# # strin = "The quick brown fox jumps over the lazy dog"



# upper = 900
# lower = 1000
# for num in range(lower,upper+1):
#     if num>1:
#         for i in range(2,num):
#             if num% i ==0:
#                 break
#             else:
#                 print(num)

# numb = 89
# flag = False
# if numb>1:
#     for i in range(2,numb):
#         if(numb%i ==0):
#             Flag = True

# if flag:
#     print("not prime")
# else:
#     print("prime")
            
lis = [1,1,2,2,3,4]
info ={}
for i in lis:
    if i in info:
        info[i] += 1
    else:
        info[i] =1
print(info)
for i,v in info.items():
    if v==1:
        print(i)
        
    else:
        print("none")

a = 'abcd'

lis= []
for i in range(len(a),1):
    
    print(i)

print(lis)

n ='abinmv'
if 'bn' in n:
    print('yes')
else:
    print('no')

## reverse list
l =[1,2,3,4,5]
print(len(l))
n=[]
for i in range(len(l)-1,-1,-1):
    n.append(l[i])
print(n)



## reverse string
j ='mahin'
k=''
for i in range(len(j)-1,-1,-1):
    k=k+j[i]

print(k)

#  remove duplicate
m= [1,2,3,4,5,3,6]
store ={} 
mm=[]
for i in m:
    if i in store:
        store[i] += 1
    else:
        store[i] =1

bi=list(sorted(store.items(),key=lambda item:item[1],reverse=True))
print(bi)

for u,v in store.items():
    if v==1:
        mm.append(u)
print(mm)       
print(store)

# valid anagram
l1 ='anagram'
l2 ='managr'
x = sorted(l1)
y = sorted(l2)
if(x== y):
    print('valid anagram')

f1=[9,0]
f2=[2,3]
f3=[*f1,*f2]
print(f3)

## 2sum
nums = [2,7,11,15]
ans =[]
for i in range(0,len(nums)-1):
    for j in range(i+1,len(nums)-1):
        if nums[i]+nums[j] == 9:
            ans.append(i)
            ans.append(j)
print(ans)

##
def my_func(*args, **kwargs):
    print("hello world", args, kwargs)

my_func("abc", "abc", 123, "abc", key=123, abc=123) 
##
s = ['a', 'b', 'c', 'd']
st = ''.join(s)
print(st)
##
