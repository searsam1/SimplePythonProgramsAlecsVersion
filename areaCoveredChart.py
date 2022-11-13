import matplotlib.pyplot as plt  #to run this code, I had to install matplotlib on my machine running Manjaro Linux 
No_of_people_voted = [23,45,31,40,35]
plt.bar(['a1','a2','a3','a4','a5'], No_of_people_voted)
plt.title('Bar Chart')
plt.xlabel('Area covered')
plt.ylabel('No. of people voted')
[plt.show()]