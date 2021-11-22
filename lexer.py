import ply.lex as lex
from colorama import Fore, Style


# APORTE EDDO
reserved = {
    'let': 'LET',
    'mut': 'MUT',
    'type': 'TYPE',
    'unit': 'UNIT',
    'fn': 'FUNCTION',
    'return': 'RETURN',
    'true': 'B_TRUE',
    'false': 'B_FALSE',
    'if': 'IF',
    'else': 'ELSE',
    'while': 'WHILE',
    'for': 'FOR',
    'as': 'AS',
    'loop': 'LOOP',
    'pub': 'PUB',
    'static': 'STATIC',
    'async': 'ASYNC',
    'break': 'BREAK',
    'enum': 'ENUM',
    'match': 'MATCH',
    'ref': 'REF',
    'unsafe': 'UNSAFE',
    'await': 'AWAIT',
    'const': 'CONST',
    'extern': 'EXTERN',
    'impl': 'IMPL',
    'mod': 'MOD',
    'super': 'SUPER',
    'use': 'USE',
    'dyn': 'DYN',
    'continue': 'CONTIN',
    'in': 'IN',
    'move': 'MOVE',
    'self': 'SELFLOWERCASE',
    'Self': 'SELF',
    'trait': 'TRAIT',
    'where': 'WHERE',
    'crate': 'CRATE',
    'tuple': 'TUPLE',
    'insert': 'INSERT_HASH',
    'union': 'UNION_HASH',
    'push': 'PUSH_VEC',
    'pop': 'POP_VEC',
    'contains': 'CONTAINS_SLICE',
    'get': 'GET_SLICE',
    'println': 'PRINT',
    'vec!': 'VECTMACRO',
    'Vec': 'VECT',
    'from': 'FROM'
}
'''
Jaime's contribution
Tokens and regular expressions (regex) for simple tokens
'''

tokens = (
    'READ',
    'NUMBER',
    'MAS',
    'MENOS',
    'MULT',
    'DIVISION',
    'MODULO',
    'OR',
    'AND',
    'ANDAND',
    'OROR',
    'NOT',
    'LESST',
    'GREATER',
    'LESSEQ',
    'GREATEQ',
    'EQUAL',
    'DIFFERENT',
    'LPAREN',
    'RPAREN',
    'MAYOR',
    'MAYORIGUAL',
    'ASIGNAR',
    'DATATYPES',
    'VARIABLE',
    'STRING',
    'NUMDATATYPES',
    'U8',
    'ASIGNATION_TYPE',
    'ARROW',
    'COMMA',
    'LLAVEIZ',
    'LLAVEDER',
    'BRACKETR',
    'BRACKETL',
    'DOLLAR',
    'DOT',
    'DOTDOTDOT',
    'ERRORPROP',
    'PATHSEP',
    'PLUSEQ',
    'MINUSEQ',
    'STAREQ',
    'SLASHEQ',
    'ENDLINE',
    'PRINTS',
    'NEWFUNC',
    'HASHSET',
    'STRUCT'
) + tuple(reserved.values())

t_MAS = r'\+'
t_MENOS = r'-'
t_MULT = r'\*'
t_DIVISION = r'/'
t_MODULO = r'%'
t_OR = r'\|'
t_AND = r'&'
t_ANDAND = r'&&'
t_OROR = r'\|\|'
t_NOT = r'!'
t_LESST = r'<'
t_GREATER = r'>'
t_LESSEQ = r'<='
t_GREATEQ = r'>='
t_EQUAL = r'=='
t_DIFFERENT = r'!='
t_ASIGNAR = r'='
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_STRING = r'\"[a-zA-Z0-9_{}]*\"'
t_U8 = r'25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9]'
t_ENDLINE = r';'
t_ASIGNATION_TYPE = r':'
t_ARROW = r'->'

t_PATHSEP = r'::'
t_PLUSEQ = r'\+='
t_MINUSEQ = r'-='
t_STAREQ = r'\*='
t_SLASHEQ = r'\/='
t_HASHSET = r'HashSet'

'''
Joangie's contribution
Tests and rules for the lexer and adding special characters
'''
t_LLAVEIZ = r'\{'
t_LLAVEDER = r'\}'
t_BRACKETR = r'\]'
t_BRACKETL = r'\['
t_DOLLAR = r'\$'
t_DOT = r'\.'
t_DOTDOTDOT = r'\.\.\.'
t_COMMA = r','
t_ERRORPROP = r'\?'

# These are not tokens but they need to be ignored by the lexer


def t_COMMENT_SIMPLE(t):
    r'//(.*?)\n'
    pass


def t_COMMENT_DOUBLE(t):
    r'/\*'
    pass


def t_WHITESPACE(t):
    r'\s+'
    pass


# Included on symbols and special characters this might change later jajaja -Joangie


# define a rule so we can track line numbers


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


def t_STRUCT(t):
    r'struct'
    return t


def t_NUMDATATYPES(t):
    r'u8 | u16 | u32 | u64 | i8 | i16 | i32 | i64 | f32 | f64'
    return t


def t_DATATYPES(t):
    r'bool | char | str'
    return t


def t_PRINTS(t):
    r'format! | print! | println! | eprint! | eprintln!'
    return t


def t_NEWFUNC(t):
    r'new\(\)'
    return t


def t_FROM(t):
    r'from'
    return t


def t_VECTMACRO(t):
    r'vec!'
    return t


def t_VECT(t):
    r'Vec'
    return t


def t_VARIABLE(t):
    r'[a-z][a-zA-Z_$0-9]*'
    print(t.value)
    t.type = reserved.get(t.value, 'VARIABLE')
    return t


# Error handling rule


def t_error(t):
    print("Componente léxico no reconocido '%s'" % t.value[0])
    t.lexer.skip(1)


lexer = lex.lex()


def menu():
    print("""   Bienvenido al analizador lexico    
    1. Pruebas por defecto 
    2. Prueba manual    
    3. Salir
    """)


def opciones(opc):
    if(opc == 1):
        data = '''
 
let mut x = 10;
let mut y = 20;
let mut z: u8 = x + y;
_x2 = x + y; 

//Hola
fn add(x: u8, y: u8) -> u8 {
        return x + y;
    }




'''
    if opc == 2:
        data = input("Ingrese su codigo:")

    if opc == 3:
        return

    # Give the lexer some input
    lexer.input(data)

    # Tokenize
    while True:
        tok = lexer.token()
        if not tok:
            break  # No more input
        print(tok)


if __name__ == '__main__':

    opc = 0
    while(opc != 3):
        menu()
        opc = int(input("Seleccione su opcion: "))
        opciones(opc)
        print("")
