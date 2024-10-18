import utilidades
import unittest


class TestUtilidades(unittest.TestCase):
    def test_es_primo(self):
        self.assertFalse(utilidades.es_primo(1))
        self.assertFalse(utilidades.es_primo(4))
        self.assertTrue(utilidades.es_primo(2))
        self.assertTrue(utilidades.es_primo(3))
        self.assertFalse(utilidades.es_primo(8))
        self.assertFalse(utilidades.es_primo(10))
        self.assertTrue(utilidades.es_primo(7))
        self.assertEqual(utilidades.es_primo(-3), "Los números negativos no están permitidos")


if __name__ == '__main__':
    unittest.main()