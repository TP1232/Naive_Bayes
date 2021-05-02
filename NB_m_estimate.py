import pandas as pd
import numpy as np

# =============================================================================
# ----------------------m-estimate Naïve Bayes Algorithm ----------------------
# =============================================================================

# ------------------- Dataset load -----------
df = pd.read_csv('data/car.data',header = None)



# =============================================================================
# Creating a transform and structre varible to convert and remove unnecessary 
# ------------------features out of the data set------------------------------
# =============================================================================
structure = {   0: ["vhigh_p", "high_p","low_p", "med_p"],
                1: ["vhigh_m", "high_m","low_m" , "med_m"],
                # 2: ["5more", "two" ,"three" , "four"],
                # 3: ["more","2","4"],
                4: ["big", "small","med"],
                # 5: ["high_s","low_s","med_s"],
                6: ["unacc", "acc"],
                # 6: ["unacc", "acc","good","vgood"],
                }


transform = {   0: {"vhigh": "vhigh_p", "high": "high_p","low":"low_p" , "med":"med_p"},
                1: {"vhigh": "vhigh_m", "high": "high_m","low":"low_m", "med":"med_m"},
                # 3: { "2": "two","4": "four"},
                # 5: {"high": "high_s", "low": "low_s","med":"med_s"},
                6: {"good" : "unacc" , "vgood" :"unacc"},
                }

# ============================================================================


# ------------------ Data Processing ------------------

df = df.replace(transform)
df = df.drop([2,3,5],axis=1)

# Selecting tuple based on their prediction to perform class balance 
dff = df[df[6] == 'unacc']
dff_2 = df[df[6] == 'acc']

# va = df[6].value_counts(1)

#  Balanced the classification variable by removing more recods of major class
df_r = pd.concat([dff[:int((len(dff))/3)], dff_2], ignore_index=True)
#  Shuffleing the data sample every time program run
df = df_r.sample(frac = 1)
# traning samples and testing sample divide ----- current is 95% train and 5% for testing 
train_size=int(0.95*df.shape[0])
X_train=df[:train_size]
X_test=df[train_size:]
Y_test =  df[6][train_size:]
m_estimate = 6

# =============================================================================
        

# =============================================================================
# ---------------------Calculating accuracy -------------
def accuracy(y_pred, y_test):
    
#  Converting prediction list and original values to numpy for accuracy calculation
    # y_pred = y_pred.to_numpy()
    y_test = y_test.to_numpy()    
    
    return np.sum(y_pred == y_test)/len(y_test)

# =============================================================================
    

# =============================================================================
# ---------------------------- Look-UP Table ----------------------------------
#  Storing all Probablites in Look -up Tables


look_up_table= {}

for (i,entry) in X_train.iterrows():
            recordDic= entry.to_dict()
            for attribute in recordDic:
                
                value=recordDic[attribute]
                c=recordDic[6]
# Counting varible total occurance for their probablites value
                n_c = len(X_train.loc[((X_train[attribute] == value) & (X_train[6] == c))].index)
                n = len(X_train.loc[(X_train[6] == c)].index)
                # m estimate value and its calculation
                m = m_estimate
                M = len(structure[attribute])
# Prior and M estimate formula
                p= float(1)/M
                prob= float(n_c+m*p)/(n+m)
# Creating a lookup table variable
                look_up_table[str(attribute) + str(value) + c] = prob

# Calculating Probablites for classification class 
O_prob = df[6].value_counts(1).to_dict()

# =============================================================================
#  -------------- Finding vales from LookUp table and put in -----------------
print(50*"#")
y_pre = []
for (i,entry) in X_test.iterrows():
            recordDic= entry.to_dict()
            Record = {}
#Retriving the value of store probablites for given combination
            for c in structure[6]:
                Record[c]= O_prob[c]
                for attribute in recordDic:
                    if not attribute == 6:
                        tmp = str(attribute) + str(recordDic[attribute]) + c
                        tmpValue = look_up_table.get(tmp)
                        if not type(tmpValue)==float:
                            tmpValue=1
                        Record[c]=Record[c]*tmpValue
# Calculating probablites for all class and selecting the max of them
            Max = max(Record, key=Record.get)
            y_pre += [Max]
            

print(accuracy(y_pre,Y_test))

# =============================================================================


`