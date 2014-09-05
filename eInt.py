def is_int(x):
    dec = x - int(x) ## pega a parte decimal (se houver) do número
    if dec == 0 or type(x) == int:
        return True
    else:
        return False

print (is_int(7.5))
print (is_int(7.0))
print (is_int(7))
print (is_int(-7))
print (is_int(-7.0))
print (is_init(-7.5))
    
