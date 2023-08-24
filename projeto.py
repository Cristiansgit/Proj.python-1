print('Bem Vindo a Nossa loja ')                
valor_produto = float(input('Digite o valor do produto : '))
qtd_produto = int(input('Digite a quantidade desejada : '))

valor_sem_frete = valor_produto * qtd_produto
valor_com_frete = 0

if qtd_produto < 11: # compra de ate 10 unidades.
  valor_com_frete = valor_sem_frete + (30.00)

elif qtd_produto >= 11 and qtd_produto < 101: # compra entre 11 e 100 unidades
  valor_com_frete = valor_sem_frete + (60.00)

elif qtd_produto >=101 and qtd_produto < 1001: # compra entre 101 e 1000 unidades
  valor_com_frete = valor_sem_frete + (120.00)

else: # compra acima de 1001 unidades
  valor_com_frete = valor_sem_frete +240

print ('o valor total com frete e de R$: {:.2f}  ' .format(valor_com_frete))
print ('o valor total sem frete e de R$: {:.2f}  '.format(valor_sem_frete))
print ('valor do frete: R$: {:.2f} : '.format (abs(valor_sem_frete - valor_com_frete)))