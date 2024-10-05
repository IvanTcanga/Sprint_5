import random


class DataGenerator:
    @staticmethod
    def generate_email():
        username = ''.join(random.sample('abcdefghijklmnopqrstuvwxyz', random.randint(2, 10)))
        email = f"{username}@ya.ru"
        return email

    @staticmethod
    def generate_password():
        characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()'
        password = ''.join(random.sample(characters, random.randint(6, 10)))
        return password
