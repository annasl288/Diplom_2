import requests
import allure
from urls import Urls

class Methods:

    @staticmethod
    @allure.step('Отправить запрос на создание нового пользователя')
    def create_new_user(user_data):

        response = requests.post(Urls.registration, data = user_data)

        return response

    @staticmethod
    @allure.step('Отправить запрос на авторизацию пользователя')

    def user_login(user_data):

        response = requests.post(Urls.authorization, data = user_data)

        return response

    @staticmethod
    @allure.step('Отправить запрос на изменение данных пользователя')

    def change_user_data(token, new_data):

        headers = {"Authorization": token}
        response = requests.patch(Urls.user, headers = headers, data = new_data)

        return response

    @staticmethod
    @allure.step('Отправить запрос на получение списка ингредиентов')

    def get_ingredients():

        response = requests.get(Urls.ingredients)

        ingredients = []
        for i in response.json()["data"]:
            ingredients.append(i["_id"])

        return ingredients


    @staticmethod
    @allure.step('Отправить запрос на создание нового заказа')
    def create_order(token, ingredients):

        headers = {"Authorization": token}
        ids = {"ingredients": ingredients}
        response = requests.post(Urls.orders, headers = headers, data = ids)

        return response

    @staticmethod
    @allure.step('Отправить запрос на получение списка заказов пользователя')
    def get_user_orders(token):

        headers = {"Authorization": token}
        response = requests.get(Urls.orders, headers = headers)

        return response

    @staticmethod
    @allure.step('Удалить пользователя')
    def delete_user():

        response = requests.delete(Urls.user)