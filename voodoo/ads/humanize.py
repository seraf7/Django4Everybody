# Función para realizar conversión de unidades de almacenamiento
def naturalsize(count):
    fcount = float(count)
    # Definición de equivalencias
    k = 1024
    m = k * k
    g = m * k

    # Creación de prefijos de unidad
    if fcount < k:
        return str(count) + 'B'
    elif fcount >= k and fcount < m:
        return str(int(fcount / (k/10.0)) / 10.0) + 'KB'
    elif fcount >= m and fcount < g:
        return str(int(fcount / (m/10.0)) / 10.0) + 'MB'
    else:
        return str(int(fcount / (g/10.0)) / 10.0) + 'GB'
