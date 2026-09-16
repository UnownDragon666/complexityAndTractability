array = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def binarySearch(arr: list[int], target: int) -> int:
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid

        elif arr[mid] > target:
            right = mid - 1

        else:
            left = mid + 1

    return -1


if __name__ == "__main__":
    print(binarySearch(array, 3))
    print(binarySearch(array, 5))
    print(binarySearch(array, 9))
    print(binarySearch(array, 10))
