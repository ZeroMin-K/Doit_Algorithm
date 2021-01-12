print('calculate sum and average of student\'s score')

score1 = int(input('no1 student score: '))
score2 = int(input('no2 student score: '))
score3 = int(input('no3 student score: '))
score4 = int(input('no4 student score: '))
score5 = int(input('no5 student score: '))

total = 0
total += score1
total += score2
total += score3
total += score4
total += score5

print(f'sum of score: {total}')
print(f'average of score: {total /5}')
