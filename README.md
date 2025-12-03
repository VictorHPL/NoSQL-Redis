# Projeto NoSQL - Redis (Cache de Chave-Valor)

Este projeto foi desenvolvido como requisito parcial da disciplina de Banco de Dados. [cite_start]O objetivo é demonstrar na prática o uso do **Redis** (Remote Dictionary Server), um banco de dados NoSQL do tipo **Key-Value Store**[cite: 27].

## 📚 Contexto do Trabalho

Conforme solicitado nas instruções do projeto:

* [cite_start]**Paradigma:** Cache de chave-valor (Key-value cache)[cite: 24].
* [cite_start]**SGBD Escolhido:** Redis[cite: 27].
* [cite_start]**Cenário de Aplicação:** Redes Sociais[cite: 41].
    * *Justificativa:* O Redis é ideal para armazenar sessões de usuários e perfis temporários (cache) devido à sua baixa latência, permitindo que dados como "Status Online" ou "Últimas interações" sejam acessados em milissegundos.

## 🛠️ Funcionalidades (CRUD)

[cite_start]O script `app.py` realiza as seguintes operações exigidas[cite: 45]:

1.  **Create:** Cria um perfil de usuário usando Hash (`HSET`).
2.  **Read:** Recupera os dados do perfil (`HGETALL`).
3.  **Update:** Atualiza o status do usuário (`HSET`).
4.  **Delete:** Remove o usuário do cache (`DEL`).

---

## 🚀 Guia de Instalação e Execução

Siga os passos abaixo para rodar o projeto no seu computador.

### 1) Subir o Redis com Docker
Você não precisa instalar o Redis localmente. Com o Docker instalado, rode:

```cmd
docker pull redis
docker run --name redis-projeto -p 6379:6379 -d redis
```

Para verificar se está rodando:

```cmd
docker ps
```

### 2) Preparar ambiente Python (Windows)
Crie e ative uma virtual env, depois instale dependências.

- Criar venv:

```cmd
python -m venv venv
```

- Ativar venv (CMD):

```cmd
venv\Scripts\activate.bat
```

- Ativar venv (PowerShell):

```powershell
# Necessário apenas na primeira vez
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# Ativar
.\venv\Scripts\Activate.ps1
```

- Instalar dependências:

```cmd
pip install -r requirements.txt
```

### 3) Executar a demonstração
Com o container do Redis ativo e a venv habilitada, execute:

```cmd
python app.py
```

O script conecta em `localhost:6379`, limpa dados de teste e demonstra o CRUD com hashes do Redis.

### 4) Testar conexão ao Redis (opcional)
Você pode abrir um shell do Redis para inspecionar as chaves criadas:

```cmd
docker exec -it redis-projeto redis-cli
KEYS *
HGETALL user:123
```

### Dicas e Solução de Problemas
- Redis não sobe: confirme o Docker instalado e porta `6379` livre (`docker ps`).
- Permissão no PowerShell: rode o `Set-ExecutionPolicy` mostrado acima e reabra o terminal.
- `pip`/Python incorretos: verifique versão com `python --version` e garanta que a venv está ativa.
- Conexão recusada: assegure que o container está em execução e acessível em `localhost:6379`.

## 🔧 CRUD direto no Docker (redis-cli)
Abra um shell do Redis dentro do container e execute os comandos abaixo para testar o CRUD de perfis. Use o mesmo nome de container criado acima (`redis-projeto`).

```cmd
docker exec -it redis-projeto redis-cli
```

Dentro do `redis-cli`, crie, leia, atualize e delete um usuário:

- Create (criar hash do usuário):

```text
HSET usuario:100 nome "Victor" idade "24" cidade "Fortaleza" status "Online"
```

- Read (ler todos os campos):

```text
HGETALL usuario:100
```

- Update (atualizar um campo):

```text
HSET usuario:100 status "Ocupado"
```

- Delete (remover a chave):

```text
DEL usuario:100
```

Comandos úteis adicionais:

```text
KEYS usuario:*      # listar usuários (use com cautela em produção)
HLEN usuario:100    # quantidade de campos
HEXISTS usuario:100 status  # verifica se campo existe
EXPIRE usuario:100 3600     # define TTL de 1 hora para a chave
TTL usuario:100     # tempo restante
```

Saída esperada típica:

```text
127.0.0.1:6379> HSET usuario:100 nome "Victor" idade "24" cidade "Fortaleza" status "Online"
(integer) 5
127.0.0.1:6379> HGETALL usuario:100
1) "nome"
2) "Victor"
3) "idade"
4) "24"
5) "cidade"
6) "Fortaleza"
7) "status"
8) "Online"
```






