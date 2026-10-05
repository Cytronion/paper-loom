"""Weave a BCA question paper with unit quotas and a difficulty arc."""

from __future__ import annotations

import random

BANK = [
    {"id": "DS1", "unit": "DS", "level": 1, "q": "State the difference between a stack and a queue with one use of each."},
    {"id": "DS2", "unit": "DS", "level": 2, "q": "Insert the keys 14, 9, 22, 3 into an empty BST and write the inorder walk."},
    {"id": "DS3", "unit": "DS", "level": 3, "q": "Compare adjacency list and matrix for a sparse graph of 10,000 nodes."},
    {"id": "DB1", "unit": "DBMS", "level": 1, "q": "Define a candidate key and a foreign key in one line each."},
    {"id": "DB2", "unit": "DBMS", "level": 2, "q": "Normalize the given order table (order_id, customer, product, city) to 3NF."},
    {"id": "DB3", "unit": "DBMS", "level": 3, "q": "Why can a schedule be serializable and still deadlock? Give a two-transaction case."},
    {"id": "OS1", "unit": "OS", "level": 1, "q": "Name the three process states used in a simple five-state model."},
    {"id": "OS2", "unit": "OS", "level": 2, "q": "Compute average waiting time for SJF on bursts 6, 2, 8, 3."},
    {"id": "OS3", "unit": "OS", "level": 3, "q": "Explain thrashing and one change that reduces it without buying RAM."},
    {"id": "CN1", "unit": "CN", "level": 1, "q": "Which OSI layer decides the route, and which one checks the frame?"},
    {"id": "CN2", "unit": "CN", "level": 2, "q": "A /26 network starts at 192.168.4.0. List the first and last usable hosts."},
    {"id": "CN3", "unit": "CN", "level": 3, "q": "Why does TCP use both a sequence number and a window, not just one?"},
]

ARC = [1, 1, 2, 3, 2, 2]


def weave(bank: list[dict], length: int = 6, seed: int = 7) -> list[dict]:
    rng = random.Random(seed)
    pool = bank[:]
    rng.shuffle(pool)
    units = sorted({q["unit"] for q in bank})
    used = {unit: 0 for unit in units}
    paper = []
    for slot in range(length):
        want = ARC[slot] if slot < len(ARC) else 2
        previous = paper[-1]["unit"] if paper else None
        short = [unit for unit, count in used.items() if count == 0]
        def legal(q):
            if previous and q["unit"] == previous:
                return False
            if short and q["unit"] not in short and len(paper) < len(units):
                return False
            return True
        ranked = sorted(pool, key=lambda q: (not legal(q), abs(q["level"] - want), rng.random()))
        pick = next(q for q in ranked if legal(q) or True)
        # Prefer a legal pick. Fall back only if the bank cannot satisfy the slot.
        legal_picks = [q for q in ranked if legal(q)]
        pick = legal_picks[0] if legal_picks else ranked[0]
        paper.append(pick)
        pool.remove(pick)
        used[pick["unit"]] += 1
    return paper


if __name__ == "__main__":
    for index, item in enumerate(weave(BANK), start=1):
        print(f"Q{index}  [{item['unit']} L{item['level']}]  {item['q']}")
