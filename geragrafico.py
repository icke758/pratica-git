from leitorarquivo import LeitorArquivo
import numpy as np
import matplotlib.pyplot as plt



def main():
    leitor = LeitorArquivo('data.txt')
    valores = leitor.getValores()
    print(valores)
    
    for serie in valores:
       plt.plot(serie)


    plt.ylabel('Valores de entrada')
    plt.xlabel('Amostragem')

    plt.title('Gráfico de linhas')

    plt.show()
    

main()