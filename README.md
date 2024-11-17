
# Gerador de CPF Válido em Python

Este script em Python gera números de CPF válidos com base nas regras oficiais brasileiras. Ele inclui comentários explicativos sobre cada etapa do processo.

---

## Código Completo

```python
import random

# 1. Gerar 9 dígitos aleatórios
# Aqui criamos uma lista com 9 números aleatórios (entre 0 e 9).
nove_digitos = [random.randint(0, 9) for _ in range(9)]

# 2. Calcular o primeiro dígito verificador
# Os multiplicadores são usados para calcular o primeiro dígito verificador.
multiplicadores = list(range(10, 1, -1))  # Multiplicadores de 10 a 2

# Combinar os nove dígitos e os multiplicadores com a função zip.
combinados = zip(nove_digitos, multiplicadores)

# Multiplicar cada número pelo seu respectivo multiplicador e somar os resultados.
resultado = [num * mult for num, mult in combinados]
soma = sum(resultado)

# O primeiro dígito verificador é calculado usando a fórmula: (soma * 10) % 11.
# Se o resultado for maior que 9, ele deve ser convertido para 0.
digito_1 = (soma * 10) % 11
digito_1 = digito_1 if digito_1 <= 9 else 0

# Adicionar o primeiro dígito verificador à lista original.
dez_digitos = nove_digitos + [digito_1]

# 3. Calcular o segundo dígito verificador
# Multiplicadores agora vão de 11 a 2.
multiplicadores = list(range(11, 1, -1))

# Repetimos o processo de combinação, multiplicação e soma para os dez dígitos.
combinados = zip(dez_digitos, multiplicadores)
resultado = [num * mult for num, mult in combinados]
soma = sum(resultado)

# Calcular o segundo dígito verificador com a mesma lógica.
digito_2 = (soma * 10) % 11
digito_2 = digito_2 if digito_2 <= 9 else 0

# Adicionar o segundo dígito verificador à lista.
cpf = dez_digitos + [digito_2]

# 4. Formatar o CPF para exibição
# Converter os dígitos do CPF em uma string.
cpf_str = "".join(map(str, cpf))

# Formatar a string no padrão XXX.XXX.XXX-XX.
cpf_formatado = f"{cpf_str[:3]}.{cpf_str[3:6]}.{cpf_str[6:9]}-{cpf_str[9:]}"

# Exibir o CPF gerado.
print("CPF :", cpf_formatado)
```

---

## Explicação do Código

1. **Geração dos dígitos iniciais**  
   O script cria uma lista com 9 números aleatórios entre 0 e 9, que formam a base do CPF.

2. **Cálculo do primeiro dígito verificador**  
   - Multiplica os 9 dígitos pelos multiplicadores de 10 a 2.  
   - Soma os produtos.  
   - Calcula o primeiro dígito usando a fórmula `(soma * 10) % 11`.  
   - Se o resultado for maior que 9, o dígito é ajustado para 0.

3. **Cálculo do segundo dígito verificador**  
   - Adiciona o primeiro dígito à lista.  
   - Multiplica os 10 números pelos multiplicadores de 11 a 2.  
   - Calcula o segundo dígito com a mesma fórmula do primeiro.

4. **Formatação do CPF**  
   Converte a lista de números em uma string e a formata no padrão brasileiro: `XXX.XXX.XXX-XX`.

---

## Resultado Esperado

O código gera e exibe um CPF válido. Exemplo de saída:

```
CPF : 123.456.789-09
```

---

## Requisitos

- Python 3.x

---

## Como Executar

1. Salve o código em um arquivo chamado `gerador_cpf.py`.
2. Execute o script com o comando:
   ```bash
   python gerador_cpf.py
   ```
3. O CPF gerado será exibido no console.

---

## Licença

Este projeto está sob a licença MIT. Sinta-se à vontade para usá-lo e modificá-lo.
