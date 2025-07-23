import nashpy as nash
import numpy as np

attack_strategies = ["Phishing", "DoS"]
defense_strategies = ["Treinar usuários", "Firewall avançado"]

attacker_payoffs = np.array(
    [
        [3, 1],
        [2, 0],
    ]
)

game = nash.Game(attacker_payoffs, -attacker_payoffs)

print(attacker_payoffs)

print("\n🔍 Procurando equilíbrios de Nash (estratégias mistas):\n")
equilibria = list(game.support_enumeration())

for eq in equilibria:
    attacker_strategy, defender_strategy = eq
    print("Estratégia do Atacante:")
    for i, prob in enumerate(attacker_strategy):
        print(f"  {attack_strategies[i]}: {prob:.2f}")
    print("Estratégia do Defensor:")
    for i, prob in enumerate(defender_strategy):
        print(f"  {defense_strategies[i]}: {prob:.2f}")
    print("—" * 40)
