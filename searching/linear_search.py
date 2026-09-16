def search(arr: list[int], target: int) -> int:

    for i in range(len(arr)):
        if arr[i] == target:
            return i

    return -1


array = [1, 2, 3, 4, 5, 6, 7, 8, 9]

if __name__ == "__main__":
    print(search(array, 3))
    print(search(array, 5))
    print(search(array, 9))
    print(search(array, 10))
