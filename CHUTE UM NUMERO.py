print("""
CHUTE UM NUMERO
CRIAR UM ALGORITIMO QUE GERA UM VALOR ALATÓRIO
E O USUARIO DEVE FICAR TENTANDO ATÉ ACERTAR
""")
#
print(50 * "=")  
#  
# Importe a  Biblioteca que gera Valors aleatórios 
import random
class ChuteONumero:
    def __init__(self):
        self.valor_aleatorio = 0
        self.valor_minimo  = 1 
        self.valor_maximo = 100
        self.tentar_novamente = True
           
    
    def Iniciar(self):
        self.GerarValorAleatorio()
        self.PedirValorAleatorio()
        self.tentar_novamente == True
            valor_do_chute = input("Chute um numero ")
            if int(self.valor_do_chute) > self.valor_aleatorio:
                print("Chute um valor mais baixo")
                self.PedirValorAleatorio()
            elif int(self.valor_do_chute) <  self.valor_aleatorio:   
                print("Chute um valor mais alto")
                self.PedirValorAleatorio()
            if self.valor_do_chute == self.valor_aleatorio:
                self.tentar_novamente = False
                print("Parabens voce Acertou")
    
    def GerarValorAleatorio(self):
        self.valor_aleatorio = random.randint(self.valor_minimo,self.valor_maximo)


chute= ChuteUmNumero()
chute.Iniciar()
 
            