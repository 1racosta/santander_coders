from datetime import datetime, date
from typing import List

#### PENDENCIAS ####
## Relatório de fim do dia:
### VENDAS
# RELATORIO DE VENDAS
# QUANTIDADE DE VENDAS NO DIA (DIA É QUANDO ABRE O PROGRAMA ATÉ FECHAR)
# QUANTIDADE DE PESSOAS DIFERENTES ANTENDIDAS
# QTD REMEDIOS FISIO VENDIDOS
# QTD REMEDISO QUIMIO VENDIDOS

### MEDICAMENTOS
## BUSCA POR NOME, FABRICANTE OU ??DESCRICAO PARCIAL?? -- if in :

class Clientes:
    clientes = []
    cpfs_utilizados: List[str] = []

    def __init__(self, cpf: str, nome: str, data_nascimento: date):
        if self.cpf_utilizado(cpf):
            return
        else:
            self.adicionar_cpf(cpf)
        self._cpf = cpf
        self.nome: str = nome
        self.data_nascimento: date = data_nascimento
        self._idade = int((date.today() - datetime.strptime(data_nascimento, "%Y-%m-%d").date()).days / 365)
    
    @classmethod
    def relatorio_cliente(cls):
        clientes_ordenados = sorted(Clientes.clientes, key=lambda cliente: cliente.nome)
        for cliente in clientes_ordenados:
            print(f"Nome: {cliente.nome}, CPF: {cliente._cpf}, Data de Nascimento: {cliente.data_nascimento}")

              
    @classmethod
    def cpf_utilizado(cls, cpf: str) -> bool:
        if cpf in cls.cpfs_utilizados:
            print('CPF já cadastrado: ', cpf)
            return True
        return False
    
    @classmethod
    def adicionar_cpf(cls, cpf: str) -> None:
        cls.cpfs_utilizados.append(cpf)

    @property
    def cpf(self) -> str:
        return self._cpf
    
    @property
    def idade(self) -> str:
        return self._idade

    @classmethod
    def adicionar_cliente(cls) -> None:
        cpf = input("Digite o CPF do cliente: ")
        nome = input("Digite o Nome do cliente: ")
        while True:
            data_nascimento = input("Digite a Data de Nascimento do cliente (AAAA-MM-DD): ")
            try:
                teste = datetime.strptime(data_nascimento, "%Y-%m-%d").date()
                break  
            except ValueError:
                print("Formato de data incorreto. Certifique-se de usar o formato AAAA-MM-DD.")

        novo_cliente = Clientes(cpf, nome, data_nascimento)
        Clientes.clientes.append(novo_cliente)


    @classmethod
    def busca_cliente_cpf(cls,cpf) -> "Clientes":
        #cpf = input("Digite o CPF do cliente: ")
        for cliente in Clientes.clientes:
            if cliente._cpf == cpf:
                print(cliente.nome)
                return cliente

class Laboratorios():
    laboratorios = []
    def __init__(self, nome: str, endereco: str, telefone: str, cidade: str, estado: str):
        self.nome: str = nome
        self.endereco: str = endereco
        self.telefone: str = telefone
        self.cidade: str = cidade
        self.estado: str = estado

    @classmethod
    def cadastrar_labotarorio(cls, nome: str, endereco: str, telefone: str, cidade: str, estado: str) -> None:
        ja_cadastrado = False
        for lab in cls.laboratorios:
            if nome == lab.nome:
                ja_cadastrado = True
                print(f'O laboratório {nome} já é cadastrado.')
                continue
            else:
                pass
        if not ja_cadastrado:
            novo_lab = cls(nome, endereco, telefone, cidade, estado)
            cls.laboratorios.append(novo_lab)
            print(f'O laboratório {nome} foi cadastrado.')

    @classmethod
    def lista_laboratorios(cls) -> None:
        for lab in cls.laboratorios:
            print(lab)
        return
    
    def __str__(self) -> str:
        return f'Laboratório: {self.nome}, Endereço: {self.endereco}, Telefone: {self.telefone}, Cidade: {self.cidade}, Estado: {self.estado}'
    
