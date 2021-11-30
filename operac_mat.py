def p_signos_aritmeticos(p):
    '''
    signo_arit : MAS
                | MENOS
                | MULT
                | DIVISION
                | MODULO
    '''

def p_operacion_matematica(p):
    '''
    op_mat : ope_u8
            | ope_f32
            | ope_i8
    '''

def p_ope_u8(p):
    '''
    ope_u8 : U8 signo_arit U8
            | U8 signo_arit VARIABLE
            | VARIABLE signo_arit U8
            | U8 signo_arit ope_u8
            | VARIABLE signo_arit ope_u8
    '''

def p_ope_f32(p):
    '''
    ope_f32 : F32 signo_arit F32
            | F32 signo_arit VARIABLE
            | VARIABLE signo_arit F32
            | F32 signo_arit ope_f32
            | VARIABLE signo_arit ope_f32
    '''

def p_ope_i8(p):
    '''
    ope_i8 : I8 signo_arit I8
            | I8 signo_arit VARIABLE
            | VARIABLE signo_arit I8
            | I8 signo_arit ope_i8
            | VARIABLE signo_arit ope_i8
    '''



