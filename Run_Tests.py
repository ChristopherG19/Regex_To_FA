# Universidad del Valle de Guatemala
# Facultad de Ingeniería
# Departamento de Ciencias de la Computación
# CC2019 Teoría de la computación
# Grupo#9 

from AFD import *
from AFN_Generator import * 
from SimulacionAFN import *
from subconjuntos  import *
from time import perf_counter

# _________________________________________
# Temporal 
# _________________________________________

# r = "a"
# r = "ab"
# r = "aab"
# r = "(0|1)"
# r = "a*"
# r = "(a|b)*"
# r = "0(0|1)0"
# r = "0*(0*|1)1"
# r = "0*11*0"
r = "(b|b)*abb(a|b)*"
# r = "(a|b)*|(a|b)*"
# r = "((a|b)|(abab))|a"
# r = "ab*ab*"
# r = "(a|b)$"
# r = "(a|b)*(abba*|(ab)*ba)"
w = "bababaaaaa"

# _________________________________________
# pruebas 
# _________________________________________

# Expresión ya minimizada
# r = '(aa|bb)*'
# w = 'aabbaa'

# Expresión ya minimizada
# r = '(a(a|b)b)*'
# w = 'abbaab'

# Expresión ya minimizada
# r = '0(0|1)0'
# w = '000'

# da AFN no simplificado 
# r = '0*(0*|1)1'
# w = '00000011'

# minimizado
# r = 'ab'
# w = 'ab' 

# minimizado
# r = 'aab'
# w = 'aab'

# minimizado
# r = '(0|1)'
# w = '0'

# minimizado 
r = '0(0|1)0' 
w = '000' 

# minimizado
# r = 'a*'
# w = 'aaaaaaaaaa'

# minimizado
# r = '0*11*0'
# w = '00001'  

# minimizado
# r = '(a|b)*|(a|b)*'
# w = 'abba'  


# --------------------------------------------------
# Construcción de AFN con Thompson
print('\n--> Construcción AFN con construcción de Thompson')
Cons = Construction(r)
AFN_Thompson, Tiempo = Cons.Thompson_Construction()
Cons.printResults(AFN_Thompson)
print('Tiempo de ejecución: %.4e s'%Tiempo)
# --------------------------------------------------

# --------------------------------------------------
# Simulación de cadenas en AFN
print('\n--> Simulación AFN')
ResultadoSimulacion, Tiempo = SimulationAFN(r, w)
print("\nExpresion regular:", r)
print("Cadena a evaluar:", w)
print("Resultado: La cadena %s"%w, ResultadoSimulacion, "es aceptada\n")
print('Tiempo de ejecución: %.4e s'%Tiempo)
# --------------------------------------------------

# --------------------------------------------------
# Construcción de AFD con subconjuntos
print('\n--> Construcción AFD con subconjuntos')
AFD_Subconjuntos = AFN_To_AFD_SC(r)
printResultsAFD(AFD_Subconjuntos[0], AFD_Subconjuntos[1], AFD_Subconjuntos[2])
print('Tiempo de ejecución: %.4e s'%AFD_Subconjuntos[-1])
# --------------------------------------------------

# --------------------------------------------------
# Simulación AFD construido por subconjuntos
print('\n--> Simulación AFD por subconjuntos\n')
t9_start = perf_counter()
AFD_Subconjuntos = AFN_To_AFD_SC(r)
dfa2 = AFD(*AFD_Subconjuntos) 
if (dfa2.simulation(w)):
    print('El string %s pertenece al AFD'%w)
else:
    print('El string %s no pertenece al AFD'%w)
t9_stop = perf_counter()
print('Tiempo de ejecución: %.4e s'%(t9_stop - t9_start))
# --------------------------------------------------

# --------------------------------------------------
# Minimización AFD por subconjuntos
print('\n--> Minimización AFD por subconjuntos\n')
t10_start = perf_counter()
dfa2.minimization()
t10_stop = perf_counter()
print(dfa2)
print('tiempo de ejecución: %.4e s'%(t10_stop - t10_start))
# --------------------------------------------------

# --------------------------------------------------
# Simulación de cadenas
print('\n--> Simulación AFD por subconjuntos minimizado\n')
t8_start = perf_counter()
if (dfa2.simulation(w)):
    print('El string %s pertenece al AFD'%w)
else:
    print('El string %s no pertenece al AFD'%w)
