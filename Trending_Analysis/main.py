import numpy as np
import pandas as pd
import datetime
import json
from IPython.display import display

import matplotlib 
import seaborn as sns #popular Python data visualization library built on top of Matplotlib. It provides a high-level interface for creating attractive and informative statistical graphics.
import matplotlib.pyplot as plt

# IN The US

file_path=r'D:\Downloads\Trending_dataset\US_youtube_trending_data.csv'
us_yt = pd.read_csv(file_path)
display(us_yt.head())
print(us_yt.columns)

us_yt.categoryId.nunique()#.unique_count().sum()
us_yt.head()

corrolation_list = ['view_count', 'likes', 'dislikes', 'comment_count']
hm_data = us_yt[corrolation_list].corr() 
display(hm_data)


matplotlib.pyplot.figure(figsize=(8,6))
sns.heatmap(hm_data, annot=True); 
plt.show() 

sns.pairplot(us_yt[['view_count', 'likes']], kind='reg',height=6);
plt.show() # function in Seaborn is used to create a grid of scatter plots that visualize the relationships between multiple variables in a dataset. It plots pairwise relationships across an entire DataFrame or a subset of columns. Each scatter plot in the grid represents the relationship between two variables, and the diagonal plots show the distributions of individual variables. 

matplotlib.pyplot.figure(figsize=(10,10))
sns.regplot(x=us_yt['view_count'], y=us_yt['likes'],scatter_kws={"color": "green"}, line_kws={"color": "blue"});
plt.show() # function in Seaborn is used to create a scatter plot with a fitted regression line. It shows the relationship between two variables and provides a visual representation of the linear relationship between them



col_list = ['video_id', 'view_count', 'likes', 'dislikes', 'comment_count']

us_yt = pd.read_csv(file_path, usecols=col_list) #USA, remaking the dataframe in the same format as the others
ca_yt = pd.read_csv('D:\Downloads\Trending_dataset\CA_youtube_trending_data.csv', usecols=col_list) #Canada
de_yt = pd.read_csv('D:\Downloads\Trending_dataset\DE_youtube_trending_data.csv', usecols=col_list) #Germany
fr_yt = pd.read_csv('D:\Downloads\Trending_dataset\FR_youtube_trending_data.csv', usecols=col_list) #France


# #
# gb_yt = pd.read_csv('../input/youtube-trending-video-dataset/GB_youtube_trending_data.csv', usecols=col_list) #United Kingdom (Great Brittain)
# in_yt = pd.read_csv('../input/youtube-trending-video-dataset/IN_youtube_trending_data.csv', usecols=col_list) #India
# jp_yt = pd.read_csv('../input/youtube-trending-video-dataset/JP_youtube_trending_data.csv', usecols=col_list) #Japan
# kr_yt = pd.read_csv('../input/youtube-trending-video-dataset/KR_youtube_trending_data.csv', usecols=col_list) #South Korea
# mx_yt = pd.read_csv('../input/youtube-trending-video-dataset/MX_youtube_trending_data.csv', usecols=col_list) #Mexico
# ru_yt = pd.read_csv('../input/youtube-trending-video-dataset/RU_youtube_trending_data.csv', usecols=col_list) #Russia
# #


#correlation table

df_list = [us_yt, ca_yt, de_yt, fr_yt, ]
df_name_list = ['United States', 'Canada', 'Germany', 'France']

# views_df = pd.DataFrame(columns=['view_count', 'likes', 'dislikes', 'comment_count'])
# likes_df = pd.DataFrame(columns=['view_count', 'likes', 'dislikes', 'comment_count'])

# display(views_df, likes_df)

# count = 0
# while count != 10:
#     print(df_name_list[count])
#     current_df = df_list[count]
#     _x = current_df[corrolation_list].corr()
#     display(_x)
#     views_df.loc[count] = _x.loc['view_count']
#     likes_df.loc[count] = _x.loc['likes']
#     count += 1


#number of videos per channel / Barplot
us= pd.read_csv(file_path)
l=us.channelTitle.value_counts()[:10].index
video_count = pd.DataFrame({'channel_title':l,'no_of_videos':us.channelTitle.value_counts()[:10]})
video_count.index=[i for i in range(1,11)]
print(video_count)
matplotlib.pyplot.figure(figsize=(9,9))
sns.barplot(y="channel_title",x="no_of_videos",data = video_count)
plt.show()


de= pd.read_csv('D:\Downloads\Trending_dataset\DE_youtube_trending_data.csv')
l=de.channelTitle.value_counts()[:10].index
video_count = pd.DataFrame({'channel_title':l,'no_of_videos':de.channelTitle.value_counts()[:10]})
video_count.index=[i for i in range(1,11)]
print(video_count)
matplotlib.pyplot.figure(figsize=(9,9))
sns.barplot(y="channel_title",x="no_of_videos",data = video_count)
plt.show()

#categories : pet, entertainlent,... / Barplot

with open('D:/Downloads/Trending_dataset/US_category_id.json') as f:

    categories = json.load(f)["items"]
cat_dict = {}
for cat in categories:
    cat_dict[int(cat["id"])] = cat["snippet"]["title"]
us['category_name'] = us['categoryId'].map(cat_dict)


i=us["category_name"].value_counts().index
m=us["category_name"].value_counts()
matplotlib.pyplot.figure(figsize=(9,9))
sns.barplot(x=m,y=i)
plt.show()

l=us.groupby("category_name").sum()["view_count"]/us["category_name"].value_counts()
s=pd.DataFrame({"category_name":l.index,"avg_views":l})
s=s.sort_values("avg_views",ascending=False)
s.index=[i for i in range(0,15)]
matplotlib.pyplot.figure(figsize=(9,9))
sns.barplot(x="avg_views",y="category_name",data=s)
plt.show()

# Tag cloud for every country 
col_list = ["title"]
def wordcld(a,j):
    from wordcloud import WordCloud 
    import matplotlib.pyplot as plt
    title_words = list(a["title"].apply(lambda x: x.split()))
    title_words = [x for y in title_words for x in y]
    #print(df_name_list[j])
    wc = WordCloud(width=1200, height=500, 
                                collocations=False, background_color="white", 
                                colormap="tab20b").generate(" ".join(title_words))
    plt.figure(figsize=(15,10))
    plt.imshow(wc, interpolation='bilinear')
    #plt.axis("off")
    plt.ylabel(df_name_list[j])

j=0
while j<len(df_list):
    #print(df_name_list[j])
    wordcld(df_list[j],j)
    j=j+1