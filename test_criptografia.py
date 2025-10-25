import unittest
import base64
from CRIPTOGRAFIA import criptografar, descriptografar

class TestCriptografia(unittest.TestCase):
    
    def test_criptografia_descriptografia(self):
        """Testa se a criptografia e descriptografia funcionam corretamente"""
        texto_original = "Texto secreto para teste"
        
        # Criptografa
        texto_criptografado = criptografar(texto_original)
        
        # Verifica se retorna string base64
        self.assertIsInstance(texto_criptografado, str)
        
        # Descriptografa
        texto_descriptografado = descriptografar(texto_criptografado)
        
        # Verifica se o texto original é igual ao descriptografado
        self.assertEqual(texto_original, texto_descriptografado)
    
    def test_texto_vazio(self):
        """Testa com texto vazio"""
        texto_original = ""
        texto_criptografado = criptografar(texto_original)
        texto_descriptografado = descriptografar(texto_criptografado)
        self.assertEqual(texto_original, texto_descriptografado)
    
    def test_texto_longo(self):
        """Testa com texto longo"""
        texto_original = "A" * 1000  # Texto longo
        texto_criptografado = criptografar(texto_original)
        texto_descriptografado = descriptografar(texto_criptografado)
        self.assertEqual(texto_original, texto_descriptografado)
    
    def test_caracteres_especiais(self):
        """Testa com caracteres especiais"""
        texto_original = "Texto com ç, á, ã, ñ e símbolos! @#$%"
        texto_criptografado = criptografar(texto_original)
        texto_descriptografado = descriptografar(texto_criptografado)
        self.assertEqual(texto_original, texto_descriptografado)

if __name__ == '__main__':
    unittest.main()
