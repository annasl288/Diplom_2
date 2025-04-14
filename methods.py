import requests
import allure
from helpers import Urls, Endpoints

class Methods:

    @staticmethod
    @allure.step('Отправить запрос на создание нового пользователя')
    def create_new_user(user_data):

        response = requests.post(f'{Urls.api}{Endpoints.registration}', data = user_data)

        return response

    @staticmethod
    @allure.step('Отправить запрос на авторизацию пользователя')

    def user_login(user_data):

        response = requests.post(f'{Urls.api}{Endpoints.authorization}', data = user_data)

        return response

    @staticmethod
    @allure.step('Отправить запрос на изменение данных пользователя')

    def change_user_data(token, new_data):

        headers = {"Authorization": token}
        response = requests.patch(f'{Urls.api}{Endpoints.user}', headers = headers, data = new_data)

        return response

    @staticmethod
    @allure.step('Отправить запрос на получение списка ингредиентов')

    def get_ingredients():

        response = requests.get(f'{Urls.api}{Endpoints.ingredients}')

        ingredients = []
        for i in response.json()["data"]:
            ingredients.append(i["_id"])

        return ingredients


    @staticmethod
    @allure.step('Отправить запрос на создание нового заказа')
    def create_order(token, ingredients):

        headers = {"Authorization": token}
        ids = {"ingredients": ingredients}
        response = requests.post(f'{Urls.api}{Endpoints.orders}', headers = headers, data = ids)

        return response

    @staticmethod
    @allure.step('Отправить запрос на получение списка заказов пользователя')

    def get_user_orders(token):

        headers = {"Authorization": token}
        response = requests.get(f'{Urls.api}{Endpoints.orders}', headers = headers)

        return response