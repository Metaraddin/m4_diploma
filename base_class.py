import random
from typing import Dict


class BaseClass:
    def __init__(self) -> None:
        self._params: Dict[str: list] = {}  # Возможные варианты параметров
        self.params: dict = {}  # Выбранные параметры

    @staticmethod
    def _wrap_values_in_lists(data: dict) -> None:
        """
        Оборачивает элементы словаря в списки, если они уже не являются списками.
        Изменяет исходный словарь
        """
        for k, v in data.items():
            if type(v) is not list:
                data[k] = [v]

    def _randomize_params(self) -> None:
        """
        Выбирает случайное значение параметров из self._params и записывает их в self.params
        """
        for k, v in self._params.items():
            self.params[k] = random.choice(v)
    
    def as_dict(self) -> dict:
        """
        Возвращает словарь с некоторыми атрибутами класса
        """
        return dict(
            type=self.__class__,
            params={k: v.as_dict() if isinstance(v, BaseClass) else v for k, v in self.params.items()},
        )

