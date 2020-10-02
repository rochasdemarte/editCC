def main():
    ccName = input("Nome da legenda:")
    ccTime = input("Ajustar quantos segundos:")

    i = 0

    with open('source/'+ccName, "r") as file:
        filedata = file.readlines()

    print("Convertendo arquivo: \n- {0}\n- {1} linhas".format(ccName, len(filedata)))

    for line in filedata:
        #print(line)
        if '00:' in line:
            if '00:00:00;00' not in line:
                prefix = line[0:3]
                sulfix = line[8:len(line)]
                min = int(line[3:5])
                seg = int(line[6:8])
                mysec = seg + int(ccTime)
                seg += int(ccTime)
                if seg > 59:
                    min += 1
                elif mysec < 0 and min > 0:
                    min -=1
                    seg = mysec+60
                if seg < 10:
                    segZero = "0"
                else:
                    segZero = ""
                if min < 10:
                    minZero = "0"
                else:
                    minZero = ""

                newline = "{0}{1}{2}:{3}{4}{5}".format(prefix, minZero, str(min), segZero, str(seg), sulfix)
                filedata[i] = newline

        i += 1

    with open('convert/'+ccName, "w") as newfile:
        newfile.writelines(filedata)

if __name__ == '__main__':
    main()
