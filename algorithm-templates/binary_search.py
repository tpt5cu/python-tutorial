"""
Binary Search Template
end result is a len(2) value, pick the one you want
"""

def index_equals_value_search(arr):
  low = 0
  high = len(arr)-1
  mid = (low+high) / 2
  
  while low+1<high:
    
    mid = low + (high-low)/2
    if arr[mid]<mid:
      low=mid
    else:
      high = mid
      
  if low == arr[low]:
    return low
  elif high == arr[high]:
    return high
  else:
    return -1