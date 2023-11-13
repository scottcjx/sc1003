"""main.py
Scott's implementation of list searching and sorting
"""

from listSearching import ListSeaching
from listSorter import ListSorter

def main():
    aList = [1,3,12,54,99,43,33,21,55]
    
    lstSort = ListSorter(aList)
    lstSort.bubbleSort()
    aListSorted = lstSort.mergeSort()
    
    lstSearchUnsorted = ListSeaching(aList)
    lstSearchSorted = ListSeaching(aListSorted)
    
    lstSearchSortedRet = lstSearchSorted.binarySearch(55)
    print("lstSearchSortedRet: ", lstSearchSortedRet)
    lstSearchUnsortedRet = lstSearchUnsorted.linearSearch(55)
    print("lstSearchUnsortedRet: ", lstSearchUnsortedRet)

if __name__ == "__main__":
    main()