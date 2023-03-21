import random
import matplotlib.pyplot as plt
print('주사위를 60000회 던집니다.')

result=[0]*6

dice = []
for i in range(60000) :
    dice.append(random.randint(1,6))
print(dice)

for i in range(60000):
    dice=random.randint(1,6)
    result[dice-1] += 1
    
for i in range(6):
    result[i]/=60000

    
plt.bar(range(1,7),result)
plt.ylim(0,0.2)
plt.ylabel('prob')
plt.xlabel('dice number')
plt.show()

plt.pie(result,autopct='%2.2f%%',labels=range(1,7))
plt.show()