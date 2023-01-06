import re

nome_arquivo = 'Commentary.csv'
pipx run charset-normalizer <arquivo>
with open(nome_arquivo, 'r+', encoding="utf8") as f:
    txt = f.read().rstrip("\n")
    txt = re.sub(r'\bEpístola de Jr( \d+)\b', 'EpJr\1', txt)
    txt = re.sub(r'\bEpJr\.( \d+)\b', 'EpJr\1', txt)
    txt = re.sub(r'\bAzarías( \d+)\b', 'Aza\1', txt)
    txt = re.sub(r'\bAza\.( \d+)\b', 'Aza\1', txt)
    print(txt)

r = open('Alterado_' + nome_arquivo, 'w', encoding="utf-8")
r.write(txt)
r.close()
