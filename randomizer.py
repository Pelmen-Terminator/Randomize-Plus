#!/usr/bin/env python3
"""Консольный рандомайзер v1.4 — Zero/Pelmen_4000. Нужен words.txt рядом.
python randomizer.py            — по одному случайному слову из каждого раздела
python randomizer.py страны     — 5 случайных из раздела, название которого содержит слово"""
import random, sys, pathlib
sec, name = {}, None
for l in (pathlib.Path(__file__).parent / "words.txt").read_text(encoding="utf-8").splitlines():
    if l.startswith("## "): name = l[3:]; sec[name] = []
    elif name and l.strip() and not l.startswith("#"): sec[name].append(l.strip())
q = " ".join(sys.argv[1:]).lower()
for n, items in sec.items():
    if q and q not in n.lower(): continue
    for x in (random.sample(items, min(5, len(items))) if q else [random.choice(items)]):
        print(f"{n}: {x}")