class Medicamentos(): 
    medicamentos =[]
    def __init__(self, nome: str, composto_principal: str,
                  laboratorio: Laboratorios, descricao: str, valor: float):
        self.nome: str = nome
        self.composto_principal: str = composto_principal
        self.laboratorio: Laboratorios = laboratorio
        self.descricao: str = descricao
        self.valor: float = valor
       
    
    @classmethod
    def busca_medicamentos_laboratorio() -> "Medicamentos":
        lista_medicamentos_laboratorio = []
        laboratorio = input("Digite o Laboratório do Medicamento: ")
        for medicamento in Medicamentos.medicamentos:
            if medicamento.laboratorio == laboratorio:
                lista_medicamentos_laboratorio.append(medicamento)
                print(medicamento.laboratorio)
                return lista_medicamentos_laboratorio
            
    @classmethod     
    def busca_medicamentos_descricao() -> "Medicamentos":
        lista_medicamentos_descricao = []
        descricao = input("Digite a Descrição do Medicamento: ")
        for medicamento in Medicamentos.medicamentos:
            if descricao in medicamento.descricao:
                lista_medicamentos_descricao.append(medicamento)
                print(medicamento.laboratorio)
                return lista_medicamentos_descricao
    
    @classmethod
    def cadastrar_medicamento(cls, nome: str, composto_principal: str,
                              laboratorio: Laboratorios, descricao: str, valor: float, tipo: str) -> None:
        novo_medicamento = cls(nome, composto_principal, laboratorio, descricao, valor, tipo)
        cls.medicamentos.append(novo_medicamento)
        print(f'O medicamento {nome} foi cadastrado.')
        return None

    @classmethod
    def lista_medicamentos(cls) -> None:
        print('\nLISTA DE MEDICAMENTOS\n')
        for medicamento in cls.medicamentos:
            print(medicamento)

    def __str__(self) -> str:
        return f'Medicamento: {self.nome}, Composto Principal: {self.composto_principal}, ' \
               f'Laboratório: {self.laboratorio.nome}, Descrição: {self.descricao}, Valor: {self.valor}'

# CLASSE MEDICAMENTO COM AJUSTE INCLUINDO ARGUMENTO "TIPO", PARA TENTAR CRIAR A HERANÇA COMPLETA DOS FITOS E QUIMIOS
# class Medicamentos(): 
#     medicamentos =[]
#     def __init__(self, nome: str, composto_principal: str,
#                   laboratorio: Laboratorios, descricao: str, valor: float, tipo: str):
#         self.nome: str = nome
#         self.composto_principal: str = composto_principal
#         self.laboratorio: Laboratorios = laboratorio
#         self.descricao: str = descricao
#         self.valor: float = valor
#         self.tipo: str = tipo
    
#     @classmethod
#     def busca_medicamentos_laboratorio() -> "Medicamentos":
#         lista_medicamentos_laboratorio = []
#         laboratorio = input("Digite o Laboratório do Medicamento: ")
#         for medicamento in Medicamentos.medicamentos:
#             if medicamento.laboratorio == laboratorio:
#                 lista_medicamentos_laboratorio.append(medicamento)
#                 print(medicamento.laboratorio)
#                 return lista_medicamentos_laboratorio
            
#     @classmethod     
#     def busca_medicamentos_descricao() -> "Medicamentos":
#         lista_medicamentos_descricao = []
#         descricao = input("Digite a Descrição do Medicamento: ")
#         for medicamento in Medicamentos.medicamentos:
#             if descricao in medicamento.descricao:
#                 lista_medicamentos_descricao.append(medicamento)
#                 print(medicamento.laboratorio)
#                 return lista_medicamentos_descricao
    
#     @classmethod
#     def cadastrar_medicamento(cls, nome: str, composto_principal: str,
#                               laboratorio: Laboratorios, descricao: str, valor: float, tipo: str) -> None:
#         novo_medicamento = cls(nome, composto_principal, laboratorio, descricao, valor, tipo)
#         cls.medicamentos.append(novo_medicamento)
#         print(f'O medicamento {nome} foi cadastrado.')
#         return None

#     @classmethod
#     def lista_medicamentos(cls) -> None:
#         print('\nLISTA DE MEDICAMENTOS\n')
#         for medicamento in cls.medicamentos:
#             print(medicamento)

#     def __str__(self) -> str:
#         return f'Medicamento: {self.nome}, Composto Principal: {self.composto_principal}, ' \
#                f'Laboratório: {self.laboratorio.nome}, Descrição: {self.descricao}, Valor: {self.valor}'

