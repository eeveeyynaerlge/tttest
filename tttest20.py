from random import choice, randint
from time import sleep
choice_more = 'y'
score = 0
avg_score = 0
streak = 0
high_streak = 0
tested = []
while choice_more == 'y': 
    tested.append(int(input("what times table do you want to practice? ")))
    choice_more = input("more times tables(y/n, lowercase)? ")
while True:
    current = choice(tested)
    randomchance = randint(1,20)
    print(current, '*', randomchance, '=? end to end. ')
    ans = input()
    if ans == 'end':
        break
    elif int(ans) == current * randomchance:
        print("correct!")
        score += 1
        streak += 1
        if high_streak < streak:
            high_streak = streak
    else:
        print('Answer was', current * randomchance)
        streak = 0
    sleep(1)
print('score = ', score)
avg_score = score
for i in tested:
    if i == 0:
        continue
    avg_score = avg_score * i
print('adjusted score =', avg_score)
print('best streak = ', high_streak)
