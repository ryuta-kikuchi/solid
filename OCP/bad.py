class ReportGenerator:
    def generate_report(self, data, format_type):
        if format_type == 'csv':
            return self._generate_csv(data)
        elif format_type == 'json':
            return self._generate_json(data)
        else:
            raise ValueError("Unsupported format type")

    def _generate_csv(self, data):
        print("CSV出力の処理")

    def _generate_json(self, data):
        print("JSON出力の処理")