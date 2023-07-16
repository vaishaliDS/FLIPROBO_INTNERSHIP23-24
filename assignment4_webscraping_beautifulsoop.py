#!/usr/bin/env python
# coding: utf-8

# ### Web_Scrapping_BeautifullSoup

# In[89]:


from bs4 import BeautifulSoup
import requests
import pandas as pd
import regex as re


# #### 1) Write a python program to display all the header tags from wikipedia.org and make data frame.

# In[12]:


url="https://www.wikipedia.org/"
page=requests.get(url)
page

soup=BeautifulSoup(page.content)
soup
header_tags=['h1','h2','h3']
for tag in header_tags:
    headers=[]
    headers=soup.find_all(tag)
    print(tag+" Header is :")
    for header in headers:
        print(header.text) 
    print('__'*50)


# #### 2) Write s python program to display list of respected former presidents of India(i.e. Name , Term ofoffice) from https://presidentofindia.nic.in/former-presidents.htm and make data frame.

# In[101]:


President={'Name':[],'Term':[]}

url='https://presidentofindia.nic.in/former-presidents.htm'
page=requests.get(url)

soup=BeautifulSoup(page.text,"html.parser")
data=soup.find('ul',class_="listing cf")
rows=data.find_all('li')
for row in rows:
    name=row.find('h3').text
   # print(row.text.split("\n"))
    data=row.text.split("\n")
    name=data[2]
    Term=data[3]
    President['Name'].append(name)
    President['Term'].append(Term)

df=pd.DataFrame(President)
df


# #### 3) Write a python program to scrape cricket rankings from icc-cricket.com. You have to scrape and make data frame-
# a) Top 10 ODI teams in men’s cricket along with the records for matches, points and rating.
# b) Top 10 ODI Batsmen along with the records of their team andrating.
# c) Top 10 ODI bowlers along with the records of their team andrating.

# In[74]:


#a) Top 10 ODI teams in men’s cricket along with the records for matches, points and rating.

team_details={'Team_ranking' :[],
               'Team_name' :[],
                'Matches' :[],
                'Points' :[],
                'Ratings' :[]}
print("Top 10 ODI teams in men’s cricket along with the records for matches, points and rating.")
print("**"*50)

url="https://www.icc-cricket.com/rankings/mens/team-rankings/odi"

page=requests.get(url)
soup=BeautifulSoup(page.text,"html.parser")

team_ranking_table= soup.find('table',class_="table")
rows=team_ranking_table.find_all('tr')
#print(rows)

for row in rows[1:12]:
   
   # print(row)
    ranks=row.find_all('td')
    # strip to delet extra space
    cols=[x.text.strip() for x in ranks]
    
    #Append all col data to dict.
    team_details['Team_ranking'].append(cols[0])
    team_details['Team_name'].append(cols[1])
    team_details['Matches'].append(cols[2])
    team_details['Points'].append(cols[3])
    team_details['Ratings'].append(cols[4])

df=pd.DataFrame(team_details ) 
#to print dataframe without index
df=df.to_string(index=False)
print(df)


# In[ ]:


#3 b) Top 10 ODI Batsmen along with the records of their team andrating.


# In[68]:


print("Top 10 ODI Batsmen along with the records of their team and rating.")
print("   ")

url = 'https://www.icc-cricket.com/rankings/mens/player-rankings/ODI/batting'
bat= requests.get(url)

Batsman_details={'POS' :[],
               'PLAYER' :[],
                'TEAM' :[],
                'RATING' :[],
                'CAREER BEST RATING' :[]}


soup=BeautifulSoup(bat.text, 'html.parser')

data=soup.find('table',class_='table')
rows=data.find_all('tr')
for row in rows[1:11]:
    player_ranking = row.find_all('td')
    cols=[x.text.strip() for x in player_ranking]
 
    Batsman_details['POS'].append(cols[0])
                                  
    Batsman_details['PLAYER'].append(cols[1])
    Batsman_details['TEAM'].append(cols[2])
    Batsman_details['RATING'].append(cols[3])
    Batsman_details['CAREER BEST RATING'].append(cols[4])
    
df=pd.DataFrame(Batsman_details)

## to format string 1\n\n\n --> 1 

df["POS"]=df["POS"].str[:1]
    
#print(df)

df


# In[ ]:


#3 c) Top 10 ODI bowlers along with the records of their team andrating.


# In[72]:


import regex as re
url="https://www.icc-cricket.com/rankings/mens/player-rankings/odi/bowling"
bowler= requests.get(url)

