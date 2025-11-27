import numpy as np
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

def draw_graph(transfers, people):
    """Draws a directed graph of who pays whom."""
    G = nx.DiGraph()
    for payer, payee, amount in transfers:
        if amount > 0:
            G.add_edge(people[payer], people[payee], weight=amount)
    pos = nx.spring_layout(G)
    fig, ax = plt.subplots()
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=10, ax=ax)
    nx.draw_networkx_edge_labels(
        G, pos, edge_labels={(u, v): f"₹{d['weight']:.2f}" for u, v, d in G.edges(data=True)}, ax=ax
    )
    plt.show()

def calculate_settlements(amounts):
    n = len(amounts)
    total = sum(amounts)
    per_head = total / n if n > 0 else 0
    # Calculate net balance for each person
    net = [amt - per_head for amt in amounts]
    # List of (index, net_balance)
    creditors = [(i, x) for i, x in enumerate(net) if x > 0]
    debtors = [(i, -x) for i, x in enumerate(net) if x < 0]
    i, j = 0, 0
    transfers = []
    while i < len(debtors) and j < len(creditors):
        debtor_idx, debt = debtors[i]
        creditor_idx, credit = creditors[j]
        pay = min(debt, credit)
        transfers.append((debtor_idx, creditor_idx, pay))
        debtors[i] = (debtor_idx, debt - pay)
        creditors[j] = (creditor_idx, credit - pay)
        if debtors[i][1] == 0:
            i += 1
        if creditors[j][1] == 0:
            j += 1
    return transfers

def main():
    print("=== FairSplit CLI ===")
    n = int(input("Enter number of people: "))
    
    people = []
    amounts = []
    
    for i in range(n):
        name = input(f"Enter name of person {i+1}: ").strip()
        if not name:
            name = f"Person {i+1}"
        while True:
            try:
                amount = float(input(f"Enter amount paid by {name}: "))
                break
            except ValueError:
                print("Invalid amount, please enter a number.")
        people.append(name)
        amounts.append(amount)
    
    if n > 1:
        total = sum(amounts)
        per_head = total / n
        print(f"\nTotal Spendings: ₹{total:.2f}")
        print(f"Per Head Expenditure: ₹{per_head:.2f}\n")
        
        transfers = calculate_settlements(amounts)
        
        if transfers:
            print("### Settlements ###")
            df = pd.DataFrame([{
                "Who Pays": people[payer],
                "To Whom": people[payee],
                "Amount": f"₹{amount:.2f}"
            } for payer, payee, amount in transfers if amount > 0])
            print(df.to_string(index=False))
        else:
            print("No settlements needed. Everyone has paid their share.")
        
        draw_graph(transfers, people)
    else:
        print("Not enough people to calculate settlements.")

if __name__ == "__main__":
    main()