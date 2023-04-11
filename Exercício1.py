from dataclasses import dataclass

@dataclass
class Socio:
  nome: str
  porcentagem_posse: float

def ler_socio() -> Socio:
  nome = input(f"Informe o nome: ")
  porcentagem_posse = float(input(f"Informe as porcentagens: "))
  return Socio (nome, porcentagem_posse)

def calculo(socio: Socio, valorempresa: float) -> float:
  return socio.porcentagem_posse/100 * valorempresa


socio1 = ler_socio()
socio2 = ler_socio()
socio3 = ler_socio()

empresa = float(input("Digite o valor da empresa: "))

print(f"O {socio1} terá {calculo(socio1, empresa)}% da empresa")
print(f"O {socio2} terá {calculo(socio2, empresa)}% da empresa")
print(f"O {socio3} terá {calculo(socio3, empresa)}% da empresa")
