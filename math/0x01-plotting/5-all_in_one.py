#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

y0 = np.arange(0, 11) ** 3

mean = [69, 0]
cov = [[15, 8], [8, 15]]
np.random.seed(5)
x1, y1 = np.random.multivariate_normal(mean, cov, 2000).T
y1 += 180

x2 = np.arange(0, 28651, 5730)
r2 = np.log(0.5)
t2 = 5730
y2 = np.exp((r2 / t2) * x2)

x3 = np.arange(0, 21000, 1000)
r3 = np.log(0.5)
t31 = 5730
t32 = 1600
y31 = np.exp((r3 / t31) * x3)
y32 = np.exp((r3 / t32) * x3)

np.random.seed(5)
student_grades = np.random.normal(68, 15, 50)

fig = plt.figure()
grid = fig.add_gridspec(3, 2)
ax1 = fig.add_subplot(grid[0, 0])
ax2 = fig.add_subplot(grid[0, 1])
ax3 = fig.add_subplot(grid[1, 0])
ax4 = fig.add_subplot(grid[1, 1])
ax5 = fig.add_subplot(grid[2, :])
fig.suptitle('All in One')

ax1.plot(y0, 'r')

ax2.scatter(x1, y1, c='m')
ax2.set_xlabel('Height (in)', size='x-small')
ax2.set_ylabel("Weight (lbs)", size='x-small')
ax2.set_title("Men's Height vs Weight", size='x-small')

ax3.plot(x2, y2)
ax3.set_xlabel("Time (years)", size='x-small')
ax3.set_ylabel("Fraction Remaining", size='x-small')
ax3.set_title("Exponential Decay of C-14", size='x-small')
ax3.set_xlim(0, 28650)
ax3.set_yscale('log')

ax4.plot(x3, y31, 'r--', label="C14")
ax4.plot(x3, y32, 'g', label="Ra-226")
ax4.set_xlim(0, 20000)
ax4.set_ylim(0, 1)
ax4.set_xlabel("Time (years)", size='x-small')
ax4.set_ylabel("Fraction Remaining", size='x-small')
ax4.set_title("Exponential Decay of Radioactive Elements", size='x-small')
ax4.legend()

bins = range(0, 101, 10)
ax5.hist(student_grades, bins, edgecolor='black')
ax5.set_xticks(bins)
ax5.set_xlim(0, 100)
ax5.set_ylim(0, 30)
ax5.set_xlabel("Grades", size='x-small')
ax5.set_ylabel("Number of Students", size='x-small')
ax5.set_title("Project A", size='x-small')

plt.tight_layout()
plt.show()
