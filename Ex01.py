def remove_whitespace(phrase):
    return [char for char in phrase if not char.isspace()]

phrase = "Sítio do pica-pau amarelo \n 2023"
resultado = remove_whitespace(phrase)

print(resultado)