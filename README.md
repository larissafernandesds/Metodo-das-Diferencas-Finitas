# Simulação da Distribuição de Potencial em uma Micro Linha com Condutores Longos por Diferenças Finitas

## Descrição do Código

O código `dif_finitas.py` implementa o seguinte:

1. **Definição da malha:**
   - Cria uma matriz de pontos que representam a região da micro linha.
   - Define as condições de contorno de Dirichlet (potencial fixo nas bordas e nos condutores internos).

2. **Definição das permissividades:**
   - Define as permissividades dos materiais que compõem a micro linha (ε₀ e 6ε₀).

3. **Método das diferenças finitas:**
   - Utiliza o método iterativo de Gauss-Seidel para resolver a equação de Laplace discretizada e obter a distribuição de potencial nos pontos da malha.
   - Implementa a condição de contorno de Neumann na interface entre os materiais com diferentes permissividades.

4. **Visualização dos resultados:**
   - Utiliza a biblioteca `matplotlib` para gerar um gráfico da distribuição de potencial na micro linha, mostrando as equipotenciais.

## Como Executar o Código

1. **Pré-requisitos:**
   - Python 3 instalado em seu sistema.
   - Instale as bibliotecas necessárias:
     ```bash
     pip install numpy matplotlib
     ```

2. **Execução:**
   - Salve o código `dif_finitas.py` em um diretório de sua preferência.
   - Abra um terminal e navegue até o diretório onde você salvou o código.
   - Execute o código:
     ```bash
     python dif_finitas.py
     ```

3. **Visualização:**
   - O código irá gerar um gráfico da distribuição de potencial na micro linha, mostrando as equipotenciais.
