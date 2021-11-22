from lexer import tokens
import ply.yacc as yacc


'''
Jaime's Contribution
Asignations for every possible type
Printing Formats
Hashset and methods
'''

start = 'rust'


def p_rust(p):
    '''
    rust : asignacion
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
    '''


def p_asignacion(p):
    '''
    asignacion : declarador ASIGNAR expresion ENDLINE
                | other_operators ENDLINE
    '''


def p_asignacion_sintipo(p):
    '''
    asignacion_sintipo : declarador_sintipo ASIGNAR expresion_sintipo ENDLINE
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


def p_operacion_matematica(p):
    '''
    op_mat : art_exp
            | VARIABLE signo_arit art_exp
            | U8 signo_arit art_exp
    '''


def p_aritmetic_expresion(p):
    '''
    art_exp : VARIABLE signo_arit VARIABLE
            | U8 signo_arit VARIABLE
            | VARIABLE signo_arit U8
            | U8 signo_arit U8
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

# closure


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
    vector_methods : VARIABLE empty DOT empty PUSH_VEC LPAREN expresion RPAREN
                    | VARIABLE empty DOT empty POP_VEC LPAREN RPAREN
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
                | F32
                | VARIABLE
    '''


def p_expresion_sintipo(p):
    '''
    expresion_sintipo : hashset
                        | op_mat
                        | slice_exp
                        | expresion
    '''


# all
parser = yacc.yacc(start='rust')

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

yacc.parse(code)

while True:
    try:
        s = input('code > ')
    except EOFError:
        break
    if not s:
        continue
    result = parser.parse(s)
    print(result)
