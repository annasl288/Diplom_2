from methods import Methods
from data import ResponseText
import allure

class TestGetUserOrder:

    @allure.title('Получение списка заказов авторизованного пользователя')
    def test_get_user_order_with_authorization(self, create_new_user):

        token = create_new_user[2]
        response = Methods.get_user_orders(token)

        assert response.status_code == 200 and response.json()["success"] is True

    @allure.title('Получение списка заказов неавторизованного пользователя')
    def test_get_user_order_without_authorization(self):

        response = Methods.get_user_orders("")

        assert response.status_code == 401 and response.json()["message"] == ResponseText.not_authorized