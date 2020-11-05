from sklearn import preprocessing
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time
import matplotlib.ticker as ticker
import matplotlib.ticker as plticker
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression


results = pd.read_csv('EPL_Set2.csv')
label_enc = preprocessing.LabelEncoder()
label_enc1=preprocessing.LabelEncoder()
prev_time=time.time()
winner=[]
for i in range(len(results['HomeTeam'])):
	if results['FTR'][i]=='H':
		winner.append(results['HomeTeam'][i])
	elif results['FTR'][i]=='A':
		winner.append(results['AwayTeam'][i])
	else:
		winner.append('Draw')

results['winning_team']=winner

# results.to_csv('EPL_Set2.csv')				

#print(results.head())

data=results.drop(['FTHG','FTAG','HTHG','HTAG','FTR','HTR','Season'],axis=1)

# print(data.head())

data.loc[data.winning_team == data.HomeTeam,'winning_team']=2
data.loc[data.winning_team == 'Draw', 'winning_team']=1
data.loc[data.winning_team == data.AwayTeam, 'winning_team']=0

# print(data.head())

# final = pd.get_dummies(data, prefix=['home_team', 'away_team'], columns=['HomeTeam', 'AwayTeam'])

data2=data['HomeTeam']
label_enc.fit(data2)
data['HomeTeam'] = label_enc.transform(data['HomeTeam'])

# print("label encode home")
# print(data.head())

data1=data['AwayTeam']
label_enc.fit(data1)
data['AwayTeam'] = label_enc.transform(data['AwayTeam'])


# print("label encode Away")
# print(data.head())

# print(data.columns)


# print(label_enc.transform(['West Ham']),"ok")
X = data.drop(['winning_team'], axis=1)
y = data["winning_team"]
y = y.astype('int')

# Separate train and test sets
# print(X.head())
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42)


logreg = LogisticRegression()
logreg.fit(X_train, y_train)



score = logreg.score(X_train, y_train)
score2 = logreg.score(X_test, y_test)

print("Training set accuracy: ", '%.3f'%(score*100))
print("Test set accuracy: ", '%.3f'%(score2*100))


print("WEST HAM vs ARSENAL ")
prediction_example = logreg.predict([[label_enc.transform(['West Ham'])[0],label_enc.transform(['Arsenal'])[0],68.0454545454545,68.92857142857143,0.371900826446281,0.36900369003690037]])


if(prediction_example[0]==0):
	print('ARSENAL IS THE WINNING TEAM')

if(prediction_example[0]==2):
	print('WEST HAM IS THE WINNING TEAM')
if(prediction_example[0]==1):
	print('DRAW')



# print(prediction_example,"a")




# home_fpl=data.at['Man United','home_fpl']

# away_fpl=data.at['NewCastle','away_fpl']


# a=["Everton"]
# b=["NewCastle"]
# c=[0]
# d=[62.3214285714286]
# e=[0.447154471544715]
# f=[0.210332103321033]
# pred['AwayTeam']=a
# pred['HomeTeam']=b
# pred['home_fpl']=c
# pred['away_fpl']=d
# pred['home_win']=e
# pred['away_win']=f


# print(pred.columns)
# missing_cols = set(final.columns) - set(pred.columns)
# print(missing_cols)
# for c in missing_cols:
#     pred[c] = 0
# pred = pred[final.columns]
# # pred_set = pd.get_dummies(pred, prefix=['home_team', 'away_team'], columns=['HomeTeam', 'AwayTeam'])
# print(pred.columns)

# predictions = logreg.predict(pred_set)

# print(predictions)

# print(pred.head())



# end_time=time.time()
# now_time=end_time-prev_time
# print("Total time taken: ",now_time)
