# Renomeador-de-Arquivos
Renomeador de Arquivos em Massa
Um script Python simples, mas poderoso, para automatizar a renomeação de múltiplos arquivos em um diretório. Perfeito para limpar bibliotecas de documentos, organizar fotos ou padronizar seus arquivos de projeto.

O Problema
Muitas vezes, baixamos arquivos (artigos, livros, imagens) que vêm com nomes confusos, cheios de carimbos de data/hora, números de versão ou outros padrões indesejados. Renomear centenas de arquivos manualmente é tedioso e sujeito a erros.

Exemplo de nomes bagunçados:

Black Hat Python_251009_112521.pdf

Aprenda_SQL_[v2]_final_251103_143451.pdf

IMG_8901_timestamp_167888.jpg

A Solução
Este script automatiza o processo. Ele varre uma pasta-alvo e usa Expressões Regulares (Regex) para encontrar e remover (ou substituir) padrões específicos nos nomes dos arquivos.

Após o script, os nomes ficam limpos:

Black Hat Python.pdf

Aprenda_SQL_[v2]_final.pdf

IMG_8901.jpg

Funcionalidades
Rápido: Processa centenas de arquivos em segundos.

Poderoso: Usa Regex, permitindo que você defina regras de renomeação complexas (remover números, datas, adicionar prefixos, etc.).

Fácil de Configurar: Você só precisa editar duas variáveis no script para começar.

Seguro: O script (atualmente) foca em arquivos .pdf, mas pode ser facilmente alterado para qualquer tipo de arquivo.

Como Usar
1. Requisitos
Python 3.x instalado.

Nenhuma biblioteca externa é necessária (usa apenas os e re).

2. Configuração
Antes de executar, abra o arquivo .py do script em um editor de texto e configure as duas variáveis principais no topo do arquivo:

Python

# 1. Defina o caminho para a pasta que contém os arquivos
PASTA_ALVO = r"C:\Caminho\Completo\Para\Sua\Pasta\De_Livros"

# 2. Defina o padrão (Regex) que você quer REMOVER
# O exemplo abaixo remove padrões como "_123456_123456"
PADRAO_REGEX = re.compile(r'_\d{6}_\d{6}')
Nota sobre o PADRAO_REGEX: Esta é a parte mais importante. re.compile(r'_\d{6}_\d{6}') é uma expressão regular que significa: "encontre um texto que comece com _, seguido por 6 dígitos, seguido por outro _, e finalizado por mais 6 dígitos". Você pode alterar isso para qualquer padrão que precisar.

3. Execução
Abra seu terminal (Prompt de Comando, PowerShell, etc.).

Navegue até a pasta onde você salvou o script:

Bash

cd C:\Caminho\Para\O\Script
Execute o script com Python:

Bash

python nome_do_seu_script.py
O script irá imprimir no terminal todos os arquivos que foram renomeados.

⚠️ Aviso Importante
Este script altera permanentemente os nomes dos seus arquivos. A ação de renomear não pode ser desfeita facilmente (não há "Ctrl+Z").

FAÇA UM BACKUP da sua pasta ou teste o script em uma pasta de cópia antes de executá-lo em seus dados importantes.

Use por sua conta e risco.

