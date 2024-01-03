primeiro = int(input('primeiro numero: '))
segundo = int(input('segundo numero: '))
terceiro = int(input('terceiro numero: '))

maior = primeiro

if (segundo > maior):
    maior = segundo
if (terceiro > maior):
    maior = terceiro

print("maior: ",maior)