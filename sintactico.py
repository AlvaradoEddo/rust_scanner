from lexer import tokens
import ply.yacc as yacc



'''
Jaime's Contribution
Asignations
3 printing prints
'''
def p_rust(p):
    '''
    rust : asignacion
         | prints
    '''

def p_asignacion(p):
    '''
    asignacion : declarador ASIGNAR expresion ENDLINE
                | other_operators ENDLINE
    '''

def p_other_operators(p):
    '''
    other_operators : VARIABLE oper_asig expresion
    '''

def p_declarador(p):
    '''
    declarador : VARIABLE
                | let_asig
    '''

def p_let_asig(p):
    '''
    let_asig : LET var_tipo
             | LET MUT var_tipo
    '''

def p_var_tipo(p):
    '''
    var_tipo : VARIABLE
             | VARIABLE  ASIGNATION_TYPE tipos
    '''

def p_tipos(p):
    '''
    tipos : DATATYPES
            | NUMDATATYPES
    '''

def p_oper_asig(p):
    '''
    oper_asig : ASIGNAR
                | PLUSEQ
                | MINUSEQ
                | STAREQ
                | SLASHEQ
    '''

def p_expresion(p):
    '''
    expresion : STRING
                | U8
    '''

def p_prints(p):
    '''
    prints : PRINTS LPAREN print_expresion RPAREN ENDLINE
    '''



def p_print_expresion(p):
    '''
    print_expresion : STRING
                    | STRING COMMA print_args
    '''

def p_print_args(p):
    '''
    print_args : print_datos COMMA print_args 
                | print_datos
    '''

def p_print_datos(p):
    '''
    print_datos : expresion
    '''

parser = yacc.yacc()
 
while True:
    try:
        s = input('calc > ')
    except EOFError:
        break
    if not s: continue
    result = parser.parse(s)
    print(result)