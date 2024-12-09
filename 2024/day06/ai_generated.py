def read_map(filename):
    with open(filename, 'r') as file:
        return [list(line.strip()) for line in file.readlines()]

def move_guard(map_grid, start_pos, direction):
    directions = ['^', '>', 'v', '<']
    dir_moves = { '^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1) }
    visited = set()
    x, y = start_pos

    while True:
        visited.add((x, y))
        dx, dy = dir_moves[direction]
        next_x, next_y = x + dx, y + dy

        if 0 <= next_x < len(map_grid) and 0 <= next_y < len(map_grid[0]) and map_grid[next_x][next_y] != '#':
            x, y = next_x, next_y
        else:
            direction = directions[(directions.index(direction) + 1) % 4]

            dx, dy = dir_moves[direction]
            next_x, next_y = x + dx, y + dy

            if 0 <= next_x < len(map_grid) and 0 <= next_y < len(map_grid[0]) and map_grid[next_x][next_y] != '#':
                x, y = next_x, next_y
            else:
                break

    return visited

def can_get_stuck(map_grid, pos):
    directions = ['^', '>', 'v', '<']
    dir_moves = { '^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1) }
    
    for direction in directions:
        dx, dy = dir_moves[direction]
        next_x, next_y = pos[0] + dx, pos[1] + dy
        
        if 0 <= next_x < len(map_grid) and 0 <= next_y < len(map_grid[0]) and map_grid[next_x][next_y] != '#':
            return False
    return True

def find_obstruction_positions(map_grid, guard_start):
    obstruction_positions = []
    for i in range(len(map_grid)):
        for j in range(len(map_grid[0])):
            if (i, j) != guard_start and map_grid[i][j] == '.':
                map_grid[i][j] = '#'  # Place a temporary obstruction
                if can_get_stuck(map_grid, guard_start):
                    obstruction_positions.append((i, j))
                map_grid[i][j] = '.'  # Remove the temporary obstruction
    return obstruction_positions

def main():
    map_grid = read_map('input.txt')
    guard_start = next((i, row.index('^')) for i, row in enumerate(map_grid) if '^' in row)
    obstruction_positions = find_obstruction_positions(map_grid, guard_start)
    
    print("Number of positions for new obstruction:", len(obstruction_positions))

if __name__ == "__main__":
    main()
