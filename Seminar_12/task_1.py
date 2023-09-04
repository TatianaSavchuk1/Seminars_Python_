# Создайте класс студента.
# Используя дескрипторы проверяйте ФИО на первую заглавную букву и наличие только букв.

class Validation:

    def __set_name__(self, owner, name):
        self._name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self._name, None)

    def __set__(self, instance, value):
        
        if not value.istitle() or not value.isalpha():
            raise ValueError('Имя должно начинаться с заглавной буквы и содержать только буквы.')
        setattr(instance, self._name, value)

        
        


class Student:
    first_name = Validation()
    last_name = Validation()
    patr = Validation()


    def __init__ (self, first_name, last_name, patr):

        self.first_name = first_name
        self.last_name = last_name
        self.patr = patr


    def __repr__ (self):
    
        return f'Student(ФИО = {self.last_name} {self.first_name} {self.patr})'
    
    

if __name__ == "__main__":
    # st1 = Student('Иван', 'Иванов', 'Иванович')
    st2 = Student('пётр', 'петров', 'петрович')
    # st3 = Student('Борис', 'Бо7рисов', 'Борисович')
    # print(st1)
    print(st2)
    # print(st3)
