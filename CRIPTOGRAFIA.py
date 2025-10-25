from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import base64

# Gera chave AES-256 (32 bytes) para criptografia simétrica
chave = get_random_bytes(32)

def criptografar(texto):
    """
    Criptografa texto usando AES-256 no modo CBC.

    Gera IV aleatório, aplica padding PKCS7 e retorna dados cifrados
    codificados em base64 (IV + texto cifrado).
    """
    iv = get_random_bytes(16)
    cipher = AES.new(chave, AES.MODE_CBC, iv)
    cifrado = cipher.encrypt(pad(texto.encode(), AES.block_size))
    return base64.b64encode(iv + cifrado).decode()

def descriptografar(texto_b64):
    """
    Descriptografa texto previamente criptografado.

    Decodifica base64, extrai IV, descriptografa e remove padding
    para recuperar texto original.
    """
    dados = base64.b64decode(texto_b64)
    iv, cifrado = dados[:16], dados[16:]
    cipher = AES.new(chave, AES.MODE_CBC, iv)
    return unpad(cipher.decrypt(cifrado), AES.block_size).decode()
"""
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
"""
