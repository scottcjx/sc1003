"""listSorter.py
Scott's implementation of list sorters in python
"""
import time


class ListSorter:
    baseList= []
    recordTimeTaken = False
    recordNumPasses = False

    def __init__(self, input_lst: list, recordTimeTaken: bool=True):
        # assert input list is not empty
        assert input_lst
        self.baseList = input_lst
        self.recordTimeTaken = recordTimeTaken

    
    def bubbleSort(self, recordNumPasses=True, efficient_sort: bool = True):
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

        else:
            # iterate lst_len -1 times (bubble sort max passes is n-1)
            for i in range(lst_len-1):
                swapped = False
                for j in range(lst_len-1):
                    if target_lst[j] > target_lst[j+1]:
                        # next 3 lines swaps the values of 2
                        # items in the list
                        temp = target_lst[j]
                        target_lst[j] = target_lst[j+1]
                        target_lst[j+1] = temp
                        
                        # flag that swap operation carried out this pass
                        swapped = True
                
                # check if swap op has been carried out this pass
                if not swapped and efficient_sort:
                    # if swap op has NOT been carried out, list is already sorted in this pass.
                    # therefore break out of sorting loop
                    break
            numPasses = i
        
        
        if self.recordTimeTaken:
            funcEndTime = time.time_ns()
            funcRunTime = funcEndTime - funcStartTime
            print("function: bubbleSort run time:", funcRunTime, "ns")
        if recordNumPasses:
            print("bubbleSort:: number of passes: ", numPasses)

        return target_lst

    
    def mergeSort(self):
        # start timer if flag recordTimeTaken is true
        if self.recordTimeTaken:
            funcStartTime = time.time_ns()
        
        # copy the baseList
        target_lst = self.baseList[:]
            
        def _mergeLists(left_lst, right_lst):
            ret_lst = []
            
            while left_lst and right_lst:
                if left_lst[0] < right_lst[0]:
                    ret_lst.append(left_lst[0])
                    left_lst.pop(0)
                else:
                    ret_lst.append(right_lst[0])
                    right_lst.pop(0)
            
            if left_lst:
                ret_lst.extend(left_lst)
            else:
                ret_lst.extend(right_lst)
            
            return ret_lst
        
        def _mergeSort(lst: list):
            lst_len = len(lst)
            
            if lst_len < 2:
                return lst
            
            left_lst = lst[:lst_len//2]
            right_lst = lst[lst_len//2:]
                
            left_lst = _mergeSort(left_lst)
            right_lst = _mergeSort(right_lst)
            
            return _mergeLists(left_lst, right_lst)
        
        if self.recordTimeTaken:
            funcEndTime = time.time_ns()
            funcRunTime = funcEndTime - funcStartTime
            print("function: mergeSort run time:", funcRunTime, "ns")

        return _mergeSort(target_lst)


if __name__ == "__main__":
    aList = [1,4,5,3,9,2,6,7]
    aListSorter = ListSorter(aList)
    aListSorter.bubbleSort()
    aListSorter.mergeSort()
    