from abc import ABC, abstractmethod

class SubjectError(Exception):
    pass

class Human(ABC):
    @abstractmethod
    def __init__(self, name: str, age: int, gender: str) -> None:
        self.name, self.age = name, age

    @property
    def age(self) -> int:
        return self._age

    @age.setter
    def age(self, new_age: int) -> None:
        if not isinstance(new_age, int):
            raise TypeError(f'Age must be int, not {type(new_age)}')
        if new_age < 0:
            raise ValueError(f'Age must be positive, not {new_age}')
        self._age = new_age

    @property
    def gender(self) -> str:
        return self._gender

    @gender.setter
    def gender(self, new_gender: str) -> None:
        if not isinstance(new_gender, str):
            raise TypeError(f'Gender must be str, not {type(new_gender)}')
        self._gender = new_gender

class Director(Human):
    def __init__(self, name: str, age: int, gender: str, salary: float, subject: str = None) -> None:
        super().__init__(name, age, gender)
        self.subject = subject
        self.salary = salary
    def __str__(self) -> str:
        return f'{self.__class__.__name__}, {self.gender}, {self.name}, {self.age}, {self.salary}, {self.subject if self.subject is None else "не преподает"}'

class Student(Human):
    def __init__(self, name: str, age: int, gender: str, class_: int) -> None:
        super().__init__(name, age, gender)
        self.class_ = class_

    @property
    def class_(self) -> int:
        return self._class_

    @class_.setter
    def age(self, class_: int) -> None:
        if not isinstance(class_, int):
            raise TypeError(f'School Class must be int, not {type(class_)}')
        if not (class_ >= 1 and class_ <= 11):
            raise ValueError(f'School Class must be positive, not {class_}')
        self._class_ = class_

    def __str__(self) -> str:
        return f'{self.__class__.__name__}, {self.gender}, {self.name}, {self.age}, {self.class_}'

class Teacher(Human):
    _subjects = 'IT', 'PE', 'Biology', 'English', 'Administration', 'Physics', 'Informatics', 'Russian'
    def __init__(self, name: str, age: int, gender: str, subject: str) -> None:
        super().__init__(name, age, gender)
        self.subject = subject
    
    @property
    def subject(self) -> str:
        return self._subject
    
    @subject.setter
    def subject(self, subject: str) -> None:
        if not isinstance(subject, str):
            raise TypeError(f'Subject must be str, not {type(subject)}')
        if subject not in self._subjects:
            raise SubjectError(f'{subject} not found in this school')
        self._subject = subject

    def __str__(self) -> str:
        return f'{self.__class__.__name__}, {self.gender}, {self.name}, {self.age}, {self.subject}'
    