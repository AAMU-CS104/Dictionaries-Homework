import easy
import unittest
from unittest.mock import patch

class Test(unittest.TestCase):
  @patch('builtins.print')
  def test_problem_one(self, mock_print):
    easy.main()
    mock_print.assert_any_call({})

  @patch('builtins.print')
  def test_problem_two(self, mock_print):
    easy.main()
    want = {
      'strawberry': 'red', 
      'blueberry': 'blue',
      'tomato': 'red'
    }
    mock_print.assert_any_call(str(want))

  @patch('builtins.print')
  def test_problem_three(self, mock_print):
    easy.main()
    want = {
      'strawberry': 'red', 
      'blueberry': 'blue',
      'tomato': 'red',
      'banana': 'yellow'
    }
    mock_print.assert_any_call(str(want))

  @patch('builtins.print')
  def test_problem_four(self, mock_print):
    easy.main()
    want = {
      'blueberry': 'blue',
      'tomato': 'red',
      'banana': 'yellow'
    }
    mock_print.assert_any_call(str(want))

  @patch('builtins.print')
  def test_problem_five(self, mock_print):
    easy.main()
    want = {
      'blueberry': 'blue',
      'tomato': 'red',
      'banana': 'green'
    }
    mock_print.assert_any_call(str(want))

  @patch('builtins.print')
  def test_problem_six(self, mock_print):
    easy.main()
    mock_print.assert_any_call("blueberry is blue")
    mock_print.assert_any_call("tomato is red")
    mock_print.assert_any_call("banana is green")
  

if __name__ == "__main__":
  unittest.main()