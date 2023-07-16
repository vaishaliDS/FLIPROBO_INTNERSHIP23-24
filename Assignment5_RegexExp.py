#!/usr/bin/env python
# coding: utf-8

# In[1]:


import re


# #### Question 1- Write a Python program to check that a string contains only a certain set of characters (in this case a-z, A-Z and 0-9).

# In[30]:


def match(str1):
    pattern='\W'
    result=re.findall(pattern,str1)
    if result:
        print("Non specified chracters a-z, A-Z and 0-9 are present in string")
    else:
        print("Only specified chractersare n a-z, A-Z and 0-9 are present in string")


msg="Welcometopython regex functions@Raj "
msg1="hsdhgs23434MNHD76"

match(msg)
match(msg1)


# #### Question 2- Create a function in python that matches a string that has an a followed by zero or more b's

# In[35]:


def match(str1):
    pattern='ab*'
    result=re.findall(pattern,str1)
    if result:
        print('match found')
    else:
        print('match doesn\'t found')
str1='abc'
str2='af'
str3='agb'
str4='abbb'
match(str1)
match(str2)
match(str3)
match(str4)


# #### Question 3-  Create a function in python that matches a string that has an a followed by one or more b's

# In[36]:


def match(str1):
    pattern='ab+'
    result=re.findall(pattern,str1)
    if result:
        print('match found')
    else:
        print('match doesn\'t found')
str1='abc'
str2='af'
str3='agb'
str4='abbb'
match(str1)
match(str2)
match(str3)
match(str4)


# #### Question 4- Create a function in Python and use RegEx that matches a string that has an a followed by zero or one 'b'.

# In[40]:


def match(str1):
    pattern='ab?'
    result=re.findall(pattern,str1)
    if result:
        print('match found')
        print(result)
    else:
        print('match doesn\'t found')
str1='abc'
str2='af'
str3='agb'
str4='abbbb'
match(str1)
match(str2)
match(str3)
match(str4)


# #### Question 5- Write a Python program that matches a string that has an a followed by three 'b'.

# In[39]:


def match(text):
    pattern='ab{3}'
    result=re.findall(pattern,text)
    if result:
        print(text+" match found")
    else:
        print(text+" match doesn\'t found")
str1='abcd'
str2='abbbb'
str3='abbb'
match(str1)
match(str2)
match(str3)


# #### Question 6- Write a regular expression in Python to split a string into uppercase letters.
# Sample text: “ImportanceOfRegularExpressionsInPython”
# Output: [‘Importance’, ‘Of’, ‘Regular’, ‘Expression’, ‘In’, ‘Python’]

# In[42]:


def match(text):
    pattern='[A-Z][a-z]*'
    result=re.findall(pattern,text)
    print(result)

str1='ImportanceOfRegularExpressionsInPython'
match(str1)


# #### Question 7- Write a Python program that matches a string that has an a followed by two to three 'b'.

# In[43]:


def match(text):
    pattern='ab{2,3}'
    result=re.findall(pattern,text)
    if result:
        print(result)
        print(str+" Match found")
    else:
         print(str+" Match not found")
str1='abcd'
str2='abbdd'
str3='abbbdd'
str4='abbbb'
match(str1)
match(str2)
match(str3)
match(str4)


# #### Question 8- Write a Python program to find sequences of lowercase letters joined with a underscore.

# In[44]:


def match(text):
    pattern='[a-z]+[_][a-z]+'
    result=re.findall(pattern,text)
    print(result)
str1='ass_D_hs_jFj_jjo_ppp'
str2='asd_skk'
match(str1)
match(str2)


# #### Question 9- Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'.

# In[52]:


def match(text):
    pattern=r'a+b$'
    result=re.findall(pattern,text)
    
    if result:
        print("match found")
    else:
        print("match not found")
str1='annb '
str2='aba'
match(str1)
match(str2)


# #### Question 10- Write a Python program that matches a word at the beginning of a string.

# In[26]:


def match_str(text):
    pattern="^The"
    result=re.findall(pattern,text)
    print(result)
    if result:
        print("Match found.")
    else:
        print("Match doesn't found.")


str1="The Sun is rising ."
str2="It's  sun set ."

