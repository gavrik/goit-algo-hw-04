def multi_sort(lst):
    result = []
    
    longest = 0
    for i in lst:
        if longest < len(i):
            longest = len(i)

    print("The longest array: ", longest)

    while longest > 0:
        m = []
        for i in lst:
            if len(i) > 0:
                m.append(i.pop())
        print(m)
        result.extend(sorted(m, reverse = True))
        longest -= 1
    result.reverse()
    return result


if __name__ == "__main__":
    lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
    print(multi_sort(lists))
