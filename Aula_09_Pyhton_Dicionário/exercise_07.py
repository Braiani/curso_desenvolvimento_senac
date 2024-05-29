print("""
Enunciado do exercício:
    7. Dicionário de Sinônimos:
      ○ Crie um dicionário com algumas palavras e seus sinônimos. Peça ao usuário para digitar uma palavra e exiba seus sinônimos.
""")

sinonimos = {
    "feliz": ["contente", "alegre", "radiante", "satisfeito"],
    "triste": ["melancólico", "deprimido", "abatido", "desolado"],
    "rápido": ["veloz", "ligeiro", "ágil", "apressado"],
    "lento": ["devagar", "moroso", "tardio", "pausado"],
    "bonito": ["belo", "formoso", "encantador", "charmoso"],
    "feio": ["horroroso", "desagradável", "repulsivo", "desprezível"],
    "rico": ["próspero", "abastado", "afortunado", "opulento"],
    "pobre": ["necessitado", "carente", "desfavorecido", "miserável"],
    "inteligente": ["perspicaz", "sagaz", "astuto", "esperto"],
    "burro": ["estúpido", "ignorante", "imbecil", "pateta"],
    "grande": ["vasto", "imenso", "amplo", "enorme"],
    "pequeno": ["minúsculo", "diminuto", "miúdo", "pequenino"],
    "forte": ["robusto", "vigoroso", "poderoso", "resistente"],
    "fraco": ["débil", "fracote", "indefeso", "vulnerável"],
    "felino": ["gato", "leão", "tigre", "onça"],
    "canino": ["cão", "cachorro", "lobo", "raposa"],
    "árvore": ["arvoredo", "floresta", "selva", "bosque"],
    "rio": ["riacho", "córrego", "torrente", "afluente"],
    "oceano": ["mar", "litoral", "golfo", "praia"],
    "montanha": ["serra", "pico", "elevação", "cume"]
}

palavra = input("Digite a palavra que deseja conhecer o significado: ").lower()

if palavra not in sinonimos:
    print()
    print("Palavra não existe em nosso dicionário.")
else:
    print()
    print(f"Os sinônimos de {palavra} são: {(", ").join(sinonimos[palavra])}")