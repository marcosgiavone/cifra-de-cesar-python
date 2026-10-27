
import base64
import hashlib


# -----------------------------
# 1. Cifra de Cesar
# -----------------------------

def cifra_cesar(texto, deslocamento):
    resultado = ""

    for char in texto:
        if "A" <= char <= "Z":
            base = ord("A")
            resultado += chr(
                (ord(char) - base + deslocamento) % 26 + base
            )

        elif "a" <= char <= "z":
            base = ord("a")
            resultado += chr(
                (ord(char) - base + deslocamento) % 26 + base
            )

        elif "0" <= char <= "9":
            base = ord("0")
            resultado += chr(
                (ord(char) - base + deslocamento) % 10 + base
            )

        else:
            resultado += char

    return resultado


# -----------------------------
# 2. Cifra de Substituicao
# -----------------------------

def cifra_substituicao(texto, descriptografar=False):
    alfabeto_original = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alfabeto_substituto = "QWERTYUIOPASDFGHJKLZXCVBNM"

    resultado = ""

    for char in texto:
        letra = char.upper()

        if letra in alfabeto_original:
            if descriptografar:
                origem = alfabeto_substituto
                destino = alfabeto_original
            else:
                origem = alfabeto_original
                destino = alfabeto_substituto

            indice = origem.index(letra)
            nova_letra = destino[indice]

            if char.islower():
                nova_letra = nova_letra.lower()

            resultado += nova_letra
        else:
            resultado += char

    return resultado


# -----------------------------
# 3. Cifra de Transposicao
# -----------------------------

def cifra_transposicao(texto, colunas, descriptografar=False):
    if colunas <= 0:
        raise ValueError(
            "A quantidade de colunas deve ser maior que zero."
        )

    if texto == "":
        return ""

    if not descriptografar:
        resultado = ""

        for coluna in range(colunas):
            for indice in range(coluna, len(texto), colunas):
                resultado += texto[indice]

        return resultado

    resultado = [""] * len(texto)
    linhas_completas = len(texto) // colunas
    resto = len(texto) % colunas

    inicio = 0

    for coluna in range(colunas):
        tamanho_coluna = linhas_completas

        if coluna < resto:
            tamanho_coluna += 1

        trecho = texto[inicio:inicio + tamanho_coluna]

        for linha, char in enumerate(trecho):
            indice_original = linha * colunas + coluna
            resultado[indice_original] = char

        inicio += tamanho_coluna

    return "".join(resultado)


# -----------------------------
# 4. Hash SHA-256
# -----------------------------

def gerar_hash(texto):
    texto_bytes = texto.encode("utf-8")
    hash_gerado = hashlib.sha256(texto_bytes).hexdigest()

    return hash_gerado


# -----------------------------
# 5. Codificacao e Decodificacao Base64
# -----------------------------

def codificar_base64(texto):
    texto_bytes = texto.encode("utf-8")
    texto_codificado = base64.b64encode(texto_bytes)

    return texto_codificado.decode("ascii")


def decodificar_base64(texto):
    texto_bytes = texto.encode("ascii")
    texto_decodificado = base64.b64decode(
        texto_bytes, validate=True
    )

    return texto_decodificado.decode("utf-8")


# -----------------------------
# 6. Material Educativo
# -----------------------------

