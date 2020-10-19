name = input()
hours_math, score_math, hours_physics, score_physics, hours_cs, score_cs = input().split()

sum_hours = float(hours_math) + float(hours_physics) + float(hours_cs)
sum_scores = int(score_math) + int(score_physics) + int(score_cs)

print(name, round(sum_hours, 1), round(sum_scores/3, 1))
