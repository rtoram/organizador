import os
import shutil

# Configuração das pastas (usuário deve ajustar esses caminhos)
pasta_entrada = "./Entrada"  # Pasta onde estão os arquivos bagunçados
pastas_destino = {
    "Documentos": "./Organizado/Documentos",
    "Fotos": "./Organizado/Fotos",
    "Outros": "./Organizado/Outros"
}

# Criar pastas de destino, se não existirem
for pasta in pastas_destino.values():
    os.makedirs(pasta, exist_ok=True)

# Função para categorizar arquivos
def categorizar_arquivo(arquivo):
    if arquivo.endswith((".jpg", ".png", ".jpeg")):
        return "Fotos"
    elif arquivo.endswith((".pdf", ".docx", ".txt")):
        return "Documentos"
    else:
        return "Outros"

# Organizar os arquivos
for nome_arquivo in os.listdir(pasta_entrada):
    caminho_arquivo = os.path.join(pasta_entrada, nome_arquivo)
    if os.path.isfile(caminho_arquivo):
        categoria = categorizar_arquivo(nome_arquivo)
        destino = pastas_destino[categoria]
        shutil.move(caminho_arquivo, destino)
        print(f"Movido '{nome_arquivo}' para '{categoria}'")

print("Organização concluída!")
