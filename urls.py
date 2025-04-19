class Endpoints:
    registration = "/auth/register"
    authorization = "/auth/login"
    user = "/auth/user"
    ingredients = "/ingredients"
    orders = "/orders"


class Urls:

    api = "https://stellarburgers.nomoreparties.site/api"
    registration = f'{api}{Endpoints.registration}'
    authorization = f'{api}{Endpoints.authorization}'
    user = f'{api}{Endpoints.user}'
    ingredients = f'{api}{Endpoints.ingredients}'
    orders = f'{api}{Endpoints.orders}'