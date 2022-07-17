import enum, uuid


class AliveStatus(enum.Enum):
    ALIVE = 1
    DECEASED = 0


class Person():
    def __init__(self, fname, lname, date_of_birth, alive: AliveStatus):
        self.first_name = fname
        self.last_name = lname
        self.dob = date_of_birth
        self.alive = alive

    def update_first_name(self, new_fname):
        self.first_name = new_fname

    def update_last_name(self, new_lname):
        self.last_name = new_lname

    def update_dob(self, new_dob):
        self.dob = new_dob

    def update_status(self, new_status: AliveStatus):
        self.alive = new_status


class Instructor(Person):
    def __init__(self, name, last_name, dob, alive):
        super().__init__(name, last_name, dob, alive)
        self.instructor_id = uuid.UUID


