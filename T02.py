# Objeto range
r = range (1, 100)

# Mutabilidad: modificar elemento del range: error
r [0] = 50

# Suma de rangos: error
r_sum = r + range (100, 1000)

# Multiplicación por un entero: error
r_mult = r * 2

# Slicing: yes
r_slice = r[4:10]
print(r_slice)

## Conversión a lista y a tupla
r_list = list(r)
r_tuple = tuple(r_list)

print ('tupla:', r_tuple)
print ('lista:', r_list)
