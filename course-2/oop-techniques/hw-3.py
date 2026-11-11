class Course:
    def __init__(self, name: str, topic: str, teacher: str, participants: int):
        self.name = name
        self.topic = topic
        self.__teacher = teacher
        self.__participants = participants

    def __str__(self):
        return f"{self.name}\n{self.topic}\n{self.__teacher}, {self.__participants} participants"

    def get_teacher(self):
        return self.__teacher

cs = Course("LCOM2.e", "Program design and development (MAA16)", "JHu", 4)

print(cs)
print(cs.get_teacher())