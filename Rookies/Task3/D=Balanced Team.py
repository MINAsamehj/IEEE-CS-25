number_of_students = int(input())
students = list(map(int, input().split()))

students.sort()

i =0
team_number=0

for j in range(number_of_students):
    if students[j] - students[i] >5:
        i+=1

    team_number= max(team_number , (j-i+1))


print(team_number)