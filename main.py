class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) \
        and course in lecturer.courses_attached \
        and course in self.courses_in_progress and grade <= 10:
            lecturer.grades += [grade]
        else:
            return 'Error'

    def get_avg_grade(self):
        if self.grades:
            sum_hw = 0
            count = 0
            for grades in self.grades.values():
                sum_hw += sum(grades)
                count += len(grades)
            return round(sum_hw / count, 2)
        else:
            return 'Error'

    def __str__(self):
        res = f'Имя: {self.name}\n'\
              f'Фамилия: {self.surname}\n'\
              f'Средняя оценка за ДЗ: {self.get_avg_grade()}\n'
        return res

    def __lt__(self, other_student):
        if not isinstance(other_student, Student):
            print('Error')
            return
        else:
            if self.get_avg_grade() and other_student.get_avg_grade() == int:
                compare = self.get_avg_grade() < other_student.get_avg_grade()
                if compare:
                    print(f'{self.name} {self.surname} учится хуже, чем {other_student.name} {other_student.surname}')
                else:
                    print(f'{other_student.name} {other_student.surname} учится хуже, чем {self.name} {self.surname}')
            else:
                return 'Error'
            return compare


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Reviewer(Mentor):

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress \
                and grade <= 10:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name}\n'\
              f'Фамилия: {self.surname}\n'
        return res


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = []

    def __str__(self):
        res = f'Имя: {self.name}\n' \
              f'Фамилия: {self.surname}\n' \
              f'Средняя оценка за лекцию: {sum(self.grades) / len(self.grades) :.2f}\n'
        return res

    def __lt__(self, other_lecturer):
        if not isinstance(other_lecturer, Lecturer):
            print('Такого лектора нет')
            return
        else:
            compare = sum(self.grades) / len(self.grades) < sum(other_lecturer.grades) / len(other_lecturer.grades)
            if compare:
                print(f'{self.name} {self.surname} преподаёт хуже, чем {other_lecturer.name} {other_lecturer.surname}')
            else:
                print(f'{other_lecturer.name} {other_lecturer.surname} преподаёт хуже, чем {self.name} {self.surname}')
        return compare


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']

cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']

cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)


def get_avg_hw_grade(student_list, course):
    total_sum = 0

    for student in student_list:
        for c, grades in student.grades.items():
            if c == course:
                total_sum += sum(grades) / len(grades)
    return round(total_sum / len(student_list), 2)


def get_avg_lect_grade(list_lect):
    total_sum = 0
    for lecturer in list_lect:
        total_sum += sum(lecturer.grades) / len(lecturer.grades)
    return total_sum / len(list_lect)