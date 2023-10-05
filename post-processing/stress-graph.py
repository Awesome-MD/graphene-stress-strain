import pandas as pd
import matplotlib.pyplot as plt

df = None
with open('../log.lammps') as f:
    content = "".join(f.readlines())
    data = content.split("run            500000")[1].split("Loop time of")[0].splitlines()[2:]
    header = [d for d in data[0].replace('  ', ' ').strip().split(' ') if d != '']
    numerical = [[float(el2) for el2 in el.replace('  ', ' ').strip().split(' ') if el2 != ''] for el in data[1:]]
    df = pd.DataFrame(numerical, columns=header)
    print(df.info())


plt.plot(df.v_strain, df.v_sigmayy)
plt.show()