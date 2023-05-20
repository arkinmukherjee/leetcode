class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        while len(sandwiches) > 0:
            if sandwiches[0] not in students:
                return len(students)
            if students[0] == sandwiches[0]:
                students.pop(0)
                sandwiches.pop(0)
            else:
                student = students.pop(0)
                students.append(student)

        return len(students)

    def countStudents2(self, students: List[int], sandwiches: List[int]) -> int:
        zeros, ones = 0, 0

        # count numbers of student preferences
        for student in students:
            if student == 0:
                zeros += 1
            else:
                ones += 1

        for sandwich in sandwiches:
            if sandwich == 0:  # if no one wants sandwich 0
                if zeros == 0:
                    return ones
                zeros -= 1
            else:
                if ones == 0:  # if no one wants sandwich 1
                    return zeros
                ones -= 1

        return 0

