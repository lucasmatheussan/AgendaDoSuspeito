'''
@author Lucas Matheus Santos Andrade,
Projeto de cobate ao crime organizado da disciplina Introdução a programação - UFRPE,

programa em Python para auxiliar à polícia no
combate ao crime organizado. A polícia possui uma ferramenta de software que é capaz de
extrair informações dos smartphones, mesmo que estejam criptografadas, e salvam em um
arquivo texto para que sejam analisadas pelos agentes. Como o objetivo da polícia é
descobrir quem são os integrantes das quadrilhas, as ferramentas extraem os dados de
diversos celulares em conjunto e os disponibilizam em um mesmo arquivo texto para que
seja possível encontrar relações entre os números dos smartphones analisados.
'''

from Controlador import Controlador
import os
import time

class InterfaceConsole(Controlador):
    def __init__(self):
        super().__init__()

    def Limpar(self):
        if os.name == "nt":
            os.system("cls")
        else:
             os.system("clear")
    def menu(self):
        return ''' 
                    Menu:
                    1 - Ver agenda de um suspeito
                    2 - Listar agendas apenas com suspeitos incluídos
                    3 - Visualizar reciprocidades
                    4 - Visualizar contatos com alto nível de suspeição
                    5 - Adicionar agendas e chamadas
                    6 - Sair
                    Digite a opção desejada: '''

    def Art(self):
        return '''
 __ __            ___ __        __    __ __       __   __  __  __          ___     __  __  
/  /  \|\/||__) /\ | |_    /\  /  \  /  |__)||\/||_   /  \|__)/ _  /\ |\ || _/ /\ |  \/  \ 
\__\__/|  ||__)/--\| |__  /--\ \__/  \__| \ ||  ||__  \__/| \ \__)/--\| \||/__/--\|__/\__/ 
                                                                                          
                           __      __                                                     
                            _)    /  \                                                    
                           /__.   \__/                                                    
                                                                                          '''
    def opcao(self,op):
         if(op == "1"):
                self.Limpar()
                nome = input("Digite o nome que deseja pesquisar: ")
                if(self.agenda(nome) == ""):
                    print("Suspeito não encontrado")
                else:
                    print("Agenda do suspeito "+nome)
                    print(self.agenda(nome))
                time.sleep(1.2)
         elif(op == "2"):
                self.Limpar()
                print(self.ListarAgendaComSupeitos())
                time.sleep(1.2)
         elif(op == "3"):
                self.Limpar()
                print(self.reciprocidades())
                time.sleep(1.2)
         elif(op== "4"):
                self.Limpar()

                try:
                    nivel = int(input("Informe a quantidade de chamadas desejadas: "))
                    print('''Lista de reciprocidades com chamadas:
-------------------------------------
                                    ''')
                    print(self.AltoNivel(nivel))
                except:
                    print("Opção invalida!!")

                time.sleep(1.2)
         elif(op == "5"):
                self.Limpar()
                arq = input("Informe o nome do arquivo: ")
                print("Carregando o novo arquivo......")
                true = True
                time.sleep(1.0)
                if(os.path.isfile(arq)):
                     self.NovoArquivo(arq)
                     print("Dados carregados com sucesso...")
                else:
                    print("Arquivo não encontrado")
         elif(op == "6"):
                self.Limpar()
                print("Tchauuuu :(")
                return True
         else:
                self.Limpar()
                print("Entrada invalida!!")


cls = InterfaceConsole()
cls.Limpar()
while True:
        print(cls.Art())
        op = input(cls.menu().center(10))
        if(cls.opcao(op) == True):
            break



