import random

count = 0
i = 0

for i in range(1,51):
    time = random.randint(5,51)
    if 5<= time and time <= 15:
        print("[0] {0}번째 손님 (소요시간 : {1}분)".format(i, time))
        count += 1
    else:
        print("[ ] {0}번째 손님 (소요시간 : {1}분)".format(i, time))
        
print("총 탑승 승객 : {0}분".format(count))

