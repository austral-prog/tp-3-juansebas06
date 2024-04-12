def slice_advanced():
    name=f'{input('texto = ').lower()}'
    print(name[:3])
    name1=len(name)
    print(name[name1//2 - 1:name1 // 2 + 2])
    print(f'{name[:4]}{name[-3:]}')


# Para verificar este ejercicio ejecutar el comando
# `pytest tp3_slice_advanced_test.py` o `python tp3_slice_advanced_test.py`
