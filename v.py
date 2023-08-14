def simulate(entries):
    """
    :param entries: (list(int)) The numerical record files
    :returns: (list(int)) The record files after running the malware
    """
    entries1 = entries
    lista = []
    
    i = 0
    while i <= (len(entries)-1):
        if i <= len(entries) - 5:
            if  entries1[i] <= entries[i+4]:
                lista.insert(i, 0)
            else:
                lista.insert(i, entries[i])
        else:
            lista.insert(i, entries[i])
        i+=1
        
    i = 0         
    while i <= (len(entries) - 1):
        if  i > 3:
            if entries[i] <= entries[i-3]:
                lista[i] = 0
            
        i+=1
             

    return lista

records = [19, 2, 0, 87, 1, 40, 80, 77, 77, 77, 77]
print(simulate(records))
# Expected output
# [19, 0, 0, 87, 0, 0, 0, 77, 77, 0, 0]