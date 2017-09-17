# importing pandas, numpy and matplotlib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
from collections import Counter

#reading file 
hubway_data = np.genfromtxt("hubway.txt", delimiter=",")

# generating numpy array
duration = np.array(hubway_data[:,3], dtype=float)
start_stn = np.array(hubway_data[:,5], dtype=float)
end_stn= np.array(hubway_data[:,7], dtype=float)
user_id = np.array(hubway_data[:,1], dtype=float)
birth_year = np.array(hubway_data[:,11], dtype=float)
age = np.array(2016-birth_year, dtype = float)
gender = np.array(hubway_data[:,-1], dtype=float)

#filtering and sorting to get required data from male visitors
yt= np.unique(start_stn)
p = len(yt)
male_age_stn = [0]*len(yt)
stn = [0]* len(yt)
t=[0]*len(duration)
u=[0]*len(duration)
r=[0]*len(yt)
avg_age=[0]*len(yt)
avg_dur=[0]*len(yt)
z=[0]*len(start_stn)

for i in range (0,p):
  pp = gender == 1    
  dd= start_stn == yt[i]
  ll= (age>10) & (age<60) #input required age
  kk=np.logical_and(dd,pp)
  lk=np.logical_and(ll,pp)
  f=np.logical_and(lk,kk)
  r=np.sum(f)
  avg_age[i]=np.sum(age[f])/r  # calculating average age of male visitors
  avg_dur[i]=np.sum(duration[f])/r   # calculating average duration of trips
gft= max(avg_dur)
gti=avg_dur.index(gft)

# printing required result
print("maximum average duration is")
print(gft)
stn_max = yt[gti]
print("at station number")
print(stn_max)
print("************************")
gft1= max(avg_age)
gti1=avg_age.index(gft1)
age_max = yt[gti1]
print("station having male visitors with most average age is station number")
print(age_max)
print("and maximum average age is")
print(gft1)
print("************************")
gftc= min(avg_dur)
gtic=avg_dur.index(gft)
print("minimum average duration is")
print(gftc)
stn_min = yt[gtic]
print("at station number")
print(stn_min)
print("************************")
gftc1= min(avg_age)
gtic1=avg_age.index(gftc1)
age_min = yt[gtic1]
print("station having male visitors with least average age is station number")
print(age_min)
print("and minimum average age is")
print(gftc1)
print("************************")

#ploting average age of male visitor visiting each station
plt.scatter(yt,avg_age, s= avg_dur*50, alpha = 0.4, c=avg_dur)
plt.xlabel('station number')
plt.title('Variation of bubble size according to duration at station')
plt.ylabel('Average age of male visitors')
plt.colorbar()
plt.grid(True)
plt.show()

#filtering and sorting to get required data from female visitors
yt2= np.unique(end_stn)
p2 = len(yt2)
r2=[0]*len(yt2)
avg_age_f=[0]*len(yt2)

for ii in range (0,p2):
  var1 = gender == 2    
  var2= end_stn == yt2[ii]
  var3= (age>20) & (age<40)
  f1=np.logical_and(var2,var1)
  f2=np.logical_and(var3,var1)
  f=np.logical_and(f2,f1)
  r2[ii]=np.sum(f)
  avg_age_f[ii]=np.sum(age[f])/r2[ii] # calculating average female age

#station with maximum and minimum female age
val= max(r2)
vari=r2.index(val)  
stn_no_1 = yt2[vari]
val1= min(avg_age_f)
vari1 =avg_age_f.index(val1)
stn_no_2 = yt2[vari1]


# printing required result
print("station with maximum female visitor is station number")
print(stn_no_1)
print("number of female visits is")
print(val)
print("************************")
print("station with least average age of female visitors is")
print(stn_no_2)
print("average age of female visitors at this station is")
print(val1)
print("************************")

#ploting number of female visitors visiting each station
plt.scatter(yt2,r2, s= avg_age_f*50, alpha = 0.4, c=avg_age_f)
plt.xlabel('station number')
plt.title('female visitor at stations')
plt.ylabel('Number of female visitors')
plt.text(30,11, 'variation of color as per average age')
plt.grid(True)
plt.show()

# to find number of trips taken between given start and end station
hub_stn_strt = [36,38] # array to contain list of start station
hub_stn_end = [39,44]  # array to contain list of end stations
for j in range (0,len(hub_stn_strt)):
    s = end_stn == hub_stn_end [j]
    s1= start_stn == hub_stn_strt [j]    
    g1=np.logical_and(s,s1)
    user_array1 = user_id[g1]
    user_array = np.array(user_array1, dtype=int)
    tot=len(user_array)
    #printing required result
    print("total trips taken between start station " + str(hub_stn_strt[j])+" and end stationstr " +str(hub_stn_end[j])+ " is")
    print(tot)
    print("*************************************")


#finding most busy station
for u in range (1,len(start_stn)):
 z[u] = (start_stn[u])*100 + end_stn[u]
op=stats.mode(z)
maxi=op[0]
nots=op[1]
end_station1 = maxi%100
start_station1 = (maxi-end_station1)/100
#printing required result
print("Maximum taffic is between is on route between station " + str(start_station1)+" and station" +str(end_station1))
print("*************************************")

# calculating traffic on each route
for u in range (1,len(start_stn)):
  z[u] = (start_stn[u])*100 + end_stn[u]
op1=Counter(z)
keys = list(op1.keys())
vals = list(op1.values())
maxi=max(vals) #calculating maximum traffic
ank=vals.index(maxi)
number=keys[ank]
itr=vals[ank]
end_station = np.mod(keys, [100]*len(vals))
start_station = (keys-end_station)/100

#ploting a scatter plot for traffic between each route
plt.scatter(start_station, end_station, s=vals*60, alpha = 1,c=vals)
plt.xlabel('Start station')
plt.ylabel('End Station')
plt.title('number of visitors on station routes')
plt.xlim(0, 55)
plt.ylim(0, 55)
plt.text(1, 50, 'color variation as per number of trips')
plt.colorbar()
plt.grid(True)
plt.show()
