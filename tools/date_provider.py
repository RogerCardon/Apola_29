from abc import ABC, abstractmethod


class DateTimeProvider(ABC):

    @abstractmethod
    def get_current_datetime(self) -> str:
        pass
