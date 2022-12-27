n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
#print(scores)-->01781457383x 
query_name = input()
print(query_name)
sum = sum(student_marks[query_name])
l = len(student_marks[query_name])
sum = (sum/l)
print(sum,'2f')