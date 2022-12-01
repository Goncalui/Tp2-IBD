from Insert import *
import pandas as pd

"""
df = pd.read_excel(file_errors_location,None)
print(df.keys())
"""
sheets = ['Curso', 'Aluno', 'Seguradora', 'Orientador', 'Supervisor', 'Concedente', 'Inscrito', 'Contrato', 'Seguro', 'Estágio']
file = 'BD IBD TP2.xlsx'

dic = {
    'Curso':CURSO,
    'Aluno':ALUNO,
    'Seguradora':SEGURADORA,
    'Orientador':ORIENTADOR,
    'Supervisor':SUPERVISOR,
    'Concedente':CONCEDENTE,
    'Inscrito':INSCRITO,
    'Contrato':CONTRATO,
    'Seguro':SEGURO,
    'Estágio':ESTAGIO
}

dic2 = {
    'Curso':"(CODCURS, NOMECURS, ESTRUTURACURS, MODALIDADECURS, CAMPUSCURS, PMINCURS, PMAXCURS)",
    'Aluno':"(CPFALUNO, NOMEALUNO)",
    'Seguradora':"(CNPJSEGURADORA, NOMESEGURADORA)",
    'Orientador':"(ORIENUMMATRICULA, ORIENOME)",
    'Supervisor':"(CPFSUPERVISOR, NOMESUPERVISOR, EMAILSUPERVISOR)",
    'Concedente':"(CNPJCONCEDENTE, NOMECONCEDENTE, ENDCONCEDENTE, BAIRROCONCEDENTE, CIDADECONCEDENTE)",
    'Inscrito':"(CODCURS, CPFALUNO,INSCMATRICULA, INSCSITUACAO, INSCPERIODO, INSCPERCENTUALPC, INSCPERCENTUALDO, INSCDATAEXPEDICAO)",
    'Contrato':"(INSCMATRICULA,CONTID, CONTESTOB, CONTDATAINICIO, CONTDATAFIM)",
    'Seguro':"( SEGACNPJ, SEGAPOLICE, SEGSTATUS)",
    'Estágio':"(CONTID, CNPJCONCEDENTE, CPFSUPERVISOR, ORIENUMMATRICULA, SEGAPOLICE)"
}


f = open('BancoDeDados' + '.sql', "w",encoding='utf-8')
from unidecode import unidecode
for sheet in sheets:
    
    for j in dic[sheet]:
        f.write(j)

    df = pd.read_excel(file, sheet_name=sheet)
    
    inserts = []
    for i in df.values.tolist():
        

        for val in range(len(i)):
            if(str(i[val]) == 'nan'):
                i[val] = 'NULL'
        


        insert = "INSERT INTO "+unidecode(sheet).upper()+" "+dic2[sheet]+" VALUES "+ str(tuple(i)).replace('Timestamp','').replace('NaT','NULL')+ ';\n'
        if(tuple(i)[0] not in inserts):
            f.write(insert)
            inserts.append(tuple(i)[0])
        elif(sheet == 'Estágio'):
            f.write(insert)
        elif(sheet == 'Inscrito'):
            print(insert)

    f.write('\n')

f.close()


