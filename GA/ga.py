import random

# Função para calcular o lucro (fitness)
def calcula_lucro(materias_primas, receita, custos):
    lucro = receita - sum([materias_primas[i] * custos[i] for i in range(len(materias_primas))])
    return lucro

# Função para criar um indivíduo (solução)
def criar_individuo(num_materias_primas):
    # Cada indivíduo é representado pela quantidade de matérias-primas utilizadas
    return [random.randint(1, 100) for _ in range(num_materias_primas)]

# Função para criar uma população inicial
def criar_populacao(tamanho_populacao, num_materias_primas):
    return [criar_individuo(num_materias_primas) for _ in range(tamanho_populacao)]

# Função de seleção de indivíduos com base no lucro (fitness)
def selecao(populacao, receita, custos):
    # Ordenar a população por lucro (fitness)
    populacao.sort(key=lambda individuo: calcula_lucro(individuo, receita, custos), reverse=True)
    # Selecionar os melhores 50%
    return populacao[:len(populacao) // 2]

# Função de cruzamento (crossover)
def crossover(individuo1, individuo2):
    ponto_corte = random.randint(1, len(individuo1) - 1)
    filho1 = individuo1[:ponto_corte] + individuo2[ponto_corte:]
    filho2 = individuo2[:ponto_corte] + individuo1[ponto_corte:]
    return [filho1, filho2]

# Função de mutação
def mutacao(individuo, taxa_mutacao=0.01):
    if random.random() < taxa_mutacao:
        posicao = random.randint(0, len(individuo) - 1)
        individuo[posicao] = random.randint(1, 100)  # Novos valores aleatórios para mutação
    return individuo

# Função principal do algoritmo genético
def algoritmo_genetico(tamanho_populacao, num_materias_primas, receita, custos, num_geracoes):
    populacao = criar_populacao(tamanho_populacao, num_materias_primas)

    for geracao in range(num_geracoes):
        # Seleção
        populacao = selecao(populacao, receita, custos)
        
        # Reprodução (crossover)
        nova_populacao = []
        while len(nova_populacao) < tamanho_populacao:
            pais = random.sample(populacao, 2)
            filhos = crossover(pais[0], pais[1])
            nova_populacao.extend(filhos)
        
        # Mutação
        populacao = [mutacao(individuo) for individuo in nova_populacao]
        
        # Avaliar o melhor indivíduo da geração atual
        melhor_individuo = max(populacao, key=lambda ind: calcula_lucro(ind, receita, custos))
        melhor_lucro = calcula_lucro(melhor_individuo, receita, custos)
        
        print(f'Geração {geracao + 1}: Melhor lucro = {melhor_lucro}')

    # Melhor solução final
    melhor_individuo_final = max(populacao, key=lambda ind: calcula_lucro(ind, receita, custos))
    return melhor_individuo_final, calcula_lucro(melhor_individuo_final, receita, custos)

# Parâmetros do problema
num_materias_primas = 5  # Número de matérias-primas
custos = [5, 10, 7, 8, 9]  # Custos das matérias-primas
tamanho_populacao = 80  # Tamanho da população
num_geracoes = 3  # Número de gerações
receita = 1000  # Receita obtida pela venda do produto

# Executar o algoritmo genético
melhor_solucao, melhor_lucro = algoritmo_genetico(tamanho_populacao, num_materias_primas, receita, custos, num_geracoes)
print(f'Melhor solução: {melhor_solucao}, Melhor lucro: {melhor_lucro}')
