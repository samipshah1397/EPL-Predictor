import pandas as pd 

import time

prev_time = time.time()
data=pd.read_csv('epldata_final.csv')
print(data.club.unique())
data2=pd.read_csv('EPL_Set.csv')

club=data.club.unique()
team=data2.HomeTeam.unique()
opteam=data2.AwayTeam.unique()
print(data2.head())
data2=data2.drop(['Div','Date'],axis=1)
for j in team:
	count=0
	for i in club:
		if (i==j):
			count+=1

	if (count==0):
		data2=data2[data2.HomeTeam!=j]

for j in opteam:
	count=0
	for i in club:
		if (i==j):
			count+=1

	if (count==0):
		data2=data2[data2.AwayTeam!=j]

print(data2.AwayTeam.unique())
print(data2.HomeTeam.unique())

if (set(data2.AwayTeam.unique())==set(data2.HomeTeam.unique())):
	print("true")

if (set(data.club.unique())==set(data2.HomeTeam.unique())):
	print("true")

if (set(data2.AwayTeam.unique())==set(data.club.unique())):
	print("true")		
	
print(data2.shape)

dic={}
clu=['Arsenal']
arsenal=data[data.club.isin(clu)]
print(arsenal['fpl_points'].sum())

for j in club:
	temp=data[data.club==j]
	dic[j]=temp['fpl_points'].sum()/len(temp)

home_teamfpl=[]
for j in data2['HomeTeam']:
	home_teamfpl.append(dic[j])

away_team_fpl=[]
for k in data2['AwayTeam']:
	away_team_fpl.append(dic[k])


data2['home_fpl']=home_teamfpl
data2['away_fpl']=away_team_fpl
print(len(away_team_fpl))

data3=data2[['HomeTeam','AwayTeam','FTR']]
print(data3.head())

# count=0
# for index, row in data3.iterrows():

# 	if(row['HomeTeam']=='Arsenal' and row['FTR']=='H'):
# 		count+=1

# count2=0
# for index, row in data3.iterrows():
	
# 	if(row['HomeTeam']=='Bournemouth'):
# 		count2+=1

# # count3=0
# # for index, row in data3.iterrows():
	
# # 	if(row['AwayTeam']=='Arsenal'):
# # 		count3+=1

# count4=0
# for index, row in data3.iterrows():

# 	if(row['AwayTeam']=='Bournemouth' and row['FTR']=='A'):
# 		count4+=1

# # print(count)
# print(count4)
# print(count2,"aa")
# print(count3)
# print(len(data3))

dichome={}
dicaway={}
for i in club:
	count1=0
	count3=0
	count2=0	
	count=0
	for index, row in data3.iterrows():
		if(row['HomeTeam']==i and row['FTR']=='H'):
 			count+=1
		if(row['HomeTeam']==i):
 			count1+=1
 		
		if(row['AwayTeam']==i and row['FTR']=='A'):
 			count2+=1

		if(row['AwayTeam']==i):
 			count3+=1	

 			
	dicaway[i]=(count2/count3)	

	dichome[i]=(count/count1)


# b=True
# for i,j in zip(dichome,dicaway):
	
# 	if (dicaway[i]>dichome[i]):
# 		b=False

# print(b)

# print(dicaway)
# print(dichome)

home_win=[]
for j in data2['HomeTeam']:
	home_win.append(dichome[j])

away_win=[]
for k in data2['AwayTeam']:
	away_win.append(dicaway[k])

print(len(home_win))

print(len(away_win))	



data2['home_win']=home_win
data2['away_win']=away_win

print(data2.head())
new_time = time.time()
total_time = new_time - prev_time

print("total time : ",total_time)
data2.drop(data2.columns[0], axis=1)
# print(dic)
data2.to_csv('EPL_Set2.csv',index=False)				
	


