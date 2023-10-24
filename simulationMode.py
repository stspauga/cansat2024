


simFile = open("cansat_2023_simp.txt","r",encoding="utf-8")
for line in simFile:
    if "#" not in line:
        print(line, end='')

simFile.close()