from ghz_naive import ghz_naive
ghz_naive_circ=ghz_naive()
ghz_naive_circ.ghz_9_circ()
ghz_naive_circ.ghz_depth()
# ghz_naive_circ.ghz_transpile()
print(f"Valid GHZ state:{ghz_naive_circ.valid()}")