def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def test_bubble_sort():
    array = [
        [64, 34, 25, 12, 22, 11, 90],
        [5, 1, 4, 2, 8],
        [3, 0, 2, 5, -1, 4, 1],
        [],
        [1]
    ]
    
    for i, case in enumerate(array):
        bubble_sort(case)
        print(f"Ordem n° {i+1}: {case}")

if __name__ == "__main__":
    test_bubble_sort()