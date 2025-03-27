def quicksort(arr, low=0, high=None):
    """
    Implementation of quicksort algorithm.
    
    Args:
        arr: List to be sorted
        low: Starting index of the array
        high: Ending index of the array
        
    Returns:
        Sorted list
    """
    
    # TODO: Implement QuickSort using the partition helper function
    
    return arr


def partition(arr, low, high):
    """
    Partition the array and return the pivot index.
    
    Args:
        arr: List to be partitioned
        low: Starting index of the segment
        high: Ending index of the segment
        
    Returns:
        The position of the pivot after partitioning
    """
    
    #TODO: Implement the partition method
    
    pass


def swap(arr, i, j):
    """
    Helper function to swap two elements in an array.
    
    Args:
        arr: List containing elements to swap
        i: Index of first element
        j: Index of second element
    """
    arr[i], arr[j] = arr[j], arr[i]


def is_sorted(arr):
    """
    Helper function to check if an array is sorted.
    
    Args:
        arr: List to check
        
    Returns:
        True if the list is sorted, False otherwise
    """
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True