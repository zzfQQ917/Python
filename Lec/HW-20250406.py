class Lecture:
    def __init__(self, title, instructor):
        self.title = title
        self.instructor = instructor
        self.students = []

    def enroll(self, student_name):
        if student_name in self.students:
            print(f"{self.title} → 이미 수강 중입니다.")
        else:
            self.students.append(student_name)
            print(f"{self.title} → 수강 신청 완료!")

    def cancel(self, student_name):
        if student_name in self.students:
            self.students.remove(student_name)
            print(f"{self.title} → 수강 취소 완료!")
        else:
            print(f"{self.title} → 수강 기록이 없습니다.")

    def show_students(self):
        print(f"{self.title} 수강자: {self.students}")

lecture1 = Lecture("파이썬 기초", "이순신")
lecture2 = Lecture("알고리즘", "유관순")

lecture1.enroll("홍길동")
lecture2.enroll("김영희")
lecture2.enroll("홍길동")
lecture2.cancel("김영희")

lecture1.show_students()
lecture2.show_students()