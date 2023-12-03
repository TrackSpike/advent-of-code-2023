from typing import List, Set, Tuple


def main():
    with open('day03/input.txt', 'r') as f:
        result = []
        lines = [line.strip() for line in f.readlines()]
        mx, my = len(lines[0]), len(lines)
        x, y = 0, 0
        while y < my:
            while x < mx:
                if lines[y][x] == "*":
                    nums = search_for_adj_nums(lines, x, y)
                    if len(nums) == 2:
                        result.append(nums[0] * nums[1])
                x += 1
            y += 1
            x = 0
        
        print(sum(result))

def build_num(lines, sx, y) -> Tuple[int, Set[Tuple[int, int]]] | None:
    seen = set()
    result = ""
    x, mx = sx, len(lines[0])
    while x < mx and lines[y][x].isdigit():
        result += lines[y][x]
        seen.add((x, y))
        x += 1
    x = sx - 1
    while x >= 0 and lines[y][x].isdigit():
        result = lines[y][x] + result
        seen.add((x, y))
        x -= 1
    
    return (int(result), seen) if result else None

def search_for_adj_nums(lines, x, y) -> List[int]:
    mx, my = len(lines[0]), len(lines)
    offset = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    seen = set()
    result = []
    for pos in offset: 
        new_pos = (x + pos[0], y + pos[1])
        if 0 <= new_pos[0] < mx and 0 <= new_pos[1] < my and new_pos not in seen and lines[new_pos[1]][new_pos[0]].isdigit():
            build_num_result = build_num(lines, new_pos[0], new_pos[1])
            if build_num_result:
                num, new_seen = build_num_result
                seen.update(new_seen)
                result.append(num)
    
    return result


if __name__ == '__main__':
    main()
