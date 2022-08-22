def two(li, val):
    left = 0
    right = len(li) - 1
    # 如果没满足要求，那么while可以和else配合
    while left <= right:
        mid = (left + right) // 2
        if li[mid] == val:
            return mid
        elif li[mid] > val:
            right = mid - 1
        elif li[mid] < val:
            left = mid + 1
    else:
        return None


a = list(range(1000))


def score(mid):
    print('位置为', mid)


if __name__ == '__main__':
    x = two(a, 566)
    score(x)
