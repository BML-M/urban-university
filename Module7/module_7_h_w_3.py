team1_num = 6
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = 82
time_avg = 45.2

# Использование %
str1 = "В команде Мастера кода участников: %d !" % team1_num
str2 = "Итого сегодня в командах участников: %d и %d !" % (team1_num, team2_num)

# Использование format()
str3 = "Команда Волшебники данных решила задач: {} !".format(score_2)
str4 = "Волшебники данных решили задачи за {} с !".format(team1_time)

# Использование f-строк
if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    challenge_result = 'Победа команды Мастера кода!'
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    challenge_result = 'Победа команды Волшебники данных!'
else:
    challenge_result = 'Ничья!'

str5 = f"Команды решили {score_1} и {score_2} задач."
str6 = f"Результат битвы: {challenge_result}"
str7 = f"Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!"

print(str1)
print(str2)
print(str3)
print(str4)
print(str5)
print(str6)
print(str7)