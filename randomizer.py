#!/usr/bin/env python3
"""Консольный рандомайзер v1.3 — Zero/Pelmen_4000.
Запуск: python randomizer.py  (файлы countries.txt и ideologies.txt лежат рядом)"""
import random, pathlib
d = pathlib.Path(__file__).parent
rd = lambda f: [l.strip() for l in (d / f).read_text(encoding="utf-8").splitlines() if l.strip()]
M = "Январь Февраль Март Апрель Май Июнь Июль Август Сентябрь Октябрь Ноябрь Декабрь".split()
S = ["Лето", "Зима", "Осень", "Весна"]
C, I = rd("countries.txt"), rd("ideologies.txt")
for n in (2, 3, 4, 5, 6, 7, 8, 9, 10, 100, 1000):
    print(f"Число 1–{n}: {random.SystemRandom().randint(1, n)}")
print("Страна:", random.choice(C))
print("Идеология:", random.choice(I))
print("Сезон:", random.choice(S))
print("Месяц:", random.choice(M))
