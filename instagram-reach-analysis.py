# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from wordcloud import WordCloud, STOPWORDS

# Read the dataset
data = pd.read_csv("Instagram data.csv", encoding='latin1')

# Display the first few rows of the dataset
print(data.head())

# Check for null values in the dataset
print(data.isnull().sum())

# Drop any rows with null values (if any)
data = data.dropna()

# Display information about the dataset
data.info()

# Analyze the distribution of impressions from home
plt.figure(figsize=(10, 8))
plt.style.use('fivethirtyeight')
plt.title("Distribution of Impressions From Home")
sns.histplot(data['From Home'])
plt.show()

# Analyze the distribution of impressions from hashtags
plt.figure(figsize=(10, 8))
plt.title("Distribution of Impressions From Hashtags")
sns.histplot(data['From Hashtags'])
plt.show()

# Analyze the distribution of impressions from the explore section
plt.figure(figsize=(10, 8))
plt.title("Distribution of Impressions From Explore")
sns.histplot(data['From Explore'])
plt.show()

# Calculate the total impressions from various sources
home = data["From Home"].sum()
hashtags = data["From Hashtags"].sum()
explore = data["From Explore"].sum()
other = data["From Other"].sum()

# Create a pie chart to show the percentage of impressions from various sources
labels = ['From Home', 'From Hashtags', 'From Explore', 'Other']
values = [home, hashtags, explore, other]

fig = px.pie(values=values, names=labels, 
             title='Impressions on Instagram Posts From Various Sources', hole=0.5)
fig.show()

# Create a word cloud for the caption column
text = " ".join(i for i in data.Caption)
stopwords = set(STOPWORDS)
wordcloud = WordCloud(stopwords=stopwords, background_color="white").generate(text)

plt.figure(figsize=(12, 10))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()

# Create a word cloud for the hashtags column
text = " ".join(i for i in data.Hashtags)
wordcloud = WordCloud(stopwords=stopwords, background_color="white").generate(text)

plt.figure(figsize=(12, 10))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()

# Analyze the relationship between likes and impressions
figure = px.scatter(data_frame=data, x="Impressions", y="Likes", size="Likes", trendline="ols", 
                    title="Relationship Between Likes and Impressions")
figure.show()

# Analyze the relationship between comments and impressions
figure = px.scatter(data_frame=data, x="Impressions", y="Comments", size="Comments", trendline="ols", 
                    title="Relationship Between Comments and Total Impressions")
figure.show()

# Analyze the relationship between shares and impressions
figure = px.scatter(data_frame=data, x="Impressions", y="Shares", size="Shares", trendline="ols", 
                    title="Relationship Between Shares and Total Impressions")
figure.show()

# Calculate and print the correlation of all columns with the Impressions column
correlation = data.corr()
print(correlation["Impressions"].sort_values(ascending=False))

# Calculate the conversion rate
conversion_rate = (data["Follows"].sum() / data["Profile Visits"].sum()) * 100
print(f"Conversion Rate: {conversion_rate:.2f}%")

# Analyze the relationship between profile visits and followers gained
figure = px.scatter(data_frame=data, x="Profile Visits", y="Follows", size="Follows", trendline="ols", 
                    title="Relationship Between Profile Visits and Followers Gained")
figure.show()

