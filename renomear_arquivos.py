import os
import re

# --- IMPORTANTE ---
# Coloque aqui o caminho para a pasta onde estão seus arquivos PDF.
# Exemplo Windows: "C:\\Users\\SeuUsuario\\Downloads\\Livros"
# Exemplo macOS/Linux: "/home/SeuUsuario/Downloads/Livros"
PASTA_ALVO = r"C:\Users\felip\OneDrive\Desktop\Biblioteca"

def renomear_pdfs_na_pasta(caminho_pasta):
    """
    Renomeia arquivos PDF na pasta especificada, removendo o padrão 
    de timestamp (ex: _251009_103451) antes da extensão.
    """
    
    # 1. Define o padrão regex:
    # Este padrão procura por:
    #   _          (um underscore)
    #   \d{6}      (exatamente 6 dígitos)
    #   _          (outro underscore)
    #   \d{6}      (exatamente 6 dígitos)
    # O padrão é compilado para melhor performance.
    padrao_timestamp = re.compile(r'_\d{6}_\d{6}')
    
    print(f"Verificando arquivos em: {caminho_pasta}\n")
    
    try:
        # 2. Lista todos os arquivos na pasta
        for nome_arquivo in os.listdir(caminho_pasta):
            
            # 3. Separa o nome base da extensão
            nome_base, extensao = os.path.splitext(nome_arquivo)
            
            # 4. Verifica se é um PDF e se o padrão existe no nome
            if extensao.lower() == '.pdf' and padrao_timestamp.search(nome_base):
                
                # 5. Remove o padrão do nome base
                # O re.sub substitui o padrão encontrado por uma string vazia ("")
                novo_nome_base = padrao_timestamp.sub("", nome_base)
                
                # 6. Limpa espaços em branco no final (ex: "Black Hat Python ")
                novo_nome_base = novo_nome_base.strip()
                
                # 7. Monta o novo nome completo
                novo_nome_completo = f"{novo_nome_base}{extensao}"
                
                # 8. Define os caminhos completos antigo e novo
                caminho_antigo = os.path.join(caminho_pasta, nome_arquivo)
                caminho_novo = os.path.join(caminho_pasta, novo_nome_completo)
                
                # 9. Renomeia o arquivo
                if caminho_antigo != caminho_novo:
                    os.rename(caminho_antigo, caminho_novo)
                    print(f'Renomeado: "{nome_arquivo}" -> "{novo_nome_completo}"')
                else:
                    print(f'Ignorado (já no formato correto): "{nome_arquivo}"')
                    
    except FileNotFoundError:
        print(f"ERRO: A pasta '{caminho_pasta}' não foi encontrada.")
        print("Por favor, atualize a variável 'PASTA_ALVO' no script.")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

# --- Ponto de entrada do script ---
if __name__ == "__main__":
    if PASTA_ALVO == r"C:\Caminho\Para\Sua\Pasta":
        print("ERRO: Por favor, edite o script e atualize a variável 'PASTA_ALVO'...")
    else:
        renomear_pdfs_na_pasta(PASTA_ALVO)