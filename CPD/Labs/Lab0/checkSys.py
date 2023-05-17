# Computação Paralela e Distribuída 2022/2023
# Aluno: João Capelas
# Número: 201901812
# Turma: 
#############################################

# A) - O que faz o import?
## R : Importa módulos de outras máquinas (bibliotecas), desta maneira tendo acesso ao código para utilizar no próprio código.

# B) - quais são algumas funcionalidades dos módulos importados?
## R : O módulo "platform" disponibiliza várias funções relativas a obter informação sobre a arquitetura do sistema.
##     O módulo "subprocess" permite criar novos processos e gerir os mesmos.

# C) - o que faz a função str ( ) ?
## R : A função "str" converte o valor dado por parâmetro numa String.

# D) - o que faz o método strip( ) ?
## R : Remove espaços no início e fim de uma String por defeito, embora dando um parâmetro ele retira os caracteres dado por parâmetro, parecido à função "trim" do Java.


# Importa os módulos necessários para verificar as características da máquina a correr o script
import platform, subprocess

# Definição da função para saber as características da máquina
def get_processor_info():
    # Caso o sistema operativo seja Windows
    if platform.system() == "Windows":
        return platform.processor()
    # Caso o sistema operativo seja Mac
    elif platform.system() == "Darwin":
        return subprocess.check_output(['/usr/sbin/sysctl', "-n", "machdep.cpu.brand_string"]).strip()
    # Caso o sistema operativo seja Linux
    elif platform.system() == "Linux":
        command = "cat /proc/cpuinfo | grep name | cut -d ' ' -f 3-8"
        return str(subprocess.check_output(command, shell=True)).strip("b'\\n")
    return ""

# Fazer print na consola do resultado da função "get_processor_info"
if __name__ == '__main__':
    print(get_processor_info())
