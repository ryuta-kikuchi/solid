class ReportGenerator:
    def __init__(self, formatter):
        self.formatter = formatter

    def generate_report(self, data):
        self.formatter.format(data)

class CSVReportFormatter:
    def format(self, data):
        print("CSVで出力する処理")

class JSONReportFormatter:
    def format(self, data):
        print("JSONで出力する処理")