# TENTANDO TROCAR A CLASSE MEDICAMENTO FITO PARA SENDO HERANÇA DA CLASSE MEDICAMENTOS SOBREPONDO TODAS AS FUNÇÕES DA
# CLASSE PAI (MEDICAMENTOS) - NÃO CONSEGUI FINALIZAR, POR ISSO COMENTEI
# class MedicamentosFitoterapicos(Medicamentos):
    
#     def __init__(self, nome: str, composto_principal: str,
#                   laboratorio: Laboratorios, descricao: str, valor: float, tipo: str = "FITOTERAPICO"):
#         super().__init__(nome, composto_principal, laboratorio, descricao, valor, tipo)

#     @classmethod
#     def cadastrar_medicamento(cls, nome: str, composto_principal: str,
#                               laboratorio: Laboratorios, descricao: str, valor: float, tipo: str = "FITOTERAPICO") -> None:
#         novo_medicamento = cls(nome, composto_principal, laboratorio, descricao, valor, tipo)
#         Medicamentos.medicamentos.append(novo_medicamento)
#         print(f'O medicamento {nome} foi cadastrado.')
#         return None

#     @classmethod
#     def lista_medicamentos(cls) -> None:
#         print('\nLISTA DE MEDICAMENTOS FITOTERÁPICOS\n')
#         lista_fito =[]

#         for medicamento in cls.medicamentos:
#             if medicamento.tipo == "FITOTERAPICO":
#                 lista_fito.append(medicamento)
        
#         for medicamento in lista_fito:
#             print(medicamento)

# CLASSE MEDICAMENTOS FITO COMO ESTAVA:
class MedicamentosFitoterapicos(Medicamentos):
    lista_fito = []
    def __init__(self, nome: str, composto_principal: str,
                  laboratorio: Laboratorios, descricao: str, valor: float):
        super().__init__(nome, composto_principal, laboratorio, descricao, valor)

    
    @classmethod
    def cadastrar_med_fito(cls, nome: str, composto_principal: str,
                              laboratorio: Laboratorios, descricao: str, valor: float) -> None:
        novo_medicamento = cls(nome, composto_principal, laboratorio, descricao, valor)
        cls.lista_fito.append(novo_medicamento)
        print(f'O medicamento {nome} foi cadastrado.')
        return 
    
    @classmethod
    def busca_fito_por_nome(cls, nome) -> List:
        fito_nome_filtrado = []
        for medicamento in cls.lista_fito:
            if medicamento.nome == nome:
                fito_nome_filtrado.append(medicamento)
            
        if fito_nome_filtrado == []:
                print('\nNão há medicamentos com este nome. Consulte abaixo a lista completa de medicamentos:')

        return fito_nome_filtrado
    
    @staticmethod
    def lista_med_fito() -> None:
        print('\nLISTA DE FITOTERÁPICOS\n')
        for med in MedicamentosFitoterapicos.lista_fito:
            print(med)
        return None
    
    # @classmethod - COMO ERA
    # def lista_med_fito(cls, list = []) -> None:
    #     print('\nLISTA DE FITOTERÁPICOS\n')
    #     if list == []:
    #         for fito in cls.lista_fito:
    #             print(fito)
    #     else:
    #         for fito in list:
    #             print(fito)
    #     return None

    def __str__(self) -> str:
        return f'Medicamento: {self.nome}, Composto Principal: {self.composto_principal}, ' \
                f'Laboratório: {self.laboratorio.nome}, Descrição: {self.descricao}, Valor: {self.valor}'

