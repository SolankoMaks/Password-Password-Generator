import random
import string

def generate_password(length):
  """Генерує випадковий пароль заданої довжини."""

  characters = string.ascii_letters + string.digits + "!@#$%^&*"
  password = ''.join(random.choice(characters) for i in range(length))
  return password

if __name__ == "__main__":
  length = int(input("Введіть бажану довжину пароля: "))
  password = generate_password(length)
  print("Згенерований пароль:", password)