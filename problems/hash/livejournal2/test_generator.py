# Текущий тест на асимптотику имеет большой размер, и может не пропускаться системой
# Сейчас он случайным образом распределяет пользователей между following и followers
# 
# Можно попробовать сгенерировать небольшой список folliwing, а список followers
# составить из случайных людей и в конец добавить following.
# Так возможен выигрыш по размеру файла теста, зато асимптотика в медленном решении
# операции x in list станет худшим случаем. Возможный хак студента list.find() и list.rfind()
# для этого можно добавить второй тест, но following поставить не в конец followers, а в начало.
# Оба теста мб будут меньшего размера и пропустятся системой

from lib.testgen import TestSet
from lib.random import seed, randint, shuffle

seed(142)


def random_name():
    return ''.join(map(chr, [randint(ord('A'), ord('Z')) for _ in range(3)]))

def random_test(size:int, tests:TestSet):
    assert size > 0, 'Size must be natural number'

    followers = []
    following = []
    counters = {'friends': 0, 'fans': 0, 'heroes': 0}

    for i in range(size):
        username = random_name() + str(i)  # str(i) - соль для уникальности
        destiny = randint(0, 2)
        if destiny == 0:
            followers.append(username)
            following.append(username)
            counters['friends'] += 1
        elif destiny == 1:
            followers.append(username)
            counters['fans'] += 1
        elif destiny == 2:
            following.append(username)
            counters['heroes'] += 1
        else:
            raise ValueError('Wrong destiny {}'.format(destiny))
    
    shuffle(following)
    shuffle(followers)

    tests.add('{}\n{}\n{}\n{}\n'.format(
            len(following), '\n'.join(following), len(followers), '\n'.join(followers)
        ),
        '{} {} {}\n'.format(counters['friends'], counters['fans'], counters['heroes'])
    )


tests = TestSet()
tests.add("""3
vasya-pupkin
bill-hates
ivan-ivanov
2
vasya-pupkin
destroyer
""", '1 1 2\n')

tests.add("""3
vasya-pupkin
bill-hates
ivan-ivanov
1
destroyer
""", '0 1 3\n')

tests.add("""1
@elonmusk
1
@roscosmosofficial
""", '0 1 1\n')

random_test(6000, tests)
