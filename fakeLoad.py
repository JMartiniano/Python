from distutils.command.clean import clean
from time import sleep
import os

for i in range(1,100):
    print("\n\nNÃO UTILIZE O COMPUTADOR NESTE MOMENTO\n\nEstamos otimizando o seu desempenho\n\n")
    print(f"{'=' * i}{'-' * (100-i)} {i}%")
    sleep(10)
    os.system('clear')