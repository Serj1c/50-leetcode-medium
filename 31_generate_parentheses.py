def generate_parentheses(n: int):
    ans = []

    def generate(left, right, cur):
        if left + right == 2*n:
            ans.append(cur)
            return
        if left < n:
            generate(left + 1, right, cur + '(')
        if right < left:
            generate(left, right + 1, cur + ')')

    generate(0, 0, '')

    return ans


print(generate_parentheses(3))
print(generate_parentheses(1))