class MedicamentosQuimioterapicos(Medicamentos):
    lista_quimio = []
    def __init__(self, nome: str, composto_principal: str,
                  laboratorio: Laboratorios, descricao: str, valor: float, receita: bool):
        super().__init__(nome, composto_principal, laboratorio, descricao, valor )
        self.receita: bool = receita

    @classmethod
    def cadastrar_med_quimio(cls, nome: str, composto_principal: str,
                              laboratorio: Laboratorios, descricao: str, valor: float, receita: bool) -> None:
        novo_medicamento = cls(nome, composto_principal, laboratorio, descricao, valor, receita)
        cls.lista_quimio.append(novo_medicamento)
        print(f'O medicamento {nome} foi cadastrado.')
        return
    
    @classmethod
    def busca_quimio_por_nome(cls, nome) -> List:
        quimio_nome_filtrado = []
        for medicamento in cls.lista_quimio:
            if medicamento.nome == nome:
                quimio_nome_filtrado.append(medicamento)
            
        if quimio_nome_filtrado == []:
                print('\nNão há medicamentos com este nome. Consulte abaixo a lista completa de medicamentos:')

        return quimio_nome_filtrado
    
    @classmethod
    def lista_med_quimio(cls, list = []) -> None:
        print('\nLISTA DE QUIMIOTERÁPICOS\n')
        if list == []:
            for quimio in cls.lista_quimio:
                print(quimio)
        else:
            for quimio in list:
                print(quimio)
        return None

    def __str__(self) -> str:
        return f'Medicamento: {self.nome}, Composto Principal: {self.composto_principal}, Laboratório: {self.laboratorio.nome}, ' \
                f'Descrição: {self.descricao}, Valor: {self.valor}, Precisa de receita: {"Sim" if self.receita else "Nâo"}'

class Carrinho():
    carrinho = []
    def __init__(self, cpf_cliente: str, medicamento: Medicamentos, quantidade: int):
        self.cpf_cliente = cpf_cliente
        self.medicamento = medicamento
        self.quantidade = quantidade
        

    @classmethod
    def criar_carrinho(cls) -> None:
        cls.carrinho = []
        return None
    
    @classmethod
    def adicionar_ao_carrinho(cls, cpf_cliente:str, medicamento: Medicamentos, qtd: int) -> None:
        items = cls(cpf_cliente, medicamento, qtd)
        cls.carrinho.append(items)
        print(f'{medicamento.nome} adicionado ao carrinho com sucesso!')
        return None
    
    @classmethod
    def decompor_carrinho(cls):
        lista_decomposta = []
        item_decomposto = []
        for item in cls.carrinho:
            if isinstance(item.medicamento,MedicamentosQuimioterapicos):
                item_decomposto.append(['QUIMIO', item.cpf_cliente, item.medicamento.nome, item.medicamento.valor, item.quantidade])
            elif isinstance(item.medicamento,MedicamentosFitoterapicos):
                item_decomposto.append(['FITO', item.cpf_cliente, item.medicamento.nome, item.medicamento.valor, item.quantidade])
        lista_decomposta.extend(item_decomposto)
        return lista_decomposta # [TIPO:srt,CPF: str, MEDICAMENTO: str, PRECO: float, QTD: int]
 


