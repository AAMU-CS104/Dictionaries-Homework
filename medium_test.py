import medium
import unittest
from callee import strings
from unittest.mock import patch

class Test(unittest.TestCase):
  @patch('builtins.input')
  @patch('builtins.print')
  def test_dictionary(self, mock_print, mock_input):
    user_input = "my cat is a tabby cat"
    mock_input.return_value = user_input
    medium.main()
    mock_print.assert_any_call(strings.Regex("cat: 2"))
    mock_print.assert_any_call(strings.Regex("a: 1"))
    mock_print.assert_any_call(strings.Regex("tabby: 1"))
    mock_print.assert_any_call(strings.Regex("my: 1"))
    mock_print.assert_any_call(strings.Regex("is: 1"))


if __name__ == "__main__":
  unittest.main()