# Conexão com firebird

> Tutorial explicando como conectar com o banco de dados firebird

## Configurações do ambiente
- Sistema Operacional: Linux
- Versão do Firebird: 2.5

### Criar docker:

``` bash
docker run -d --name firebird -p 3050:3050 -v firebird-data:/firebird/data -e "ISC_PASSWORD=masterkey" jacobalberty/firebird:2.5-ss
``` 

### Copiar o banco para o container

``` bash
docker cp <LOCAL_BANCO> firebird:/firebird/data
```

### Instalar cliente para Linux:

``` bash
sudo apt update
sudo apt install libfbclient2
```

### Exemplo de conexão com Python:

``` python
import fdb

consulta = "SELECT * FROM PRODUTO"

def conectar_banco(tipo_banco, nome_banco, porta=None):
    # Função fictícia para simular a conexão com o banco de dados
    if tipo_banco == 'firebird':
        return fdb.connect(
                host='localhost',
                port=porta,
                database=nome_banco,
                user='SYSDBA',
                password='masterkey',
                charset='WIN1252'
            )
    else:
        raise ValueError("Tipo de banco não suportado")

try:
    conexao = conectar_banco('firebird', '/firebird/data/unifar.fdb', porta=3050)
    print('Conexão estabelecida com sucesso')

    cursor = conexao.cursor()
    cursor.execute(consulta)
    resultados = cursor.fetchall()
    print(f"Resultados da consulta: {resultados}")
except Exception as e:
    print(f"Erro: {e}")
```