class Vendas():
    vendas_registradas = [] #lista das vendas registradas: [TIPO: srt, CPF: str, MEDICAMENTO: str, PRECO: float, QTD: int, VALOR_S_DESCONTO: float, VALOR_C_DESCONTO: float ]

    def __init__(self, cliente: Clientes):
        self._data: datetime = datetime.now()
        self._cliente: Clientes = cliente
        self._itens_vendidos : list= [] 
        self.vendas_registradas: list = []
        self._valor_total: float = 0.0

    @classmethod
    def apresentar_catalogo(cls) -> None:
        print(f'\nOlá, hoje temos os seguintes itens disponíveis:\n')
        for i in lista_todos_medicamentos():
            print(i)
        return None

    @classmethod
    def _calculo_valor(self,lista_carrinho: list,cpf_cliente ) -> list:
        lista_pre_venda = []
        total_sem_desconto =0
        desconto_final = 0
        cliente =Clientes.busca_cliente_cpf(cpf_cliente)
        desconto_valor = 0.9 if total_sem_desconto > 150.00 else 1.0
        desconto_idade = 0.8 if cliente.idade > 65 else 1.0
        desconto_final = min(desconto_valor, desconto_idade)
        for item in lista_carrinho:
            quantidade = item[-1]
            valor_unitario = item[-2] 
            total_sem_desconto += quantidade * valor_unitario # quantidade * valor
            total_com_desconto = quantidade * valor_unitario * desconto_final # quantidade * valor * desconto
            item.append(total_sem_desconto)
            item.append(total_com_desconto)
            lista_pre_venda.extend(item)
        
        return lista_pre_venda # [TIPO: srt, CPF: str, MEDICAMENTO: str, PRECO: float, QTD: int, VALOR_S_DESCONTO: float, VALOR_C_DESCONTO: float ]
    
    @classmethod
    def registrar_venda(self, lista_pre_venda: list) -> None:
        Vendas.vendas_registradas.append(lista_pre_venda)
        print("Venda registrada!")
        return None
    
    # @classmethod
    # def finalizar_venda(cls, carrinho: Carrinho) -> None:
    #     cls()
    #     return
    @classmethod
    def contagem_clientes(cls):
        clientes_atendidos = set() 

        for item in cls.vendas_registradas:
            for i in range(1, len(item), 7):  
                cpf_cliente = item[i]
                clientes_atendidos.add(cpf_cliente)

        num_clientes = len(clientes_atendidos)
        print(f"Número de clientes atendidos: {num_clientes}")
        
    @classmethod
    def med_mais_vendido(cls):
        medicamentos_quantidades = {}
        medicamentos_valores = {}

        for item in cls.vendas_registradas:
            for i in range(0, len(item), 7):  
                nome_medicamento = item[i + 2]
                quantidade = item[i + 4]
                valor = item[i + 6]

                if nome_medicamento not in medicamentos_quantidades:
                    medicamentos_quantidades[nome_medicamento] = 0
                    medicamentos_valores[nome_medicamento] = 0.0

                medicamentos_quantidades[nome_medicamento] += quantidade
                medicamentos_valores[nome_medicamento] += valor

            medicamento_mais_vendido = max(medicamentos_quantidades, key=medicamentos_quantidades.get)
            quantidade_mais_vendida = medicamentos_quantidades[medicamento_mais_vendido]
            valor_total_mais_vendido = medicamentos_valores[medicamento_mais_vendido]
            
            print(f"O medicamento mais vendido: {medicamento_mais_vendido}")
            print(f"O Valor total: {valor_total_mais_vendido}")
            print(f"A quantidade: {quantidade_mais_vendida}")
            return medicamento_mais_vendido, quantidade_mais_vendida, valor_total_mais_vendido

    @classmethod
    def calcular(cls, tipo_medicamento):
        quantidade_total_vendida = 0
        valor_total_vendas = 0

        for venda in cls.vendas_registradas:
            valor_total_vendas = 0
            for i in range(0, len(venda), 7):
                if venda[i].lower() == tipo_medicamento.lower():
                    quantidade_total_vendida += venda[i+4]    
                    valor_total_vendas += venda[i+5] 
            

        print(f"Número de remédios {tipo_medicamento.lower()}terapicos vendidos no dia:")
        print(f"Quantidade total vendida: {quantidade_total_vendida}")
        print(f"Valor total das vendas: R${valor_total_vendas:.2f}")

    @classmethod
    def vendas_quimioterapicos(cls):
        cls.calcular("QUIMIO")

    @classmethod
    def vendas_fitoterapicos(cls):
        cls.calcular("FITO")
            
