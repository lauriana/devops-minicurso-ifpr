📖 GUIA NÍVEL 1: Para Coordenação do Projeto
Objetivo: Tudo aqui para apresentar a Nível 1

Tempo de leitura: 20 minutos

Antes da oficina: Leia tudo!


⏱️ TIMELINE (2 HORAS EXATAS)
0:00-0:05   | Abertura (Slide 1-2)
0:05-0:15   | Conceitos DevOps (Slide 3-5)
0:15-0:25   | Estrutura Profissional (Slide 6-8)
0:25-0:35   | Git + Versionamento (Slide 9-11)
0:35-0:45   | ☕ INTERVALO
0:45-1:00   | PRÁTICA #1: Git + Estrutura (15 min)
1:00-1:20   | PRÁTICA #2: Azure SQL (20 min)
1:20-1:45   | PRÁTICA #3: Debug VS Code (25 min)
1:45-2:00   | Resumo + Desafio


🎨 SLIDES (22 SLIDES NO TOTAL)
Use o PPTX: DevOps_Nivel_1_Python_Azure.pptx

Slides 1-2:    Título + Bem-vindo
Slides 3-5:    DevOps (conceitos)
Slides 6-8:    Estrutura profissional
Slides 9-11:   Git + Versionamento
Slide 12:      ☕ INTERVALO
Slides 13-14:  PRÁTICA #1 (objetivo)
Slides 15-16:  PRÁTICA #2 (objetivo)
Slides 17-18:  PRÁTICA #3 (objetivo)
Slides 19-20:  Resumo
Slides 21-22:  Desafio + Próximo


🎯 PRÁTICA #1: GIT + ESTRUTURA (15 MIN)
O que o aluno vai fazer
1. Criar pasta "meu-projeto"
2. cd meu-projeto
3. git init
4. Criar estrutura:
   - src/main.py
   - src/database.py
   - requirements.txt
   - .gitignore
5. git add .
6. git commit -m "Estrutura inicial"
Você mostra (Screen share)
# 1. Criar pasta
mkdir meu-projeto
cd meu-projeto

# 2. Inicializar Git
git init

# 3. Criar estrutura
mkdir src
mkdir tests

# 4. Criar arquivo de requisitos (vazio por enquanto)
touch requirements.txt
touch .gitignore

# 5. Criar arquivo principal
touch src/main.py

# 6. Adicionar tudo ao Git
git add .

# 7. Fazer primeiro commit
git commit -m "Estrutura inicial do projeto"

# 8. Ver commits
git log
O que esperar
Resultado:
meu-projeto/
├── src/
│   └── main.py
├── tests/
├── requirements.txt
├── .gitignore
└── .git/ (pasta criada por Git)

Git log mostra:
commit [XYZ]
Author: seu-nome
Date: ...
    Estrutura inicial do projeto
Se der erro
"Git não encontrado"

# Instalou Git? Testou?
git --version

"Permission denied"

# Mac/Linux
chmod +x .git/objects


🎯 PRÁTICA #2: AZURE SQL (20 MIN)
O que o aluno vai fazer
1. Conectar a Azure SQL (fornecer connection string)
2. Rodar: python main.py
3. Ver lista de produtos no console
Você mostra (Screen share)
Arquivo: src/database.py

import pyodbc

# Connection string (fornecer aos alunos)
CONNECTION_STRING = (
    "Driver={ODBC Driver 17 for SQL Server};"
    "Server=seu-servidor.database.windows.net;"
    "Database=seu-database;"
    "UID=seu_usuario;PWD=SenhaForte123!;"
    "Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30"
)

def get_connection():
    try:
        connection = pyodbc.connect(CONNECTION_STRING)
        print("✓ Conectado ao Azure SQL!")
        return connection
    except Exception as e:
        print(f"✗ Erro ao conectar: {e}")
        return None

def get_all_produtos():
    """Busca todos os produtos do banco"""
    connection = get_connection()
    if connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM Produtos")
        return cursor.fetchall()
    return []

Arquivo: src/main.py

from database import get_all_produtos

print("=" * 50)
print("PRODUTOS DO BANCO DE DADOS")
print("=" * 50)

