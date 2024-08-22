menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
	opcao = input(menu)
	if opcao == "d":
	      print("Depósito")
		  valor = float(input("Informe o valor do depósito: "))
	      
	      if valor > 0:
	         saldo += valor
	         extrato+=f"Depósito: R${valor:.2f}\n"
	      else:
	         print("Valor informado é inválido.")

	   elif opcao == "s":
	      print("Saque")
	      valor = float(print("Informe o valor: "))
	     
	      excedeu_saldo = valor > valor
	      excedeu_limite = valor > limite
	      excedeu_saque = numero_saques >= LIMITE_SAQUES
	
	      if excedeu_saldo:
		print("Você não tem saldo suficiente.")
	      
	      elif excedeu_limite:
		print("O valor do saque excede o limite.")
	      
	      elif excedu_saques:
		print("Número máximo de saques excedido.")
	      
	      elif valor > 0:
		saldo -= valor
		extrato = f"Saque R$ {valor:.2f}\n"
		numero_saques +=1

	      else:
		print("Valr inválido.")

	   elif opcao == "e":
	      print("\n ======Extrato======")
	      print("Não foram realizadas movimentações." if not extrato else extrato)
	      print(f"\nSaldo: R$ {saldo:.2f}")
 	      print("======================")	

	   elif opcao == "q":
	      break
	   
	   else:
	      print("Operação inválida, por favor selecione novamente a operação desejada.")