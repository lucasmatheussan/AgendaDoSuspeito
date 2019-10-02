from dadosSmartphone import DadosSmartphone
class Controlador(DadosSmartphone):

    def __init__(self):
        self.listaDados = []
        self.clsDados = []
        self.__fileName ="agendasuspeitos.txt"
        self.ProcessamentoNovo()

    @property
    def getNomeArquivo(self):
        return self.__fileName
    @getNomeArquivo.setter
    def setNomeArquivo(self, arquivo):
        self.__fileName = arquivo

    def iniciar(self):
        for i in self.listaDados:
            self.clsDados.append(DadosSmartphone(i[0],i[1],i[2],i[3]))

    def agenda(self, nome):
        str=""
        for j in self.clsDados:
            if(j.getNome == nome):
                 for i in j.getContatos:
                     str+=i + "\n"
        return str
    def ListarAgendaComSupeitos(self):
        str=""
        for p in self.clsDados:
            str+=p.getNome +":"
            for i in self.clsDados:
                if(p.AcharContato(i.getNumero)):
                    str+=i.getNome+","
            str = str[:-1]
            str += "\n"
        return str[:-1]
    def reciprocidades(self):
        str=""
        lista = self.clsDados[:]
        for i in self.clsDados:
            for j in lista:
                if(i.AcharContato(j.getNumero) and j.AcharContato(i.getNumero)):
                    str+=j.getNome +"<->"+ i.getNome+"\n"
                    try:
                        lista.remove(i)
                    except:
                        ok=0
        return str[:-1]

    def AltoNivel(self,  opp):
        str = ""
        dupli = self.clsDados[:]
        lista = [[0]]
        for k, i in enumerate(dupli):
            for p, j in enumerate(self.clsDados):
                true = True
                for u in lista:
                    if (i in u and j in u):
                        true = False
                if ((i.getNumero in j.getContatos and j.getNumero in i.getContatos) and ( dupli[k].getNumero in j.getChamadas or j.getNumero in dupli[k].getChamadas) and true):
                    cont = 0
                    lista2 = [i, j]
                    lista.append(lista2)
                    for w in j.getChamadas:
                        if (dupli[k].getNumero == w):
                            cont += 1
                    for v in dupli[k].getChamadas:
                        if (v == j.getNumero):
                            cont += 1
                    if (cont >= opp):
                        str += dupli[k].getNome + "<->" + j.getNome + " (nível alto de suspeição) \n"
                    else:
                        str += (dupli[k].getNome + "<->" + j.getNome + "\n")
        return str[:-1]

    def NovoArquivo(self, fileName):
        arq = self.lerArquivo()
        abrir = open("agenda_completa.txt", "w")
        arq2 = self.leraArquivoUsuario(fileName)
        agenda1 = arq[0:arq.index("chamadas")]
        agenda2 = arq2[1:arq2.index("chamadas")]
        chamadas = arq[arq.index("chamadas"):]
        chamadas2 = arq2[arq2.index("chamadas") + 1:]
        for i in agenda1:
            abrir.write(i + "\n")
        for j in agenda2:
            abrir.write(j + "\n")
        for i in chamadas:
            abrir.write(i + "\n")
        for i in chamadas2:
            abrir.write(i + "\n")
        abrir.close()
        self.setNomeArquivo = "agenda_completa.txt"
        self.ProcessamentoNovo()

    def ProcessamentoNovo(self):
        file = open(self.getNomeArquivo, "r")
        conteudo = file.readlines()
        for i in range(len(conteudo)):
            conteudo[i] = conteudo[i].replace("\n", "")
        listaOO = []
        CorteContato = conteudo[1:conteudo.index("chamadas")]
        CorteChamadas = conteudo[conteudo.index("chamadas") + 1:]
        for j in CorteContato:
            nome = j.split("-")
            for i in CorteChamadas:
                if (nome[0] in i):
                    name = j.split("-")
                    numero = name[1].split(":")
                    contato = numero[1].split(",")
                    chamadas = i.split(":")[1].split(",")
                    listaOO.append([nome[0], numero[0], contato, chamadas])
        self.listaDados = listaOO[:]
        self.clsDados = []
        self.iniciar()

    def lerArquivo(self):
        file = open(self.getNomeArquivo, "r")
        conteudo = file.readlines()
        for i in range(len(conteudo)):
            conteudo[i] = conteudo[i].replace("\n", "")
        return conteudo
    def leraArquivoUsuario(self,filename):
        file = open(filename, "r")
        conteudo = file.readlines()
        for i in range(len(conteudo)):
            conteudo[i] = conteudo[i].replace("\n", "")
        return conteudo