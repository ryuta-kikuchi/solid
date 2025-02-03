from abc import ABC, abstractmethod

class ReportFormatter(ABC):
    @abstractmethod
    def format(self, data):
        pass

# CSV形式の出力実装
class CSVReportFormatter(ReportFormatter):
    def format(self, data):
        print("CSVで出力する処理")

# JSON形式の出力実装
class JSONReportFormatter(ReportFormatter):
    def format(self, data):
        print("JSONで出力する処理")

class ReportGenerator:
    def __init__(self, formatter: ReportFormatter):
        self.formatter = formatter

    def generate_report(self, data):
        return self.formatter.format(data)