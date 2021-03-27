# | | | | | |
# | | | | | |
# | | | | | |
# | | | | | |
# | | | | | |

n = int(input('Map size n: '))
m = int(input('Map size m: '))

x = int(input('Player x: '))
y = int(input('Player y: '))

print(f'Generating map {n}x{m}...')
direction = 'initially'

while True:
    
    world_map = ''

    for i in range(m):

        row = ''

        for j in range(n):

            cell = '| '

            if x == j and y == i:
                print(f'Moving character {direction} to {x}:{y}')
                cell = '|X'

            row += cell

        row += '|\n'

        world_map += row

    print(world_map)

    action = input('Action: ')

    if action == 'move':
        
        direction = input('Direction: ')

        if direction == 'up' and y > 0:
            y -= 1
        elif direction == 'down' and y < m - 1:
            y += 1
        elif direction == 'left':
            x -= 1
            x = n - 1 if x < 0 else x
        elif direction == 'right':
            x += 1
            x = 0 if x == n else x
        else:
            print('Wrong direction. Please try again.')

    elif action == 'exit':
        break
    else:
        print('Wrong action. Please try again.')

print('Game Over')
