def find_repeated_dna_sequences(s: str):
    seen, res = set(), set()

    for l in range(len(s)-9):
        cur = s[l:l+10]
        if cur in seen:
            res.add(cur)
        else:
            seen.add(cur)
    return list(res)


print(find_repeated_dna_sequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"))