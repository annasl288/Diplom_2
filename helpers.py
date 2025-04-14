from faker import Faker

class Urls:

    api = "https://stellarburgers.nomoreparties.site/api"

class Endpoints:

    registration = "/auth/register"
    authorization = "/auth/login"
    user = "/auth/user"
    ingredients = "/ingredients"
    orders = "/orders"

class RandomUser:

    @staticmethod
    def generate_random_user():

        fake = Faker(locale = "ru_RU")
        data = {
            "email": fake.email(),
            "password": fake.password(),
            "name": fake.name()
        }

        return data

class ResponseText:
    not_authorized = "You should be authorised"
    no_ingredients = "Ingredient ids must be provided"
    user_already_exists = 'User already exists'
    required_fields = 'Email, password and name are required fields'
    wrong_user_data = 'email or password are incorrect'