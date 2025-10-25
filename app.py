from CRIPTOGRAFIA import criptografar, descriptografar

# Loop principal para interface interativa com usuário
while True:
    texto = input("Digite texto para criptografar (ou 'sair' para encerrar): ")

    if texto.lower() == 'sair':
        break

    if texto.strip():
        # Demonstra ciclo completo: criptografia → descriptografia
        cifrado = criptografar(texto)
        print(f"Criptografado: {cifrado}")

        original = descriptografar(cifrado)
        print(f"Original: {original}")
    else:
        print("Texto vazio!")
