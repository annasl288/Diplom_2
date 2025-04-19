from data import TestData, ResponseText
from methods import Methods
import allure

class TestUserLogin:

    @allure.title('Авторизация существующего пользователя')
    def test_user_login(self, create_new_user):

        user_data = create_new_user[0]
        response = Methods.user_login(user_data)

        assert response.status_code == 200 and response.json()["success"] is True

    @allure.title('Авторизация пользователя с неверными логином и паролем')
    def test_user_login_wrong_data_error(self):

        user_data = TestData.generate_random_user()
        response = Methods.user_login(user_data)

        assert response.status_code == 401 and response.json()["message"] == ResponseText.wrong_user_data