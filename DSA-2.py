'''arr=[1,5,9,13,6,12,7,11,14]

def findNum(num):
    for a in arr:
        if a==num:
            return True
        else:
            return False
ans=0
for i in range(0,len(arr)):
    start = arr[i]
    while(findNum(start)):
        start+=1
    ans=max(ans,start-arr[i])
print (ans)
'''

'''
Set Matrix zero
'''







'''
for x in a:
    if x != k:
        a[i] = x
        i += 1
print (i)
'''

'''
rw = len(mat)
cl = len(mat[0])
old = rw * cl
new = r * c
		
if old != new:
    print (mat)

old = [ i for e in mat for i in e]
new = []

a = 0
for i in range(r):
    temp = []
    for j in range(c):
        temp.append(old[a])
        a += 1
        new.append(temp)
print (new)

'''
'''
mat=[[1,2,3,4],[5,6,7,8],[9,10,11,12]]
m=len(mat)
print(m)
n=len(mat[0])
print(n)
rw=0
cl=0
New=[]
r=2
c=6
if m*n!= r*c:
    print (mat)
    
else:
    for i in range(m):
        for j in range(n):
            New[rw][cl]=mat[i][j]
            cl+=1
            if cl==c:
                rw+=1
                cl=0
            
            
    print(New)
'''

'''
cols = collections.defaultdict(set)
rows = collections.defaultdict(set)
squares = collections.defaultdict(set)
        
for r in range(9):
    for c in range(9):
        if board[r][c] == '.':
            continue
        elif (board[r][c] in rows[r] or 
                board[r][c] in cols[c] or
                board[r][c] in squares[(r//3, c//3)]):
                    return False
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r//3, c//3)].add(board[r][c])
        return True
'''
'''
a=[[1,2,3,4],[5,6,7,8],[9,10,11,12]]
r=2
c=6
rw=0
cl=0
k=[]
new=[[0]*c for _ in range(r)]
print(new)
for i in range(len(a)):
    for j in range (len(a[0])):
        k.append(a[i][j])
print(k)
for i in range(c):
    while rw<r:
        new[rw][cl]=k[i]
        if cl==c:
            rw=rw+1
            cl=0
print(new)
'''

'''
#Valid Sudoku
board =[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

seen=[]
for i in range(9):
    for j in range(9):
        seen.append(board[i][j])    
print(seen)
for i in range(9):
    for j in range(9):
        if board[i][j] != 0:
            if (seen.append("row" + i + board[i][j]) or seen.append("col" + j + board[i][j]) or seen.append("box" + ((i/3)*3+(j/3)) + board[i][j])) not in seen:
                print('false')
            else:
                print('true')
print(seen)
'''

'''
SEARCH 2D MATRIX

from pickle import FALSE, TRUE


matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3
box=[]
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        box.append(matrix[i][j])
                
if target in box:
    print(True)
else:
    print(False)
'''

'''
FIRST UNIQUE CHARACTER IN STRING
from collections import defaultdict

s = "loveleetcode"

d=defaultdict(int)

a=[]
for i in s:
    d[i]+=1
print(d)
for i in s:
    if d[i]==1:
        a.append(i)
        print(a)
        b = a[0]
        index=s.index(b)
        print(index)
        if d[i]!=1:
            print(-1)
index = -1
for i in range(len(s)):
    if d[s[i]] == 1:
        index = i
        break
        
print (index)            

'''
'''
Ransome Note
from collections import defaultdict

ransomNote = "fihjjjjei"

magazine = "hjibagacbhadfaefdjaeaebgi"


r=defaultdict(int)
m=defaultdict(int)
for i in ransomNote:
        r[i]+=1
for j in magazine:
    m[j]+=1
print(r)
print(m)
for key in r:
    if key in magazine:
        if r[key] > m[key]:
            print(False)
            break
        else:
            print(True)

'''
'''
ANAGRAM
from collections import defaultdict



s="rat"
t="car"  
a=defaultdict(int)
b=defaultdict(int)
for i in s:
    a[i]+=1
print(a)
for i in t:
    b[i]+=1
print(b)
for x in a:
    print(a[x])
    for y in b:
        if x == y:
            if a[x]==b[y]:


                print (True)
        else:
            print(False)
            '''
'''

# OOPS
class Node:
    def __init__(self , data) :
        self.data = data
        self.next = None  #Address of next node
class LinkedList :
    def __init__(self):
        self.head = None  #Empty List

    def print_LL(self):
        if self.head is None:
            print("Linked List is Empty")
        else:
            n = self.head
            while n is not None:
                print(n.data,"--->",end=" ")
                n = n.next

    def add_begin(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def add_end(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node    
        else:
            n = self.head
            while n.next is not None:
                
                n = n.next
            n.next = new_node


L = LinkedList()
L.add_begin(10)
L.add_end(100)
L.add_begin(20)
L.print_LL()




'''
'''
# Valid Parantheses

s="()[]{}"
for c in range(len(s)):
    if (s[c] == '(' and s[c+1] == ')') or (s[c] == '{' and s[c+1]=='}' or (s[c]=='[' and s[c+1]==']') ):
        print("Valid")
        c+=1
    else:
        print("invalid")  
'''
'''
s=[1,2,3,4,5]
for i in range(len(s)-1,2,-1):
    print(s[i])
'''
'''
#Valid Anagram

from collections import defaultdict


s = "anagram"
a = defaultdict(int)
for c in s:
    a[c]+=1
print(a)
'''



