import random
import time
def naive_search(l,target):
    for i in range(len(l)):
        if l[i]==target:
            return i
        
    return-1


def binary_search(l,target,low=None,high=None):
    if low==None:
        low=0
    if high==None:
        high=len(l)-1
    if high<low:
        return -1
    midpoint=(low+high)//2
    if target==l[midpoint]:
        return midpoint
    elif target<l[midpoint]:
        return binary_search(l,target,low,midpoint-1)
    elif target>l[midpoint]:
        return binary_search(l,target,midpoint+1,high)
    

if __name__=='__main__':
    l=[1,4,45,343,777]
    target=4
    print(naive_search(l,4))
    print(binary_search(l,4))


length=10000
sorted_list=set()
while len(sorted_list)<length:
    sorted_list.add(random.randint(-3*length,3*length))
sorted_list=sorted(list(sorted_list))



start =time.time()
for target in sorted_list:
    naive_search(sorted_list,target)
end_time = time.time()
print("The search time for the Naive approach is",(end_time-start)/length,"seconds")
start =time.time()
for target in sorted_list:
    binary_search(sorted_list,target)
end_time = time.time()
print("The search time for the Binary Search approach is",(end_time-start)/length,"seconds")


