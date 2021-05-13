######################################
# @author: Iago Sousa                #
# @email: iagosousadev@gmail.com     #
# @GitHub: github.com/iagosousadev   #
# @Twitter: twitter.com/IagoSousaDEV #
######################################

# This script takes a file with questions and turn it into a .csv ANSI file which
# is the standard file for importing questions on the "EAD Plataforma" system.

header = "PERGUNTA;TIPO;TIPO_QUESTAO;OBSERVACAO;ALTERNATIVA 1;ALTERNATIVA 2;ALTERNATIVA 3;ALTERNATIVA 4;ALTERNATIVA 5;ALTERNATIVA 6;ALTERNATIVA 7;ALTERNATIVA 8\n"
with open("./questions.csv", "w", encoding="ANSI") as outputFile:
    with open("./questions.txt", encoding="utf8") as inputFile:
        rawText = inputFile.read().split(";")
        for i in range(1, len(rawText)):
            rawText[i] = rawText[i][1:]
        outputFile.write(header)
        for rawQuestion in rawText:
            question = rawQuestion.split("\n")
            csvLine = (question[0] + ";2;1;;" + ";".join(question[1:]))[:-1] + "\n"
            outputFile.write(csvLine)