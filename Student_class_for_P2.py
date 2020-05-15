#student class
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