Bowler_details={'POS' :[],
               'PLAYER' :[],
                'TEAM' :[],
                'RATING' :[],
                'CAREER BEST RATING' :[]}


soup=BeautifulSoup(bowler.text, 'html.parser')

data=soup.find('table',class_='table')
rows=data.find_all('tr')
for row in rows[1:11]:
    player_ranking = row.find_all('td')
    cols=[x.text.strip() for x in player_ranking]
 
    Bowler_details['POS'].append(cols[0])
                                  
    Bowler_details['PLAYER'].append(cols[1])
    Bowler_details['TEAM'].append(cols[2])
    Bowler_details['RATING'].append(cols[3])
    Bowler_details['CAREER BEST RATING'].append(cols[4])
    
df=pd.DataFrame(Bowler_details)

## to format string 1\n\n\n --> 1 

df["POS"]=df["POS"].str[:1]
   

df


# #### 4) Write a python program to scrape cricket rankings from icc-cricket.com. You have to scrape and make data frame-
# a) Top 10 ODI teams in women’s cricket along with the records for matches, points and rating.
# b) Top 10 women’s ODI Batting players along with the records of their team and rating.
# c) Top 10 women’s ODI all-rounder along with the records of their team and rating.
# 

# In[ ]:


a) Top 10 ODI teams in women’s cricket along with the records for matches, points and rating.


# In[24]:


url='https://www.icc-cricket.com/rankings/womens/team-rankings/odi'
page= requests.get(url)
soup = BeautifulSoup(page.text, "html.parser")
table_body =soup.find('table')
row_data=[]
header_data=[]
i=0
for row in table_body.find_all('tr'):
    cols=row.find_all('td')
    col=[ele.text.strip() for ele in cols]
    
    
    row_data.append(col)
for headers in soup.find_all('th'):
    header=[headers.text.strip() ]
    header_data.append(header)

#ValueError: 1 columns passed, passed data had 5 columns getting this
#df=pd.DataFrame(row_data,columns=header_data) 

df=pd.DataFrame(row_data,columns=['Pos','Team','Matches','Points','Rating'])
df=df.replace('\n','  ',regex=True)
df2=df.dropna()
df2.head(10)


# In[ ]:


b) Top 10 women’s ODI Batting players along with the records of their team and rating. 


# In[25]:


url='https://www.icc-cricket.com/rankings/womens/player-rankings/odi'
page= requests.get(url)
soup = BeautifulSoup(page.text, "html.parser")
table_body =soup.find('table')
row_data=[]
header_data=[]

row_data_1=[] #to save 1st palyer data
row_data_1_rank=soup.find('span',class_='rankings-block__pos-number').text


row_data_1_name=soup.find('div',class_='rankings-block__banner--name').text

row_data_1_team=soup.find('div',class_='rankings-block__banner--nationality').text

row_data_1.append(row_data_1_rank.strip())
row_data_1.append(row_data_1_name.strip())
team_rate=row_data_1_team.split()

row_data_1.append(team_rate[0])
row_data_1.append(team_rate[1])

row_data.append(row_data_1)

for row in table_body.find_all('tr'):
    cols=row.find_all('td')
    col=[ele.text.strip() for ele in cols]
    
    row_data.append(col)
for headers in soup.find_all('th'):
    header=[headers.text.strip() ]
    header_data.append(header)

#ValueError: 1 columns passed, passed data had 5 columns getting this
#df=pd.DataFrame(row_data,columns=header_data) 

df=pd.DataFrame(row_data,columns=['Pos','Player','Team','Rating'])
df=df.replace('\n','  ',regex=True)
df2=df.dropna()
df2.head(10)


# In[ ]:


c) Top 10 women’s ODI all-rounder along with the records of their team and rating.


# In[77]:


women_all_rounder={'Pos':[],
                    'Name':[],
                     'Team':[],
                  'Rating':[]}



url='https://www.icc-cricket.com/rankings/womens/player-rankings/odi'
page= requests.get(url)
soup = BeautifulSoup(page.text, "html.parser")

rank1=soup.find('span' , class_="rankings-block__pos-number" ).text
rank1.strip()

name1=soup.find_all('div',class_="rankings-block__banner--name")
name1[2].text

team1=soup.find_all('div',class_="rankings-block__banner--nationality")
#team1[2].text.strip().split('\n')[0])
#print(team1[2].text.strip().split('\n')[1])

