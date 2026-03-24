# isa-energia-26
PDI | RESILIÊNCIA DA TRANSMISSÃO DE ENERGIA ELÉTRICA A EVENTOS CLIMÁTICOS EXTREMOS

# Para usar o R, python

## 📊 Sobre

Este repositório fornece um ambiente de desenvolvimento para estatística e ciência de dados usando **Jupyter Notebook** com suporte ao **R**, ao **Python** e Postgres no **VS Code** através do **GitHub Codespaces**.

## 🚀 Como Usar

### Opção 1: GitHub Codespaces (Recomendado)

1. Clique no botão **Code** (verde) no topo deste repositório
2. Selecione a aba **Codespaces**
3. Clique em **Create codespace on main** (ou no branch desejado)
4. Aguarde a criação do ambiente (pode levar alguns minutos na primeira vez)
5. O ambiente será configurado automaticamente com:
   - Python e Jupyter Notebook
   - R e IRkernel (kernel R para Jupyter)
   - Pacotes R comuns para estatística (ggplot2, dplyr, tidyr, etc.)
   - Extensões do VS Code para Jupyter e R

### Opção 2: Desenvolvimento Local

Se preferir trabalhar localmente, você precisará ter o Docker instalado:

1. Clone este repositório:
   ```bash
   git clone https://github.com/FGV-Fundacao-Getulio-Vargas/Stats-In-Codespace.git
   cd Stats-In-Codespace
   ```

2. Abra no VS Code:
   ```bash
   code .
   ```

3. O VS Code detectará o arquivo `.devcontainer` e perguntará se deseja reabrir no container
4. Clique em **Reopen in Container**

## 📝 Usando Jupyter Notebooks

### No VS Code

1. Abra ou crie um arquivo `.ipynb`
2. Clique em **Select Kernel** no canto superior direito
3. Escolha o kernel conectando-se ao ambiente codespace (se estiver no codespace)
4. Abra os exemplos indicados pelo professor, compreenda e atualize conforme a sua evolução

### Via Terminal

Você também pode iniciar o Jupyter Notebook ou JupyterLab via terminal:

```bash
# Jupyter Notebook
jupyter notebook

# JupyterLab (interface moderna)
jupyter lab
```

## 📚 Exemplo

Um notebook de exemplo está incluído: `exemplo_estatistica.ipynb`

Este exemplo demonstra:
- Carregamento de bibliotecas R
- Criação de dados
- Estatísticas descritivas
- Visualização de dados com ggplot2
- Análise por grupos com dplyr

## 🔧 Pacotes R Instalados

Os seguintes pacotes R estão pré-instalados:

- **IRkernel**: Kernel R para Jupyter
- **ggplot2**: Visualização de dados
- **dplyr**: Manipulação de dados
- **tidyr**: Organização de dados
- **readr**: Leitura de dados
- **tibble**: Data frames modernos
- **stringr**: Manipulação de strings
- **forcats**: Trabalho com fatores
- **purrr**: Programação funcional

## 📦 Instalando Pacotes Adicionais

Para instalar pacotes R adicionais, ver "exemplo-de-aula.ipynb".

## 🛠️ Extensões VS Code Incluídas

- **Jupyter**: Suporte completo para notebooks Jupyter
- **Python**: Suporte para Python
- **R**: Suporte para linguagem R
- **R LSP**: Language Server Protocol para R (autocompletar, linting)

## 📖 Recursos Adicionais

- [Documentação Jupyter](https://jupyter.org/documentation)
- [Documentação R](https://www.r-project.org/)
- [IRkernel](https://irkernel.github.io/)
- [GitHub Codespaces](https://github.com/features/codespaces)


### Como fazer clone de repositório com arquivos grandes

#### Instalar Git LFS
```bash
# Ubuntu/Debian
sudo apt install git-lfs

# MacOS
brew install git-lfs

# Windows - baixar de: https://git-lfs.github.io/
```

#### Configurar Git LFS
```bash
# Inicializar Git LFS (uma vez por usuário)
git lfs install
```

#### Clonar com Git LFS
```bash
# Método padrão (mais lento)
git clone https://github.com/usuario/repositorio.git
```

#### Método otimizado (mais rápido)
git lfs clone https://github.com/usuario/repositorio.git

*Diferenças entre os Métodos*

git clone: Baixa arquivos LFS um por vez durante o checkout

git lfs clone: Baixa arquivos LFS em lote após completar o clone (muito mais rápido)


## 🤝 Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests.

## 📄 Licença

Este projeto é de código aberto e está disponível para uso educacional.



---- anexo


# Para ativar julius-code no ps1

C:\Users\julio.chaves\PycharmProjects\julius-code\.venv\Scripts\activate.ps1

# Para ativar julius-tex no ps1

C:\Users\julio.chaves\PycharmProjects\julius-tex\.venv\Scripts\activate.ps1

# Para ativar markitdown no ubuntu 24.04

source /home/juliochaves/.virtualenvs/markitdown/bin/activate

# Para ativar o vide-code
vibe
## install
curl -LsSf https://mistral.ai/vibe/install.sh | bash
uv tool install mistral-vibe

# Claude code
claude
## install
curl -fsSL https://claude.ai/install.sh | bash

# Copilot code
copilot
## install
curl -fsSL https://gh.io/copilot-install | bash