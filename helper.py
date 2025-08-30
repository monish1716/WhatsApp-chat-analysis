from urlextract import URLExtract
from wordcloud import WordCloud
import pandas as pd
from collections import Counter
import emoji
extract = URLExtract()

def fetch_stats(selected_user, df):

    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]
    num_messages = df.shape[0]
    words = []

    for message in df['message']:         # use new_df, not df
            words.extend(message.split())

    num_media_message = df[df['message'] == '<Media omitted>\n'].shape[0]

    links = []
    for message in df['message']:
        links.extend(extract.find_urls(message))

    return num_messages, len(words), num_media_message, len(links)

def most_busy_users(df):
    # Top 5 users by message count
    x = df['user'].value_counts().head()

    # Percentage of messages per user
    percent_df = (df['user'].value_counts() / df.shape[0] * 100).round(2).reset_index()
    percent_df.rename(columns={'index': 'name', 'user': 'percent'}, inplace=True)

    return x, percent_df

from wordcloud import WordCloud

def create_wordcloud(selected_user, df):
    # Read stopwords and convert to a set for faster lookup
    with open('stop_hinglish.txt', 'r') as f:
        stop_words = set(f.read().splitlines())  # each line is a word

    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    temp = df[df['user'] != 'group_notification']
    temp = temp[temp['message'] != '<Media omitted>\n']

    def remove_stop_words(message):
        words = []
        for word in message.split():
            if word.lower() not in stop_words:
                words.append(word)
        return " ".join(words)

    temp['message'] = temp['message'].apply(remove_stop_words)

    wc = WordCloud(width=500, height=500, min_font_size=10, background_color='white')
    df_wc = wc.generate(temp['message'].str.cat(sep=" "))

    return df_wc


def most_common_words(selected_user, df):
    
    f = open('stop_hinglish.txt', 'r')
    stopwords = f.read()

    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    

    temp = df[df['user'] != 'group_notification']

    temp = temp[temp['message'] != '<Media omitted>\n']

    words = []
    for message in temp['message']:
        for word in message.lower().split():
            if word not in stopwords:
                words.append(word)


    most_common_df = pd.DataFrame(Counter(words).most_common(20))

    return most_common_df

def emoji_helper(selected_user, df):
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    emojis = []
    for message in df['message']:
        emojis.extend([c for c in message if c in emoji.EMOJI_DATA])

    emoji_df = pd.DataFrame(Counter(emojis).most_common(20),  # top 20 emojis
                            columns=['Emoji', 'Count'])

    return emoji_df

def monthly_timeline(selected_user, df):
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    timeline = df.groupby(['year','month_num','month']).count()['message'].reset_index()

    # Create a 'time' column
    timeline['time'] = timeline.apply(lambda row: row['month'] + "-" + str(row['year']), axis=1)

    # Rename the message count column for clarity
    timeline.rename(columns={'message': 'message_count'}, inplace=True)

    return timeline

def daily_timeline(selected_user, df):
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]
    
    daily_timeline = df.groupby('only_date').count()['message'].reset_index()
    daily_timeline.rename(columns={'message': 'message_count'}, inplace=True)
    
    return daily_timeline

def week_activity_map(selected_user, df):
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]    

    return df['day_name'].value_counts()

def month_activity_map(selected_user, df):
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    return df['month'].value_counts()

def activity_heatmap(selected_user, df):
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]
    heatmap = df.pivot_table(index='day_name', columns='period', values='message', aggfunc='count').fillna(0)

    return heatmap