rating1=soup.find_all('div',class_="rankings-block__banner--rating")
#print(rating1[2].text)
women_all_rounder['Pos'].append(rank1.strip())
women_all_rounder['Name'].append(name1[2].text)
women_all_rounder['Team'].append(team1[2].text.strip().split('\n')[0])
women_all_rounder['Rating'].append(team1[2].text.strip().split('\n')[1])
                    
table=soup.find_all('table',class_="table rankings-card-table")

rows=table[2].find_all('tr')
for row in rows[1:10]:
    rank=row.find('span',class_="rankings-table__pos-number").text.strip()
    women_all_rounder['Pos'].append(rank)
    
    name=row.find('td',class_="table-body__cell name").text.strip()
    women_all_rounder['Name'].append(name)
    
    team=row.find('span',class_="table-body__logo-text").text
    women_all_rounder['Team'].append(team)
    
    rating=row.find('td',class_="table-body__cell u-text-right rating").text
    women_all_rounder['Rating'].append(team)

 
#print(women_all_rounder['Pos'])
df=pd.DataFrame(women_all_rounder)

df


# #### 5) Write a python program to scrape mentioned news details from https://www.cnbc.com/world/?region=world and make data frame-
# i) Headline
# ii) Time
# iii) News Link

# In[23]:


News ={'Headline':[],
        'Time':[],
        'News Link':[]}

url=" https://www.cnbc.com/world/?region=world"
page=requests.get(url)

soup=BeautifulSoup(page.text,"html.parser")
data=soup.find("ul",class_="LatestNews-list")
rows=data.find_all('li')
for row in rows:
    headline=row.find('a').text
    time=row.find('time',class_="LatestNews-timestamp").text
    link=row.find('a').get('href')
    
    News['Headline'].append(headline)
    News['Time'].append(time)
    News['News Link'].append(link)
    
df=pd.DataFrame(News)
df


# #### 6) Write a python program to scrape the details of most downloaded articles from AI in last 90 days.https://www.journals.elsevier.com/artificial-intelligence/most-downloaded-articles Scrape below mentioned details and make data frame-
# i) Paper Title
# ii) Authors
# iii) Published Date
# iv) Paper URL

# In[16]:


Downloaded_articels ={'Paper Title':[],
                      'Authors':[],
                      'Published Date':[],
                      'Paper URL':[]}
url="https://www.journals.elsevier.com/artificial-intelligence/most-downloaded-articles"
page=requests.get(url)
soup=BeautifulSoup(page.text,"html.parser")
data=soup.find("ul",class_="sc-9zxyh7-0 cMKaMj")
rows=data.find_all('li')
for row in rows:
    #print(row.text.split(','))
    name=row.find('h2').text
    Downloaded_articels['Paper Title'].append(name)
    
    url_article=row.find('a').get('href')
    Downloaded_articels['Paper URL'].append(url_article)
    
    author=name=row.find('span',class_="sc-1w3fpd7-0 dnCnAO").text
    Downloaded_articels['Authors'].append(author)
    
    Published_Date=row.find('span',class_="sc-1thf9ly-2 dvggWt").text
    Downloaded_articels['Published Date'].append(Published_Date)

df=pd.DataFrame(Downloaded_articels)
df


# #### 7) Write a python program to scrape mentioned details from dineout.co.in and make data frame-
# i) Restaurant name
# ii) Cuisine
# iii) Location
# iv) Ratings
# v) Image URL

# In[116]:


Dineout_details ={'Restaurant name':[],
                'Cuisine':[],
                'Location':[],
                'Ratings':[],
                'Image URL':[]}
url='https://www.dineout.co.in/delhi-restaurants/central-delhi/connaught-place/continental-cuisine'
page = requests.get(url)
soup=BeautifulSoup(page.text,'html.parser')


rows=soup.find_all('div',class_="restnt-main-wrap clearfix")
for row in rows:
    name=row.find('a').text
    Dineout_details['Restaurant name'].append(name)
    
    cousine=row.find('span',class_='double-line-ellipsis').text.split('|')[1]
    Dineout_details['Cuisine'].append(cousine)
    
    location=row.find('div',class_='restnt-loc ellipsis').text
    Dineout_details['Location'].append(location)
    
    rating=row.find('div',class_='restnt-rating rating-4')
    if(rating==None):
        Dineout_details['Ratings'].append("NA")
    else:    
        Dineout_details['Ratings'].append(rating.text)
        
    image=row.find('img',class_='no-img').get('data-src')
    Dineout_details['Image URL'].append(image)
    
df=pd.DataFrame(Dineout_details)
df


# In[ ]:




