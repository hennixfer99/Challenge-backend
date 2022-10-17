def leitura():
    arquivo = "CNAB.txt"

    data = []
    campos = [
        "type",
        "date",
        "value",
        "cpf",
        "card",
        "time",
        "owner_store",
        "store_name"
    ]

    with open(arquivo) as arq:

        for line in arq:
            description = line.strip().split(None, 0)
            data_string = {}
            data_string.update({campos[0]: description[0][0:1]})
            data_string.update({campos[1]: description[0][1:9]})
            data_string.update({campos[2]: description[0][9:19]})
            data_string.update({campos[3]: description[0][19:30]})
            data_string.update({campos[4]: description[0][30:42]})
            data_string.update({campos[5]: description[0][42:48]})
            data_string.update({campos[6]: description[0][48:62]})
            data_string.update({campos[7]: description[0][62:80]})
            data.append(data_string)

        print(data)
        return data


leitura()