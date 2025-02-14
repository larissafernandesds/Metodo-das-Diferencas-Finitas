import numpy as np
import matplotlib.pyplot as plt

# Parâmetros da malha
N = 50  # Número de pontos na malha (N x N). Escolhemos N = 50 para balancear precisão e tempo de execução.
V = np.zeros((N, N))  # Matriz de potenciais. Inicialmente, todos os pontos têm potencial zero.

# Condições de contorno
V[:, 0] = 0  # Potencial na borda esquerda fixado em 0 V (condição de Dirichlet).
V[:, -1] = 0  # Potencial na borda direita fixado em 0 V (condição de Dirichlet).
V[0, :] = 0  # Potencial na borda superior fixado em 0 V (condição de Dirichlet).
V[-1, :] = 0  # Potencial na borda inferior fixado em 0 V (condição de Dirichlet).

# Condutores internos ajustados
V[20:30, 20:30] = 10  # Potencial no condutor interno 1 fixado em +10 V (condição de Dirichlet).
V[35:45, 35:45] = -10  # Potencial no condutor interno 2 fixado em -10 V (condição de Dirichlet).

# Permissividades dos materiais
epsilon = np.ones((N, N))  # Permissividade padrão (epsilon_1 = 1).
epsilon[25:35, 25:35] = 6  # Região com permissividade epsilon_2 = 6 * epsilon_1.

# Parâmetros da iteração
max_iter = 10000  # Número máximo de iterações. Escolhido para garantir que o método tenha tempo suficiente para convergir.
tolerancia = 0.01  # Tolerância para convergência. A iteração para quando a diferença máxima entre duas iterações é menor que 0.01 V.

# Método das diferenças finitas com relaxação
for k in range(max_iter):
    V_old = V.copy()  # Salva o potencial da iteração anterior para verificar a convergência.
    for i in range(1, N-1):  # Percorre os pontos internos da malha (ignorando as bordas).
        for j in range(1, N-1):
            # Mantém o potencial fixo nos condutores internos
            if 20 <= i < 30 and 20 <= j < 30:
                continue  # Condutor 1 (+10 V): não atualiza o potencial.
            if 35 <= i < 45 and 35 <= j < 45:
                continue  # Condutor 2 (-10 V): não atualiza o potencial.

            # Verifica se há mudança na permissividade (interface entre materiais)
            if (epsilon[i, j] != epsilon[i+1, j] or epsilon[i, j] != epsilon[i-1, j] or 
                epsilon[i, j] != epsilon[i, j+1] or epsilon[i, j] != epsilon[i, j-1]):
                # Continuidade do deslocamento elétrico na interface
                # A equação discretizada é ajustada para levar em conta as diferentes permissividades.
                V[i, j] = (epsilon[i+1, j] * V_old[i+1, j] + epsilon[i-1, j] * V_old[i-1, j] +
                           epsilon[i, j+1] * V_old[i, j+1] + epsilon[i, j-1] * V_old[i, j-1]) / \
                          (epsilon[i+1, j] + epsilon[i-1, j] + epsilon[i, j+1] + epsilon[i, j-1])
            else:
                # Aplica a equação de Laplace padrão (média dos vizinhos)
                V[i, j] = 0.25 * (V_old[i+1, j] + V_old[i-1, j] + V_old[i, j+1] + V_old[i, j-1])

    # Verifica a convergência
    diff = np.max(np.abs(V - V_old))  # Calcula a diferença máxima entre duas iterações.
    if diff < tolerancia:
        print(f"Convergência alcançada após {k} iterações.")
        break  # Para a iteração se a solução convergir.

# Plotagem do resultado
plt.figure(figsize=(8, 6))
plt.imshow(V, cmap='viridis', origin='lower')  # Plota a distribuição de potenciais.
plt.colorbar(label='Potencial (V)')  # Adiciona uma barra de cores para indicar o potencial.
plt.title('Distribuição de Potencial na Micro Linha')  # Título do gráfico.
plt.xlabel('x')  # Rótulo do eixo x.
plt.ylabel('y')  # Rótulo do eixo y.
plt.show()  # Exibe o gráfico.