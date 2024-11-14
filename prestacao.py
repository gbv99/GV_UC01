#Prestacao atrasada
parcela= float(input("insira valor da parcela: "))
tempo= float(input("insira o tempo em atraso (meses): "))
taxa= float(input("insira a taxa: "))
valorfinal= parcela+(parcela*(taxa/100)*tempo)
print(f"o valor final da prestação é R$ {valorfinal:.2f}")
              
              