'''
a=[1,2,0,1,0,2,1,0,0]
l=0
m=0
h=len(a)-1
def swap(a,b):
    temp = b
    b=a
    a = temp

while m <= h:
    if a[m] == 0:
        a[m],a[l] = a[l],a[m]
        m = m+1
        l = l+1
    elif a[m]==1:
        m = m+1
    else:
        a[h],a[m] = a[m],a[h]
        h = h-1

print(a)

'''
'''
ans = 10000000
n = 6 
k=2 
arr=[2,4,3,6,1,3]
def solve(arr, n ,k , index , sum , maxsum):
    global ans

    if k == 1:
        maxsum=max(maxsum,sum)
        sum = 0
        for i in range (index,n):
            sum += arr[i]

        maxsum = max(maxsum,sum)
        ans = min(ans,maxsum)
        return

    sum = 0

    for i in range(index,n):
        sum += arr[i]
        maxsum = max(maxsum,sum)
        
        solve(arr, n ,k-1,i+1,sum,maxsum)
solve(arr,n , k, 0,0,0)
print(ans)
'''

'''
#Bubble_sort
def sort(nums):
    for i in range(len(nums)-1,0,-1):
        for j in range(i):
            if nums[j] > nums[j+1]:
                nums[j],nums[j+1] = nums[j+1],nums[j]




nums=[5,3,8,7,2]
sort(nums)
print(nums)
'''
'''
#Insertion_sort
def insertion_sort(arr):
    for i in range(1,len(arr)):
        j=i
        while (arr[j-1] > arr[j]) and j>0:
            arr[j-1],arr[j]=arr[j],arr[j-1]
            j-=1
arr=[2,6,5,1,3,4]
insertion_sort(arr)
print(arr)'''
'''
#Selection Sort
def sort(nums):
    for i in range(len(nums)-1):
        minpos=i
        for j in range(i,len(nums)):
            if nums[j] < nums[minpos]:
                minpos=j
        nums[i],nums[minpos]= nums[minpos],nums[i]

nums=[5,3,8,6,7,2]
sort(nums)
print(nums)
'''
'''
name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)        # Writing output to STDOUT
def Buzz(T,N):
    while T>=0:
        for i in range(N):
            a = i+1
            if a%3==0:
                return('Fizz')
            elif a%5==0:
                return('Buzz')
            elif a%15==0:
                return('FizzBuzz')
        T-=1
        '''


'''
class Node:
    def __init__(self,value):
        self.left = None
        self.data = value
        self.right = None

class Tree:
    def createNode(self,data):
        return Node(data)

    def insert(self,node,data):
        if node is None:
            return self.createNode(data)
        if data < node.data:
            node.left = self.insert(node.left,data)
        else:
            node.right = self.insert(node.right,data)
        return node

    def traverse_inorder(self,root):
        if root is not None:
            self.traverse_inorder(root.left)
            print(root.data)
            self.traverse_inorder(root.right)

tree=Tree() #tree is an object of class Tree
root=tree.createNode(5) #node created with value 5 with left and right as none
print(root.data) #prints root data i.e 5 in this
tree.insert(root,2) #inserts data to the root node
tree.insert(root,10)
tree.insert(root,17)
tree.insert(root,15)
tree.insert(root,12)
tree.insert(root,20)
tree.insert(root,30)
tree.insert(root,6)
tree.insert(root,8)
print('Inorder--->')
tree.traverse_inorder(root)

'''
'''
s='the sky is blue'

print(s.split())
print()
'''


'''
node = SinglyLinkedListNode(data)
    if head != None:
        node.next = head
    return node
        '''

'''
#Permutation of a string to check pallindrome


s='meayl'
t = defaultdict(int)
for i in s:
    t[i]+=1
print(t)
ss = list(t.values())
print(ss)
count = 0
for i in range(len(ss)):
    if (ss[i]%2)!=0:
        count +=1
print(count)
if count>1:
    print('No')
else:
    print('yes')
'''

'''
nums1 = [1,3]
nums2 = [2]
m=len(nums1)
n=len(nums2)
res=[]
for i in range(m):
    res.append(nums1[i])
for j in range(n):
    res.append(nums2[j])
res.sort()
o=len(res)
print()
'''

'''
nums = [2,7,11,15]
target = 9  
d={}
for i,num in enumerate(nums):
    print (i)
    if target-num in d:
        print (d[target-num], i)
    d[num]=i

'''

'''
nums = [4,1,3,3]
l=[nums[i] - i for i in range(len(nums))]
print(l)
d=defaultdict(int)
count=0
for pos,i in enumerate(l):
    count+= pos-d[i]
    d[i]+=1
    print(d[i])
print(d)
'''


