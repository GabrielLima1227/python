tabela_brasileirao_2025 = ("Botafogo", "Palmeiras", "Flamengo", "Fortaleza", "Internacional", "São Paulo", "Corinthians", "Bahia", "Cruzeiro", "Vasco", "Vitória", "Atlético-MG", "Fluminense", "Grêmio", "Juventude", "Red Bull Bragantino", "Santos", "Mirassol", "Sport", "Ceará")

print(f"Lista dos times do Brasileirão {tabela_brasileirao_2025}")
print(f"Os primeiros 5 times da tabela são {tabela_brasileirao_2025[0:5:1]}")
print(f"Os últimos 4 times da tabela são {tabela_brasileirao_2025[-4::1]}")
print(f"Times do Brasileirão em ordem alfabetica {sorted(tabela_brasileirao_2025)}")
print(f"O time do Flamengo está na {tabela_brasileirao_2025.index("Flamengo") + 1}º posição")