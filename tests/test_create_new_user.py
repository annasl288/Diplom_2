import pytest
import allure
from helpers import RandomUser, ResponseText
from methods import Methods

class TestNewUser:

    @allure.title('Создание нового пользователя')
    def test_create_new_user(self, create_new_user):

        response = create_new_user[1]

        assert response.status_code == 200 and response.json()["success"] is True

    @allure.title('Создание уже существующего пользователя')
    def test_new_user_already_exists_403(self, create_new_user):

        user_data = create_new_user[0]
        response = Methods.create_new_user(user_data)

        assert response.status_code == 403 and response.json()['message'] == ResponseText.user_already_exists

    @allure.title('Создание нового пользователя без обязательного поля')
    @pytest.mark.parametrize("field", ["email", "password", "name"])
    def test_create_new_user_without_one_field_error(self, field):

        user_data = RandomUser.generate_random_user()
        user_data.pop(field)
        response = Methods.create_new_user(user_data)

        assert response.status_code == 403 and response.json()['message'] == ResponseText.required_fields