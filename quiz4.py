
height = int(input("당신의 키는?"))
gender = input("당신의 성별은?")

def std_weight(height, gender):
    if gender ==  "남자":
        print("키 {0}cm {1}의 표준 체중은 {2}입니다.".format(height, gender, round((height/100) * (height/100) * 22)),4)
    elif gender == "여자":
        print("키 {0}cm {1}의 표준 체중은 {2}입니다.".format(height, gender, round((height/100) * (height/100) * 21), 4))
    else:
        print("정확히 입력해주세요.")


result = std_weight(height, gender)