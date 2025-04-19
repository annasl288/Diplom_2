from data import TestData, ResponseText
from methods import Methods
import allure

class TestCreateOrder:

    @allure.title('Создание заказа с ингредиентами с авторизацией')
    def test_create_order_with_authorization_and_ingredients(self, create_new_user):

        ingredients = Methods.get_ingredients()
        token = create_new_user[2]
        response = Methods.create_order(token, ingredients)

        assert response.status_code == 200 and response.json()["success"] is True

    @allure.title('Создание заказа без ингредиентов с авторизацией')
    def test_create_order_with_authorization_and_no_ingredients_error(self, create_new_user):

        token = create_new_user[2]
        response = Methods.create_order(token, "")

        assert response.status_code == 400 and response.json()["message"] == ResponseText.no_ingredients

    @allure.title('Создание заказа без авторизации')
    def test_create_order_without_authorization(self):

        ingredients = Methods.get_ingredients()
        response = Methods.create_order("", ingredients)

        assert response.status_code == 200 and response.json()["success"] is True

    @allure.title('Создание заказа с неверным хешем ингредиента')
    def test_create_order_with_incorrect_hash_error(self):

        response = Methods.create_order("", TestData.incorrect_hash)

        assert response.status_code == 500