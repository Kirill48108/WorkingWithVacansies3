from pydantic import BaseModel, ValidationError


class Vacancy(BaseModel):
    """Класс для работы с вакансиями"""

    __slots__ = ("name", "alternate_url", "salary_from", "salary_to", "area_name", "requirement", "responsibility")

    def __init__(
        self,
        name,
        alternate_url,
        salary_from,
        salary_to,
        area_name,
        requirement,
    ):
        """Конструктор класса"""

        self.name: str = name
        self.alternate_url: str = alternate_url
        self.salary_from: int = salary_from
        self.salary_to: int = salary_to
        self.area_name: str = area_name
        self.requirement: str = requirement

        try:
            vacancy_data = {
                "name": "Тестировщик",
                "alternate_url": "https://api.hh.ru/areas/26",
                salary_from: 1234,
                salary_to: 34278,
                "area_name": "QA Тестировщик",
                requirement: "3+ лет опыта работы в области QA",
            }
            vacancy = Vacancy(**vacancy_data)
            print("Валидация прошла успешно:", vacancy)

            invalid_vacancy_data = {
                "name": 123,
                "alternate_url": 4465,
                salary_from: "по результатам собесдоания",
                salary_to: "по результатам собесдоания",
                "area_name": 5464664,
                requirement: 354446,
            }
            invalid_vacancy = Vacancy(**invalid_vacancy_data)
        except ValidationError as e:
            print("Ошибка валидации:", e)

    def __str__(self) -> str:
        """Строковое представление вакансии"""

        return (
            f"Наименование вакансии: {self.name}\n"
            f"Ссылка на вакансию: {self.alternate_url}\n"
            f"Зарплата: от {self.salary_from} до {self.salary_to}\n"
            f"Место работы: {self.area_name}\n"
            f"Краткое описание: {self.requirement}\n"
        )

    def __lt__(self, other) -> bool:
        """Метод сравнения от большего к меньшему"""

        return self.salary_from < other.salary_from

    @classmethod
    def from_hh_dict(cls, vacancy_data: dict):
        """Метод возвращает экземпляр класса в виде списка"""

        salary = vacancy_data.get("salary")

        return cls(
            vacancy_data["name"],
            vacancy_data["alternate_url"],
            salary.get("from") if salary.get("from") else 0,
            salary.get("to") if salary.get("to") else 0,
            vacancy_data["area"]["name"],
            vacancy_data["snippet"]["requirement"],
        )

    def to_dict(self) -> dict:
        """Метод возвращает вакансию в виде словаря"""

        return {
            "name": self.name,
            "alternate_url": self.alternate_url,
            "salary_from": self.salary_from,
            "salary_to": self.salary_to,
            "area_name": self.area_name,
            "requirement": self.requirement,
        }
