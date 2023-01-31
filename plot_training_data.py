import matplotlib
from matplotlib import pyplot as plt

x=open('ML_data.csv','r')
m=x.readlines()

m_x=[]
m_y=[]
for i in m:
    m_1=i.split(',')
    m_x.append(float(m_1[0]))
    m_y.append(float(m_1[1]))
  
    
plt.plot(m_x,m_y,'o')
plt.xlabel('X-coordinates represent values of feature A')
plt.ylabel('Y-coordinates represent values of feature B')
plt.show()