def seed():

    Laboratorios.cadastrar_labotarorio('Lab01', 'Rua 001', '00000000', 'cidade 001', 'estado 001')
    Laboratorios.cadastrar_labotarorio('Lab02', 'Rua 002', '000000002', 'cidade 002', 'estado 002')
    Laboratorios.cadastrar_labotarorio('Lab03', 'Rua 003', '000000003', 'cidade 003', 'estado 003')
    Laboratorios.cadastrar_labotarorio('Lab04', 'Rua 004', '000000004', 'cidade 004', 'estado 004')
    Laboratorios.cadastrar_labotarorio('Lab05', 'Rua 005', '000000005', 'cidade 005', 'estado 005')

    # PARA TESTAR NOVA CLASSE DE MEDICAMENTO FITO 
    # MedicamentosFitoterapicos.cadastrar_medicamento('Med01', 'Composto A', Laboratorios.laboratorios[0], 'Descrição do medicamento 1', 10.0)
    # MedicamentosFitoterapicos.cadastrar_medicamento('Med02', 'Composto B', Laboratorios.laboratorios[1], 'Descrição do medicamento 2', 15.0)
    # MedicamentosFitoterapicos.cadastrar_medicamento('Med03', 'Composto c', Laboratorios.laboratorios[2], 'Descrição do medicamento 3', 10.0)
    # MedicamentosFitoterapicos.cadastrar_medicamento('Med04', 'Composto D', Laboratorios.laboratorios[3], 'Descrição do medicamento 4', 15.0)
    # MedicamentosFitoterapicos.cadastrar_medicamento('Med05', 'Composto E', Laboratorios.laboratorios[4], 'Descrição do medicamento 5', 10.0)
    
    MedicamentosFitoterapicos.cadastrar_med_fito('Med01', 'Composto A', Laboratorios.laboratorios[0], 'Descrição do medicamento 1', 10.0)
    MedicamentosFitoterapicos.cadastrar_med_fito('Med02', 'Composto B', Laboratorios.laboratorios[1], 'Descrição do medicamento 2', 15.0)
    MedicamentosFitoterapicos.cadastrar_med_fito('Med03', 'Composto c', Laboratorios.laboratorios[2], 'Descrição do medicamento 3', 10.0)
    MedicamentosFitoterapicos.cadastrar_med_fito('Med04', 'Composto D', Laboratorios.laboratorios[3], 'Descrição do medicamento 4', 15.0)
    MedicamentosFitoterapicos.cadastrar_med_fito('Med05', 'Composto E', Laboratorios.laboratorios[4], 'Descrição do medicamento 5', 10.0)
    MedicamentosQuimioterapicos.cadastrar_med_quimio('Med06', 'Composto F', Laboratorios.laboratorios[0], 'Descrição do medicamento 6', 10.0, True)
    MedicamentosQuimioterapicos.cadastrar_med_quimio('Med07', 'Composto G', Laboratorios.laboratorios[1], 'Descrição do medicamento 7', 15.0, True)
    MedicamentosQuimioterapicos.cadastrar_med_quimio('Med08', 'Composto H', Laboratorios.laboratorios[2], 'Descrição do medicamento 8', 10.0, True)
    MedicamentosQuimioterapicos.cadastrar_med_quimio('Med09', 'Composto I', Laboratorios.laboratorios[3], 'Descrição do medicamento 9', 15.0, True)
    MedicamentosQuimioterapicos.cadastrar_med_quimio('Med010', 'Composto J', Laboratorios.laboratorios[4], 'Descrição do medicamento 10', 10.0, True)

    clientes_padrao=[
    Clientes("111", "Cliente A", "1990-01-01"),
    Clientes("222", "Cliente C", "1985-05-15"),
    Clientes("333", "Cliente B", "1978-08-20")
    ]
    Clientes.clientes.extend(clientes_padrao)


def lista_todos_medicamentos() -> list:
    lista = []
    lista_fito = MedicamentosFitoterapicos.lista_fito
    lista_quimio = MedicamentosQuimioterapicos.lista_quimio
    lista.extend(lista_fito)
    lista.extend(lista_quimio) 
    return lista
    
