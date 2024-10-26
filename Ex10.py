def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def test_bubble_sort():
    array = [
        ["banana", "apple", "cherry", "date"],
        ["dog", "cat", "elephant", "bear"],
        ["zebra", "monkey", "lion", "giraffe"],
        ["python", "java", "c++", "ruby"],
        ["a", "b", "c", "d"]
    ]
    
    for i, case in enumerate(array):
        bubble_sort(case)
        print(f"Ordem n° {i+1}: {case}")

if __name__ == "__main__":
    test_bubble_sort()