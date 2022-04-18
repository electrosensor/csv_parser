import pytest
from solution import Solution
from solution import CsvFileReader


def test_data_read():
    expected_lines = [
        "message",
        "Please put us in for 5000000 CAT 5yr?",
        "Please put us in for 4500000 IBM 2yr?",
        "Please put us in for CIT 1500000 4yr?",
        "Please put us in for 3500000 YZR 2yr?",
        "Please put us in for some OPS 3yr?",
        "Please put us in for 5000009a CAT 5yr?",
        "Please put us in for 4500000 LPS 2yr?",
        "Please buy 1500011 CIT 4yr?",
        "Please buy 3920000 YZR 2yr?",
        "Please put us in for 2550 OPS 3yr?",
        "Please put us in for 5000010 CAT 5yr?",
        "Please buy 4500000 ABM 2yr?",
        "Please buy 1500100 CIT 4yr?",
        "Please put us in for 2yr 3500000 HJK?",
        "Please put us in for OPS 2500200 3yr?",
        "Please put us in for 5000008 CAT 5 years?",
        "Please put us in for 4MM ORB 2yr?",
        "Please put us in for 8500000 CIT 4yr?",
        "Please put us in for 3500400 YZU 2yr?",
        "Please put us in for 2520000 APS 3yr?",
    ]

    csv_test_filepath = 'test_input.csv'
    reader = CsvFileReader(csv_filepath=csv_test_filepath)
    actual_lines = reader.read_data()

    assert len(actual_lines) == len(expected_lines)

    for actual_line, expected_line in zip(actual_lines, expected_lines):
        assert actual_line == expected_line


def test_find_stock():
    test_lines = [
        "Please put us in for 5000000 CAT 5yr?",
        "Please put us in for 4500000 IBM 2yr?",
        "Please put us in for CIT 1500000 4yr?",
        "Please put us in for 3500000 YZR 2yr?",
        "Please put us in for some OPS 3yr?",
        "Please put us in for 5000009a CAT 5yr?",
        "Please put us in for 4500000 LPS 2yr?",
        "Please buy 1500011 CIT 4yr?",
        "Please buy 3920000 YZR 2yr?",
        "Please put us in for 2550 OPS 3yr?",
        "Please put us in for 5000010 CAT 5yr?",
        "Please buy 4500000 ABM 2yr?",
        "Please buy 1500100 CIT 4yr?",
        "Please put us in for 2yr 3500000 HJK?",
        "Please put us in for OPS 2500200 3yr?",
        "Please put us in for 5000008 CAT 5 years?",
        "Please put us in for 4MM ORB 2yr?",
        "Please put us in for 8500000 CIT 4yr?",
        "Please put us in for 3500400 YZU 2yr?",
        "Please put us in for 2520000 APS 3yr?",
    ]
    expected_stocks = [
        "CAT",
        "IBM",
        "CIT",
        "YZR",
        "OPS",
        "CAT",
        "LPS",
        "CIT",
        "YZR",
        "OPS",
        "CAT",
        "ABM",
        "CIT",
        "HJK",
        "OPS",
        "CAT",
        "ORB",
        "CIT",
        "YZU",
        "APS",
    ]
    reader = CsvFileReader(csv_filepath='')
    solution = Solution(reader)

    assert len(test_lines) == len(expected_stocks)
    for line, stock in zip(test_lines, expected_stocks):
        assert solution.find_stock(line)[0] == stock


if __name__ == '__main__':
    pytest.main([__file__])
