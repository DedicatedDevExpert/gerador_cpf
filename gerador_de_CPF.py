import random
for _ in range(100):
            # Gerar 9 dígitos aleatórios e armazenar em uma lista
            nove_digitos = [random.randint(0, 9) for _ in range(9)]

            # Lista dos multiplicadores de 10 a 2 para o primeiro dígito verificador
            multiplicadores = list(range(10, 1, -1))  # [10, 9, 8, 7, 6, 5, 4, 3, 2]

            # Usando zip para combinar as listas
            combinados = zip(nove_digitos, multiplicadores)

            # Multiplicando os elementos correspondentes
            resultado = [num * mult for num, mult in combinados]
            soma = sum(resultado)

            # Calcular o primeiro dígito verificador
            digito_1 = (soma * 10) % 11
            digito_1 = digito_1 if digito_1 <= 9 else 0

            # Adicionar o primeiro dígito verificador aos nove primeiros dígitos
            dez_digitos = nove_digitos + [digito_1]

            # Lista dos multiplicadores de 11 a 2 para o segundo dígito verificador
            multiplicadores = list(range(11, 1, -1))  # [11, 10, 9, 8, 7, 6, 5, 4, 3, 2]

            # Usando zip para combinar as listas
            combinados = zip(dez_digitos, multiplicadores)

            # Multiplicando os elementos correspondentes
            resultado = [num * mult for num, mult in combinados]
            soma = sum(resultado)

            # Calcular o segundo dígito verificador
            digito_2 = (soma * 10) % 11
            digito_2 = digito_2 if digito_2 <= 9 else 0

            # Adicionar o segundo dígito verificador à lista
            cpf = dez_digitos + [digito_2]

            # Converter a lista de CPF para string para exibição
            cpf_str = "".join(map(str, cpf))

            cpf_formatado = f"{cpf_str[:3]}.{cpf_str[3:6]}.{cpf_str[6:9]}-{cpf_str[9:]}"
            print( cpf_formatado)