def exibir_material_educativo():
    print("\n=== APRENDA SOBRE SEGURANCA DIGITAL ===")

    print("""
1. CIFRA DE CESAR
Substitui letras por outras deslocadas no alfabeto.
Exemplo: com deslocamento 3, ABC vira DEF.
E uma cifra classica e insegura para proteger dados reais.

2. CIFRA DE SUBSTITUICAO
Cada letra e substituida por outra letra de um alfabeto
alternativo. A mesma letra sempre recebe a mesma substituicao.
E vulneravel a analise de frequencia.

3. CIFRA DE TRANSPOSICAO
Muda a posicao dos caracteres sem substituir as letras.
A quantidade de colunas determina a organizacao da mensagem.
Esta implementacao nao adiciona caracteres artificiais.

4. SHA-256
Gera um resumo digital (hash) do texto.
E uma funcao unidirecional: nao existe uma operacao de
descriptografia que recupere diretamente a mensagem original.
SHA-256 sozinho nao e recomendado para armazenar senhas.

5. BASE64
Transforma dados em uma representacao textual.
Nao e criptografia: qualquer pessoa pode decodificar os dados.

BOAS PRATICAS DE SEGURANCA
- Use senhas longas e exclusivas.
- Ative autenticacao multifator quando disponivel.
- Desconfie de links e anexos inesperados.
- Nao compartilhe codigos de verificacao ou senhas.
- Para proteger dados reais, utilize ferramentas modernas
  e protocolos de seguranca apropriados.
""")

    print("=== EXEMPLOS PRATICOS ===")
    print("Cesar: ABC, deslocamento 3 -> DEF")
    print("Substituicao: OLA -> GSQ")
    print("Transposicao: ABACATE, 3 colunas -> ACEBAAT")
    print("Base64: Ola -> T2xh")
    print("SHA-256: gera um resumo hexadecimal do texto")


# -----------------------------
# 7. Menu Principal
# -----------------------------

def exibir_menu():
    print("\n========== CAIXA DE FERRAMENTAS ==========")
    print("1  - Codificar com Cifra de Cesar")
    print("2  - Decodificar com Cifra de Cesar")
    print("3  - Codificar com Cifra de Substituicao")
    print("4  - Decodificar Cifra de Substituicao")
    print("5  - Codificar com Cifra de Transposicao")
    print("6  - Decodificar Cifra de Transposicao")
    print("7  - Gerar hash SHA-256")
    print("8  - Codificar em Base64")
    print("9  - Decodificar Base64")
    print("10 - Material educativo e exemplos")
    print("0  - Sair")
    print("==========================================")


def main():
    while True:
        exibir_menu()
        opcao = input("Escolha uma opcao: ").strip()

        if opcao == "0":
            print("Programa encerrado. Ate mais!")
            break

        elif opcao in ("1", "2"):
            texto = input("Digite a mensagem: ")

            try:
                deslocamento = int(
                    input("Digite o deslocamento: ")
                )
            except ValueError:
                print("Erro: informe um numero inteiro.")
                continue

            if opcao == "2":
                deslocamento = -deslocamento

            resultado = cifra_cesar(texto, deslocamento)

            if opcao == "1":
                print("\nMensagem codificada:", resultado)
            else:
                print("\nMensagem decodificada:", resultado)

        elif opcao in ("3", "4"):
            texto = input("Digite a mensagem: ")

            resultado = cifra_substituicao(
                texto,
                descriptografar=(opcao == "4")
            )

            if opcao == "3":
                print("\nMensagem codificada:", resultado)
            else:
                print("\nMensagem decodificada:", resultado)

        elif opcao in ("5", "6"):
            texto = input("Digite a mensagem: ")

            try:
                colunas = int(
                    input("Digite a quantidade de colunas: ")
                )

                resultado = cifra_transposicao(
                    texto,
                    colunas,
                    descriptografar=(opcao == "6")
                )

                if opcao == "5":
                    print("\nMensagem codificada:", resultado)
                else:
                    print("\nMensagem decodificada:", resultado)

            except ValueError as erro:
                print("Erro:", erro)

        elif opcao == "7":
            texto = input("Digite o texto para gerar o hash: ")
            resultado = gerar_hash(texto)
            print("\nHash SHA-256:", resultado)

        elif opcao == "8":
            texto = input("Digite o texto para codificar: ")
            resultado = codificar_base64(texto)
            print("\nTexto em Base64:", resultado)

        elif opcao == "9":
            texto = input("Digite o texto em Base64: ")

            try:
                resultado = decodificar_base64(texto)
                print("\nTexto decodificado:", resultado)

            except (ValueError, UnicodeError):
                print(
                    "Erro: Base64 invalido ou conteudo "
                    "que nao representa texto UTF-8 valido."
                )

        elif opcao == "10":
            exibir_material_educativo()

        else:
            print("Opcao invalida. Escolha uma opcao do menu.")


if __name__ == "__main__":
    main()
