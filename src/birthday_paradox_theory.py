def birthday_paradox_theoretical(group_size):
    probability_unique = 1.0
    for i in range(group_size):
        probability_unique *= (365 - i) / 365
    return 1 - probability_unique


group_size = 23
theoretical_probability = birthday_paradox_theoretical(group_size)
print(
    f"Probabilidade teórica de pelo menos duas pessoas compartilharem o aniversário (grupo de {group_size}): {theoretical_probability:.4f}"
)
