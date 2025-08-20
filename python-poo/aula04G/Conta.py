class Conta:
    def __init__(self) -> None:
        self.num_conta = None
        self._tipo = None
        self.__dono = None
        self.__saldo = 0
        self.__status = False

    def estatisticas_da_conta(self) -> None:
        print("Sobre a Conta")
        print(f"Número da Conta: {self.num_conta}")
        print(f"Tipo: {self._tipo}")
        print(f"Dono: {self.__dono}")
        print(f"Saldo: {self.__saldo}")
        print(f"Status: {self.__status}")

    def getter_num_conta(self) -> int:
        return self.num_conta
    def setter_num_conta(self, valor) -> None:
        self.num_conta = valor

    def getter_tipo(self) -> str:
        return self._tipo
    def setter_tipo(self,valor) -> None:
        self._tipo = valor

    def getter_dono (self) -> str:
        return self.__dono
    def setter_dono(self,valor) -> None:
        self.__dono = valor

    def getter_saldo (self) -> float:
        return self.__saldo
    def setter_saldo(self,valor) -> float:
        self.__saldo = valor

    def getter_status(self) -> bool:
        return self.__status
    def setter_status(self,valor) -> None:
        self.__status = valor

    def abrir_conta(self) -> None:
        if self.__status == False and self._tipo == "CC":
            #Não tenho certeza se é uma atribuição direta ou devo chamar o método setter
            self.__saldo = 50
            self.__status = True
        elif self.__status == False and self._tipo == "CP":
            self.__saldo = 150
            self.__status = True
        else:
            print("Sua conta já está aberta")

    def fechar_conta(self) -> None:
        if self.__status == True and self.__saldo == 0:
            print("Sua conta foi inativada/fechada.")
            self.__status = False
        elif self.__status == True and self.__saldo > 0:
            print(f"Não foi possivel fecha a conta, pois ainda há {self.__saldo}R$ de saldo nela")
            self.__status = False
        elif self.__status == True and self.__saldo < 0:
            print(f"Não foi possivel fecha a conta, pois ainda há uma dívida de {self.__saldo}R$ nela")
            self.__status = False
        else:
            print("Sua conta já está inativada/fechada")

    def deposito(self,valor) -> None:
        if self.__status:
            print(f"Depósito de {valor}R$ realizado com sucesso!")
            self.__saldo += valor
        else:
            print("Operação não permitida. Sua conta está inativa ou fechada.")

    def sacar(self,valor_de_saque) -> None:
        if self.__status == True and self.__saldo >= valor_de_saque:
            self.__saldo -= valor_de_saque
            print(f"Saque de R$ {valor_de_saque:.2f} realizado com sucesso! Novo saldo: R$ {self.__saldo:.2f}")
        elif self.__status == True and valor_de_saque > self.__saldo:
            print(f"Saldo insuficiente para sacar R$ {valor_de_saque:.2f}. Seu saldo atual é de R$ {self.__saldo:.2f}.")
        else:
            print("Operação não permitida. Sua conta está inativa ou fechada.")

    def pagar_mensalidade(self) -> None:
        if self.__status == True and self._tipo == "CC" and self.__saldo >= 12:
            self.__saldo -= 12
            print(f"Pagamento da Mensalidade feito com sucesso. Novo saldo: R$ {self.__saldo:.2f}")
        elif self.__status == True and self._tipo == "CP" and self.__saldo >= 20:
            self.__saldo -= 20
            print(f"Pagamento da Mensalidade feito com sucesso. Novo saldo: R$ {self.__saldo:.2f}")
        elif self.__status == True and self._tipo in "CP CC":
            print("Sua conta está ativa, mas sem saldo para pagar a mensalidade")
        else:
            print("Operação não permitida. Sua conta está inativa ou fechada.")
