characterStrength = 2
characterValues = [characterStrength, 0, 0, 0]
spiderValues = [2, 0, 0, 1]


def spider_encounter(character):
    if character[0] > spiderValues[0]:
        return True
    else:
        return False


weight_lift = input('Would you like to lift some weight? ')
if weight_lift == 'YES':
    characterValues[0] = characterValues[0] + 1
    print('After toiling at the gym for years, you have painstakingly increased your strength stat by one.')

spider_fight = input('Would you like to fight the spider? ')
if spider_fight == 'YES':
    fight_outcome = spider_encounter(characterValues)
    if fight_outcome is True:
        print('Congratulations! You won!')
    else:
        print('You died, game over')

else:
    print('You got away safely')