produtos = get_all_produtos()
if produtos:
    for produto in produtos:
        print(f"ID: {produto[0]}")
        print(f"  Nome: {produto[1]}")
        print(f"  Preço: R${produto[2]:.2f}")
        print()
    print(f"Total: {len(produtos)} produtos")
else:
    print("Nenhum produto encontrado!")

Arquivo: requirements.txt

pyodbc==4.0.37
python-dotenv==0.21.0
Como executar
# 1. Ativar ambiente virtual
# Windows: venv\Scripts\activate
# Mac/Linux: source venv/bin/activate

# 2. Instalar dependências
pip install -r requirements.txt

# 3. Rodar programa
cd src
python main.py
O que esperar
==================================================
PRODUTOS DO BANCO DE DADOS
==================================================
✓ Conectado ao Azure SQL!
ID: 1
  Nome: Mouse
  Preço: R$50.00

ID: 2
  Nome: Teclado
  Preço: R$150.00

ID: 3
  Nome: Monitor
  Preço: R$800.00

Total: 3 produtos
Schema Azure SQL (que você cria antes)
CREATE TABLE Produtos (
    ID INT PRIMARY KEY IDENTITY(1,1),
    Nome VARCHAR(100),
    Preco DECIMAL(10, 2),
    DataCriacao DATETIME DEFAULT GETDATE()
);

INSERT INTO Produtos (Nome, Preco) VALUES ('Mouse', 50.00);
INSERT INTO Produtos (Nome, Preco) VALUES ('Teclado', 150.00);
INSERT INTO Produtos (Nome, Preco) VALUES ('Monitor', 800.00);
Se der erro
"ModuleNotFoundError: No module named 'pyodbc'"

# Ativar virtual environment!
# Windows: venv\Scripts\activate
# Mac/Linux: source venv/bin/activate

# Depois instalar:
pip install -r requirements.txt

"Erro ao conectar: [28000]"

Significa: Autenticação falhou

Verifique:
1. Senha está correta? (maiúsculas/minúsculas importam!)
2. Server name está correto?
3. Email/usuário correto?
4. Firewall do Azure permite seu IP?

Solução:
- Copie connection string exatamente (sem espaços)
- Teste no Azure Portal: Query editor
- Me avisa se continuar

"Nenhum produto encontrado"

Significa: Conectou, mas tabela vazia ou não existe

Verifique:
1. Tabela "Produtos" foi criada?
2. INSERT dos dados foi executado?

Teste no Query editor do Azure:
SELECT * FROM Produtos;


🎯 PRÁTICA #3: DEBUG VS CODE (25 MIN)
O que o aluno vai fazer
1. Abrir VS Code
2. Pressionar F5 (Debug)
3. Ver código rodar passo-a-passo
4. Adicionar breakpoint
5. Ver variáveis
Você mostra (Screen share)
1. Abrir VS Code com projeto

cd projeto-devops-minicurso
code .

2. Pressionar F5 (Debug)

VS Code pergunta: "Qual debugger?"
Escolha: Python
Código começa a rodar

3. Adicionar Breakpoint

Abra: src/main.py
Clique na linha do print() de Produtos
Vermelha ponto aparece (breakpoint)
F5 novamente
Código para naquela linha!

4. Comandos Debug

F5            → Continuar (play)
Shift+F5      → Parar
F10           → Step over (próxima linha)
F11           → Step into (entrar em função)
Shift+F11     → Step out (sair de função)
Ctrl+Shift+D  → Abrir Debug panel

5. Ver Variáveis

Lado esquerdo: "Variables"
Veja valor de cada variável
Enquanto está parado no breakpoint

6. Console

Abaixo: "Debug Console"
Digite: print(variável)
Ver resultado em tempo real
Exemplo prático
Arquivo src/main.py com debug:

from database import get_all_produtos

print("=" * 50)
print("PRODUTOS DO BANCO DE DADOS")
print("=" * 50)

produtos = get_all_produtos()  # ← BREAKPOINT AQUI

if produtos:
    for produto in produtos:
        print(f"ID: {produto[0]}")
        print(f"  Nome: {produto[1]}")
        print(f"  Preço: R${produto[2]:.2f}")
        print()
    
    total = len(produtos)  # ← OUTRO BREAKPOINT
    print(f"Total: {total} produtos")
else:
    print("Nenhum produto encontrado!")

Quando debugar:

