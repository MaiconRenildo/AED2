def get_nums_from_file(filename):
    ref_arquivo = open(filename+'.txt',"r")
    for linha in ref_arquivo:
        valores = linha.split(',')
    ref_arquivo.close()
    valores.pop(len(valores)-1)
    nums = [int(num) for num in valores]
    return nums
