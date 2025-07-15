import requests
from requests import Response

from src.get_vacancies import GetVacanciesAPI


class HeadHunterAPI(GetVacanciesAPI):
    """Класс для подключения к hh.ru"""

    def __init__(self):
        self.__url = "https://api.hh.ru/vacancies"
        self.__headers = {"User-Agent": "HH-User-Agent"}
        self.__params = {"text": "", "per_page": "", "only_with_salary": True}

    def get_response(self, keyword, per_page) -> Response:
        self.__params["text"] = keyword
        self.__params["per_page"] = per_page
        request = requests.get(self.__url, params=self.__params)
        request.raise_for_status()
        return request

    def get_vacancies(self, keyword: str, per_page: int):
        return self.get_response(keyword, per_page).json()["items"]
