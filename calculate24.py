#general idea

#main function: create 4 numbers (1-13) randomly , examine whether they can calculate 24
#if can't, create 4 #s again
#if can , print it out , and let the user to think
#if the user press enter, show him the answer

#the basic tools
#1.create_numbers: create 4 numbers (1-13) , and return in the form of a list
#2.examine: check whether they can form 24, return True/False, the answer

#main problem: how to construct examine?
#nums[a]_+-*/_nums[b]_+-*/_nums[c]_+-*/_nums[d]
#first, choose two nums 
#secomd, try +-*/, let it be temp1
#third, choose another num, try +-*/, let it be temp2
#fourth, choose the last one, try +-*/, examine __ ?= 24


from typing import List, Tuple
from random import randint
from fractions import Fraction
from itertools import permutations

def create_numbers() ->List:
    return [ randint( 1, 13 ), randint( 1, 13 ), randint( 1, 13 ), randint( 1, 13 ) ]

def get_the_numbers() -> List:
    return [list(p) for p in permutations(range(4))]

def try_four_operations( two_nums: List ) -> List:
    for i in range(2):
        two_nums[ i ] = Fraction ( two_nums[i] )
    return [ two_nums[0] + two_nums[1] ,
                two_nums[0] - two_nums[1] , 
                two_nums[0] * two_nums[1] , 
                two_nums[0] / two_nums[1] ]

def print_out_expression( i: int , number1: int, number2: int ) ->str :
    if i == 0:
        return f"{ number1 } + { number2 } = { number1 + number2 }\n"
    if i == 1:
        return f"{ number1 } - { number2 } = { number1 - number2 }\n"
    if i == 2:
        return f"{ number1 } * { number2 } = { number1 * number2 }\n"
    if i == 3:
        return f"{ number1 } / { number2 } = { number1 / number2 }\n"

def examine( nums: List ) -> Tuple[ bool, str ] :
    temp1 = try_four_operations( [ nums[ 0 ] , nums[ 1 ] ] )
    for i in range( 4 ):
        temp2 = try_four_operations( [ temp1[ i ] , nums[ 2 ] ] )
        for j in range( 4 ):
            temp3 = try_four_operations( [ temp2[ j ] , nums[ 3 ] ] )
            for k in range( 4 ):
                if 24 == temp3[ k ]:
                    expression = ( print_out_expression( i , nums[ 0 ] , nums[ 1 ] ) 
                                    + print_out_expression( j , temp1[ i ] , nums[ 2 ] ) 
                                    + print_out_expression( k , temp2[ j ] , nums[ 3 ] ) )
                    return True, expression
    return False , None

def examine_all( nums: List ) -> Tuple[ bool, str ] :
    flag = False
    for list2 in get_the_numbers() :
        nums_temp = [ nums[ list2[0] ] , nums[ list2[ 1 ]] , nums[ list2[2] ] , nums[ list2[3] ] ]
        flag , expression = examine( nums_temp )
        if flag :
            return True , expression
    return False , None

#now we have constructed the basic tools

#main function: create 4 numbers (1-13) randomly , examine whether they can calculate 24
#if can't create 4 #s , again
#if can , print it out , and let the user to think
#if the user press enter, show him the answer 
while True:
    list1 = create_numbers()
    flag , expression = examine_all ( list1 )
    if flag:
        break

print("Attempt to obtain 24 by applying the four arithmetic operations to these four numbers.")
print(list1[0] , list1[1] , list1[2] , list1[3])
print("\n")
input("Please think for a while, and press 'Enter' to see the answer.")
print(expression)