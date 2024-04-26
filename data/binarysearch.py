from typing import List


class BinarySearch:
  def __init__(self,data: List[int]):
    self.data = data
  
  def search(self, target: int) -> int: 
    left = 0
    right = len(self.data) - 1
    while left <= right:
      mid = left + (right - left) // 2
      if self.data[mid] == target:
        return mid
      elif self.data[mid] < target:
        left = mid + 1
      else:
        right = mid - 1
    return -1
  
  
  def search_first(self, target: int) -> int:
    left = 0
    right = len(self.data) - 1
    while left <= right:
      mid = left + (right - left) // 2
      if self.data[mid] == target:
        if mid == 0 or self.data[mid - 1] != target:
          return mid
        right = mid - 1
      elif self.data[mid] < target:
        left = mid + 1
      else:
        right = mid - 1
    return -1
  
  def search_last(self, target: int) -> int:
    left = 0
    right = len(self.data) - 1
    while left <= right:
      mid = left + (right - left) // 2
      if self.data[mid] == target:
        if mid == len(self.data) - 1 or self.data[mid + 1] != target:
          return mid
        left = mid + 1
      elif self.data[mid] < target:
        left = mid + 1
      else:
        right = mid - 1
    return -1
  

list1=[1,2,3,4,5,6,7]

search=BinarySearch(list1)


x=search.search(5)
print(x)
