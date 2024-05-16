from collections import defaultdict


def total_fruit(fruits) -> int:
    s = fruits
    k = 2
        
    left = 0
    ans = 0
    cnt = defaultdict(int)

    for right in range(len(s)):
        cnt[s[right]] += 1

        while len(cnt) > k:
            left_char = s[left]
            cnt[left_char] -= 1
            if cnt[left_char] == 0:
                del cnt[left_char]
            left += 1

        ans = max(ans, right - left + 1)
    return ans


print(total_fruit([1, 2, 1]))
print(total_fruit([0, 1, 2, 2]))
print(total_fruit([1, 2, 3, 2, 2]))