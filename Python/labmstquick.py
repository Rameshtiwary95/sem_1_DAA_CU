# def Quick_sort(arr):
#     if len(arr) <= 1:
#         return arr
#     pivot = arr[len(arr) // 2]
#     left = [x for x in arr if x < pivot]
#     middle = [x for x in arr if x == pivot]
#     right = [x for x in arr if x > pivot]
#     return Quick_sort(left) + middle + Quick_sort(right)

# number = [1, 2, 6, 54, 78, 90]
# print("unsorted :", number)
# print("sorted :", Quick_sort(number))

# def merge_sort(arr):
#     if len(arr) <= 1: return arr
#     mid = len(arr)//2
#     left = merge_sort(arr[:mid]); right = merge_sort(arr[mid:])
#     res=[]; i=j=0
#     while i<len(left) and j<len(right):
#         if left[i]<right[j]: res.append(left[i]); i+=1
#         else: res.append(right[j]); j+=1
#     return res+left[i:]+right[j:]

# print(merge_sort([3,6,8,10,1,2,1]))



def linear_search(arr,x):
    for i in range(len(arr)):
        if arr[i]==x: return i
    return -1

print(linear_search([3,6,8,10,1,2,1],10))








def dfs(graph,start,visited=None):
    if visited is None: visited=set()
    visited.add(start); print(start,end=" ")
    for nxt in graph[start]:
        if nxt not in visited: dfs(graph,nxt,visited)

g={0:[1,2],1:[2],2:[0,3],3:[3]}
dfs(g,2)







from collections import deque
def bfs(graph,start):
    q=deque([start]); vis={start}
    while q:
        v=q.popleft(); print(v,end=" ")
        for nxt in graph[v]:
            if nxt not in vis: vis.add(nxt); q.append(nxt)

g={0:[1,2],1:[2],2:[0,3],3:[3]}
bfs(g,2)