'''
s = "axc"
t = "ahbgdc"

box=[]
for i in range(len(t)):
    box.append(t[i])
for i in s:
    if i not in box:
        print(True)
    else:
        print(False)
'''

'''
items1=[[1,1],[4,5],[3,8]]
items2=[[3,1],[1,5]]
c=defaultdict(int)
for i,j in items1+items2:
    c[i]+=j
print(c)
res=[]
for i in sorted(c):
    print(i)
    res.append([i,c[i]])
print(res)
'''
'''
#Merge sorted array
nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
for i in range(6,m,-1):
    nums1.pop(i-1)
print(nums1)
for i in range(n):
    nums1.append(nums2[i])
print(sorted(nums1))
'''


'''

s="dd"
res=[]
for i in s:
    res.append(i)
print(res)
d=defaultdict(int)
for i in res:
    d[i]+=1
print(d)
count=0
for i in d:
    if d[i]%2!=0:
        count+=1
print(count)
if count == 0:
    print(len(res))
else:

    print(len(res)-count+1)

'''

'''

#Container with most water

arr=[1,8,6,2,5,4,8,3,7]
n=len(arr)
l=0
r=n-1
maxDistance=[]       
while l<=r:
    if arr[l]<arr[r]:
        l+=1
    else:
        r-=1
    maxDistance.append(r-l)
    break
print(l,r)
length=min(arr[l],arr[r])
print(length)
maxDistance=max(maxDistance)
print(maxDistance)

print(maxDistance*length)
'''

'''
#2nd largest
a=[1,2,3,4,5,6,7,8,9,10,11,12]
first=second=-inf
n=len(a)
for i in range(n):
    if a[i]>first:
        second=first
        first=a[i]
    elif (a[i] > second and a[i] != first):
            second = a[i]
    elif first == second:
        print(-1)

print (second)
'''

'''
#swap
a=3
b=9
a=a+b
b=a-b
a=a-b
print('a=',a,'b=',b)
'''

'''
#Litrearry Competition
def CalculateTime(W, wt, val, n):
    if n == 0 or W == 0:
        return 0

    if (wt[n-1] > W):
        return CalculateTime(W, wt, val, n-1)
    else:
        return max(val[n-1] + CalculateTime(W-wt[n-1], wt, val, n-1), CalculateTime(W, wt, val, n-1))



n = 3
W = 7
val = [2,6,9]
wt = [3,5,3]
print(CalculateTime(W, wt, val, n))
'''

'''
#The card game
#import sys
n=5
arr=[-1,2,3,4,-5]
min_sum=inf

curr_sum=0
for i in range(n):
    curr_sum = curr_sum + arr[i]
    if curr_sum < min_sum:
        min_sum=curr_sum
    if curr_sum > 0:
        curr_sum = 0
s = sum(arr)
print('size is',min_sum)
print (min_sum*(-2) + s)


'''
'''
X = 10
Y = 1
n = 1
walls = [10]
jumps = 0
for i in range(0, n):
    reach = X
    jump = Y
    while reach < walls[i]:
        reach += (X-Y)
        jump += 1
    jumps += jump

print(jumps)
'''

'''
a=[1,5,7,1]
k = 6

map=[]
count=0
for i in a:
    diff = k-i
    if diff in map:
        count+=1
    else:
        map.append(i)
print(count)
'''

'''
ransomNote ="aa"
magazine ="aab"
r=defaultdict(int)
m=defaultdict(int)
        
for i in ransomNote:
    r[i]+=1
print(r)
for i in magazine:
    m[i]+=1
print(m)
        
for key in r:
    print(key)
    if key not in m:
        print (False)
    if key in magazine:
        if r[key]>m[key]:
            print (False)
            continue
        else:
            print (True)'''



'''
#1st negetive in a window
a=[12,-1,-7,8,-15,30,16,28]
k=3
i=0
j=0
n=len(a)
temp=[]
while j < n:
    if a[j]<0:
        temp.append(a[j])
    j+=1
print(temp)

'''


'''
#Pascals Triangle
numRows=5
res=[]
for i in range(numRows):
    res.append([])
    for j in range(i+1):
        if j == 0 or j == i:
            res[i].append(1)
        else:
            res[i].append(res[i-1][j-1] + res[i-1][j])
print (res)        
'''

#Set Matrix Zeroes(leetcode-73)
mat= [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
rows=len(mat)
cols=len(mat[0])
rowZero = False

for r in range(rows):
    for c in range(cols):
        if mat[r][c] == 0:
            mat[0][c]=0

            if r>0:
                mat[r][0] = 0
            else:
                rowZero = True
for r in range(1,rows):
    for c in range(1,cols):
        if mat[0][c] == 0 or mat[r][0]==0:
            mat[r][c] = 0
for r in range(rows):
	if rowZero==True:
            mat[r][0]=0
for c in range(cols):
	if mat[0][0]==0:
            mat[0][c]=0
        
        
print(mat)

