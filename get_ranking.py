import numbers
import sys
import fileinput

# 初期化
logFile = sys.argv[1]
logs = []
text = str

# 解体
if logFile:
    for index, line in enumerate(fileinput.input()):
        if(index != 0):
            log = line.replace('\n', '').split(',')
            logs += [[log[0], log[1], int(log[2])]]

# ソート
logs.sort(key=lambda x: x[2])
logs.reverse()

# 表示
latest = 0
rank = 0
print('rank,player_id,mean_score')
for index, line in enumerate(logs):
    if latest != line[2]:
        rank += 1
    print(str(rank) + ',' + line[1] + ',' + str(line[2]))
    latest = line[2]
