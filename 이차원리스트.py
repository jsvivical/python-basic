kor_score = [49, 70, 29, 50, 10]
eng_score = [10, 20, 50, 52, 60]
math_score = [60, 29, 67, 12, 55]

total_score = [kor_score, eng_score, math_score]

print(total_score)
print(total_score[1][0])
print(id(total_score[0]))
print(id(total_score[1]))
print(id(kor_score[3]))
print(id(eng_score[2]))
