import pytest
import allure
from helpers import RandomUser
from methods import Methods

@allure.step('Создать нового пользователя')
@pytest.fixture
def create_new_user():

    user_data = RandomUser.generate_random_user()
    response = Methods.create_new_user(user_data)
    token = response.json()["accessToken"]

    yield user_data, response, token