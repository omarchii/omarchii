import random
import hashlib

# Número primo estándar de 2048 bits para Diffie-Hellman (simplificado a 256 bits para fines demostrativos)
P = 0xFFFFFFFFFFFFFFFFC90FDAA22168C234C4C6628B80DC1CD1 
G = 2  # Generador

# Generar llaves privadas de Alice, Bob y Eve
def generate_private_key():
    return random.randint(2, P-2)

# Computar la llave pública
def compute_public_key(private_key):
    return pow(G, private_key, P)

# Computar la llave secreta compartida
def compute_shared_secret(private_key, public_key):
    return pow(public_key, private_key, P)

# Función hash para derivar una clave segura
def hash_secret(secret):
    return hashlib.sha256(str(secret).encode()).hexdigest()

# Alice y Bob generan sus llaves privadas
alice_private = generate_private_key()
bob_private = generate_private_key()
eve_private = generate_private_key()

# Alice y Bob generan sus llaves públicas
alice_public = compute_public_key(alice_private)
bob_public = compute_public_key(bob_private)

# Ataque MITM: Eve intercepta y genera llaves falsas
eve_alice_public = compute_public_key(eve_private)
eve_bob_public = compute_public_key(eve_private)

# Alice envía su clave pública a Bob, pero Eve intercepta y reemplaza
# Bob envía su clave pública a Alice, pero Eve intercepta y reemplaza

# Alice y Bob calculan su llave compartida (pero en realidad se comunican con Eve)
shared_secret_alice_eve = compute_shared_secret(alice_private, eve_alice_public)
shared_secret_bob_eve = compute_shared_secret(bob_private, eve_bob_public)

# Eve calcula la misma llave compartida con Alice y Bob
hashed_secret_alice_eve = hash_secret(shared_secret_alice_eve)
hashed_secret_bob_eve = hash_secret(shared_secret_bob_eve)

# Verificación
print(f"Llave secreta entre Alice y Eve (hash): {hashed_secret_alice_eve}")
print(f"Llave secreta entre Bob y Eve (hash): {hashed_secret_bob_eve}")
print("Eve logró obtener la misma llave que Alice y Bob, permitiendo un ataque MITM.")
