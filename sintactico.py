from lexer import tokens
import ply.yacc as yacc


def p_asignacion(p):
    '''
    asignacion : declarador ASIGNAR expresion
                | VARIABLE oper_asig expresion
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


parser = yacc.yacc()
 
while True:
    try:
        s = input('calc > ')
    except EOFError:
        break
    if not s: continue
    result = parser.parse(s)
    print(result)