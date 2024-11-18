from flask import Flask, jsonify, request
from flask_marshmallow import Marshmallow

app = Flask(__name__)

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
        return target
    return -1


def mergeSort(arr):
    if len(arr)> 1:
        mid = len(arr) // 2
        leftside = arr[:mid]
        rightside = arr[mid:]

        mergeSort(leftside)
        mergeSort(rightside)

        i = j = k = 0

        while i < len(leftside) and j < len(rightside):
            if leftside[i] < rightside[j]:
                arr[k] = leftside[i]
                i += 1
            else:
                arr[k] = rightside[j]
                j += 1
            k += 1

        while i < len(leftside):
            arr[k] = leftside[i]
            i += 1
            k += 1

        while j < len(rightside):
            arr[k] = rightside[j]
            j += 1
            k += 1
    return arr



@app.route('/videos', methods = ['GET'])
def getvids():
    sortedvids = mergeSort(video_titles)
    return jsonify(sortedvids)

@app.route('/videos/<title>', methods = ['GET'])
def searchVids(title):
    searchedVid = searchVideos(video_titles, title)
    return jsonify(searchedVid)


if __name__ == '__main__':
    app.run(debug=True)

