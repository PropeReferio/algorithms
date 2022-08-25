def track_ball(ball: int, grid):
    cur_y = 0
    # ball is also cur_x, and the column number if it exits
    while cur_y < len(grid):
        ramp = grid[cur_y][ball]
        if ball + ramp < 0 or ball + ramp == len(grid[0]) or grid[cur_y][ball + ramp] != ramp:
            return -1
        else:
            ball += ramp
            cur_y += 1
    return ball


def find_ball(grid):
    answers = []
    for ball in range(len(grid[0])):
        answers.append(track_ball(ball, grid))
    return answers


print(find_ball([[1,1,1,1,1,1],[-1,-1,-1,-1,-1,-1],[1,1,1,1,1,1],[-1,-1,-1,-1,-1,-1]]))
