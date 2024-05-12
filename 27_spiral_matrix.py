def spiral_order(matrix):
        top = 0
        btm = len(matrix) - 1
        left = 0
        right = len(matrix[0]) - 1

        ans = []
        direction = 0
        while top <= btm and left <= right:
            if direction == 0:
                for i in range(left, right+1):
                    ans.append(matrix[top][i])
                top += 1
                direction = 1
            elif direction == 1:
                for i in range(top, btm + 1):
                    ans.append(matrix[i][right])
                right -= 1
                direction = 2
            elif direction == 2:
                for i in range(right, left - 1, -1):
                    ans.append(matrix[btm][i])
                btm -= 1
                direction = 3
            elif direction == 3:
                for i in range(btm, top - 1, -1):
                    ans.append(matrix[i][left])
                left += 1
                direction = 0
        
        return ans