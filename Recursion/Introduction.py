# #    Some recursion practice here....   ########
# import time
#
#
# #   -----------------------------------
# #   ------ Array using recursion ______
# #   -----------------------------------
#
# def fibonacci(n):
#     if n < 2:
#         return n
#     return fibonacci(n - 1) + fibonacci(n - 2)
#
#
# print(fibonacci(3))
#
#
# def linearSearch(arr: list, k: int) -> bool:
#     if not arr:
#         return False
#     if arr[0] == k:
#         return True
#     return linearSearch(arr[1:], k)
#
#
# print(linearSearch([1, 2, 3, 4, 5], 3))
#
#
# def binarySearch(arr: list, k: int) -> bool:
#     def recursiveBS(l: int, h: int) -> bool:
#         if l > h:
#             return False
#         mid = (l + h) // 2
#         if k == arr[mid]:
#             return True
#         if k < arr[mid]:
#             return recursiveBS(l, mid - 1)
#         return recursiveBS(mid + 1, h)
#
#     return recursiveBS(0, len(arr) - 1)
#
#
# start = time.time()
# print(binarySearch([1, 2, 3, 4, 5], 1))
# end = time.time()
# print(f'Runtime: {end - start}')
#
#
# # *Output:*
# # True
# # Runtime: 0.0
#
#
# def rotatedBinarySearch(arr: list, k: int) -> bool:
#     def recursiveRBS(l: int, h: int) -> bool:
#         if l > h:
#             return False
#         mid = (l + h) // 2
#         if k == arr[mid]:
#             return True
#         if arr[l] <= arr[mid]:
#             if arr[mid] > k >= arr[l]:
#                 return recursiveRBS(l, mid - 1)
#             return recursiveRBS(mid + 1, h)
#         else:
#             if arr[mid] < k <= arr[h]:
#                 return recursiveRBS(l, mid - 1)
#             return recursiveRBS(mid + 1, h)
#
#     return recursiveRBS(0, len(arr) - 1)
#
#
# start = time.time()
# print(rotatedBinarySearch([3, 4, 5, 1, 2], 4))
# end = time.time()
# print(f'Runtime: {end - start}')
#
#
# # *Output:*
# # True
# # Runtime: 0.0
#
#
# #   ---------------------------------------
# #   ------ Patterns using recursion ______
# #   ---------------------------------------
#
#
# def pattern1(i, j=0):
#     if i < 1:
#         return
#     print("*", end=" ")
#     if j >= i - 1:
#         print()
#         pattern1(i - 1, 0)
#     else:
#         pattern1(i, j + 1)
#
#
# # pattern1(5)
# #
# # Output:
# # * * * * *
# # * * * *
# # * * *
# # * *
# # *
#
#
# def pattern2(i, j=0):
#     if i == 0:
#         return
#
#     if j >= i:
#         pattern2(i - 1, 0)
#         print()
#     else:
#         pattern2(i, j + 1)
#         print("*", end=" ")
#
#
# # pattern2(5)
# #
# # Output:
# # * * * * *
# # * * * *
# # * * *
# # * *
# # *
#
#
# def bubbleSort(arr, n, row=0):
#     if n <= 1:
#         return arr
#     if row >= n:
#         return bubbleSort(arr, n - 1, 0)
#     if arr[row] > arr[n]:
#         arr[row], arr[n] = arr[n], arr[row]
#     return bubbleSort(arr, n, row + 1)
#
#
# unsortedArr = [5, 4, 3, 2, 1]
# print(bubbleSort(unsortedArr, 4))
#
#
# def selectionSort(arr, n, row=0):
#     if row >= n:
#         return arr
#     if row < n:
#         maxSmall = arr.index(max(arr[:n - row + 1]))
#         arr[n - row], arr[maxSmall] = arr[maxSmall], arr[n - row]
#         return selectionSort(arr, n, row + 1)
#
#
# unsortedArr1 = [7, 9, 10, 2, 3, 1]
# print(selectionSort(unsortedArr1, 5))
#
#
# def insertionSort(arr, n):
#     for i in range(1, n):
#         for j in range(i + 1, 0, -1):
#             if arr[j] < arr[j - 1]:
#                 arr[j], arr[j - 1] = arr[j - 1], arr[j]
#     return arr
#
#
# unsortedArr2 = [7, 9, 10, 2, 1]
# print(insertionSort(unsortedArr2, 4))
#
#
# def mergeSort(arr):
#
#     def merge(a, b, res=[]):
#         if not a and not b:
#             return res
#         if not a:
#             res.extend(b)
#             return res
#         if not b:
#             res.extend(a)
#             return res
#         if a[0] < b[0]:
#             res.append(a[0])
#             return merge(a[1:], b, res)
#         else:
#             res.append(b[0])
#             return merge(a, b[1:], res)
#
#     if not arr:
#         return None
#     if len(arr) == 1:
#         return arr
#     mid = len(arr) // 2
#     s1 = mergeSort(arr[:mid])
#     s2 = mergeSort(arr[mid:])
#     return merge(s1, s2)
#
#
# unsortedArr3 = [7, 9, 10, 2, 1]
# print(mergeSort(unsortedArr3))
#
# def mergeSortInPlace(arr, s=0, e=0):
#     def merge(arr, s, m, e):
#         mix = []
#         i, j = s, m
#         while i < m and j < e:
#             if arr[i] < arr[j]:
#                 mix.append(arr[i])
#                 i += 1
#             else:
#                 mix.append(arr[j])
#                 j += 1
#         while i < m:
#             mix.append(arr[i])
#             i += 1
#         while j < e:
#             mix.append(arr[j])
#             j += 1
#         print(mix)
#         for l in range(len(mix)):
#             arr[s + l] = mix[l]
#
#     if e - s == 1:
#         return
#     if len(arr) == 1:
#         return arr
#     mid = s + (e - s) // 2
#     mergeSortInPlace(arr, s, mid)
#     mergeSortInPlace(arr, mid, e)
#     return merge(arr, s, mid, e)
#
#
# unsortedArr3 = [7, 9, 10, 2, 1]
# mergeSortInPlace(unsortedArr3, e=len(unsortedArr3))
# print(unsortedArr3)
#
#
# def quickSort(arr, n):
#     """
#     arr: An unsorted list
#     n: length of list
#     return: sorted list
#
#     LOGIC:
#     1) Pivot : any position in the list which is going to have all smaller than it to left and greater to
#                it's right after 1 pass. Means you are putting at it's correct position
#     2) Pivot Position : worst case : corners, best case: middle element
#
#     """
#
#     def quick(low, high):
#         if low >= high:
#             return
#         s, e = low, high
#         m = s + (e - s) // 2
#         pivot = arr[m]
#         while s < e:
#             while arr[s] < pivot:
#                 s += 1
#             while arr[e] > pivot:
#                 e -= 1
#             if s <= e:
#                 arr[s], arr[e] = arr[e], arr[s]
#                 s += 1
#                 e -= 1
#
#         quick(low, e)
#         quick(s, high)
#
#     # if not arr or len(arr) == 1:
#     #     return arr
#     quick(0, n - 1)
#     return arr
#
#
# unsortedArr4 = [7, 9, 3, 1, 2]
# print(quickSort(unsortedArr4, 5))
#


