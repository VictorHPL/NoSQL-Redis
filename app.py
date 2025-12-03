import redis
import time

def linha_separadora(titulo):
    print("\n" + "="*40)
    print(f" {titulo}")
    print("="*40)

def main():
    # 1. CONEXÃO
    # Conecta no Redis rodando no Docker (localhost:6379)
    # decode_responses=True faz o Redis retornar string ao invés de bytes (b'texto')
    try:
        r = redis.Redis(host='localhost', port=6379, decode_responses=True)
        # Testa a conexão
        r.ping()
        print("✅ [CONEXÃO] Sucesso! Conectado ao Redis no Docker.")
    except redis.ConnectionError:
        print("❌ [ERRO] Não foi possível conectar. Verifique se o Docker está rodando.")
        return

    # Limpa dados antigos para o teste (opcional, mas bom para apresentações)
    r.delete("usuario:100")
    
    # ---------------------------------------------------------
    # CREATE (Inserção) - Requisito do Trabalho
    # ---------------------------------------------------------
    linha_separadora("1. CREATE (Inserindo Dados)")
    print("Criando perfil de usuário para Rede Social...")
    
    # HSET é usado para criar um Hash (objeto)
    dados_usuario = {
        "nome": "Victor",
        "idade": "24",
        "curso": "Ciência da Computação",
        "status": "Online",
        "interesses": "Python, Elixir, Games"
    }
    
    r.hset("usuario:100", mapping=dados_usuario)
    print(f"Usuario criado: ID 100 -> {dados_usuario['nome']}")
    time.sleep(2) # Pausa dramática para explicação

    # ---------------------------------------------------------
    # READ (Leitura) - Requisito do Trabalho
    # ---------------------------------------------------------
    linha_separadora("2. READ (Lendo Dados)")
    print("Buscando dados do 'usuario:100' no banco...")
    
    # HGETALL pega todos os campos do hash
    resultado = r.hgetall("usuario:100")
    
    print("Dados recuperados do Redis:")
    for chave, valor in resultado.items():
        print(f" - {chave}: {valor}")
    
    time.sleep(2)

    # ---------------------------------------------------------
    # UPDATE (Atualização) - Requisito do Trabalho
    # ---------------------------------------------------------
    linha_separadora("3. UPDATE (Atualizando Dados)")
    print("Alterando status de 'Online' para 'Ocupado'...")
    
    # Basta setar novamente a chave específica
    r.hset("usuario:100", "status", "Ocupado")
    
    # Verificando a mudança
    novo_status = r.hget("usuario:100", "status")
    print(f"Novo Status no banco: {novo_status}")
    
    time.sleep(2)

    # ---------------------------------------------------------
    # DELETE (Exclusão) - Requisito do Trabalho
    # ---------------------------------------------------------
    linha_separadora("4. DELETE (Deletando Dados)")
    print("Removendo o usuário da base de dados...")
    
    r.delete("usuario:100")
    
    # Tentar buscar de novo para provar que sumiu
    verificacao = r.hgetall("usuario:100")
    if not verificacao:
        print("✅ Sucesso: O usuário foi removido e a chave não existe mais.")
    else:
        print("❌ Erro: O usuário ainda existe.")

    linha_separadora("FIM DA DEMONSTRAÇÃO")

if __name__ == "__main__":
    main()