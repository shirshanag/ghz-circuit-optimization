from ghz_optimized import ghz_9
ghz_optimized=ghz_9()
ghz_optimized.ghz_9_circ()
ghz_optimized.ghz_depth()
# ghz_optimized.ghz_transpile()
print(f"Valid GHZ:{ghz_optimized.valid()}")
