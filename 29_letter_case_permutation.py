def letter_case_permutation(s: str):
    res = []
    def traverse(res, cur, s, i):
        if len(cur) == len(s):
            res.append(cur)
            return res
            
        traverse(res, cur+s[i], s, i + 1)
        if s[i].isalpha():
            traverse(res, cur+s[i].swapcase(), s, i+1)
        return res

    traverse(res, '', s, 0)

    return res


print(letter_case_permutation('a1b2'))
print(letter_case_permutation('3z4'))