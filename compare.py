from ghz_naive import ghz_naive
from ghz_optimized import ghz_9

naive = ghz_naive()
naive.ghz_9_circ()

alternative = ghz_9()
alternative.ghz_9_circ()

naive_depth=naive.qc_9.depth()
optimized_depth=alternative.qc_9.depth()

print("Naive depth:", naive_depth)
print("Alternative depth:", optimized_depth )


naive_cx=naive.qc_9.count_ops().get('cx',0)
optimized_cx=alternative.qc_9.count_ops().get('cx',0)

print("Naive gates:",naive_cx )
print("Alternative gates:", alternative.qc_9.count_ops())

print("Naive valid:", naive.valid())
print("Alternative valid:", alternative.valid())

import matplotlib.pyplot as plt

names = ["Naive GHZ", "New GHZ"]
depths = [naive_depth, optimized_depth]
cx_counts = [naive_cx, optimized_cx]

plt.bar(names, depths)
plt.ylabel("Circuit Depth")
plt.title("GHZ Circuit Depth Comparison")
plt.show()