def main():
    

    seed()

    while True:
        menu_str = """
        \nBoas vindas ao nosso sistema:

        1 - Inserir Clientes
        2 - Cadastrar Medicamento Quimioterápicos
        3 - Cadastrar Medicamento Fitoterápico
        4 - Realizar Venda
        5 - Relatório de Clientes
        6 - Lista de Todos os Medicamentos
        7 - Lista de medicamentos Fitoterápicos 
        8 - Lista de medicamentos Quimioterápicos 
        0 - Sair\n
        """
        print(menu_str)

        opcao = input("Escolha uma opção: ")
        if opcao == '1':
            Clientes.adicionar_cliente()
        elif opcao == '2':
            validacao_lab = True
            while validacao_lab:
                Laboratorios.lista_laboratorios()
                lab = input('\nEntre os laboratórios acima, informe o nome do Laboratório deste medicamento:')
                for laboratorio in Laboratorios.laboratorios:
                    if laboratorio.nome == lab:
                        validacao_lab = False
                        lab = laboratorio
                        
                                   
                #print('\nNome inválido, por favor, digite o nome exato do laboratório.') EMOVIDO DEVIDO AJUSTE NO WHILE
                #Laboratorios.lista_laboratorios() REMOVIDO DEVIDO AJUSTE NO WHILE
                #lab = input('\nEntre os laboratórios acima, informe o nome do Laboratório deste medicamento: ') REMOVIDO DEVIDO AJUSTE NO WHILE
            med_nome = input('\nInforme o nome medicamento: ')
            med_principal_composto = input('\nInforme o principal composto do medicamento: ')
            med_descricao = input('\nInforme a descrição do medicamento: ')
            med_valor = float(input('\nInforme o valor de venda do medicamento: '))
            med_receita = True if 's' in input('\nO medicamento precisa de receita? (S/N): ').lower() else False
            
            MedicamentosQuimioterapicos.cadastrar_med_quimio(med_nome, med_principal_composto, lab, med_descricao, med_valor, med_receita)

        elif opcao == '3':
                 
            validacao_lab = True
            while validacao_lab:
                Laboratorios.lista_laboratorios()
                lab = input('\nEntre os laboratórios acima, informe o nome do Laboratório deste medicamento:')
                for laboratorio in Laboratorios.laboratorios:
                    if laboratorio.nome == lab:
                        validacao_lab = False
                        lab = laboratorio
                    
            med_nome = input('\nInforme o nome do medicamento: ')
            med_principal_composto = input('\nInforme o principal composto do medicamento: ')
            med_descricao = input('\nInforme a descrição do medicamento: ')
            med_valor = float(input('\nInforme o valor de venda do medicamento: '))
            
            MedicamentosFitoterapicos.cadastrar_med_fito(med_nome, med_principal_composto, lab, med_descricao, med_valor)

        elif opcao == '4':
            validacao_cpf = True 
            while validacao_cpf: # VALIDACAO DE CLIENTE CADASTRADO
                cpf_cliente = input('Informe o CPF do cliente para realizar a venda:')
                for c in Clientes.cpfs_utilizados:
                    if cpf_cliente in c:
                        loop_venda = True
                        validacao_cpf = False
                        break
                
                print(f'O CPF {cpf_cliente} não possui cadastro')

            Carrinho.criar_carrinho() # INICIA CARRINHO PARA LIMPAR VARIAVEL DA VENDA ANTERIOR
            print("aqui") #REMOVER DEPOIS, SÓ PARA TESTE ISSO??
            Vendas.apresentar_catalogo()
            while loop_venda:
                input_catalogo = str(input('\n Informe o nome do medicamento que deseja comprar, ou digite 0 para finalizar a venda:'))
                if input_catalogo == '0':
                    loop_venda = False
                else:
                    lista_medicamentos = lista_todos_medicamentos()
                    print(f'\n esse é o tipo: {type(lista_medicamentos)}')
                    produto_existe = False
                    for med in lista_medicamentos:
                        if med.nome == input_catalogo:
                            produto_existe = True
                            if isinstance(med, MedicamentosQuimioterapicos):
                                if med.receita == True:
                                    print(f"O Medicamento {med.nome} necessita de receita! Confira a Receita!\n")
                                else:
                                    pass
                            else:
                                pass   
                            qtd_invalida = True
                            while qtd_invalida:
                                qtd = input(f"O produo selecionado foi: \n {med}. \n" \
                                        f"Quantas unidades do produto deseja levar? \n")
                                try:
                                    qtd = int(qtd)
                                    qtd_invalida = False
                                except:
                                    print('\nQuantidade invalida, por favor, digite um número:')
        
                            Carrinho.adicionar_ao_carrinho(cpf_cliente, med, qtd)
                    if not produto_existe:
                        print("Não encontramos esta produto, pode favor, revise o nome digitado.")
        
            var1 = Vendas._calculo_valor(Carrinho.decompor_carrinho(), cpf_cliente)
            Vendas.registrar_venda(var1)
        elif opcao == '5':
            Clientes.relatorio_cliente()
        elif opcao == '6':
            lista_6 = lista_todos_medicamentos()
            for i in lista_6:
                print(i)
            # Medicamentos.lista_todos_medicamentos()
        elif opcao == '7': #LISTA FITO
            MedicamentosFitoterapicos.lista_med_fito()
        elif opcao == '8': #LISTA QUIMIO
            for i in MedicamentosQuimioterapicos.lista_quimio:
                print(i)
        elif opcao == '9': ## REVISAR 
            nome = str(input("Digite o Nome do Medicamento: "))
            quimio_filtrado = MedicamentosQuimioterapicos.busca_quimio_por_nome(nome)
            fito_filtrado = MedicamentosQuimioterapicos.busca_quimio_por_nome(nome)
            MedicamentosQuimioterapicos.lista_med_quimio(quimio_filtrado)
            MedicamentosFitoterapicos.lista_med_fito(fito_filtrado)

        elif opcao == '0':
            print("\nEstatísticas das vendas do dia:")
            Vendas.contagem_clientes()
            Vendas.med_mais_vendido()
            Vendas.vendas_fitoterapicos()
            Vendas.vendas_quimioterapicos()
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    main()