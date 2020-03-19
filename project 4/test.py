import unittest
import game_logic
import user_interface

class TestGameLogic(unittest.TestCase):

    def test_empty(self):
        '''
        test if the game can begin with an empty field of the correct size.
        '''
        expect=[['   ', '   ', '   ', '   ', '   ', '   ', '   '], ['   ', '   ', '   ', '   ', '   ', '   ', '   '], ['   ', '   ', '   ', '   ', '   ', '   ', '   '], ['   ', '   ', '   ', '   ', '   ', '   ', '   '], ['   ', '   ', '   ', '   ', '   ', '   ', '   ']]
        self.assertEqual(expect,user_interface.empty(4,5))
    
    def test_gravity(self):
        '''
        test if the jewels will "fall" immediately to fill the empty spaces below them
        '''
        takein_list=[['   ', '   ', '   ', '   ', ' S ', ' T ', ' X '],
                     ['   ', '   ', '   ', ' Y ', '   ', ' X ', '   '],
                     ['   ', '   ', '   ', '   ', ' V ', '   ', ' X '],
                     ['   ', '   ', '   ', ' X ', '   ', ' S ', ' Y ']]
        expect=[['   ', '   ', '   ', '   ', ' S ', ' T ', ' X '],
                ['   ', '   ', '   ', '   ', '   ', ' Y ', ' X '],
                ['   ', '   ', '   ', '   ', '   ', ' V ', ' X '],
                ['   ', '   ', '   ', '   ', ' X ', ' S ', ' Y ']]
        self.assertEqual(expect,game_logic.gravity(takein_list))
        
    def test_start_game(self):
        '''
        test if it is possible to quit the program with the Q command.
        '''
        takein_list=[['   ', '   ', '   ', '   ', '   ', '   ', '   '],
                     ['   ', '   ', '   ', '   ', '   ', '   ', '   '],
                     ['   ', '   ', '   ', '   ', '   ', '   ', '   '],
                     ['   ', '   ', '   ', '   ', '   ', '   ', '   ']]
        self.assertEqual(None,user_interface.start_game(takein_list,'Q'))

    def test_is_game_over(self):
        '''
        The game ends when a faller freezes but cannot be displayed entirely in the field because it didn't move down far enough.
        '''
        takein_list1=[['   ', ' Y ', ' Y ', ' Y ', ' X ', ' X ', ' X '],
                     ['   ', '   ', '   ', '   ', '   ', '   ', '   '],
                     ['   ', '   ', '   ', '   ', '   ', '   ', '   '],
                     ['   ', '   ', '   ', '   ', '   ', '   ', '   ']]
        takein_list2=[['   ', '   ', '   ', ' X ', ' X ', ' X ', ' X '],
                     ['   ', '   ', '   ', '   ', '   ', '   ', '   '],
                     ['   ', '   ', '   ', '   ', '   ', '   ', '   '],
                     ['   ', '   ', '   ', '   ', '   ', '   ', '   ']]
        self.assertEqual(True, game_logic.is_game_over(takein_list1))
        self.assertEqual(False, game_logic.is_game_over(takein_list2))
        


if __name__ == '__main__':
    unittest.main()                

