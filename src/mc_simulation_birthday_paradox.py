import random


def has_duplicate_birthdays(group_size):
    birthdays = set()
    for _ in range(group_size):
        birthday = random.randint(1, 365)
        if birthday in birthdays:
            return True
        birthdays.add(birthday)
    return False


def birthday_paradox_simulation(group_size, num_simulations=10000):
    count = 0
    for _ in range(num_simulations):
        if has_duplicate_birthdays(group_size):
            count += 1
    probability = count / num_simulations
    return probability


group_size = 23
estimated_probability = birthday_paradox_simulation(group_size)
print(
    f"Probabilidade estimada de pelo menos duas pessoas compartilharem o aniversário (grupo de {group_size}): {estimated_probability:.4f}"
)
