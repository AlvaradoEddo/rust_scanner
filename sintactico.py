from lexer import tokens
import ply.yacc as yacc


'''
Jaime's Contribution
Asignations
Printing Formats

'''

start = 'rust'


def p_rust(p):
    '''
    rust : asignacion
         | prints
         | hashset
         | hashfunc
         | conditional
         | conditional_asigned
         | for_loop
         | struct_s
         | while_loop
         | empty_vector
         | vector_methods
         | data_vector
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


def p_oper_asig(p):
    '''
    oper_asig : ASIGNAR
                | PLUSEQ
                | MINUSEQ
                | STAREQ
                | SLASHEQ
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
# Aporte Eddo


def p_comparison(p):
    '''
    comparison : VARIABLE signo_comp VARIABLE
                | VARIABLE signo_comp U8
                | U8 signo_comp VARIABLE
    '''


def p_signoComparaion(p):
    '''
    signo_comp : GREATER
                | LESST
                | GREATEQ
                | EQUAL
                | DIFFERENT
    '''


def p_condicionFor(p):
    '''
    f_comparacion : U8 DOT DOT U8
                    | VARIABLE
    '''


def p_for(p):
    '''
    for_loop : FOR VARIABLE IN f_comparacion LLAVEIZ rust LLAVEDER
    '''


def p_struct(p):
    '''
    struct_s : STRUCT sent_stru
    '''


def p_argumentos_juntos(p):
    '''
    argumentos_juntos : VARIABLE ASIGNATION_TYPE tipos
                        | VARIABLE ASIGNATION_TYPE tipos COMMA argumentos_juntos
                        | PUB VARIABLE ASIGNATION_TYPE tipos COMMA argumentos_juntos
    '''


def p_argumento_tipo(p):
    '''
    argumentos_tipo : tipos
                    | tipos COMMA argumentos_tipo
    '''


def p_sentenciaStruct(p):
    '''
    sent_stru : UNIT ENDLINE
                | TUPLE LPAREN argumentos_tipo RPAREN ENDLINE
                | VARIABLE LLAVEIZ argumentos_juntos LLAVEDER
    '''


'''
Joangie's contribution 21/11/2021
- while loop
- read data
- vector and its two methos
- functions
- algorithm 
'''

# while loop


def p_while(p):
    '''
    while_loop : WHILE validations LLAVEIZ rust LLAVEDER
    '''
# read data with std:io


def p_empty_vector(p):
    '''
    empty_vector : declare_vector VECT types_vector empty_vec

    '''


def p_data_vector(p):
    '''
    data_vector : declare_vector VECT types_vector vector_content
                | declare_vector vector_content
                | declare_vector ASIGNAR VECTMACRO LLAVEIZ element_type COMMA vector_elements LLAVEDER ENDLINE
    '''


def p_vector_content(p):
    '''
    vector_content :  VECTMACRO LLAVEIZ vector_elements LLAVEDER ENDLINE
                    | VECT PATHSEP FROM LPAREN LLAVEIZ vector_elements LLAVEDER RPAREN ENDLINE
    '''


def p_vector_elements(p):
    '''
    vector_elements : element
                    | element COMMA vector_elements
    '''


def p_element(p):
    '''
    element : expresion
    '''


def p_element_type(p):
    '''
    element_type : U8 NUMDATATYPES
    '''


def p_types_vector(p):
    '''
    types_vector : LESST DATATYPES GREATER
                | LESST NUMDATATYPES GREATER
    '''


def p_declare_vector(p):
    '''
    declare_vector : LET MUT VARIABLE ASIGNATION_TYPE 
                    | LET VARIABLE ASIGNATION_TYPE

    '''


def p_assign_empty(p):
    '''
    empty_vec : ASIGNAR VECT PATHSEP NEWFUNC ENDLINE
            | ASIGNAR VECTMACRO BRACKETL BRACKETR ENDLINE
            | ASIGNAR VECT PATHSEP FROM LPAREN RPAREN ENDLINE
    '''


def p_vector_methods(p):
    '''
    vector_methods : VARIABLE DOT PUSH_VEC LPAREN expresion RPAREN
                    | VARIABLE DOT POP_VEC LPAREN RPAREN
    '''


# JAIME


def p_expresion(p):
    '''
    expresion : STRING
                | U8
    '''


def p_tipos(p):
    '''
    tipos : DATATYPES
            | NUMDATATYPES
    '''


# all
parser = yacc.yacc(start='rust')

while True:
    try:
        s = input('calc > ')
    except EOFError:
        break
    if not s:
        continue
    result = parser.parse(s)
    print(result)
