import pytest
import allure
from faker import Faker
from methods import Methods
from helpers import ResponseText

class TestChangeUserData:

    fake = Faker()

    @allure.title('Изменение данных пользователя с авторизацией')
    @pytest.mark.parametrize("new_data", [
        {"email": fake.email()},
        {"password": fake.password()},
        {"name": fake.name()}
    ])
    def test_change_user_data_with_authorization(self, create_new_user, new_data):

        token = create_new_user[2]
        response = Methods().change_user_data(token, new_data)

        assert response.status_code == 200 and response.json()["success"] is True

    @allure.title('Изменение данных пользователя без авторизации')
    @pytest.mark.parametrize("new_data", [
        {"email": fake.email()},
        {"password": fake.password()},
        {"name": fake.name()}
    ])
    def test_change_user_data_without_authorization_error(self, new_data):

        response = Methods().change_user_data("", new_data)

        assert response.status_code == 401 and response.json()["message"] == ResponseText.not_authorized