import random

# Dicionário contendo possíveis personagens e suas características
personagens = {
    "guerreiro": ["forte", "bravo", "hábil com armas"],
    "mago": ["inteligente", "sábio", "domina a magia"],
    "ladino": ["astuto", "ágil", "especialista em furtividade"]
}

# Dicionário contendo possíveis locais e suas características
locais = {
    "floresta": ["densa", "misteriosa", "habitada por criaturas perigosas"],
    "montanha": ["íngreme", "coberta de neve", "habitada por gigantes"],
    "cidade": ["grande", "movimentada", "cheia de pessoas interessantes"]
}

# Dicionário contendo possíveis eventos e suas consequências
eventos = {
    "encontro com um dragão": "O personagem enfrenta o dragão em uma batalha épica.",
    "descoberta de um tesouro": "O personagem encontra um tesouro valioso.",
    "emboscada por ladrões": "O personagem é emboscado por ladrões e precisa lutar para sobreviver."
}

# Gera um personagem aleatório e uma de suas características
personagem, caracteristica_personagem = random.choice(list(personagens.items()))
caracteristica_personagem = random.choice(caracteristica_personagem)

# Gera um local aleatório e uma de suas características
local, caracteristica_local = random.choice(list(locais.items()))
caracteristica_local = random.choice(caracteristica_local)

# Gera um evento aleatório e sua consequência
evento, consequencia = random.choice(list(eventos.items()))

# Imprime a história gerada
print(f"O {personagem} {caracteristica_personagem} viaja para a {local} {caracteristica_local} e lá encontra um {evento}. {consequencia}")

# O código define as variáveis de forma semântica, além disso, 
# possui indicações do que cada parte faz (Para futuras modificações). 
# Também utiliza o formato padrão (Definir variáveis em cima e fazer as funções abaixo).