# MAZE PROBLEMS #

# 1) Let's have 3X3 matrix as maze and we are trying to get count of  all possible ways to reach the last box
# Note : we can only traverse through ->R and ->D direction
# def numberOfWaysToReachDestination(r, c):
#     if r == 3 or c == 3:
#         return 1
#     return numberOfWaysToReachDestination(r + 1, c) + numberOfWaysToReachDestination(r, c + 1)
#
#
# print(numberOfWaysToReachDestination(2, 2))


# # 2) get all possible ways to reach the last box
# Note : we can only traverse through ->R and ->D direction
# def waysToReachDestination(r, c, p=''):
#     if r == 3 and c == 3:
#         print(p)
#         return
#     if r < 3:
#         waysToReachDestination(r + 1, c, p + "D")
#     if c < 3:
#         waysToReachDestination(r, c + 1, p + "R")
#
#
# waysToReachDestination(1, 1)


# # 3) get all possible ways to reach the last box in list
# Note : we can only traverse through ->R and ->D direction
# def waysToReachDestination(r, c, p='', lst=[]):
#     if r == 3 and c == 3:
#         lst += [p]
#         return
#     if r < 3:
#         waysToReachDestination(r + 1, c, p + "D", lst)
#     if c < 3:
#         waysToReachDestination(r, c + 1, p + "R", lst)
#
#     return lst
#
#
# print(waysToReachDestination(1, 1))


# # 4) get all possible ways to reach the last box in list
# # Note : we can traverse in all direction
# def waysToReachDestinationWithDiags(r, c, p='', lst=[]):
#     if r == 3 and c == 3:
#         lst += [p]
#         return
#     if r < 3 and c < 3:
#         waysToReachDestinationWithDiags(r + 1, c + 1, p + "M", lst)
#     if r < 3:
#         waysToReachDestinationWithDiags(r + 1, c, p + "D", lst)
#     if c < 3:
#         waysToReachDestinationWithDiags(r, c + 1, p + "R", lst)
#
#     return lst
#
#
# print(waysToReachDestinationWithDiags(1,1))


# # 5) walk on maze having obstacles
# # Note : we can traverse in r,d direction
#
# def mazeWithObstacle(r, c, maze, p=""):
#     if r == len(maze[0]) - 1 and c == len(maze) - 1:
#         print(p)
#         return
#     if not maze[r][c]:
#         return
#     if r < len(maze[0]) - 1:
#         mazeWithObstacle(r + 1, c, maze, p + "D")
#     if c < len(maze) - 1:
#         mazeWithObstacle(r, c + 1, maze, p + "R")
#
#
#
# board = [
#     [True, True, True],
#     [True, False, True],
#     [True, True, True]
# ]
# mazeWithObstacle(0, 0, board)


