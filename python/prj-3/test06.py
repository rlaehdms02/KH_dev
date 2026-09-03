score_list = []
i = int(0)
score_list.append(int(input("학생 성적 : ")))
score_list.append(int(input("학생 성적 : ")))
score_list.append(int(input("학생 성적 : ")))
for i in range(1,len(score_list)):
    score_list[i] = score_list[i] + 5


print(score_list)

score_list[0] = score_list[0] + 5
score_list[1] = score_list[1] + 5
score_list[2] = score_list[2] + 5

print(score_list)


# 첫번째요소 , 마지막요소 출력
fruits = ["사과", "바나나", "포도", "귤", "감"]

number_list = [10, 20, 30]
number_list.append(40)

# 리스트 [10, 20, 30]에 다음을 순서대로 적용
# 1. 맨 끝에 40 추가
# 2. 맨 앞에 5 삽입
# 3. 20 삭제
# 최종 결과 출력 (기대값: [5, 10, 30, 40])