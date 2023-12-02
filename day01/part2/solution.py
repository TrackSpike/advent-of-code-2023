def main():
    numWords = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    numToValue = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}
    with open('day1/part1/input.txt', 'r') as f:
        lines = [line.strip() for line in f.readlines()]
        nums = []
        for line in lines:
            i = 0
            flag = False
            while not flag:
                if line[i].isdigit():
                    nums.append(line[i])
                    flag = True
                else:
                    j = 0
                    while line[i:i+j] in [word[:j] for word in numWords]:
                        if line[i:i+j] in numWords:
                            nums.append(numToValue[line[i:i+j]])
                            flag = True
                            break
                        else:
                            j += 1
                i += 1

            i = len(line) - 1
            flag = False
            while not flag:
                if line[i].isdigit():
                    nums[-1] = int(nums[-1] + line[i])
                    flag = True
                else:
                    j = 0
                    while line[i-j:i+1] in [word[-(j+1):] for word in numWords]:
                        if line[i-j:i+1] in numWords:
                            nums[-1] = int(nums[-1] + numToValue[line[i-j:i+1]])
                            flag = True
                            break
                        else:
                            j += 1
                i -= 1

        print(sum(nums))

def top_letters(words, i):
    return [word[:i] for word in words]


if __name__ == '__main__':
    main()