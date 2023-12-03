def main():
    with open('day03/input.txt', 'r') as f:
        result = []
        lines = [line.strip() for line in f.readlines()]
        mx, my = len(lines[0]), len(lines)
        x, y = 0, 0
        while y < my:
            while x < mx:
                is_valid = False
                num = ""
                while x < mx and lines[y][x].isdigit():
                    num += lines[y][x]
                    if not is_valid and search_for_adjacent_symbol(lines, x, y):
                        is_valid = True
                    x += 1
                if num and is_valid:
                    result.append(int(num))
                if not num:
                    x += 1
            y += 1
            x = 0
        
        print(sum(result))


def search_for_adjacent_symbol(lines, x, y):
    mx, my = len(lines[0]), len(lines)
    offset = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    for pos in offset: 
        if 0 <= x + pos[0] < mx and 0 <= y + pos[1] < my:
            val = lines[y + pos[1]][x + pos[0]]
            if not val.isdigit() and val != '.':
                return True
    return False

if __name__ == '__main__':
    main()
