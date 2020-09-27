count_patients = int(input())
temp_sum = 0
count_special = 0

for _ in range(count_patients):
    age, height, weight, temperature = input().split()
    age, height, weight = int(age), int(height), int(weight)
    temperature = float(temperature)

    if age >= 60 or abs(height - weight - 100) > 10:
        temp_sum += temperature
        count_special += 1

print(0 if not count_special else round(temp_sum/count_special, 5))