match_str(str1)
match_str(str2)


# #### Question 11- Write a Python program to match a string that contains only upper and lowercase letters, numbers, and underscores.

# In[81]:


def match_str(text):
    pattern=r"^[a-zA-z0-9_]*$"
    result=re.findall(pattern,text)
    print(result)
    if result:
        print("Match found.")
    else:
        print("Match doesn't found.")


str1="sdhSSS233_66Asd"
str2="It'ssun set?@ ."

match_str(str1)
match_str(str2)


# #### Question 12- Write a Python program where a string will start with a specific number. 

# In[82]:


def match_str(text):
    pattern=r"^9"
    result=re.findall(pattern,text)
    print(result)
    if result:
        print("Match found.")
    else:
        print("Match doesn't found.")


str1="9sdhSSS233_66Asd"
str2="It'ssun set?@ ."

match_str(str1)
match_str(str2)


# #### Question 13- Write a Python program to remove leading zeros from an IP address

# In[58]:


ip1 = "255.18.075.108"
string = re.sub('\.[0]*', '.', ip1)
print(string)


# #### Question 14- Write a regular expression in python to match a date string in the form of Month name followed by day number and year stored in a text file.
# Sample text : ' On August 15th 1947 that India was declared independent from British colonialism, and the reins of control were handed over to the leaders of the Country’.
# Output- August 15th 1947
# Hint- Use re.match() method here

# In[33]:


text="On August 15th 1947 that India was declared independent from British colonialism, and the reins of control were handed over to the leaders of the Country ."

pattern=r"\w+\s\d{1,2}th\s\d{4}"
x=re.findall(pattern,text)
x


# #### Question 15- Write a Python program to search some literals strings in a string. Go to the editor
# Sample text : 'The quick brown fox jumps over the lazy dog.'
# Searched words : 'fox', 'dog', 'horse'

# In[34]:


text='The quick brown fox jumps over the lazy dog.' 
search=['fox', 'dog', 'horse']
for i in search:
    x=re.findall(i,text)
    if x:
        
        print(f"found {i} in statement {text}" )
    else:
        print(f"Didn't found { i} in statement {text}" )


# #### Question 16- Write a Python program to search a literals string in a string and also find the location within the original string where the pattern occurs
# Sample text : 'The quick brown fox jumps over the lazy dog.'
# Searched words : 'fox'

# In[28]:


text='The quick brown fox jumps over the lazy dog.' 
x=re.search('fox',text)
if x:
    print(f'"fox" found in string {text} at position : {x.span()}')
else:
    (f"didn't found fox in string {text} ")


# #### Question 17- Write a Python program to find the substrings within a string.
# Sample text : 'Python exercises, PHP exercises, C# exercises'
# Pattern : 'exercises'.

# In[39]:


text='Python exercises, PHP exercises, C# exercises' 
sub_str= 'exercises'
x=re.search(sub_str,text)
print(x)
print(x.group())
print("location of sub string is:",x.span())


# #### Question 18- Write a Python program to find the occurrence and position of the substrings within a string.

# In[45]:


text='This is our 5th assignment .' 
sub_str= ['assignment','solution']
for i in sub_str:
    x=re.search(i,text)
    print(x)
    
    if x:
        print("found the substring :")
        print(x.group())
        print("location of sub string is:",x.span())
    else:
         print("didn't found the substring :")
    print('-'*50)


# #### Question 19- Write a Python program to convert a date of yyyy-mm-dd format to dd-mm-yyyy format.

# In[54]:


date='2022-12-11'
x=re.split('-',date)

print(x)
date_new=x[2]+"-"+x[1]+"-"+x[0]
print(f"original date yyyy-mm-dd:",date)
print(f"New date dd-mm-yyy:",date_new)
    


# #### Question 20- Write a Python program to find all words starting with 'a' or 'e' in a given string.

# In[84]:


text='''This is an amazing place.
       English is the most spoken language here.
       All people are enthusiastic here.'''

x=re.split(r'\s',text)
print(x)
print('-'*100)
for word in x:
    start=re.search(r'\A[a|e]\w*',word)
    
    if start:
        print(start.group())
        


