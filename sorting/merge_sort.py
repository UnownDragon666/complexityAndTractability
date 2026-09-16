### Merge Sort

# Best TIME O(nlogn) SPACE O(n)
# Average TIME O(nlogn) SPACE O(n)
# Worst TIME O(nlogn) SPACE O(n)


def merge_sort(arr: list[int]) -> list[int]:

    # Divide array until there's only arrays of size one?\
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    arr1 = arr[:mid]
    arr2 = arr[mid:]

    a = merge_sort(arr1)
    b = merge_sort(arr2)
    merged = merge(a, b)

    return merged


def merge(a: list[int], b: list[int]) -> list[int]:
    arr = []

    i = 0
    j = 0

    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            arr.append(a[i])
            i += 1
        else:
            arr.append(b[j])
            j += 1

    arr.extend(a[i:])
    arr.extend(b[j:])

    return arr


if __name__ == "__main__":
    print(merge_sort([1, 12, 23, 24, 52, 65, 64, 74, 52, 557, 45, 256, 23456, 73]))
