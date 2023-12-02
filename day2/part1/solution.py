def main():
    with open('day2/part1/input.txt', 'r') as f:
        possibleGames = []
        target = {'red' : 12, 'blue' : 14, 'green' : 13}
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
            
            if gameValues['red'] <= target['red'] and gameValues['blue'] <= target['blue'] and gameValues['green'] <= target['green']:
                possibleGames.append(id)
            
        print(sum(possibleGames))
        

if __name__ == '__main__':
    main()
