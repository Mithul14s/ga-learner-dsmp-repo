# --------------
#Code starts here
import numpy as np

age = census[:,0]
max_age = np.max(age)
min_age = np.min(age)
age_mean = np.mean(age)
age_std = np.std(age)


# --------------
# Importing header files
import numpy as np

#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]

#Code starts here

#Loading data file and saving it into a new numpy array 
data = np.genfromtxt(path, delimiter=",", skip_header=1)

print(data.shape)

#Concatenating the new record to the existing numpy array
census=np.concatenate((data, new_record),axis = 0)

print(census.shape)

#Code ends here


# --------------
#Code starts here
import numpy as np
print(census)
race_0 = census[census[:,2]==0]
race_1 = census[census[:,2]==1]
race_2 = census[census[:,2]==2]
race_3 = census[census[:,2]==3]
race_4 = census[census[:,2]==4]
len_0 = len(race_0)
len_1 = len(race_1)
len_2 = len(race_2)
len_3 = len(race_3)
len_4 = len(race_4)

#Storing the different race lengths with appropriate indexes
race_list=[len_0, len_1,len_2, len_3, len_4]

#Storing the race with minimum length into a variable 
minority_race=race_list.index(min(race_list))


# --------------
#Code starts here

#Subsetting the array based on the age 
senior_citizens=census[census[:,0]>60]

#Calculating the sum of all the values of array
working_hours_sum=senior_citizens.sum(axis=0)[6]

print(working_hours_sum)

#Finding the length of the array
senior_citizens_len=len(senior_citizens)

#Finding the average working hours
avg_working_hours=working_hours_sum/senior_citizens_len

#Printing the average working hours
print((avg_working_hours))

#Code ends here


# --------------
#Code starts here
high = census[census[:,1]>10]
low = census[census[:,1]<=10]
avg_pay_high = high.mean(axis=0)[7]
avg_pay_low = low.mean(axis=0)[7]
print(avg_pay_high>avg_pay_low)