F5 → Para na linha produtos = ...
Veja no "Variables" o que tem em produtos
F10 → Próxima linha
F10 → Entra no if
Veja variável total aparecer
Se der erro
"Debug não funciona"

Verificar:
1. Extensão Python instalada?
   - VS Code → Extensions
   - Procure: Python (Microsoft)
   - Está instalada?
2. Interpretador correto?
   - Ctrl+Shift+P
   - "Python: Select Interpreter"
   - Escolha o do venv

"Breakpoint não funciona"

Verificar:
1. Clicou na linha correta?
2. Ponto vermelho apareceu?
3. Pressionou F5?
4. Código chegou naquela linha?

Se não:
- Tente colocar breakpoint antes
- F5 novamente


📋 CHECKLIST PRÉ-OFICINA (Coordenação)
1 semana antes
Leia este guia (este arquivo)
Abra o PPTX: DevOps_Nivel_1_Python_Azure.pptx
Pratique as 3 práticas no seu PC
Teste: python main.py (mostra produtos?)
Teste: F5 (debug funciona?)
1 dia antes
Envie email aos alunos

Pessoal, façam o setup em casa!
Link: github.com/seu-repo/setup-inicial/
Tempo: 30 min
Me avisa quando terminar

Prepare Azure SQL (crie tabela + dados)
Prepare connection string
Dia da oficina (30 min antes)
Abra PPTX
Teste projetor (resolução OK?)
Teste som (microfone funciona?)
Abra terminal e teste:

git --version
python --version
code .

Deixe este guia aberto
Deixe VS Code aberto
Pronto!


🚨 PROBLEMAS COMUNS + SOLUÇÕES
"Python não encontrado"
# Verificar PATH
python --version

# Se não:
python3 --version

# Se continuar:
# Reinstale Python
# https://www.python.org/downloads/
# Marque "Add Python to PATH"!
"Git não encontrado"
# Reinstale
# Windows: https://git-scm.com/download/win
# Mac: brew install git
# Linux: sudo apt install git
"Erro ao conectar Azure SQL"
Erro [28000] = Autenticação falhou

Verificar:
1. Senha está correta?
2. Server name está correto?
3. Firewall permite seu IP?

Solução:
- Teste no Azure Portal (Query Editor)
- Copie connection string exatamente
- Sem espaços extras!
"ModuleNotFoundError: No module named 'pyodbc'"
# Ativar virtual environment!
# Windows: venv\Scripts\activate
# Mac/Linux: source venv/bin/activate

# Depois:
pip install -r requirements.txt
"F5 não funciona"
Verificar:
1. Extensão Python instalada?
2. Interpretador correto selecionado?
   - Ctrl+Shift+P
   - "Python: Select Interpreter"
   - Escolha venv


🎯 O QUE ALUNO APRENDE
Depois de Nível 1, aluno sabe:

✓ Estrutura profissional de projeto ✓ Git (init, add, commit) ✓ Conectar a Azure SQL ✓ Rodar Python que fala com banco ✓ Debugar código no VS Code ✓ Usar breakpoints ✓ Ver variáveis durante execução


📝 DESAFIO (SLIDE 21)
"Após a oficina, faça em casa (30 min):

Pegue um projeto Python seu (ou crie um novo: mkdir desafio-python)

Organize com estrutura profissional:

Pasta src/
Pasta tests/
requirements.txt
.gitignore

Inicialize Git:

git init
git add .
git commit -m 'estrutura'

Opcional: Conecte a um banco (Azure SQL ou até SQLite local)

Screenshot resultado

Abra GitHub → Discussions

Categoria: Nível 1 - Fundamentos
Título: 'Completei o desafio!'
Compartilhe screenshot + link repo

Me avisa quando terminar! 🎉"


📞 SUPORTE VIA GITHUB
Se aluno tiver dúvida:

Abre: github.com/seu-repo/issues
Clica: "New issue"
Escolhe: Template "Dúvida"
Descreve problema
Clica: "Submit"

Você responde em < 24h!


🎉 VOCÊ ESTÁ 100% PRONTO!
Tem: ✅ Timeline exata (2 horas) ✅ Slides prontos (22 slides) ✅ Código Python (copiar/colar) ✅ Troubleshooting (para tudo) ✅ Checklist pré-oficina ✅ Desafio para depois

Boa sorte! 🚀

