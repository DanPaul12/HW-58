video_titles = [
    "The Art of Coding",
    "Exploring the Cosmos",
    "Cooking Masterclass: Italian Cuisine",
    "History Uncovered: Ancient Civilizations",
    "Fitness Fundamentals: Strength Training",
    "Digital Photography Essentials",
    "Financial Planning for Beginners",
    "Nature's Wonders: National Geographic",
    "Artificial Intelligence Revolution",
    "Travel Diaries: Discovering Europe"
]

def searchVideos(arr, target):
    low = 0
    high = len(arr) - 1 
    
    while target:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid +1
        else:
            high = mid - 1
        return 1
    return -1


def mergeSort(arr):
    mid = len(arr) // 2
    leftside = arr[:mid]
    rightside = arr[mid:]

    mergeSort(leftside)
    mergeSort(rightside)

    i = j = k = 0

    while i < len(leftside) and j < len(rightside):
        if leftside[i] < rightside[j]:
            arr[k] = leftside[i]
            i + 1
        else:
            arr[k] = rightside[j]
            j + 1
        k + 1

    while i < len(leftside):
        arr[k] = leftside[i]
        i + 1
        k + 1

    while j < len(rightside):
        arr[k] = rightside[j]
        j + 1
        k + 1

