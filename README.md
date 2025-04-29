# 🧩 Validador de Bandeira de Cartão de Crédito

Projeto em Python que identifica a bandeira de um cartão de crédito com base nos prefixos e no comprimento do número informado.

# 📄 Sobre o Código

O script possui a função principal validar_bandeira_cartao(numero_cartao), que executa a identificação da bandeira de acordo com as seguintes etapas:

# Conversão do Número

O número informado é convertido para str para facilitar a verificação de prefixos.

# Configuração das Regras

Um dicionário bandeiras armazena:

--Lista de prefixos válidos para cada bandeira.

--Comprimento esperado para o número do cartão.

# Validação

Para cada bandeira:

--Verifica se o número do cartão começa com algum prefixo associado.

--Confere se o comprimento do número corresponde ao esperado.

# Retorno

--Caso uma bandeira seja identificada corretamente, retorna:
Bandeira: Nome da bandeira

--Caso contrário, retorna:
"Bandeira desconhecida ou número inválido."

--Execução Direta
Quando executado como script:

  --Solicita a entrada do número do cartão via terminal.

  --Valida se a entrada contém apenas dígitos.

  --Imprime o resultado da validação.

# Tratamento de Erros

Erros inesperados são capturados e exibidos de forma amigável para o usuário.

# 🛠️ Tecnologias Utilizadas

Linguagem: Python 3.x

# 📑 Estrutura da Função Principal

--

def validar_bandeira_cartao(numero_cartao):

    # Converte número para string
    
    # Define dicionário de bandeiras com prefixos e comprimento
    
    # Para cada bandeira:
    
        # Verifica se prefixo e comprimento batem
        
        # Retorna nome da bandeira se encontrado
        
    # Retorna mensagem de erro caso não encontrado
--

# 📋 Licença

Distribuído sob a licença MIT.
