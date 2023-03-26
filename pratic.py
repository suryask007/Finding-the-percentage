#Finding the percentage
n = int(input())
student_marks = {}
for _ in range(n):
   name, *line = input().split()
   scores = list(map(float, line))
   student_marks[name] = scores
query_name = input("q:")
som=student_marks[query_name]
count=0
for x in som:
   count+=x
div=count/len(som)
print("%.2f"%div)
