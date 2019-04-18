import datetime

class Student:
    def __init__(self, id, name, birthday, score, credit):
        try:
            id = int(id)
        except ValueError:
            raise ValueError("ID must be a number")

        if len(str(id)) > 3:
            raise ValueError("Student ID must have 3 number")

        try:
            credit = int(credit)
        except ValueError:
            raise ValueError("Credit must be int type")

        try:
            name = str(name)
        except ValueError:
            raise ValueError("Name must be int type")

        try:
            datetime.datetime.strptime(birthday, '%d/%m/%Y')
        except ValueError:
            raise ValueError("Incorrect data format, should be DD/MM/YYYY")

        try:
            score = float(score)
        except ValueError:
            raise ValueError("Credit must be float type")


        if score>10:
            raise ValueError("Credit must less than 10")

        self.id = id
        self.name = name
        self.birthday = birthday
        self.credit = credit
        self.score = score

    def __eq__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.id == other.id

    def __ne__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.id != other.id

    def __lt__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.id < other.id

    def __gt__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.id > other.id

    def __le__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.id <= other.id

    def __ge__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.id >= other.id

    def __str__(self):
        return ("[Student ID: " + str(self.id) + ", Name: " + str(self.name)
                + ", Birthday: " + str(self.birthday) + ", Credit: " + str(self.credit)
				+ ", Score: " + str(self.score) + "]")

