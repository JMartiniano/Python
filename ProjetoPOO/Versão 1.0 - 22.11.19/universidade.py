class Universidade():
    def __init__(self):
        self.__curso1 = {'Nome':'Redes de Computadores', '1':'Comutação', '2':'Estrutura de Dados', '1.1.1':'C1DCP1T1', '1.1.2':'C1DCP1T2', '1.2.1':'C1DCP2T1', '1.2.2':'C1DCP2T2'}
        self.__curso2 = {'Nome':'Sistemas para Internet', '1':'Script', '2':'Algoritimos', '2.1.1':'C2DCP1T1', '2.1.2':'C2DCP1T2', '2.2.1':'C2DCP2T1', '2.2.2':'C2DCP2T2'}

#   GETS DO CURSO 1

    def get_curso1(self):
        return self.__curso1
    def get_nomeCurso1(self):
        return self.__curso1['Nome']
    def get_curso1DCP1(self):
        return self.__curso1['1']
    def get_curso1DCP2(self):
        return self.__curso1['2']

    #    GETS DOS TEMAS DAS DISCIPLINAS

    def get_curso1DCP1T1(self):
        return self.__curso1['1.1.1']
    def get_curso1DCP1T2(self):
        return self.__curso1['1.1.2']
    def get_curso1DCP2T1(self):
        return self.__curso1['1.2.1']
    def get_curso1DCP2T2(self):
        return self.__curso1['1.2.2']


#   GETS DO CURSO 2

    def get_curso2(self):
        return self.__curso2
    def get_nomeCurso2(self):
        return self.__curso2['Nome']
    def get_curso2DCP1(self):
        return self.__curso2['1']
    def get_curso2DCP2(self):
        return self.__curso2['2']

    #   GETS DOS TEMAS DAS DISCIPLINAS

    def get_curso2DCP1T1(self):
        return self.__curso2['3.1']
    def get_curso2DCP1T2(self):
        return self.__curso2['3.2']
    def get_curso2DCP2T1(self):
        return self.__curso2['4.1']
    def get_curso2DCP2T2(self):
        return self.__curso2['4.2']


#   SETS DO CURSO 1

    def set_nomeCurso1(self, novo):
        self.__curso1["Nome"] = novo
    def set_curso1DCP1(self, novo):
        self.__curso1['1'] = novo
    def set_curso1DCP2(self, novo):
        self.__curso1['2'] = novo
    def set_curso1(self, novo):
        self.__curso1 = novo

    #    SETS DOS TEMAS DAS DISCIPLINAS

    def set_curso1DCP1T1(self, novo):
        self.__curso1['1.1'] = novo
    def set_curso1DCP1T2(self, novo):
        self.__curso1['1.2'] = novo
    def set_curso1DCP2T1(self, novo):
        self.__curso1['2.1'] = novo
    def set_curso1DCP2T2(self, novo):
        self.__curso1['2.2'] = novo

#   SETS DO CURSO 2

    def set_curso2(self, novo):
        self.__curso2 = novo
    def set_nomeCurso2(self, novo):
        self.__curso2["Nome"] = novo
    def set_curso2DCP1(self, novo):
        self.__curso2['1'] = novo
    def set_curso2DCP2(self, novo):
        self.__curso2['2'] = novo

    # SETS DOS TEMAS DAS DISCIPLINAS

    def set_curso2DCP1T1(self, novo):
        self.__curso2['2.1.1'] = novo
    def set_curso2DCP1T2(self, novo):
        self.__curso2['2.1.2'] = novo
    def set_curso2DCP2T1(self, novo):
        self.__curso2['2.2.1'] = novo
    def set_curso2DCP2T2(self, novo):
        self.__curso2['2.2.2'] = novo

#   PROPRIEDADES GERAIS
    curso1 = property(get_curso1, set_curso1)
    curso2 = property(get_curso2, set_curso2)
    c1DCP1 = property(get_curso1DCP1, set_curso1DCP1)
    c2DCP2 = property(get_curso2DCP1, set_curso2DCP1)

    def __str__(self):
        s = f'Curso: {str(self.__curso1["Nome"])}\nDisciplina 1: {str(self.__curso1["DCP1"])}'
        return s