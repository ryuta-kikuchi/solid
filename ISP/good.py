from abc import ABC, abstractmethod

# 各機能ごとにインターフェースを分割
class Printable(ABC):
    @abstractmethod
    def print(self, document: str) -> None:
        pass

class Scannable(ABC):
    @abstractmethod
    def scan(self, document: str) -> None:
        pass