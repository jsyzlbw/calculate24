from itertools import permutations, product
from fractions import Fraction
from random import randint
from typing import List, Tuple, Optional
from operator import add, sub, mul, div

# Define the 4 basic operators
OPS = [
    ('+', add),
    ('-', sub),
    ('*', mul),
    ('/', div),
]

def generate_numbers() -> List[int]:
    """Generate 4 random numbers between 1 and 13."""
    return [randint(1, 13) for _ in range(4)]

def apply_op(x: Fraction, y: Fraction, op_idx: int) -> Optional[Fraction]:
    """Apply the operator at op_idx to two Fractions, return None if invalid (e.g., division by zero)."""
    return OPS[op_idx][1](x, y)

def generate_expressions(nums: List[int], ops: List[str]) -> List[str]:
    """Generate the 5 bracket forms for 4 numbers and 3 operators."""
    a, b, c, d = map(str, nums)
    op1, op2, op3 = ops
    return [
        f"(({a}{op1}{b}){op2}{c}){op3}{d}",
        f"({a}{op1}({b}{op2}{c})){op3}{d}",
        f"({a}{op1}{b}){op2}({c}{op3}{d})",
        f"{a}{op1}(({b}{op2}{c}){op3}{d})",
        f"{a}{op1}({b}{op2}({c}{op3}{d}))"
    ]

def calculate24(nums: List[int]) -> Tuple[bool, Optional[str]]:
    """Try to find a solution using nums to reach 24. Returns (True, expression) or (False, None)."""
    target = Fraction(24, 1)
    
    # Try all permutations of numbers and all operator combinations
    for num_perm in permutations(nums):
        for ops_idx in product(range(4), repeat=3):
            a, b, c, d = map(Fraction, num_perm)
            o1, o2, o3 = ops_idx
            
            # 5 possible bracket patterns
            patterns = [
                apply_op(apply_op(apply_op(a, b, o1), c, o2), d, o3),
                apply_op(apply_op(a, apply_op(b, c, o2), o1), d, o3),
                apply_op(apply_op(a, b, o1), apply_op(c, d, o3), o2),
                apply_op(a, apply_op(apply_op(b, c, o2), d, o3), o1),
                apply_op(a, apply_op(b, apply_op(c, d, o3), o2), o1),
            ]
            
            for idx, val in enumerate(patterns):
                if val is not None and val == target:
                    expr = generate_expressions(num_perm, [OPS[i][0] for i in ops_idx])[idx]
                    return True, expr
    return False, None

# ======================
# Main program
# ======================
while True:
    numbers = generate_numbers()
    ok, solution = calculate24(numbers)
    if ok:
        break

print("Try to get 24 using these four numbers:")
print(numbers)
input("Think about it, then press Enter to see the solution.")
print("Solution:", solution)
