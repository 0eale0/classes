import random

posts = ('Therapist', 'Surgeon', "Neurologist", "Endocrinologist", "Pharmacis")
specializations = ('Surgery', 'Traumatology', 'Coronavirus Department',)


class Employee():
    def __init__(self, name, age, post):
        self.__name = name
        self.__age = age
        self.__post = post

    @property
    def post(self):
        return self

    @post.setter
    def post(self, post):
        if post in posts:
            self.__post = post
        else:
            print('Не существует такой должности')


@property
def age(self):
    return self.__age


@age.setter
def age(self, age):
    if age in range(1, 100):
        self.__age = age
    else:
        print("Недопустимый возраст")


@property
def name(self):
    return self.__name


def display_info(self):
    print("Имя:", self.__name, "\tВозраст:", self.__age, 'Должность:', self.post)


class Pharmacist(Employee):
    def __init__(self, name, age, post, pharmacist_rang, has_labotory_access, recipe_release_available):
        Employee.__init__(self, name, age, post)
        self.__rang = pharmacist_rang
        self.labotory__access = has_labotory_access
        self.recipe__release = recipe_release_available

    @property
    def rang(self):
        return self.rang

    @rang.setter
    def rang(self, rang):
        if 0 <= rang <= 25:
            self.__rang = rang
        else:
            print('Ранг не соответствует')

    def medicine(self):
        print("Имеется на складе")


class Surgeon(Employee):
    def __init__(self, name, age, post, surgeon_rang):
        Employee.__init__(self, name, age, post)
        self.__rang = surgeon_rang

    @property
    def rang(self):
        return self.rang

    @rang.setter
    def rang(self, rang):
        if 0 <= rang <= 50:
            self.__rang = rang
        else:
            print('Ранг не соответствует')


class Hospital:
    def __init__(self, location, specialization, best_doctor):
        self.location = location
        self.specialization = specialization
        self.best_doctor = best_doctor

    @property
    def specialization(self):
        return self.specialization

    @specialization.setter
    def specialization(self, specialization):
        if specialization in specializations:
            self.__specialization = specialization
        else:
            print('Не та специализация')

    def appointment_to_the_best_doctor(self, best_doctor):
        if random.choice([True, False]):
            print(f'Вы записаны к {best_doctor}')
        else:
            print('Вся запись забита')


class Blood_test(Hospital):
    def __init__(self, name, age, gender, blood):
        self.name = name
        self.age = age
        self.gender = gender
        self.blood = blood  # dict

    def erythrocytes(self):
        if self.blood['Er'] >= 4 and self.blood['Er'] <= 5:
            print("Значение в норме —", self.blood['Er'])
        else:
            print("Значение не в допустимой норме —", self.blood['Er'])

    def leukocytes(self):
        if self.blood['Le'] >= 4 and self.blood['Le'] <= 9:
            print("Значение в норме —", self.blood['Le'])
        else:
            print("Значение не в допустимой норме —", self.blood['Le'])

    def platelets(self):
        if self.blood['Tr'] >= 180 and self.blood['Tr'] <= 320:
            print("Значение в норме —", self.blood['Tr'])
        else:
            print("Значение не в допустимой норме —", self.blood['Tr'])
