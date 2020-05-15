from student import Student
from random import shuffle
TITLE = "Student Roster"
def main():
    print(TITLE) 
    roster = []
    roster.append(Student("Alex", 10))
    roster.append(Student("Carson", 10))
    roster.append(Student("Chase", 10))
    roster.append(Student("Silas", 10))
    roster.append(Student("Ramiro", 10))
    roster.append(Student("Don", 10))
    roster.append(Student("Carmen", 10))
    roster.append(Student("Ann", 10))
    roster.append(Student("Ryuji", 10))
    roster.append(Student("William", 10))
    roster.append(Student("Haru", 10))
    roster.append(Student("Lucy", 10))
    roster.append(Student("Yusuke", 10))
    roster.append(Student("Gorokichi", 10))
    roster.append(Student("Akechi", 10))
    roster.append(Student("Loki", 10))
    roster.append(Student("Makoto", 10))
    roster.append(Student("Johanna", 10))
    roster.append(Student("Arsene", 10))
    answer = "No"
    if roster[4] < roster[14]:
        answer = "Yes."
    else: 
        answer = "No"
    print("Does %s's name start before %s? %s" %(roster[4].getname(), roster[14].getname(), answer))

    if roster[1] > roster[10]:
        answer = "Yes."
    else: 
        answer = "No"
    print("Does %s's name start after %s? %s" %(roster[1].getname(), roster[10].getname(), answer))

    if roster[7] <= roster[12]:
        answer = "Yes."
    else: 
        answer = "No"
    print("Does %s's name start before or is the same as %s? %s" %(roster[7].getname(), roster[12].getname(), answer))

    if roster[5] >= roster[16]:
        answer = "Yes."
    else: 
        answer = "No"
    print("Does %s's name start after or is the same as %s? %s" %(roster[5].getname(), roster[16].getname(), answer))

    if roster[2] == roster[8]:
        answer = "Yes."
    else: 
        answer = "No"
    print("Is %s's name the same as %s? %s\n" %(roster[2].getname(), roster[8].getname(), answer))
    shuffle(roster)
    print("Unsorted list of students:")
    for s in roster:
        print(s)
    roster.sort()
    print("\nSorted list of students:")
    for s in roster:
        print(s) 
main()

class Student(object):
    def __init__(self, name, number):
        self.name = name
        self.scores = []
        for count in range(number):
            self.scores.append(0)
    def set_score(self, tNumber, score):
        self.scores[tNumber - 1] = score
    def getname(self):
        return self.name
      def get_score(self, tNumber):
        return self.scores[tNumber - 1]
    def get_average(self):
        return sum(self.scores) / len(self.scores)
    def getHighScore(self):
        return max(self.scores)
    def __str__(self):
        return "Name: %s\nScores: %s" %(self.name, self.scores)
    def __lt__(self, other):
        return self.name < other.name
    def __gt__(self, other):
        return not (self.name == other.name or self.name < other.name)
    def __le__(self, other):
        return self.name == other.name or self.name < other.name
    def __ge__(self, other):
        return self.name == other.name or self.name > other.name
    def __eq__(self, other):
        if self.name is other.name: 
            return True
        elif type(self.name) != type(other.name):
            return False
        else:
            return self.name == other.name
