import unittest
import piecesofland

class TestLand(unittest.TestCase):

    def test_maximum_piece(self):
        actualresult=piecesofland.maximum_piece(1)
        expectedresult=1
        self.assertEquals(expectedresult,actualresult)
        
        actualresult=piecesofland.maximum_piece(2)
        expectedresult=2
        self.assertTrue(expectedresult,actualresult)
        
        actualresult=piecesofland.maximum_piece(3)
        expectedresult=4
        self.assertEquals(expectedresult,actualresult)
        
        actualresult=piecesofland.maximum_piece(4)
        expectedresult=8
        self.assertTrue(expectedresult,actualresult)
    
    
        
       
    

    

if __name__ == '__main__':
    unittest.main()        