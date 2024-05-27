from ctypes import cdll
import os

# Get the absolute path to the directory containing the script
script_dir = os.path.dirname(os.path.abspath(__file__))
# Construct the absolute path to the shared library
lib_path = os.path.join(script_dir, 'libcalculator.so')

# Load the shared library
lib = cdll.LoadLibrary(lib_path)

# Define the Calculator class
class Calculator:
    def __init__(self):
        # Attribute
        self.obj = lib.Calculator_new()

    # Define method
    def add(self, a, b):
        return lib.Calculator_add(self.obj, a, b)
    def multiply(self, a,b):
        return lib.multi(self.obj, a,b)

# Create an instance of Calculator
calculator = Calculator()

a, b = map(int, input("duriin 2 toogoo oruulna uu: ").split())

result = calculator.multiply(a,b)

# Print the result
print(f"The sum of {a} and {b} is:", result)
