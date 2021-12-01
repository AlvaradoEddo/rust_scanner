import ply.yacc as yacc
import ply.lex as lex
from operac_mat import *
from error_manager import *
from lexer import *


'''
Jaime's Contribution
Asignations for every possible type
Printing Formats
Hashset and methods
'''

start = 'rust'


def p_rust(p):
    '''
    rust : sentencias
    '''

def p_sentencias(p):
    '''
    sentencias : sentencia 
               | sentencia sentencias
               | empty
    '''

def p_sentencia(p):
    '''
    sentencia : asignacion
         | asignacion_sintipo
         | prints
         | hashfunc
         | conditional
         | conditional_asigned
         | for_loop
         | struct_s
         | while_loop
         | empty_vector
         | vector_methods
         | data_vector
         | slice_get
         | slice_contains
         | read_data
        | function
        | empty
    '''


def p_asignacion(p):
    '''
    asignacion : declarador ASIGNAR expresion ENDLINE
                | other_operators ENDLINE
                | op_mat ENDLINE
                | bool_operation ENDLINE
    '''


def p_asignacion_sintipo(p):
    '''
    asignacion_sintipo : declarador_sintipo ASIGNAR expresion_sintipo ENDLINE
    '''


def p_other_operators(p):
    '''
    other_operators : VARIABLE oper_asig expresion_sintipo
    '''


def p_declarador(p):
    '''
    declarador : VARIABLE
                | let_asig
    '''


def p_declarador_sintipo(p):
    '''
    declarador_sintipo : VARIABLE 
                        | let_asig_sintipo
    '''


def p_let_asig(p):
    '''
    let_asig : LET var_tipo
             | LET MUT var_tipo
    '''


def p_let_asig_sintipo(p):
    '''
    let_asig_sintipo : LET MUT VARIABLE
                     | LET VARIABLE
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
    prints : PRINTS empty LPAREN print_expresion RPAREN empty ENDLINE
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
    hashset : HASHSET empty PATHSEP empty NEWFUNC
    '''


def p_hashfunc(p):
    '''
    hashfunc : hashset_insert
            | hashset_union
    '''


def p_hashset_insert(p):
    '''
    hashset_insert : VARIABLE empty DOT empty INSERT_HASH empty LPAREN expresion RPAREN empty ENDLINE
    '''


def p_hashset_union(p):
    '''
    hashset_union : VARIABLE empty DOT empty UNION_HASH empty LPAREN AND empty VARIABLE RPAREN empty ENDLINE
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

def p_bool_operation(p):
    '''
    bool_operation : boolean
                    | boolean AND bool_operation
                    | boolean OR bool_operation
                    | boolean ANDAND bool_operation
                    | boolean OROR bool_operation
    '''

def p_boolean(p):
    '''
    boolean : B_TRUE
            | B_FALSE
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
    f_comparacion : rango
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


def p_signos_aritmeticos(p):
    '''
    signo_arit : MAS
                | MENOS
                | MULT
                | DIVISION
                | MODULO
    '''


def p_rango(p):
    '''
    rango : U8 DOT DOT U8
    '''


def p_slice(p):
    '''
    slice_exp : AND empty VARIABLE empty BRACKETL rango BRACKETR
    '''


def p_slice_get(p):
    '''
    slice_get : VARIABLE empty DOT empty GET_SLICE empty LPAREN valor_get RPAREN
    '''


def p_valor_get(p):
    '''
    valor_get : rango
                | U8
    '''


def p_contains(p):
    '''
    slice_contains : VARIABLE empty DOT empty CONTAINS_SLICE empty LPAREN AND U8 RPAREN
    '''


def p_empty(p):
    'empty :'
    pass


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


def p_read_data(p):
    # io::stdin().read_line(&mut s)
    '''
    read_data : IO empty PATHSEP empty STDIN LPAREN RPAREN empty DOT empty READ LPAREN reference RPAREN ENDLINE
    '''


def p_reference(p):
    '''
    reference : AND empty MUT VARIABLE
    '''

# function


def p_function(p):
    ''' 
    function : no_return_function
              | return_function
    '''


