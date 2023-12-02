def main():
    with open('day2/part2/input.txt', 'r') as f:
        powers = []
        lines = [line.strip() for line in f.readlines()]
        for line in lines:
            id = int(line.split()[1][:-1])
            game = ' '.join(line.split()[2:])
            gameValues = {'red' : 0, 'blue' : 0, 'green' : 0} 
            draws = game.split(';')
            for draw in draws:
                for group in draw.split(','):
                    count, color = group.strip().split()
                    gameValues[color] = max(gameValues[color], int(count))

            powers.append(gameValues['red'] * gameValues['blue'] * gameValues['green'])
            
        print(sum(powers))

if __name__ == '__main__':
    main()
