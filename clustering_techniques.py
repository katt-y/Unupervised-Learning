# the plot for the data points without running any clustering technique are stored in main_20155_plot.py
#You have to run this file
# Note that DB scan is the best clustering technique for this kind of dataset.
# Executing this file would provide you with the the plots for different clustering techniques.
# running file for DBSCAN .i.e. entering 1 as the input would overwrite a text file called 'DB_2.txt' with datasets and their labels
#  Running the file for each clustering technique returns the plots for them
#   a nested array will only be printed when you run it for DBScan
# Class labels are stored in the DB.txt file permanently.
# DB_2.txt file gets overwitten everytime you run this program for DBScan.
# 
# DB scan is also  submitted using a seperate file called 20155_best.py
#
#  you will have to kill the terminal after every run to run the code again.




from sklearn.cluster import KMeans
from sklearn.cluster import AgglomerativeClustering
from sklearn.cluster import DBSCAN
from sklearn.cluster import SpectralClustering
from sklearn.cluster import BisectingKMeans
import matplotlib
from matplotlib import pyplot as plt
import sys

class techniques():
    def __init__(self,path='ML_data.csv'):

        self.path=path
        x=open(self.path,'r')
        m=x.readlines()
        m_train=[]
        for i in m:
          m_0=[]
          m_1=i.split(',')
          m_0.append(float(m_1[0]))
          m_0.append(float(m_1[1]))
          m_train.append(m_0)

        self.data= m_train

    def K_means(self):

        kmeans = KMeans(n_clusters=2, random_state=0).fit(self.data)
        m_trains_2=[]

        for i in range(len(self.data)):
    
         m_trains_2.append([self.data[i][0],self.data[i][1],kmeans.labels_[i]])
        

        for i in m_trains_2:
          if i[2]==0:
             plt.plot(i[0],i[1],'o',color='red')
          else:
             plt.plot(i[0],i[1],'o',color='green')
        plt.show()
        return m_trains_2


        
        




        
       

    def spectral_clustering(self):
     spectral_clustering = SpectralClustering(n_clusters=2, assign_labels='kmeans',random_state=0).fit(self.data)
     
     m_trains_2=[]

     for i in range(len(self.data)):
    
      m_trains_2.append([self.data[i][0],self.data[i][1],spectral_clustering.labels_[i]])
        

     for i in m_trains_2:
          if i[2]==0:
             plt.plot(i[0],i[1],'o',color='red')
          else:
             plt.plot(i[0],i[1],'o',color='green')
      
     plt.show()

     return m_trains_2


      



    def agglomerative_clustering(self):
        
        agg_clustering_ward = AgglomerativeClustering(n_clusters=2).fit(self.data)

        m_trains_2=[]

        for i in range(len(self.data)):
    
         m_trains_2.append([self.data[i][0],self.data[i][1],agg_clustering_ward.labels_[i]])
        

        for i in m_trains_2:
          if i[2]==0:
             plt.plot(i[0],i[1],'o',color='red')
          else:
             plt.plot(i[0],i[1],'o',color='green')
        plt.show()
        return m_trains_2

    def bisectingKmeans(self):
       

       bisecting_KMeans = BisectingKMeans(n_clusters=2, random_state=0,max_iter=300).fit(self.data)
       
       m_trains_2=[]

       for i in range(len(self.data)):
    
          m_trains_2.append([self.data[i][0],self.data[i][1],bisecting_KMeans.labels_[i]])
        

       for i in m_trains_2:
          if i[2]==0:
             plt.plot(i[0],i[1],'o',color='red')
             
          else:
             plt.plot(i[0],i[1],'o',color='green')
       plt.show()  
       return m_trains_2


    def DBscan(self):
        DB = DBSCAN(eps=.06).fit(self.data)
        j=0
        k=open('DB_2.csv','w')
        for i in self.data:
           k.write('{},{},{}\n'.format(i[0],i[1],DB.labels_[j]))

           j+=1

        index=[]
        inlier_list=[0,1]
        for i in list(range((len(DB.labels_)))):
         if DB.labels_[i] not in inlier_list :
          index.append(i)

        
        def distance(a,b):
         d=((a[0]-b[0])**2+(a[1]-b[1])**2)**(1/2)
         return d

        def shortest_distance_label(a):
         l=distance(a,[100,100])
    
         for i in range(len(self.data)):
          if i in index:
            continue
          else:
            m=distance(self.data[i],a)
            if m<l:
                l=m
                k=DB.labels_[i]
         return k 

        m_trains_2=[]

        for i in range(len(self.data)):
         if i in index:
          m_trains_2.append([self.data[i][0],self.data[i][1],shortest_distance_label(self.data[i])])
         else:
          m_trains_2.append([self.data[i][0],self.data[i][1],DB.labels_[i]])

        print(m_trains_2)
        
        for i in m_trains_2:
          if i[2]==0:
            plt.plot(i[0],i[1],'o',color='red')
          else:
            plt.plot(i[0],i[1],'o',color='green')
        plt.show()

        f=open('DB_2.txt','w')
        for i in m_trains_2:
           f.write('{},{},{}\n'.format(i[0],i[1],i[2]))
        return m_trains_2

ex=techniques()

x=input('Please enter the code clustering technique of which you want to see the results (DBSCAN:1,Agglomerative Clustering:2,K-means:3, Spectral Clustering:4,Bisecting KMeans=5): ')

if x=='1':
   y=ex.DBscan()
elif x=='2':
     y=ex.agglomerative_clustering()
elif x=='3':
    y=ex.K_means()
elif x=='4':
   y=ex.spectral_clustering()
elif x=='5':
    y=ex.bisectingKmeans()
else:
    print('Please give a valid input')


print(y)






        







        
