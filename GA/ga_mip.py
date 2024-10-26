from mip import Model, xsum, maximize, BINARY

def calcularLucro(profits, weights, capacity):
    print('called 2')
    item_indices = range(len(weights))  # Índices dos itens

    # Criação do modelo
    model = Model("mochila")

    # Variáveis binárias: 1 se o item é selecionado, 0 caso contrário
    selection_vars = [model.add_var(var_type=BINARY) for item_index in item_indices]

    # Função objetivo: maximizar o lucro total
    model.objective = maximize(xsum(profits[item_index] * selection_vars[item_index] for item_index in item_indices))

    # Restrição de capacidade: o peso total dos itens selecionados não pode exceder a capacidade da mochila
    model += xsum(weights[item_index] * selection_vars[item_index] for item_index in item_indices) <= capacity

    # Otimização do modelo
    model.optimize()

    # Coleta os itens selecionados
    selected_items = [item_index for item_index in item_indices if selection_vars[item_index].x >= 0.99]
    print("Itens selecionados: {}".format(selected_items))
    return selected_items