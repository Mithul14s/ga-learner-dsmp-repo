# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv(path)
loan_status = data['Loan_Status'].value_counts()

loan_status.plot.bar()
plt.xlabel('Loan_Status')
plt.ylabel('Count of each status')
plt.title('Loan Status Bar Plot')
plt.show()


#Code starts here


# --------------
#Code starts here
property_and_loan = data.groupby(['Property_Area','Loan_Status']).size().unstack()
print(property_and_loan['Y'].sort_values())
#property_and_loan=property_and_loan['Y','N'].sort_values(ascending=False)
#property_and_loan.sort_values(property_and_loan['Property_Area'].value_counts).plot.bar()
property_and_loan.plot.bar()
plt.xlabel('Property Area')
plt.ylabel('Loan Status')
plt.xticks(rotation=45)
plt.show()


# --------------
#Code starts here
education_and_loan = data.groupby(['Education','Loan_Status']).size().unstack()
education_and_loan.plot.bar()
plt.xlabel('Education Status')
plt.ylabel('Loan Status')
plt.xticks(rotation=45)
plt.show()


# --------------
#Code starts here

graduate = data[data['Education'] == 'Graduate']
not_graduate = data[data['Education'] == 'Not Graduate']

graduate['LoanAmount'].plot(kind='density',label='Graduate')
not_graduate['LoanAmount'].plot(kind='density',label='Not Graduate')











#Code ends here

#For automatic legend display
plt.legend()


# --------------
#Code starts here
fig,(ax_1,ax_2,ax_3) = plt.subplots(nrows=3,ncols=1)
data.plot.scatter('ApplicantIncome','LoanAmount',ax=ax_1)
ax_1.set_title('Applicant Income')

data.plot.scatter('CoapplicantIncome','LoanAmount',ax=ax_2)
ax_2.set_title('Coapplicant  Income')

data['TotalIncome']=data['ApplicantIncome'] + data['CoapplicantIncome']
data.plot.scatter('TotalIncome','LoanAmount',ax=ax_3)
ax_3.set_title('Total Income')
plt.tight_layout()
plt.legend()


