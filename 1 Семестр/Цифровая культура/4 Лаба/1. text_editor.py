fin = open("brain216.txt", encoding="utf8")
fout = open("edited_text.txt", "w")

for line in fin:
    line = line.replace("!", "").replace("?", "").replace(",", "").replace(";", "")
    line = line.replace(".", "").replace(":", "").replace("«", "").replace("(", "")
    line = line.replace(")", "").replace("»", "").lower()
    print(line, file=fout, end='')

fin.close()
fout.close()
