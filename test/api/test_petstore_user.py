import pytest  # framework de teste unitario = engine
import requests  # framework de teste api = Requests/responses

# Endereço da Api

base_url = 'https://petstore.swagger.io/v2/user'  # URL Base
headers = {'Content-Type': 'application/json'}


# Os Testes

def testar_criar_usuario():
    # Configura
    status_code_esperado = 200
    codigo_esperado = 200
    tipo_esperado = "unknown"
    mensagem_esperada = '1554'

    # Executa
    resposta = requests.post(  # Faz requisição , passando: endpoint da api, o body json, o header
        url=base_url,
        data=open('C:/Users/jessi/PycharmProjects/fts132_inicial3/test/db/user1.json', 'rb'),
        headers=headers

    )

    # Formatação
    corpo_da_resposta = resposta.json()
    print(resposta)  # Resposta Bruta
    print(resposta.status_code)
    print(corpo_da_resposta)

    # Valida
    assert resposta.status_code == status_code_esperado
    assert corpo_da_resposta['code'] == codigo_esperado
    assert corpo_da_resposta['type'] == tipo_esperado
    assert corpo_da_resposta['message'] == mensagem_esperada


def testar_consultar_usuario():
    # Configura
    status_code = 200
    id = 1554
    username = 'padawan'
    firstName = 'luke'
    lastName = 'skywalker'
    email = 'luke.lightforce@teste.com.br'
    password = 'string'
    phone = '1999999999'
    userStatus = 0

    # Executa
    resposta = requests.get(f'{base_url}/{username}',
                            headers=headers

                            )

    # Formatação
    corpo_da_resposta = resposta.json()
    print(resposta)  # Resposta Bruta
    print(resposta.status_code)
    print(corpo_da_resposta)

    # Valida
    assert resposta.status_code == status_code
    assert corpo_da_resposta['id'] == id
    assert corpo_da_resposta['username'] == username
    assert corpo_da_resposta['email'] == email
    assert corpo_da_resposta['phone'] == phone


def testar_alterar_usuario():
    # Configura
    username = 'padawan'
    status_code_esperado = 200
    codigo_esperado = 200
    tipo_esperado = 'unknown'
    mensagem_esperada = '1554'

    # Executa
    resposta = requests.put(
        url=f'{base_url}/{username}',
        data=open('C:/Users/jessi/PycharmProjects/fts132_inicial3/test/db/user2.json', 'rb'),
        headers=headers
    )

    # Formatação
    corpo_da_resposta = resposta.json()
    print(resposta)
    print(resposta.status_code)
    print(corpo_da_resposta)

    # Validação
    assert resposta.status_code == status_code_esperado
    assert corpo_da_resposta['code'] == codigo_esperado
    assert corpo_da_resposta['type'] == tipo_esperado
    assert corpo_da_resposta['message'] == mensagem_esperada


def testar_excluir_usuario():
    # Configura
    username = 'padawan'
    status_code_esperado = 200
    codigo_esperado = 200
    tipo_esperado = 'unknown'
    mensagem_esperada = 'padawan'

    # Executa
    resposta = requests.delete(
        url=f'{base_url}/{username}',
        headers=headers
    )

    # Formatação

    corpo_da_resposta = resposta.json()
    print(resposta)
    print(resposta.status_code)
    print(corpo_da_resposta)

            # Validação
    assert resposta.status_code == status_code_esperado
    assert corpo_da_resposta['code'] == codigo_esperado
    assert corpo_da_resposta['type'] == tipo_esperado
    assert corpo_da_resposta['message'] == mensagem_esperada

