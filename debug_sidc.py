import sys
import os

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from milsymbol import Symbol

sidc = "130310000012110007061100000000"
print(f"Testing SIDC: {sidc}")

# Instantiate symbol
symbol = Symbol(sidc)

# Access internal metadata to see how it parsed
# We'll use the getMetadata method if available or inspect internal properties
print(f"Symbol properties: {symbol.getMetadata()}")
