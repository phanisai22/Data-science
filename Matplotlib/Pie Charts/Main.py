from matplotlib import pyplot as plt
import numpy as np 

# print(plt.style.available)

plt.style.use("fivethirtyeight")

slices = [59219, 55466, 47544, 36443, 35917, 31991, 27097,
          23030, 20524, 18523, 18017, 7920, 7331, 7201, 5833]
labels = ['JavaScript', 'HTML/CSS', 'SQL', 'Python', 'Java', 'Bash/Shell/PowerShell',
          'C#', 'PHP', 'C++', 'TypeScript', 'C', 'Other(s):', 'Ruby', 'Go', 'Assembly']

explode = np.zeros(len(labels))
explode[3] = 0.1
explode[0] = 0.1

plt.pie(slices, labels=labels, wedgeprops={"edgecolor": "black" }, explode=explode, autopct="%1.1f%%")

plt.title("Awesome PieChart")
plt.tight_layout()
plt.savefig("plot.png")
plt.show()


# Colors:
# Blue = #008fd5
# Red = #fc4f30
# Yellow = #e5ae37
# Green = #6d904f
