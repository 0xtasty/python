import random
import time


margemA = [
  "pai", "mae", "filho1", "filho2", "filha1", "filha2", "policial",
  "prisioneira"
]

margemB = []
jangada = []


#-- Printando nomes na margem

def printMargem(margem):
  tamanho = len(margem)
  i = 0
  for name in margem:
    i += 1
    print(f"~> {name}")
    if i == tamanho:
      print("\n")

#-- Verificando se há alguém habilitado para andar com a jangada
def checkJangada(potentialDrivers):
  if len(potentialDrivers) >= 1:
    if "policial" in potentialDrivers:
      return True
    elif "mae" in potentialDrivers:
      return True
    elif "pai" in potentialDrivers:
      return True
    else:
      return False
  else:
    return False


def checkIfPoliceOrPrisioner(pessoa):
  if pessoa == "policial":
    return True
  elif pessoa == "prisioneira":
    return True
  else:
    return False

def checktrue(pessoa, pessoa2):
  if pessoa in pessoa2:
    return True
  else:
    return False


def checkTransportAvailability(pessoa):
  if "mae" in pessoa and "filho1" in pessoa:
    return False
  elif "mae" in pessoa and "filho2" in pessoa:
    return False
  elif "pai" in pessoa and "filha1" in pessoa:
    return False
  elif "pai" in pessoa and "filha2" in pessoa:
    return False
  elif "mae" in pessoa and "filha1" in pessoa:
    return True
  elif "mae" in pessoa and "filha2" in pessoa:
    return True
  elif "pai" in pessoa and "filho1" in pessoa:
    return True
  elif "pai" in pessoa and "filho2" in pessoa:
    return True
  else:
    return True


def checkScenario(pessoa1, pessoa2):
  if checkJangada([pessoa1, pessoa2]):
      return True
  else:
    return False

def checkIfEqual(number1, number2):
  if number1 == number2:
    return True
  elif number2 == number1:
    return True
  else:
    return False

def checkIfItsSamePerson(nome1, nome2):
  if nome1 == nome2:
    return True
  elif nome2 == nome1:
    return True
  else:
    return False


while True:
    try:
      if len(margemA) <= 2:
        print("Agora o pai foi para margem A sozinho")
        margemB.remove("pai")
        print("Pessoas na jangada:")
        jangada.append("pai")
        printMargem(jangada)
        jangada.remove("pai")
        time.sleep(1)

        print("Agora o policial e o pai vão para margem B")
        print("Pessoas na jangada:")
        jangada.append("pai")
        jangada.append("policial")
        printMargem(jangada)
        jangada.remove("pai")
        jangada.remove("policial")
        time.sleep(1)
        margemB.append("policial")
        margemB.append("pai")
        margemA.remove("policial")
        print("O policial volta para margem A e traz a prisioneira para margem B")
        print("Pessoas na jangada:")
        jangada.append("policial")
        jangada.append("prisioneira")
        printMargem(jangada)
        jangada.remove("prisioneira")
        jangada.remove("policial")
        time.sleep(1)
        margemA.append("policial")
        margemB.append("prisioneira")
        margemB.append("policial")
        margemA.remove("policial")
        margemA.remove("prisioneira")

        print("\n\nFIM\n\n")
        print("Todos passaram, cumprindo todas as condicionais")
        print("Margem A:")
        printMargem(margemA)
        print("Margem B:")
        printMargem(margemB)
        
        break
      
      atravessando1 = random.randint(0, len(margemA))
      atravessando2 = random.randint(0, len(margemA))
      while checkIfEqual(atravessando1,atravessando2):
        atravessando1 = random.randint(0, len(margemA))
        atravessando2 = random.randint(0, len(margemA))
        time.sleep(1)
    
    
      if atravessando1 >= len(margemA):
        atravessando1 = random.randint(0, len(margemA))
      if atravessando2 >= len(margemA):
        atravessando2 = random.randint(0, len(margemA))
    
      
      pessoa1 = margemA[atravessando1]
      pessoa2 = margemA[atravessando2]
    
      while pessoa1 == pessoa2:
        try:
          atravessando1 = random.randint(0, len(margemA))
          atravessando2 = random.randint(0, len(margemA))
          pessoa1 = margemA[atravessando1]
          pessoa2 = margemA[atravessando2]
          time.sleep(1)
        finally:
          break
    
      while checkIfItsSamePerson(pessoa1, pessoa2):
        try:
          atravessando1 = random.randint(0, len(margemA))
          atravessando2 = random.randint(0, len(margemA))
          pessoa1 = margemA[atravessando1]
          pessoa2 = margemA[atravessando2]
        finally:
          break
    
    
      pessoa1 = margemA[atravessando1]
      pessoa2 = margemA[atravessando2]
    
      while checkIfPoliceOrPrisioner(pessoa1):
        valor = random.randint(0, len(margemA))
        if valor >= len(margemA):
          continue
        else:
          pessoa1 = margemA[valor]
        time.sleep(1)
    
      while checkIfPoliceOrPrisioner(pessoa2):
        valor = random.randint(0, len(margemA))
        if valor >= len(margemA):
          continue
        else:
          pessoa2 = margemA[valor]
        time.sleep(1)
    
      while pessoa1 == pessoa2:
        try:
          atravessando1 = random.randint(0, len(margemA))
          atravessando2 = random.randint(0, len(margemA))
          pessoa1 = margemA[atravessando1]
          pessoa2 = margemA[atravessando2]
          time.sleep(1)
        finally:
          break
          
      print(f"Escolhidos para atravessar: {pessoa1} e {pessoa2}")
      if checkTransportAvailability([pessoa1,pessoa2]):
        if checkScenario(pessoa1, pessoa2):
          print("Pessoas na jangada:")
          jangada.append(pessoa1)
          jangada.append(pessoa2)
          printMargem(jangada)
          jangada.remove(pessoa1)
          jangada.remove(pessoa2)          
          margemB.append(pessoa1)
          margemB.append(pessoa2)
          margemA.remove(pessoa1)
          margemA.remove(pessoa2)
          print("Pessoas na margemA:")
          printMargem(margemA)
          print("Pessoas na margemB:")
          printMargem(margemB)
        else:
          print("Não atravessou pois ninguém sabe operar a jangada")
    
      else:
        print("Não atravessou pois não atende os requisitos, gerando outros")
    
      if "pai" in margemB and "mae" in margemB:
        if "filha1" in margemA or "filha2" in margemA:
          print("Pai e mãe foram juntos, retornando um")
          margemB.remove("mae")
          margemA.append("mae")
          print("A mãe voltou a margem A")
        elif "filho1" in margemA or "filho2" in margemA:
          print("Pai e mãe foram juntos, retornando um")
          margemB.remove("pai")
          margemA.append("pai")
          print("O pai voltou a margem A")
    
    finally:
      print("")
    
