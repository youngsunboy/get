from matplotlib import pyplot as plt
def plot_voltage_vs_time(time, voltage, max_voltage):
    plt.figure(figsize=(10,6))
    plt.plot(time, voltage)
    plt.title("V(t)")
    plt.ylabel("voltage V")
    plt.xlabel("time s")
    plt.xlim(left = 0)
    plt.ylim(0,max_voltage)
    plt.grid()
    plt.show()
def plot_sampling_hist(time):
    per = []
    for i in range(len(time)-2):
        per.append(time[i+1]-time[i])
    plt.figure(figsize=(10, 6))
    plt.hist(per)
    plt.title("gist t")
    plt.ylabel("how many times was recorded")
    plt.xlabel("time s")
    plt.xlim(0,0.06)
    plt.grid()
    plt.show()
