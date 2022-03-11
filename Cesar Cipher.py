#Esta cifra foi (provavelmente) inventada e usada por Caio Júlio César e suas tropas durante as Guerras Gálicas.
# A ideia é bastante simples - cada letra da mensagem é substituída pela sua consequente mais próxima
# (A torna-se B, B torna-se C, e assim por diante). A única exceção é Z, que se torna A.
text = input('Enter your message: ')
cipher = ''
for char in text:
    if not char.isalpha():
        continue
    char = char.upper()
    code = ord(char) + 1
    if code > ord('Z'):
        code = ord('A')
    cipher += chr(code)

print(cipher)