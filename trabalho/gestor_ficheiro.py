import json
import os

class GestorFicheiro:
    def __init__(self, nome_arquivo: str):
        self.__nome_arquivo = nome_arquivo

    def __verificar_ficheiro(self):
        return os.path.exists(self.__nome_arquivo)

    def ler_ficheiro(self):
        if not self.__verificar_ficheiro():
            return None
        try:
            with open(self.__nome_arquivo, "r", encoding="utf-8") as f:
                return json.load(f)
        except:
            return None

    def escrever_ficheiro(self, dados):
        with open(self.__nome_arquivo, "w", encoding="utf-8") as f:
            json.dump(dados, f, indent=4, ensure_ascii=False)

    def atualizar_ficheiro(self, novos_dados):
        conteudo_antigo = self.ler_ficheiro()
        if conteudo_antigo == novos_dados:
            print(f"\033[93m[INFO] O ficheiro {self.__nome_arquivo} já estava atualizado.\033[00m")
        else:
            self.escrever_ficheiro(novos_dados)
            print(f"\033[92m[OK] Ficheiro {self.__nome_arquivo} atualizado com novos dados.\033[00m")
