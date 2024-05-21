import random
import timeit

def generate_random_list(c):
    l = []
    for i in range(c):
        l.append(random.randint(0, c))
    return l

def test_sorted(ldata):
    return sorted(ldata)

def test_merge_sort(ldata):

    def merge_sort(arr):
        if len(arr) <= 1:
            return arr
        mid = len(arr) // 2
        left_arr = arr[:mid]
        right_arr = arr[mid:]

        return merge(merge_sort(left_arr), merge_sort(right_arr))

    def merge(left_arr, right_arr):
        merged = []
        left_idx = 0
        right_idx = 0

        while left_idx < len(left_arr) and right_idx < len(right_arr):
            if left_arr[left_idx] <= right_arr[right_idx]:
                merged.append(left_arr[left_idx])
                left_idx += 1
            else:
                merged.append(right_arr[right_idx])
                right_idx += 1

        while left_idx < len(left_arr):
            merged.append(left_arr[left_idx])
            left_idx += 1
        
        while right_idx < len(right_arr):
            merged.append(right_arr[right_idx])
            right_idx += 1

        return merged

    return merge_sort(ldata)

def test_insertion_sort(ldata):
    for i in range(1, len(ldata)):
        k = ldata[i]
        j = i - 1
        while j >= 0 and k < ldata[j]:
            ldata[j + 1] = ldata[j]
            j -= 1
        ldata[j + 1] = k
    return ldata

if __name__ == "__main__":
    cnumber = 100
    ldata = generate_random_list(cnumber)
    #print(sorted(ldata))
    print(f"--- {cnumber} ---")
    ndata = 100
    print("sorted 100: ", timeit.timeit("test_sorted(generate_random_list(cnumber))", globals=globals(), number=ndata))
    print("merge sort 100: ", timeit.timeit("test_merge_sort(generate_random_list(cnumber))", globals=globals(), number=ndata))
    print("insertion sort 100: ", timeit.timeit("test_insertion_sort(generate_random_list(cnumber))", globals=globals(), number=ndata))
    ndata = 1000
    print("sorted 1k: ", timeit.timeit("test_sorted(generate_random_list(cnumber))", globals=globals(), number=ndata))
    print("merge sort 1k: ", timeit.timeit("test_merge_sort(generate_random_list(cnumber))", globals=globals(), number=ndata))
    print("insertion sort 1k: ", timeit.timeit("test_insertion_sort(generate_random_list(cnumber))", globals=globals(), number=ndata))
    ndata = 10000
    print("sorted 10k: ", timeit.timeit("test_sorted(generate_random_list(cnumber))", globals=globals(), number=ndata))
    print("merge sort 10k: ", timeit.timeit("test_merge_sort(generate_random_list(cnumber))", globals=globals(), number=ndata))
    print("insertion sort 10k: ", timeit.timeit("test_insertion_sort(generate_random_list(cnumber))", globals=globals(), number=ndata))

    cnumber = 1000
    ldata = generate_random_list(cnumber)
    #print(sorted(ldata))
    print(f"--- {cnumber} ---")
    ndata = 100
    print("sorted 100: ", timeit.timeit("test_sorted(generate_random_list(cnumber))", globals=globals(), number=ndata))
    print("merge sort 100: ", timeit.timeit("test_merge_sort(generate_random_list(cnumber))", globals=globals(), number=ndata))
    print("insertion sort 100: ", timeit.timeit("test_insertion_sort(generate_random_list(cnumber))", globals=globals(), number=ndata))
    ndata = 1000
    print("sorted 1k: ", timeit.timeit("test_sorted(generate_random_list(cnumber))", globals=globals(), number=ndata))
    print("merge sort 1k: ", timeit.timeit("test_merge_sort(generate_random_list(cnumber))", globals=globals(), number=ndata))
    print("insertion sort 1k: ", timeit.timeit("test_insertion_sort(generate_random_list(cnumber))", globals=globals(), number=ndata))
    ndata = 10000
    print("sorted 10k: ", timeit.timeit("test_sorted(generate_random_list(cnumber))", globals=globals(), number=ndata))
    print("merge sort 10k: ", timeit.timeit("test_merge_sort(generate_random_list(cnumber))", globals=globals(), number=ndata))
    print("insertion sort 10k: ", timeit.timeit("test_insertion_sort(generate_random_list(cnumber))", globals=globals(), number=ndata))

    cnumber = 10000
    ldata = generate_random_list(cnumber)
    #print(sorted(ldata))
    print(f"--- {cnumber} ---")
    ndata = 100
    print("sorted 100: ", timeit.timeit("test_sorted(generate_random_list(cnumber))", globals=globals(), number=ndata))
    print("merge sort 100: ", timeit.timeit("test_merge_sort(generate_random_list(cnumber))", globals=globals(), number=ndata))
    print("insertion sort 100: ", timeit.timeit("test_insertion_sort(generate_random_list(cnumber))", globals=globals(), number=ndata))
    ndata = 1000
    print("sorted 1k: ", timeit.timeit("test_sorted(generate_random_list(cnumber))", globals=globals(), number=ndata))
    print("merge sort 1k: ", timeit.timeit("test_merge_sort(generate_random_list(cnumber))", globals=globals(), number=ndata))
    print("insertion sort 1k: ", timeit.timeit("test_insertion_sort(generate_random_list(cnumber))", globals=globals(), number=ndata))
    ndata = 10000
    print("sorted 10k: ", timeit.timeit("test_sorted(generate_random_list(cnumber))", globals=globals(), number=ndata))
    print("merge sort 10k: ", timeit.timeit("test_merge_sort(generate_random_list(cnumber))", globals=globals(), number=ndata))
    print("insertion sort 10k: ", timeit.timeit("test_insertion_sort(generate_random_list(cnumber))", globals=globals(), number=ndata))

