from binarysearch import BinarySearch
from typing import List
class ReBinarysearch:
  def __init__(self,data:List[int]) -> int:
    self.data=data
    
  def search(self,target:int,*args,**c)->int:
    left=0
    right=len(self.data)-1
    
    if left==right:
      if self.data[left]==target:
        return left
      else:
        return -1
    else:
      mid=left+(right-left)//2
      
      if self.data[mid]==target:
        return mid
      if self.data[mid]>target:
        return ReBinarysearch(mid)
      
      