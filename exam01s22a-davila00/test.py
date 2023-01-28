import unittest
import io
import sys
from unittest.mock import patch
from tracker import transition

class Test01_id_not_equal_to_3_chars(unittest.TestCase):
    def test_list_int(self):
        """
        *** Test01 ****  GIVEN: id='a7d3f22' *** EXPECT: Return value 901
        """
        self.assertEqual(transition(tracker=[], id='a7d3f22', enter=''),901)
        print()




class Test02_enter_floor_not_number(unittest.TestCase):
    def test_list_int(self):
        """
        *** Test02 ****  GIVEN: enter='p-2' *** EXPECT: Return value 902
        """
        self.assertEqual(transition(tracker=[], id='a4f', enter='p-2'),902)
        print()

class Test03_enter_floor_less_than_1(unittest.TestCase):
    def test_list_int(self):
        """
        *** Test03 ****  GIVEN: enter='0-2' *** EXPECT: Return value 903
        """
        self.assertEqual(transition(tracker=[], id='a4f', enter='0-2'),903)
        print()

class Test04_enter_floor_greater_than_3(unittest.TestCase):
    def test_list_int(self):
        """
        *** Test04 ****  GIVEN: enter='4-2' *** EXPECT: Return value 904
        """
        self.assertEqual(transition(tracker=[], id='a4f', enter='4-2'),904)
        print()

class Test05_enter_room_not_number(unittest.TestCase):
    def test_list_int(self):
        """
        *** Test05 ****  GIVEN: enter='1-p' *** EXPECT: Return value 905
        """
        self.assertEqual(transition(tracker=[], id='a4f', enter='1-p'),905)
        print()

class Test06_enter_room_greater_than_4(unittest.TestCase):
    def test_list_int(self):
        """
        *** Test06 ****  GIVEN: enter='1-5' *** EXPECT: Return value 906
        """
        self.assertEqual(transition(tracker=[], id='a4f', enter='1-5'),906)
        print()

class Test07_invalid_move_enter_floor_2_from_outside(unittest.TestCase):
    def test_list_int(self):
        """
        *** Test07 ****  GIVEN: tracker=empty id='afa' enter='2-1' *** EXPECT: Return value 999
        """
        tracker = [[[],[],[],[]],[[],[],[],[]],[[],[],[],[]]]
        self.assertEqual(transition(tracker=tracker, id='a4f', enter='2-1'),999)
        print()

class Test08_invalid_move_enter_floor_3_from_outside(unittest.TestCase):
    def test_list_int(self):
        """
        *** Test08 ****  GIVEN: tracker=empty id='afa' enter='3-1' *** EXPECT: Return value 999
        """
        tracker = [[[],[],[],[]],[[],[],[],[]],[[],[],[],[]]]
        self.assertEqual(transition(tracker=tracker, id='a4f', enter='3-1'),999)
        print()

class Test09_invalid_move_enter_floor_2_from_floor_1_room_3(unittest.TestCase):
    def test_list_int(self):
        """
        *** Test09 ****  GIVEN: tracker=[[[],[],['a4f'],[]],[[],[],[],[]],[[],[],[],[]]] id='a4f' enter='2-4' *** EXPECT: Return value 999
        """
        tracker = [[[],[],['a4f'],[]],[[],[],[],[]],[[],[],[],[]]]
        self.assertEqual(transition(tracker=tracker, id='a4f', enter='2-4'),999)
        print()

class Test10_invalid_move_enter_floor_3_from_floor_1_room_3(unittest.TestCase):
    def test_list_int(self):
        """
        *** Test10 ****  GIVEN: tracker=[[[],[],['a4f'],[]],[[],[],[],[]],[[],[],[],[]]] id='a4f' enter='3-2' *** EXPECT: Return value 999
        """
        tracker = [[[],[],['a4f'],[]],[[],[],[],[]],[[],[],[],[]]]
        self.assertEqual(transition(tracker=tracker, id='a4f', enter='3-2'),999)
        print()

class Test11_invalid_move_enter_floor_3_from_floor_2_room_3(unittest.TestCase):
    def test_list_int(self):
        """
        *** Test11 ****  GIVEN: tracker=[[[],[],[],[]],[[],['a4f'],[],[]],[[],[],[],[]]] id='a4f' enter='3-2' *** EXPECT: Return value 999
        """
        tracker = [[[],[],[],[]],[[],[],['a4f'],[]],[[],[],[],[]]]
        self.assertEqual(transition(tracker=tracker, id='a4f', enter='3-2'),999)
        print()

class Test12_valid_move_enter_floor_1_room_1_from_outside(unittest.TestCase):
    def test_list_int(self):
        """
        *** Test12 ****  GIVEN: tracker=[[[],[],[],[]],[[],[],[],[]],[[],[],[],[]]] id='a4f' enter='1-1' *** EXPECT: tracker=[[['a4f'],[],[],[]],[[],[],[],[]],[[],[],[],[]]]
        """
        tracker = [[[],[],[],[]],[[],[],[],[]],[[],[],[],[]]]
        transition(tracker=tracker, id='a4f', enter='1-1')
        self.assertEqual(tracker,[[['a4f'],[],[],[]],[[],[],[],[]],[[],[],[],[]]])
        print()

class Test13_valid_move_enter_floor_1_room_4_from_floor_1_room_1(unittest.TestCase):
    def test_list_int(self):
        """
        *** Test13 ****  GIVEN: tracker=[[['a4f'],[],[],[]],[[],[],[],[]],[[],[],[],[]]] id='a4f' enter='1-4' *** EXPECT: tracker=[[[],[],[],['a4f']],[[],[],[],[]],[[],[],[],[]]]
        """
        tracker = [[['a4f'],[],[],[]],[[],[],[],[]],[[],[],[],[]]]
        transition(tracker=tracker, id='a4f', enter='1-4')
        self.assertEqual(tracker,[[[],[],[],['a4f']],[[],[],[],[]],[[],[],[],[]]])
        print()

