"""listSearching.py
Scott's implementation of list sorters in python
"""
import time
from enum import Enum


class ListSeaching:
    baseList = []
    recordTimeTaken = False
    recordNumPasses = False
    
    class processMode(Enum):
        RECURSIVE = 1
        ITERATIVE = 2
    
    def __init__(self, input_lst: list, recordTimeTaken: bool=True):
        # assert input list is not empty
        assert input_lst
        self.baseList = input_lst
        self.recordTimeTaken = recordTimeTaken
        
    def binarySearch(self, target=None, useMode: processMode = processMode.RECURSIVE):
        assert target

        # start timer if flag recordTimeTaken is true
        if self.recordTimeTaken:
            funcStartTime = time.time_ns()
        numPasses = -1
        
        # copy the baseList
        target_lst = self.baseList[:]
        lst_len = len(target_lst)
        
        # checks if lst only have 1 element
        if lst_len == 1:
            # if list has only 1 element, list is already sorted
            pass
        elif useMode == self.processMode.ITERATIVE:
            return BinarySearch.iterative(target_lst, target)
        elif useMode == self.processMode.RECURSIVE:
            return BinarySearch.recursive(target_lst, target)
        
        if self.recordTimeTaken:
            funcEndTime = time.time_ns()
            funcRunTime = funcEndTime - funcStartTime
            print("function: binarySearch run time:", funcRunTime, "ns")
        return numPasses
    
    
    def linearSearch(self, target=None):
        
        assert target
        
        # start timer if flag recordTimeTaken is true
        if self.recordTimeTaken:
            funcStartTime = time.time_ns()
        numPasses = 0
        
        # copy the baseList
        target_lst = self.baseList[:]
        lst_len = len(target_lst)
        
        # checks if lst only have 1 element
        if lst_len == 1:
            # if list has only 1 element, list is already sorted
            pass
        
        # for else loop (if elem found in lst, return index, else -return 1)
        for elem in target_lst:
            if elem == target:    
                break
            numPasses += 1
        else:
            numPasses = -1
            
        if self.recordTimeTaken:
            funcEndTime = time.time_ns()
            funcRunTime = funcEndTime - funcStartTime
            print("function: linearSearch run time:", funcRunTime, "ns")
        
        return numPasses


class BinarySearch:
    def __init__(self, inpLst: list):
        pass
    
    @staticmethod
    def recursive(input_list: list, target=None) -> int:
        assert type(input_list) == list and input_list != []
        assert target
        
        def bSearch(items, target, low=0, high=None):
            if high == None:
                high = len(items) -1
            
            if low > high:
                return False, -1
            
            mid = (low + high) // 2
            
            if (target == items[mid]):
                return True, mid
            elif target > items[mid]:
                return bSearch(items, target, low = (mid + 1), high=high)
            else:
                return bSearch(items, target, low=low, high=(mid-1))
    
        _, idxFound = bSearch(input_list, target)
        return idxFound
    
    @staticmethod
    def iterative(input_list: list, target=None) -> int:
        assert type(input_list) == "list" and input_list != []
        assert target
        
        ret = -1
        low = 0
        high = len(input_list) -1 
        
        """ loop dividing lst by 2 until either target is found, OR 
        low == high and item not found; this is because:
        if low == high, there is only 1 item left to search AND 
        if target not == low or high, target is NOT in the input list"""
        while low <= high:
            # first define the middle of list (floor div)
            mid = (low + high) // 2
            
            # if target == (current mid of subdivided list), return index of current_mid
            if input_list[mid] == target:
                return mid
            
            elif target < input_list[mid]:
                high = mid - 1 
            else:
                low = mid + 1
        
        return ret
