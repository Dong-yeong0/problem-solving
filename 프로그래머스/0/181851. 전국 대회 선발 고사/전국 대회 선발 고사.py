def solution(rank, attendance):
    students = [(rank[i], i) for i in range(len(rank)) if attendance[i]]
    students.sort()
    a, b, c = [student[1] for student in students[:3]]
    return 10_000 * a + 100 * b + c
