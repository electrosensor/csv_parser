import csv
import re
from abc import ABC, abstractmethod
import pprint


class DataReader(ABC):
    @abstractmethod
    def read_data(self):
        pass


class CsvFileReader(DataReader):
    def __init__(self, csv_filepath):
        self.csv_filepath = csv_filepath

    def read_data(self):
        lines = []
        with open(self.csv_filepath, mode='r') as file:
                data = csv.reader(file)
                for line in data:
                    lines.append(line[0])
        return lines


class Solution:
    def __init__(self, data_reader: DataReader):
        self.data_reader = data_reader

    def find_stock(self, line):
        matches = re.search(r"\b[A-Z][A-Z][A-Z]\b", line)
        span = matches.span()
        return line[span[0]:span[1]], span[0]

    def find_amount(self, line):
        matches = re.search(r"[0-9]+", line)
        span = matches.span()
        return line[span[0]:span[1]], span[0]

    # def find_period(self, line):
    #     matches = re.search(r"", line)
    #     span = matches.span()
    #     return line[span[0]:span[1]], span[0]

    def solution(self, preprocess_stock=None):
        data = self.data_reader.read_data()

        stocks = {}
        for line_index, line in enumerate(data):
            # print(line_index, line)
            if line_index != 0:
                stock, offset = self.find_stock(line)
                if preprocess_stock:
                    stock = preprocess_stock(stock)
                stocks[stock] = {
                    'line_index': line_index,
                    'stock': {
                        'value:': stock,
                        'offset': offset
                    },
                }

                amount, offset = self.find_amount(line)
                stocks[stock].update({
                    'amount': {
                        'value': amount,
                        'offset': offset
                    },
                })

                # period, offset = self.find_period(line)
                # stocks[stock].update({
                #     'period': {
                #         'value': amount,
                #         'offset': offset
                #     },
                # })

        return stocks


if __name__ == '__main__':
    pprint = pprint.PrettyPrinter()

    csv_filepath = 'input.csv'
    data_reader = CsvFileReader(csv_filepath)

    parsed_data = Solution(data_reader).solution()

    pprint.pprint(parsed_data)

    parsed_data = Solution(data_reader).solution(preprocess_stock=str.lower)
    pprint.pprint(parsed_data)