# #### Question 21- Write a Python program to separate and print the numbers and their position of a given string.
# 

# In[102]:


text="Sachin has 54675 rs balance in his acc. his salary is 25032 rs."
matches=re.finditer('\d+',text)
for match in matches:
    print(f"number found is {match.group()} at position {match.span()}")
    print()


# #### Question 22- Write a regular expression in python program to extract maximum numeric value from a string

# In[106]:


text="hfdh6435hghg45hjj34344"
x=re.findall('\d+',text)
print("All numeric values in string :",x)
print()
#convert all string list items into int by using map n storing in list 
print("Maximum numeric value from a string is : ",max(map(int,x)))


# #### Question 23- Write a Regex in Python to put spaces between words starting with capital letters

# In[122]:


text="HelloIndiaJapanAmerica"
x=re.findall(r'[A-Z][a-z]*',text)
#joining list items with space
print(' '.join(x))


# #### Question 24- Python regex to find sequences of one upper case letter followed by lower case letters

# In[128]:


text="HelloIndiaRANGEJJapanAmerica"
x=re.findall(r'[A-Z][a-z]+',text)
#joining list items with space
print(x)


# #### Question 25- Write a Python program to remove duplicate words from Sentence using Regular Expression

# In[6]:


str_1="Welcome to my my python class class."
pattern=r"\b(\w+)(?:\W+\1\b)+"

x=re.sub(pattern,r'\1',str_1)
x


# #### Question 26-  Write a python program using RegEx to accept string ending with alphanumeric character.

# In[12]:


text=input("Enter the string.")
pattern=r"[A-Za-z0-9]$"
x=re.search(pattern,text)
if x:
    print("string endingwith alpha numeric .")
else:
    
    print("string doesn't ending with alpha numeric .")


# #### Question 27-Write a python program using RegEx to extract the hashtags.
# Sample Text: text = """RT @kapil_kausik: #Doltiwal I mean #xyzabc is "hurt" by #Demonetization as the same has rendered USELESS <ed><U+00A0><U+00BD><ed><U+00B1><U+0089> "acquired funds" No wo"""
# Output: ['#Doltiwal', '#xyzabc', '#Demonetization']

# In[20]:


text = """RT @kapil_kausik: #Doltiwal I mean #xyzabc is "hurt" by 
        #Demonetization as the same has rendered USELESS <U+00A0><U+00BD><U+00B1><U+0089> "acquired funds" No wo"""
pattern=r"#\w+"
x=re.findall(pattern, text)
print(x)


# #### Question 28- Write a python program using RegEx to remove <U+..> like symbols
# Check the below sample text, there are strange symbols something of the sort <U+..> all over the place. You need to come up with a general Regex expression that will cover all such symbols.
# Sample Text: "@Jags123456 Bharat band on 28??<ed><U+00A0><U+00BD><ed><U+00B8><U+0082>Those who  are protesting #demonetization  are all different party leaders"
# Output: @Jags123456 Bharat band on 28??<ed><ed>Those who  are protesting #demonetization  are all different party leaders
# 

# In[26]:


text='''@Jags123456 Bharat band on 28??<U+00A0><U+00BD><U+00B8><U+0082>Those who are protesting #demonetization are all different party leaders'''
pattern=r"<U\+\w+>"
x=re.sub(pattern,"",text)
x


# #### Question 29- Write a python program to extract dates from the text stored in the text file.
# Sample Text: Ron was born on 12-09-1992 and he was admitted to school 15-12-1999.
# Store this sample text in the file and then extract dates.

# In[28]:


text="Ron was born on 12-09-1992 and he was admitted to school 15-12-1999 ."
pattern=r"\d{2}-\d{2}-\d{4}"
x=re.findall(pattern,text)
x


# #### Question 30- Write a Python program to replace all occurrences of a space, comma, or dot with a colon.
# Sample Text- 'Python Exercises, PHP exercises.'
# Output: Python:Exercises::PHP:exercises:

# In[143]:


Text='Python Exercises, PHP exercises.'
pattern = r"[\s,.]"
x=re.sub(pattern , ':' ,Text)
x


# In[ ]:





# In[ ]:




