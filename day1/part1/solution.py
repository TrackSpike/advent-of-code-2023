def main():
    with open('day1/part1/input.txt', 'r') as f:
        lines = [line for line in f.readlines()]
        nums = []
        for line in lines:
            i = 0
            while not line[i].isdigit():
                i += 1
            nums.append(line[i])
            i = len(line) - 1
            while not line[i].isdigit():
                i -= 1
            nums[-1] = int(nums[-1] + line[i])
        print(sum(nums))


if __name__ == '__main__':
    main()