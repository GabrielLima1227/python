class SistemaCadastral:
    """ "
    def cadastrar(self, nome: str, idade: int) -> None:
        if isinstance(nome, str) and isinstance(idade, int): #1
            print("Acessando o banco de dados....") #2
            print(f"Cadastrar Usuario {nome}, idade {idade}")
        else:
            print("Dados Invalidos") #3
    """

    def cadastrar(self, nome: str, idade: int) -> None:
        if self.__validate_input(nome, idade):
            self.__register_user(nome, idade)
        else:
            self.__erro_handle()

    def __validate_input(self, nome: str, idade: int):
        return isinstance(nome, str) and isinstance(idade, int)

    def __register_user(self, nome: str, idade: int) -> None:
        print("Acessando o banco de dados....")  # 2
        print(f"Cadastrar Usuario {nome}, idade {idade}")

    def __erro_handle(self) -> None:
        print("Dados Invalidos")


sistema = SistemaCadastral()
sistema.cadastrar("Gabriel", 20)
