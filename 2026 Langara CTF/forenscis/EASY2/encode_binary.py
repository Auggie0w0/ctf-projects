#!/usr/bin/env python3
"""Encode zip file: each byte → 8 bits, then 1→oui, 0→non. Output plain text .txt"""

path = "/Users/augustlam/Documents/Langara CTF/forenscis/TEHEHE/flag.png.zip"
out_path = "/Users/augustlam/Documents/Langara CTF/forenscis/EASY2/encoded.txt"

with open(path, "rb") as f:
    data = f.read()

# Each byte → 8 bits (e.g. "01010000")
binary_str = "".join(f"{b:08b}" for b in data)

# 1 → "oui", 0 → "non"
result = "".join("oui" if bit == "1" else "non" for bit in binary_str)

with open(out_path, "w", encoding="utf-8") as f:
    f.write(result)

print(f"Encoded {len(data)} bytes -> {len(result)} chars -> {out_path}")
