import unittest
import requests

def parse_service_call(expression):
    if not type(expression) is str:
        return None
    if expression == None:
        expression = "#NONE#"
    expression = str(expression)
    result = requests.get("http://localhost:8080/calc/"+expression)
    assert result.status_code == 200
    assert 'json' in result.headers['Content-Type']
    data = result.json()
    value = data['value']
    if value == "#NONE#":
        value = None
    return value

class Parser_TestCase(unittest.TestCase):
    def test_000_parser_function_exists(self):
        parse_service_call("3")

    def test_001_parser_returns_None_for_nonsense(self):
        assert parse_service_call("slfdkjs;lged") == None
        assert parse_service_call("") == None
        assert parse_service_call(None) == None
        assert parse_service_call(23425) == None

    def test_002_parser_can_parse_one_digit_numbers(self):
        assert parse_service_call("0") == 0
        assert parse_service_call("1") == 1
        assert parse_service_call("9") == 9
        assert parse_service_call("x") == None
        assert parse_service_call(".") == None

    def test_003_parser_can_parse_multiple_digit_numbers(self):
        assert parse_service_call("00") == 0
        assert parse_service_call("01") == 1
        assert parse_service_call("10") == 10
        assert parse_service_call("9999") == 9999
        assert parse_service_call("123456789") == 123456789

    def test_004_parser_can_parse_negative_multiple_digit_numbers(self):
        assert parse_service_call("-00") == -0
        assert parse_service_call("-01") == -1
        assert parse_service_call("-10") == -10
        assert parse_service_call("-9999") == -9999
        assert parse_service_call("-123456789") == -123456789
        assert parse_service_call("--9999") == 9999

    def test_005_parser_can_parse_decimal_numbers(self):
        assert parse_service_call("0.0") == 0.0
        assert parse_service_call("0.1") == 0.1
        assert parse_service_call("1.0") == 1.0
        assert parse_service_call("9.999") == 9.999
        assert parse_service_call("123.4567") == 123.4567
        assert parse_service_call(".999") == .999
        assert parse_service_call("999.") == 999.0

    def test_006_parser_can_parse_negative_decimal_numbers(self):
        assert parse_service_call("-0.0") == -0.0
        assert parse_service_call("-0.1") == -0.1
        assert parse_service_call("-1.0") == -1.0
        assert parse_service_call("-9.999") == -9.999
        assert parse_service_call("-123.4567") == -123.4567
        assert parse_service_call("-.999") == -.999
        assert parse_service_call("-999.") == -999.0
        assert parse_service_call("--999.") == 999.0

    def test_007_parser_can_add_numbers(self):
        assert parse_service_call("1+2+3+4") == 10
        assert parse_service_call("1+2+3+NOTHING") == None

if __name__ == "__main__":
    unittest.main(verbosity=2, exit=False)
