from qiskit import QuantumCircuit, transpile, generate_preset_pass_manager
import matplotlib.pyplot as plt
from qiskit.quantum_info import Statevector
from qiskit_ibm_runtime.fake_provider import FakeTorino
from IPython.display import display
import numpy as np 

class ghz_9:
  def __init__(self):
    self.qc_9=None
  def ghz_9_circ(self):
    self.qc_9=QuantumCircuit(9)
    self.qc_9.h(3) #layer1
    self.qc_9.cx(3,5) #layer2
    self.qc_9.cx(5,6) #layer3
    self.qc_9.cx(3,1) #layer3
    self.qc_9.cx(6,7) #layer4
    self.qc_9.cx(3,4) #layer4
    self.qc_9.cx(1,2) #layer5
    self.qc_9.cx(3,0) #layer5
    self.qc_9.cx(7,8) #layer5
    return self.qc_9
  def ghz_depth(self):
    print(f"Depth:{self.qc_9.depth()}")
  def valid(self):
    sv=Statevector(self.qc_9)
    expected=1/np.sqrt(2)
    zero=sv["000000000"]
    one=sv["111111111"]
    return np.isclose(abs(zero),expected) and np.isclose(abs(one),expected)
  # def ghz_transpile(self):
  #   backend=FakeTorino()
  #   qc_copy=self.qc_9.copy()
  #   qc_copy.measure_all()
  #   pm=generate_preset_pass_manager(optimization_level=1,backend=backend)
  #   ghz_qc=pm.run(qc_copy)
  #   print(f"Transpiled Depth:{ghz_qc.depth()}")
  #   print(f"Gate count:{ghz_qc.count_ops()}")

