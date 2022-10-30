from ContasBancos import ContaCorrente, CartaoCredito

#Programa
conta_Lira = ContaCorrente("Lira", "436.881.198-43", 1234, 34062)

cartao_Lira = CartaoCredito("Lira", conta_Lira)

print(cartao_Lira.conta_corrente.num_conta)

print(conta_Lira.cartoes[0].numero)

print(cartao_Lira.cod_seguranca)

print(cartao_Lira.validade)

cartao_Lira.senha = "1255"
print(cartao_Lira.senha)

print(conta_Lira.__dict__)