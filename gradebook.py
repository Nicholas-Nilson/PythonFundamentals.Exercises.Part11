import enum, uuid


class AliveStatus(enum.Enum):
    ALIVE = 1
    DECEASED = 0

class ZipCodeTrack(enum.Enum):
    JAVA = 0
    DATA = 1


class Person():
    def __init__(self, fname, lname, date_of_birth, alive: AliveStatus):
        self.first_name = fname
        self.last_name = lname
        self.dob = date_of_birth
        self.alive = alive

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)

    def update_first_name(self, new_fname):
        self.first_name = new_fname

    def update_last_name(self, new_lname):
        self.last_name = new_lname

    def update_dob(self, new_dob):
        self.dob = new_dob

    def update_status(self, new_status: AliveStatus):
        self.alive = new_status


# this uuid implementation may double up on ID#s if someone's name & surname match.
# will have to look in to how the uuid is created.
class Instructor(Person):
    def __init__(self, name, last_name, dob, alive):
        super().__init__(name, last_name, dob, alive)
        self.instructor_id = "Instructor_" + \
                             str(uuid.uuid3(uuid.NAMESPACE_DNS, name+last_name))

    def __str__(self):
        return "Instructor: " + super().__str__()


class Student(Person):
    def __init__(self, name, last_name, dob, alive):
        super().__init__(name, last_name, dob, alive)
        self.student_id = "Student_" + \
                             str(uuid.uuid3(uuid.NAMESPACE_DNS, name+last_name))

    def __str__(self):
        return "Student: " + super().__str__()


class ZipCodeStudent(Student):
    def __init__(self, name, last_name, dob, alive, track: ZipCodeTrack):
        super().__init__(name, last_name, dob, alive)
        self.track = track

    def __str__(self):
        return "Zipcode " + super().__str__()


class MeditationStudent(Student):
    def __init__(self, name, last_name, dob, alive, practice_style):
        super().__init__(name, last_name, dob, alive)
        self.practice = practice_style

    def ___str__(self):
        return "Meditation " + super().__str__()


class Classroom:
    def __init__(self):
        self.students = []
        self.instructors = []

    def add_instructor(self, instructor):
        self.instructors.append(instructor)

    def remove_instructor(self, instructor):
        self.instructors.remove(instructor)

    def add_student(self, student):
        self.students.append(student)

    def remove_student(self, student):
        self.students.remove(student)

    def print_instructors(self):
        for instructor in self.instructors:
            print(str(instructor))

    def print_students(self):
        print(*self.students, sep= ' | ')

