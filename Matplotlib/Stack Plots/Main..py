import matplotlib.pyplot as plt
import numpy as np

plt.style.use("fivethirtyeight")

minutes = np.arange(1, 10)
player1 = [8, 6, 5, 5, 4, 2, 1, 1, 0]
player2 = [0, 1, 2, 2, 2, 4, 4, 4, 4]
player3 = [0, 1, 1, 1, 2, 2, 3, 3, 4]

labels = ["player1", "player2", "player3"]

plt.stackplot(minutes, player1, player2, player3, labels=labels)

# plt.legend(loc= "upper left")
plt.legend(loc =(0.07, 0.05))

plt.title("Awesome Stack Plot")
plt.tight_layout()
# plt.savefig("plot.png")
plt.show()
