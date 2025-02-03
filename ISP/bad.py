from abc import ABC, abstractmethod

class Printer(ABC):
    @abstractmethod
    def print(self, document: str) -> None:
        pass

    @abstractmethod
    def scan(self, document: str) -> None:
        pass

    @abstractmethod
    def fax(self, document: str) -> None:
        pass

class SimplePrinter(Printer):
    def print(self, document: str) -> None:
        print("印刷処理")

    def scan(self, document: str) -> None:
        """スキャン機能なしだが、実装を強制される"""
        raise NotImplementedError("このプリンターにはスキャン機能がありません")

    def fax(self, document: str) -> None:
        """FAX機能なしだが、実装を強制される"""
        raise NotImplementedError("このプリンターにはFAX機能がありません")