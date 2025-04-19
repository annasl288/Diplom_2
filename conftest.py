import pytest
import allure
from data import TestData
from methods import Methods

@allure.step('Создать нового пользователя')
@pytest.fixture
def create_new_user():

    user_data = TestData.generate_random_user()
    response = Methods.create_new_user(user_data)
    token = response.json()["accessToken"]

    yield user_data, response, token

    Methods.delete_user()