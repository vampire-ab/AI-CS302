import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y1 = [3.779036283493042, 4.945213317871094,
      5.52109956741333, 4.976000547409058, 4.900119066238403]
y2 = [9.627954006195068, 10.389164209365845,
      10.441717624664307, 13.90779161453247, 15.597124576568604]
      
plt.plot(x, y1, label="A*")
plt.plot(x, y2, label="Best First")
plt.xlabel("Each game played")
plt.ylabel("Time (seconds)")
plt.show()