class Test14_valid_move_enter_floor_2_room_4_from_floor_1_room_4(unittest.TestCase):
    def test_list_int(self):
        """
        *** Test14 ****  GIVEN: tracker=[[[],[],[],['a4f']],[[],[],[],[]],[[],[],[],[]]] id='a4f' enter='2-4' *** EXPECT: tracker=[[[],[],[],[]],[[],[],[],['a4f']],[[],[],[],[]]]
        """
        tracker = [[[],[],[],['a4f']],[[],[],[],[]],[[],[],[],[]]]
        transition(tracker=tracker, id='a4f', enter='2-4')
        self.assertEqual(tracker,[[[],[],[],[]],[[],[],[],['a4f']],[[],[],[],[]]])
        print()

class Test15_valid_move_enter_floor_2_room_2_from_floor_2_room_4(unittest.TestCase):
    def test_list_int(self):
        """
        *** Test15 ****  GIVEN: tracker=[[[],[],[],[]],[[],[],[],['a4f']],[[],[],[],[]]] id='a4f' enter='2-2' *** EXPECT: tracker=[[[],[],[],[]],[[],['a4f'],[],[]],[[],[],[],[]]]
        """
        tracker = [[[],[],[],[]],[[],[],[],['a4f']],[[],[],[],[]]]
        transition(tracker=tracker, id='a4f', enter='2-2')
        self.assertEqual(tracker,[[[],[],[],[]],[[],['a4f'],[],[]],[[],[],[],[]]])
        print()

class Test16_valid_move_enter_floor_3_room_2_from_floor_2_room_2(unittest.TestCase):
    def test_list_int(self):
        """
        *** Test16 ****  GIVEN: tracker=[[[],[],[],[]],[[],['a4f'],[],[]],[[],[],[],[]]] id='a4f' enter='3-2' *** EXPECT: tracker=[[[],[],[],[]],[[],[],[],[]],[[],['a4f'],[],[]]]
        """
        tracker = [[[],[],[],[]],[[],['a4f'],[],[]],[[],[],[],[]]]
        transition(tracker=tracker, id='a4f', enter='3-2')
        self.assertEqual(tracker,[[[],[],[],[]],[[],[],[],[]],[[],['a4f'],[],[]]])
        print()

class Test17_valid_move_enter_floor_2_room_2_from_floor_3_room_2(unittest.TestCase):
    def test_list_int(self):
        """
        *** Test17 ****  GIVEN: tracker=[[[],[],[],[]],[[],[],[],[]],[[],['a4f'],[],[]]] id='a4f' enter='2-2' *** EXPECT: tracker=[[[],[],[],[]],[[],['a4f'],[],[]],[[],[],[],[]]]
        """
        tracker = [[[],[],[],[]],[[],[],[],[]],[[],['a4f'],[],[]]]
        transition(tracker=tracker, id='a4f', enter='2-2')
        self.assertEqual(tracker,[[[],[],[],[]],[[],['a4f'],[],[]],[[],[],[],[]]])
        print()

class Test18_valid_move_enter_floor_2_room_4_from_floor_2_room_2(unittest.TestCase):
    def test_list_int(self):
        """
        *** Test18 ****  GIVEN: tracker=[[[],[],[],[]],[[],['a4f'],[],[]],[[],[],[],[]]] id='a4f' enter='2-4' *** EXPECT: tracker=[[[],[],[],[]],[[],[],[],['a4f']],[[],[],[],[]]]
        """
        tracker = [[[],[],[],[]],[[],['a4f'],[],[]],[[],[],[],[]]]
        transition(tracker=tracker, id='a4f', enter='2-4')
        self.assertEqual(tracker,[[[],[],[],[]],[[],[],[],['a4f']],[[],[],[],[]]])
        print()

class Test19_valid_move_enter_floor_1_room_4_from_floor_2_room_4(unittest.TestCase):
    def test_list_int(self):
        """
        *** Test19 ****  GIVEN: tracker=[[[],[],[],[]],[[],[],[],['a4f']],[[],[],[],[]]] id='a4f' enter='1-4' *** EXPECT: tracker=[[[],[],[],['a4f']],[[],[],[],[]],[[],[],[],[]]]
        """
        tracker = [[[],[],[],[]],[[],[],[],['a4f']],[[],[],[],[]]]
        transition(tracker=tracker, id='a4f', enter='1-4')
        self.assertEqual(tracker,[[[],[],[],['a4f']],[[],[],[],[]],[[],[],[],[]]])
        print()

class Test20_valid_move_enter_outside_from_floor_1_room_1(unittest.TestCase):
    def test_list_int(self):
        """
        *** Test20 ****  GIVEN: tracker=[[['a4f'],[],[],[]],[[],[],[],[]],[[],[],[],[]]] id='a4f' enter='1-0' *** EXPECT: tracker=[[[],[],[],[]],[[],[],[],[]],[[],[],[],[]]]
        """
        tracker = [[['a4f'],[],[],[]],[[],[],[],[]],[[],[],[],[]]]
        transition(tracker=tracker, id='a4f', enter='1-0')
        self.assertEqual(tracker,[[[],[],[],[]],[[],[],[],[]],[[],[],[],[]]])
        print()


if __name__ == '__main__':
    with open('test.txt', "w") as f:
        runner = unittest.TextTestRunner(f)
        unittest.main(testRunner=runner)
