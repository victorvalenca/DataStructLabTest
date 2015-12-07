import Student

class Students:
    """
        This represents a program containing a list of students with a
        very crude and rudimentary hash collision resolution
    """
    def __init__(self, max):
        self.student_list = [None] * max
        self.max_size = max
        self.size = 0

    def add(self, student):
        """
            Manual control over array size. It will still fail to add
            a new entry if the collision resolution fails.
            Returns True if addition successful.
        """
        if self.size >= self.max_size:
            return False
        target = doHash(student.student_number)
        while target < self.max_size:
            if self.student_list[target] != None:
                target += 1
            else:
                self.student_list[target] = student
                self.size += 1
                return True
        return False

    def search(self, number):
        """
            Unused method for now. Probably Needs work.
        """
        target = doHash(number)
        while target < self.max_size:
            if self.student_list[target] == None:
                print("No student found with number: ", number)
                return None
            elif self.student_list[target].student_number != number:
                target += 1
            else:
                print("Found at index [%d] %s\n", target, self.student_list[target])
                return self.student_list[target]
    
    def get(self, number):
        """
            Returns the direct location to the first student with matching student number
            Returns None if no student found
        """
        return self.student_list[doHash(number)]

    def __str__(self):
        out = ""
        for student in self.student_list:
            if student:
               out += str(student) + "\n"
        return out

def doHash(number):
    """
        The ultimate crude hashing algorithm
    """
    return number % 10
