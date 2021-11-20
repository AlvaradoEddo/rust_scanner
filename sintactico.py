from lexer import tokens
import ply.yacc as yacc



'''
Jaime's Contribution
Asignations
Printing Formats

'''
def p_rust(p):
    '''
    rust : asignacion
         | prints
         | hashset
         | hashfunc
         | conditional
         | conditional_asigned

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

def p_hashset(p):
    '''
    hashset : LET MUT VARIABLE ASIGNAR HASHSET PATHSEP NEWFUNC ENDLINE
    '''
def p_hashfunc(p):
    '''
    hashfunc : hashset_insert
            | hashset_union
    '''

def p_hashset_insert(p):
    '''
    hashset_insert : VARIABLE DOT INSERT_HASH LPAREN expresion RPAREN ENDLINE
    '''

def p_hashset_union(p):
    '''
    hashset_union : VARIABLE DOT UNION_HASH LPAREN AND VARIABLE RPAREN ENDLINE
    '''

# An if-statement can be assigned to a variable
def p_conditional_asigned(p):
    '''
    conditional_asigned : declarador ASIGNAR conditional ENDLINE
    '''

def p_conditional(p):
    '''
    conditional : if_type validations LLAVEIZ rust LLAVEDER
    '''

def p_if_type(p):
    '''
    if_type : IF
            | ELSE IF
            | ELSE
    '''

def p_validations(p):
    '''
    validations : comparison
                | comparison ANDAND validations
                | comparison OROR validations
    '''

def p_comparison(p):
    '''
    comparison : VARIABLE GREATER VARIABLE
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