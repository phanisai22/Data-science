import pandas as pd
from matplotlib import pyplot as plt

plt.style.use("seaborn")

data = pd.read_csv(
    "C:\\Users\\uppup\\Documents\\Git Clones\\Data-science\\Matplotlib\\Scatter Plots\\2019-05-31-data.csv")
view_count = data["view_count"]
likes = data["likes"]
ratio = data["ratio"]

plt.scatter(view_count, likes, c=ratio, cmap="summer", edgecolors="Black", alpha=0.75)

cbar = plt.colorbar()
cbar.set_label("Like/Dislike ratio")

plt.xscale("log")
plt.yscale("log")

plt.title("Trending youtube videos")
plt.xlabel("View count")
plt.ylabel("Total likes")

plt.tight_layout()
# plt.savefig("Main_plot.png")
plt.show()