# # 6) walk on maze having obstacles
# # Note : we can traverse in all direction
#
# def mazeWithObstacle(r, c, maze, p=""):
#     if r == len(maze[0]) - 1 and c == len(maze) - 1:
#         print(p)
#         return
#     if not maze[r][c]:
#         return
#     if r < len(maze[0]) - 1 and c < len(maze) - 1:
#         mazeWithObstacle(r + 1, c + 1, maze, p + "M")
#     if r < len(maze[0]) - 1:
#         mazeWithObstacle(r + 1, c, maze, p + "D")
#     if c < len(maze) - 1:
#         mazeWithObstacle(r, c + 1, maze, p + "R")
#
#
# board = [
#     [True, True, True],
#     [True, False, True],
#     [True, True, True]
# ]
# mazeWithObstacle(0, 0, board)


# Backtracking : what if I have not taken this path what would my array look like
#                +
#                changes by that recursion calls should also be not available!


# # 7) walk on maze
# # Note : we can traverse in all (L, R , U, D)direction
#
# def travelInMaze(r, c, maze, p=""):
#     if r == len(maze[0]) - 1 and c == len(maze) - 1:
#         print(p)
#         return
#     if not maze[r][c]:
#         return
#     maze[r][c] = False
#     if r < len(maze[0]) - 1 and c < len(maze) - 1:
#         travelInMaze(r + 1, c + 1, maze, p + "M")
#     if r < len(maze[0]) - 1:
#         travelInMaze(r + 1, c, maze, p + "D")
#     if c < len(maze) - 1:
#         travelInMaze(r, c + 1, maze, p + "R")
#     if c > 0:
#         travelInMaze(r, c - 1, maze, p + "L")
#     if r > 0:
#         travelInMaze(r - 1, c, maze, p + "U")
#     maze[r][c] = True
#
#
# board = [
#     [True, True, True],
#     [True, True, True],
#     [True, True, True]
# ]
# travelInMaze(0, 0, board)
#
#
# # 8) walk on maze, print all possible path with number on matrix
# # Note : we can traverse in all (L, R , U, D)direction
#
# def travelInMaze(r, c, maze, p="", step=1):
#     if r == len(maze[0]) - 1 and c == len(maze) - 1:
#         maze[r][c] = step
#         for arr in maze:
#             print(arr)
#         print(p)
#         print()  # linebreak
#         return
#
#     if maze[r][c]:
#         return
#
#     maze[r][c] = step
#     if r < len(maze[0]) - 1 and c < len(maze) - 1:
#         travelInMaze(r + 1, c + 1, maze, p + "M", step+1)
#     if r < len(maze[0]) - 1:
#         travelInMaze(r + 1, c, maze, p + "D", step+1)
#     if c < len(maze) - 1:
#         travelInMaze(r, c + 1, maze, p + "R", step+1)
#     if c > 0:
#         travelInMaze(r, c - 1, maze, p + "L", step+1)
#     if r > 0:
#         travelInMaze(r - 1, c, maze, p + "U", step+1)
#     maze[r][c] = 0
#
#
# board = [
#     [True, True, True],
#     [True, True, True],
#     [True, True, True]
# ]
# path = [[0 for x in range(len(board[0]))] for y in range(len(board))]
# travelInMaze(1, 1, path)


## CHECK IF REDUNDANT BRACKETS ARE PRESENT OR NOT?
# def checkRedundantBrackets(expression) :
#     s = []
#     for ex in expression:
#         if ex in "+-/*":
#             s.append(ex)
#         elif ex == '{':
#             if s and s[-1] == '{':
#                 return True
#             s.append(ex)
#         elif ex == '[':
#             if s and s[-1] == '[':
#                 return True
#             s.append(ex)
#         elif ex == '(':
#             if s and s[-1] == '(':
#                 return True
#             s.append(ex)
#         elif ex == '}':
#             if s and s[-1] != '{':
#                 return True
#             s.pop()
#         elif ex == ']':
#             if s and s[-1] != '[':
#                 return True
#             s.pop()
#         elif ex == ')':
#             if s and s[-1] == '(':
#                 return True
#             while s[-1] in "+-/*":
#                 s.pop()
#     # if not s:
#     #     return True
#     return False
#
#
# # main
# expression = "(x+y*(a-b))".strip()
#
# if checkRedundantBrackets(expression):
#     print("true")
#
# else:
#     print("false")


# # Find the stockspan as number of bars from current(including current) which are lower
# def stockSpan(price, n):
#     ans = [0] * n
#     ans[0] = 1
#     # Calculate span values for rest
#     # of the elements
#     for i in range(1, n):
#         counter = 1
#
#         while ((i - counter) >= 0 and
#                price[i] >= price[i - counter]):
#             counter += ans[i - counter]
#         ans[i] = counter
#     return ans
#
#
# print(stockSpan([60, 70, 80, 100, 90, 75, 80, 120], 8))


