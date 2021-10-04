from haff import Haff
import unittest


class Test_haff_1(unittest.TestCase):
    def setUp(self):
        self.big_number = 1+10**4

    def tearDown(self):
        pass

    def test_huffman_encode_values(self):
        self.assertEqual(Haff.huffman_encode(self, 'aedae'), {'e': '0', 'd': '10', 'a': '11'})
        self.assertEqual(Haff.huffman_encode(self, '12./-=/""'),
                         {'"': '00', '1': '010', '2': '011', '.': '100', '-': '101', '=': '110', '/': '111'})
        self.assertEqual(Haff.huffman_encode(self, '1111'), {'1': '0'})
        self.assertEqual(Haff.huffman_encode(self, '0'), {'0': '0'})
        self.assertEqual(Haff.huffman_encode(self, ''), {})

    def test_huffman_encode_raises(self):
        self.assertRaises(TypeError,self, Haff.huffman_encode, 1)
        self.assertRaises(TypeError,self, Haff.huffman_encode, True)
        self.assertRaises(TypeError,self, Haff.huffman_encode, [234])

    def test_huffman_encode_values_errors(self):
        self.assertRaises(ValueError, Haff.huffman_encode, self, s= '1' * self.big_number)



    def test_huffman_decode_values(self):
        self.assertEqual(Haff.huffman_decode(self, '10001111', {'2': '00', '3': '01', '1': '1'}), '123111')
        self.assertEqual(Haff.huffman_decode(self, '10111000111100010101110111011101010110000111101100',
                                             {'b': '000', 'h': '001', 'i': '01', 'u': '100', 'w': '101', 'e': '110',
                                              'f': '111'}), "wehfbwiefiewiuhfiu")

    def test_huffman_decode_raises(self):
        self.assertRaises(TypeError, Haff.huffman_decode, self, encoded='10100101', code=1)
        self.assertRaises(TypeError, Haff.huffman_decode, self, encoded=1101, code=1)



    if __name__ == '__main__':
        unittest.main()
