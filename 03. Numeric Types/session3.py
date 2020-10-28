from  fractions import Fraction
def encoded_from_base10(number, base, digit_map):
    '''
    This function returns a string encoding in the "base" for the the "number" using the "digit_map"
    Conditions that this function must satisfy:
    - 2 <= base <= 36 else raise ValueError
    - invalid base ValueError must have relevant information
    - digit_map must have sufficient length to represent the base
    - must return proper encoding for all base ranges between 2 to 36 (including)
    - must return proper encoding for all negative "numbers" (hint: this is equal to encoding for +ve number, but with - sign added)
    - the digit_map must not have any repeated character, else ValueError
    - the repeating character ValueError message must be relevant
    - you cannot use any in-built functions in the MATH module

    '''

    if base <2 or base>36:
        raise ValueError("The base value should be in greaters than equal to 2 and less than equal to 36 ")
    if len(digit_map)<base:
        raise ValueError("The digit_map length should be atleast the size of the base so that it can match properly")
    if len(digit_map) != len(set(digit_map)):
        raise ValueError("There are repeating words in the string, it requires unique words")
    digit = []
    check = 0
    if number < 0:
        check = 1
        number = -number
    while number> 0:
        m = number%base
        number = number // base
        digit.insert(0,m)
    if check ==1:
        return '-'+''.join(map(lambda x:digit_map[x],digit))
    else:
        return ''.join(map(lambda x:digit_map[x],digit))


def float_equality_testing(a, b):
    '''
        This function emulates the ISCLOSE method from the MATH module, but you can't use this function
        We are going to assume:
        - rel_tol = 1e-12
        - abs_tol = 1e-05
    '''
    rel_tol = 1e-12
    abs_tol = 1e-05
    tol_tol = max(rel_tol*max(abs(a),abs(b)),abs_tol)
    return abs(a-b) < tol_tol


def manual_truncation_function(f_num):
    '''
    This function emulates python's MATH.TRUNC method. It ignores everything after the decimal point. 
    It must check whether f_num is of correct type before proceed. You can use inbuilt constructors like int, float, etc
    '''
    if f_num >= 0:
        return f_num //1
    else:
        return f_num//1 + 1

def manual_rounding_function(f_num):
    '''
    This function emulates python's inbuild ROUND function. You are not allowed to use ROUND function, but
    expected to write your one manually.
    '''
    if f_num > 0:
        quo,rem = f_num//1,f_num%1
        rvalue = quo
        if rem >= 0.5:
            rvalue = rvalue + 1
    elif f_num == 0:
        rvalue = 0
    else:
        quo,rem = f_num//1+1,f_num%1
        rvalue = quo
        if rem < -0.5:
            rvalue = rvalue + 1
    return rvalue

def rounding_away_from_zero(f_num):
    '''
    This function implements rounding away from zero as covered in the class
    Desperately need to use INT constructor? Well you can't. 
    Hint: use FRACTIONS and extract numerator. 
    '''
    return 3.0