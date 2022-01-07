import os
if not os.path.isdir("log"):
    os.mkdir("log")

if not os.path.exists("log/count_log.txt"):
    f = open("log/count_log.txt", "w", encoding="utf8")
    f.write("기록이 시작된다.")
    f.close

with open("log/count_log.txt", "w", encoding="utf8") as f:
    import random
    import datetime
    for i in range(1, 11):
        stamp = str(datetime.datetime.now())
        value = random.randint(0, 10000)
        log_line = stamp + "\t" + str(value) + " 값이 생성되었다.\n"
        f.write(log_line)
