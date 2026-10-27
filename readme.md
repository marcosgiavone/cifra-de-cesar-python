# Caixa de Ferramentas de Criptografia em Python

Projeto acadêmico desenvolvido em Python para demonstrar técnicas clássicas de criptografia, codificação de dados, geração de hashes e conceitos fundamentais de segurança digital.

A aplicação funciona pelo terminal e permite que o usuário interaja com diferentes ferramentas por meio de um menu de opções.

## Objetivos

- Demonstrar o funcionamento de algoritmos clássicos de criptografia.
- Permitir a codificação e a decodificação de mensagens.
- Apresentar conceitos de hash e codificação de dados.
- Desenvolver conhecimentos de programação estruturada, validação de entradas e testes automatizados.
- Promover a conscientização sobre segurança digital e proteção da informação.

## Funcionalidades

| Ferramenta | Descrição |
|---|---|
| Cifra de César | Codifica e decodifica mensagens utilizando deslocamentos de caracteres. |
| Cifra de substituição | Substitui letras de acordo com um alfabeto alternativo. |
| Cifra de transposição | Altera a posição dos caracteres conforme a quantidade de colunas informada. |
| SHA-256 | Gera um hash hexadecimal a partir de um texto. |
| Base64 | Codifica e decodifica textos utilizando a representação Base64. |
| Material educativo | Apresenta explicações sobre os métodos implementados e boas práticas de segurança digital. |

## Tecnologias utilizadas

- **Python:** linguagem utilizada no desenvolvimento.
- **hashlib:** biblioteca padrão utilizada para gerar hashes SHA-256.
- **base64:** biblioteca padrão utilizada para codificação e decodificação Base64.
- **unittest:** biblioteca padrão utilizada para executar testes automatizados.

Não é necessário instalar bibliotecas externas para executar as funcionalidades implementadas.

## Requisitos

- Python instalado no computador.
- Terminal ou PowerShell para executar o programa.

## Como executar

1. Faça o download ou clone o repositório.
2. Abra o terminal na pasta raiz do projeto, onde está localizado o arquivo `main.py`.
3. Execute o comando:

```bash
python main.py
```

Em alguns ambientes Windows, também pode ser utilizado:

```bash
py main.py
```

Após a execução, o menu principal será exibido. Digite o número correspondente à ferramenta desejada e siga as instruções apresentadas na tela.

## Exemplos de utilização

### 1. Cifra de César

**Entrada:**

```text
Mensagem: ABC
Deslocamento: 3
```

**Resultado:**

```text
DEF
```

A decodificação pode recuperar a mensagem original utilizando o deslocamento inverso.

### 2. Cifra de substituição

**Entrada:**

```text
OLA
```

**Resultado:**

```text
GSQ
```

A operação inversa utiliza o alfabeto original e o alfabeto substituto para recuperar o texto.

### 3. Cifra de transposição

**Entrada:**

```text
Mensagem: ABACATE
Quantidade de colunas: 3
```

**Resultado:**

```text
ACEBAAT
```

A decodificação recupera a mensagem original quando utiliza a mesma quantidade de colunas.

### 4. Base64

**Entrada:**

```text
Ola
```

**Resultado:**

```text
T2xh
```

A opção de decodificação permite recuperar o texto original.

### 5. SHA-256

Ao informar um texto, o programa gera um resumo digital em formato hexadecimal.

O hash não é uma mensagem criptografada e não pode ser revertido diretamente para recuperar o texto original.

## Testes automatizados

O projeto possui testes automatizados para verificar o comportamento das funções implementadas, incluindo casos válidos, limites e entradas inválidas.

Para executar os testes, utilize o terminal na pasta raiz do projeto:

```bash
python -m unittest tests.test_main -v
```

No Windows, também pode ser utilizado:

```bash
py -m unittest tests.test_main -v
```

A suíte atual contém **25 testes automatizados**, cobrindo:

- Cifra de César.
- Cifra de substituição.
- Cifra de transposição.
- Geração de hashes SHA-256.
- Codificação e decodificação Base64.

## Conceitos importantes de segurança

**Cifras clássicas:** os métodos de César, substituição e transposição possuem valor didático, mas são vulneráveis e não devem ser utilizados para proteger informações reais.

**Base64:** é uma técnica de codificação, não de criptografia. Os dados podem ser decodificados sem uma chave secreta.

**SHA-256:** é uma função de hash unidirecional. Não possui um procedimento de descriptografia que recupere diretamente a mensagem original. Para armazenar senhas, devem ser utilizadas soluções específicas de derivação de chaves, com salt e parâmetros apropriados.

Para proteger informações reais, utilize ferramentas modernas e protocolos de segurança adequados.

## Estrutura do projeto

```text
cifra-de-cesar-python/
├── main.py
├── README.md
└── tests/
    ├── __init__.py
    └── test_main.py
```

- `main.py`: contém as funções de codificação, decodificação, geração de hash, material educativo e menu principal.
- `tests/test_main.py`: contém os testes automatizados das funções implementadas.
- `README.md`: apresenta o projeto, suas funcionalidades e instruções de execução.

## Finalidade acadêmica

Este projeto tem finalidade educacional e demonstra conceitos introdutórios de programação e segurança da informação.

Ele não substitui ferramentas profissionais de criptografia nem deve ser utilizado como mecanismo de proteção de dados sensíveis.

## Autor

**Marcos Giavone**

Projeto acadêmico — Python e Segurança Digital.
