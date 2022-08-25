def spiral_order(matrix):
    cur_x, cur_y, min_x, min_y, max_x, max_y = 0, 0, 0, 0, len(matrix[0]) - 1, len(matrix) - 1
    total_elements = (max_x + 1) * (max_y + 1)
    final = [matrix[cur_y][cur_x]]
    while len(final) < total_elements:
        while cur_x < max_x:
            # move right
            cur_x += 1
            final.append(matrix[cur_y][cur_x])
        min_y += 1
        while cur_y < max_y and len(final) < total_elements:
            # move down
            cur_y += 1
            final.append(matrix[cur_y][cur_x])
        max_x -= 1
        while cur_x > min_x and len(final) < total_elements:
            # move left
            cur_x -= 1
            final.append(matrix[cur_y][cur_x])
        max_y -= 1
        while cur_y > min_y and len(final) < total_elements:
            # move up
            cur_y -= 1
            final.append(matrix[cur_y][cur_x])
        min_x += 1
    return final


# spiral_order([[1,2,3],[4,5,6],[7,8,9]])

print(spiral_order([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))