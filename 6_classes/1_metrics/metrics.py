import csv
from datetime import datetime, UTC


class FileTXT:

    def __init__(self, path):
        self.path = path
        self.create_file()

    def create_file(self):
        with open(self.path, 'w', newline='') as txt_file:
            pass

    def writing_to_file(self, data) -> None:
        with open(self.path, "a", newline="") as file:
            for metrics in data:
                date, metric, value = metrics
                file.write(date + ' ' + metric + ' ' + value + '\n')


class FileCSV:

    def __init__(self, path):
        self.path = path
        self.create_file()

    def create_file(self):
        with open(self.path, 'w', newline='') as csv_file:
            csv.writer(csv_file, delimiter = ';').writerow(["date", "metric", "value"])

    def writing_to_file(self, data) -> None:
        with open(self.path, "a", newline="") as csv_file:
            csv.writer(csv_file, delimiter=";", lineterminator="\n").writerows(data)


class Statsd:

    def __init__(self, buffer_limit, path):
        self.buffer_limit = buffer_limit
        self.path = path
        self.buffer = []
        self.control_count = 0

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.append_info_to_file()

    def append_info_to_file(self) -> None:
        self.path.writing_to_file(self.buffer)
        self.buffer = []

    def append_info_to_buffer(self, info, value):
        self.control_count += 1
        self.buffer.append(
                (datetime.now(UTC).strftime('%Y-%m-%dT%H:%M:%S%z'), info, str(value))
        )
        if self.control_count == self.buffer_limit:
            self.append_info_to_file()
            self.control_count = 0

    def incr(self, info):
        self.append_info_to_buffer(info, 1)

    def decr(self, info):
        self.append_info_to_buffer(info, -1)


def get_txt_statsd(path: str, buffer_limit: int = 10) -> Statsd:
     if path[-4:] != '.txt':
         raise ValueError("Файл должен иметь расширение '.txt'")
     return Statsd(buffer_limit, FileTXT(path))

def get_csv_statsd(path: str, buffer_limit: int = 10) -> Statsd:
     if path[-4:] != '.csv':
         raise ValueError("Файл должен иметь расширение '.csv'")
     return Statsd(buffer_limit, FileCSV(path))