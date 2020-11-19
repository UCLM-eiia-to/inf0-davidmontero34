Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:43:08) [MSC v.1926 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #ejercicio_10
>>> def es_ondulante (digito):
    longitud = str(digito)
    aux = ""
    menor = True
    for digit in longitud:
        if aux == "":
            aux = digit
            continue
        if menor == True:
            if int (digit) > int(aux):
                return False
        if menor == False:
            if int(digit) < int(aux):
                return False
            menor = True
        aux = digit
    return True

>>> #ejercicio_6
>>> def suma_digitos (digito):
	longitud=str(digito)
	digits_sum = 0
	for digit in longitud:
		digits_sum += int (digit)
	print (digits_sum)