
import unittest

from main import (
    cifra_cesar,
    cifra_substituicao,
    cifra_transposicao,
    gerar_hash,
    codificar_base64,
    decodificar_base64,
)


class TestCifraCesar(unittest.TestCase):
    
    def test_texto_vazio(self):
        self.assertEqual(cifra_cesar("", 5), "")

    def test_deslocamento_grande(self):
        self.assertEqual(cifra_cesar("ABC", 1000), "MNO")

    def test_limite_alfabetico(self):
        self.assertEqual(cifra_cesar("Z", 1), "A")
        self.assertEqual(cifra_cesar("z", 1), "a")

    def test_deslocamento_multiplo_de_26(self):
        self.assertEqual(cifra_cesar("ABCxyz", 26), "ABCxyz")

    def test_codificar_letras(self):
        self.assertEqual(cifra_cesar("ABC", 3), "DEF")

    def test_deslocamento_negativo(self):
        self.assertEqual(cifra_cesar("ABC", -3), "XYZ")

    def test_numeros(self):
        self.assertEqual(cifra_cesar("7890", 3), "0123")

    def test_preservar_caracteres(self):
        self.assertEqual(cifra_cesar("Ola, mundo! 123", 3), "Rod, pxqgr! 456")

    def test_decodificar_recupera_original(self):
        texto = "Python 123!"
        codificado = cifra_cesar(texto, 7)
        decodificado = cifra_cesar(codificado, -7)

        self.assertEqual(decodificado, texto)


class TestCifraSubstituicao(unittest.TestCase):

    def test_codificar(self):
        self.assertEqual(cifra_substituicao("OLA"), "GSQ")

    def test_descriptografar(self):
        self.assertEqual(
            cifra_substituicao("GSQ", descriptografar=True),
            "OLA"
        )

    def test_preservar_minusculas(self):
        self.assertEqual(cifra_substituicao("Ola"), "Gsq")

    def test_preservar_caracteres_especiais(self):
        self.assertEqual(
        cifra_substituicao("Olá, mundo! 123"),
        "Gsá, dxfrg! 123"
    )

    def test_recuperar_texto_original(self):
        texto = "Python 123!"
        codificado = cifra_substituicao(texto)

        decodificado = cifra_substituicao(
            codificado,
            descriptografar=True
        )

        self.assertEqual(decodificado, texto)


class TestCifraTransposicao(unittest.TestCase):

    def test_codificar(self):
        self.assertEqual(
            cifra_transposicao("ABACATE", 3),
            "ACEBAAT"
        )

    def test_descriptografar(self):
        self.assertEqual(
            cifra_transposicao("ACEBAAT", 3, descriptografar=True),
            "ABACATE"
        )

    def test_recuperar_texto_original(self):
        texto = "Olá, mundo! 123"
        codificado = cifra_transposicao(texto, 4)

        decodificado = cifra_transposicao(
            codificado, 4, descriptografar=True
        )

        self.assertEqual(decodificado, texto)

    def test_texto_vazio(self):
        self.assertEqual(cifra_transposicao("", 3), "")

    def test_colunas_invalidas(self):
        with self.assertRaises(ValueError):
            cifra_transposicao("ABACATE", 0)

    def test_mais_colunas_que_caracteres(self):
        texto = "ABC"
        codificado = cifra_transposicao(texto, 5)

        self.assertEqual(
            cifra_transposicao(codificado, 5, descriptografar=True),
            texto
        )


class TestHash(unittest.TestCase):

    def test_hash_sha256(self):
        self.assertEqual(
            gerar_hash("abc"),
            "ba7816bf8f01cfea414140de5dae2223"
            "b00361a396177a9cb410ff61f20015ad",
        )

    def test_textos_diferentes_geram_hashes_diferentes(self):
        self.assertNotEqual(gerar_hash("abc"), gerar_hash("abcd"))


class TestBase64(unittest.TestCase):

    def test_codificar(self):
        self.assertEqual(codificar_base64("Olá, mundo!"), "T2zDoSwgbXVuZG8h")

    def test_decodificar(self):
        self.assertEqual(decodificar_base64("T2zDoSwgbXVuZG8h"), "Olá, mundo!")

    def test_base64_invalido(self):
        with self.assertRaises(ValueError):
            decodificar_base64("###")


if __name__ == "__main__":
    unittest.main()