t8_stop = perf_counter()
print('tiempo de ejecución: %.4e s'%(t8_stop - t8_start))
# --------------------------------------------------

# --------------------------------------------------
# Construcción del árbol sintáctico
print('\n--> Árbol sintáctico')
t4_start = perf_counter()
arbol = Tree(r)
t4_stop = perf_counter()
print(arbol)
print('tiempo de ejecución: %.4e s'%(t4_stop - t4_start))

# --------------------------------------------------
# Construcción directa
print('\n--> Construcción directa')
t5_start = perf_counter()
dfa = AFD()
dfa.directConstruction(arbol)
t5_stop = perf_counter()
print(dfa)
print("Estados de aceptación: ", ", ".join(dfa.getFinalStates()))
print('tiempo de ejecución: %.4e s'%(t5_stop - t5_start))
# --------------------------------------------------
lines3 = [
    'AFD-Directo',
    'Estados = %s'%dfa.Dstates,
    'Simbolos = %s'%dfa.Symbols,
    'Inicio = %s'%dfa.initState,
    'Aceptacion = %s'%dfa.getFinalStates(),
    'Transiciones = %s'%dfa
]

# --------------------------------------------------
# Simulación de cadenas
print('\n--> Simulación AFD\n')
t6_start = perf_counter()
if (dfa.simulation(w)):
    print('El string %s SÍ pertenece al AFD'%w)
else:
    print('El string %s NO pertenece al AFD'%w)
t6_stop = perf_counter()
print('tiempo de ejecución: %.4e s'%(t6_stop - t6_start))

# --------------------------------------------------

# --------------------------------------------------
# Minimización
print('\n--> Minimización\n')
t7_start = perf_counter()
dfa.minimization()
t7_stop = perf_counter()
print(dfa)
print('tiempo de ejecución: %.4e s'%(t7_stop - t7_start))
# --------------------------------------------------

# --------------------------------------------------
# Simulación de cadenas
print('\n--> Simulación AFD minimizado\n')
t8_start = perf_counter()
if (dfa.simulation(w)):
    print('El string %s SÍ pertenece al AFD'%w)
else:
    print('El string %s NO pertenece al AFD'%w)
t8_stop = perf_counter()
print('tiempo de ejecución: %.4e s'%(t8_stop - t8_start))
print()
# --------------------------------------------------

lines1 = [
    'AFN-Thompson',
    'Estados = %s'%Cons.states,
    'Simbolos = %s'%Cons.symbols,
    'Inicio = %s'%list(Cons.symbols)[0],
    'Aceptacion = %s'%list(Cons.symbols)[-1],
    'Transiciones = %s'%Cons.FinalTransitions
]

lines5 = [
    'AFD-Subconjuntos',
    'Estados = %s'%Cons.states,
    'Simbolos = %s'%Cons.symbols,
    'Inicio = %s'%AFD_Subconjuntos[0],
    'Aceptacion = %s'%AFD_Subconjuntos[1],
    'Transiciones = %s'%AFD_Subconjuntos[2]
]

lines2 = [
    'AFD-Subconjunto-Minimizado',
    'Estados = %s'%dfa2.Dstates,
    'Simbolos = %s'%dfa2.Symbols,
    'Inicio = %s'%dfa2.initState,
    'Aceptacion = %s'%dfa2.getFinalStates(),
    'Transiciones = %s'%dfa2
]

lines4 = [
    'AFD-min',
    'Estados = %s'%dfa.Dstates,
    'Simbolos = %s'%dfa.Symbols,
    'Inicio = %s'%dfa.initState,
    'Aceptacion = %s'%dfa.getFinalStates(),
    'Transiciones = %s'%dfa
]

# Escribir a un archivo
with open('Results.txt', 'w') as f:
    f.write('_________________________________________________\n')
    for line in lines1:
        f.write(line)
        f.write('\n')
    f.write('_________________________________________________\n')
    for line in lines5:
        f.write(line)
        f.write('\n') 
    f.write('_________________________________________________\n')
    for line in lines2:
        f.write(line)  
        f.write('\n') 
    f.write('_________________________________________________\n')
    for line in lines3:
        f.write(line)  
        f.write('\n')  
    f.write('_________________________________________________\n')
    for line in lines4:
        f.write(line)  
        f.write('\n')         
    f.write('_________________________________________________\n')