def p_return_function(p):
    '''
    return_function : FUNCTION VARIABLE LPAREN arguments RPAREN ARROW tipos LLAVEIZ rust return LLAVEDER
                    | FUNCTION VARIABLE LPAREN RPAREN ARROW tipos LLAVEIZ rust return LLAVEDER
                    | FUNCTION VARIABLE LPAREN RPAREN ARROW tipos LLAVEIZ return LLAVEDER
    '''


def p_noreturn_function(p):
    '''
    no_return_function : FUNCTION VARIABLE LPAREN arguments RPAREN LLAVEIZ rust LLAVEDER
                | FUNCTION VARIABLE LPAREN RPAREN LLAVEIZ rust LLAVEDER
    '''


def p_arguments(p):
    '''
    arguments : VARIABLE ASIGNATION_TYPE tipos 
                | VARIABLE ASIGNATION_TYPE tipos COMMA arguments
    '''


def p_return(p):
    '''
    return : RETURN expresion ENDLINE
            | expresion
    '''

# # closure
# def p_closure(p):
#     '''
#     closure :  let_asig_sintipo ASIGNAR orclosure ARROW tipos LLAVEIZ expresion LLAVEDER ENDLINE
#     '''


# def p_orclosure(p):
#     '''
#     orclosure : OR var_tipo OR
#     '''

# vector


def p_empty_vector(p):
    '''
    empty_vector : declare_vector types_vector empty_vec

    '''


def p_data_vector(p):
    '''
    data_vector : declare_vector types_vector vector_content
                | declare_vector ASIGNAR VECTMACRO BRACKETL element_type COMMA vector_elements BRACKETR ENDLINE

    '''


def p_vector_content(p):
    '''
    vector_content : ASIGNAR VECTMACRO vect_list ENDLINE
                    | ASIGNAR VECT PATHSEP FROM LPAREN vect_list RPAREN ENDLINE
    '''


def p_vector_list(p):
    '''
    vect_list : BRACKETL vector_elements BRACKETR
    '''


def p_vector_elements(p):
    '''
    vector_elements : expresion
                    | expresion COMMA vector_elements
    '''


def p_element_type(p):
    '''
    element_type : U8 empty NUMDATATYPES
    '''


def p_types_vector(p):
    '''
    types_vector : VECT empty LESST DATATYPES GREATER
                | VECT empty LESST NUMDATATYPES GREATER
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
    vector_methods : VARIABLE empty DOT empty PUSH_VEC LPAREN expresion RPAREN ENDLINE
                    | VARIABLE empty DOT empty POP_VEC LPAREN RPAREN ENDLINE
    '''


# JAIME

def p_tipos(p):
    '''
    tipos : DATATYPES
            | NUMDATATYPES
    '''


def p_expresion(p):
    '''
    expresion : STRING
                | U8
                | I8
                | F32
                | VARIABLE
                | op_mat
                | bool_operation
                | hashset
    '''


def p_expresion_sintipo(p):
    '''
    expresion_sintipo : hashset
                        | slice_exp
                        | expresion
    '''


# all

code = '''
fn main() {
let mut counter = 0;
let mut counter_2 = 20;
let mut a: Vec<i32> = vec![1,2,3,4];
let mut v: Vec<i32> = Vec::from([1,2,3,4]);

let mut set = HashSet::new();
set.insert("a");
set.insert("b");
let x = &mut [1, 2, 3];
for n in numbers {
    println!("hola");
}

while counter<10 && counter_2 > 0{
    counter+=1;
    counter_2-=1;
    v.push(counter_2);
    println!("hola");
}

v.pop();

}
'''

# yacc.parse(code)


#parser = yacc.yacc(start='rust')

# while True:
#     try:
#         s = input('code > ')
#     except EOFError:
#         break
#     if not s:
#         continue
#     result = parser.parse(s)
#     print(result)

def p_error(p):
    if p is not None:
        print(f"Syntax error in line {p.lineno} at {p.value}\n")
        error_manager.syntax_err += 1
        error_manager.syntax_err_descript += f"Syntax error in line {p.lineno} at {p.value}\n"
    else:
        print("Syntax error at EOF\n")
        error_manager.syntax_err += 1
        error_manager.syntax_err_descript += f"Syntax error at EOF.\n"


def run_parser(code):
    run_lexer(code)
    parser = yacc.yacc(start='rust')
    result = parser.parse(code)
    return result
