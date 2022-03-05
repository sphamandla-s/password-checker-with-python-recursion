import unittest
from unittest.mock import patch
import io
import sys
import password_cracker

class TestCase(unittest.TestCase):
    text = io.StringIO()
    sys.stdout = text
    def test_find_possible_password_combination(self):
        # comb means combinations
        possible_comb = password_cracker.possible_password_comb(['1','#'],2)
        result_possible_comb = ['11', '1#', '#1', '##']
        self.assertEqual(result_possible_comb, possible_comb)
    

    def test_character_set(self):
        result = ['1','2','3','4','5','6','7','8','9','0',
        '!','@','#','$','%','&','*','(',')','-','=','+',' ']
        self.assertEqual(result, password_cracker.password_character_set())


    def test_break_user_password(self):
        user_password = '1#1'
        possible_comb = password_cracker.possible_password_comb(['1','#'],3)
        password_crackered = password_cracker.break_user_password(possible_comb,user_password)
        self.assertTrue(password_crackered)



if __name__ == '__main__':
    unittest.main()