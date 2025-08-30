import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import preprocessor, helper
import seaborn as sns

st.sidebar.title("Whatsapp Chat Analyzer")
uploaded_file = st.sidebar.file_uploader("Choose a file")
if uploaded_file is not None:
    bytes_data = uploaded_file.getvalue()
        try:
        data = bytes_data.decode("utf-8")   # default
        except UnicodeDecodeError:
            try:
                data = bytes_data.decode("utf-16")   # iPhone exports
            except UnicodeDecodeError:
                data = bytes_data.decode("utf-8-sig")  # fallback

    df = preprocessor.preprocess(data)

    # st.dataframe(df)

    # Fetch unique users
    user_list = df['user'].unique().tolist()
    if 'group_notification' in user_list:
        user_list.remove('group_notification')  # remove system messages
    user_list.sort()
    user_list.insert(0, "Overall")  # add option to analyze all users together

    st.sidebar.title("Show analysis wrt")
    selected_user = st.sidebar.selectbox("Select user", user_list)

    if st.sidebar.button("Show Analysis"):

        num_messages,words,num_media_meassage,num_links = helper.fetch_stats(selected_user, df)
        st.title("Top Statistics")
        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.header("Total Messages")
            st.subheader(num_messages)

        with col2:
            st.header("Total Words")
            st.subheader(words)

        with col3:
            st.header("Total media shared")
            st.subheader(num_media_meassage)

        with col4:
            st.header("Total links shared")
            st.subheader(num_links)

        #monthly timeline
        Timeline = helper.monthly_timeline(selected_user, df)
        st.title("Monthly Timeline")
        
        if Timeline.empty:
            st.write("No data available for monthly timeline.")
        else:
            fig, ax = plt.subplots()
            ax.plot(Timeline['time'], Timeline['message_count'], color='green', marker='o')
            plt.xticks(rotation=90)
            ax.set_xlabel("Month")
            ax.set_ylabel("Number of Messages")
            st.pyplot(fig)



        #daily timeline
        daily = helper.daily_timeline(selected_user, df)
        st.title("Daily Timeline")
        fig, ax = plt.subplots()
        ax.plot(daily['only_date'], daily['message_count'], color='red')
        plt.xticks(rotation=90)
        ax.set_xlabel("Date")
        ax.set_ylabel("Number of Messages")
        st.pyplot(fig)

        #activity map
        st.title("Activity Map")
        col1, col2 = st.columns(2)

        with col1:  
            st.header("Most busy day")
            busy_day = helper.week_activity_map(selected_user, df)
            fig, ax = plt.subplots()
            ax.bar(busy_day.index, busy_day.values, color='purple')
            plt.xticks(rotation=90)
            ax.set_xlabel("Day")
            ax.set_ylabel("Number of Messages")
            st.pyplot(fig)
        with col2:
            st.header("Most busy month")
            busy_month = helper.month_activity_map(selected_user, df)
            fig, ax = plt.subplots()
            ax.bar(busy_month.index, busy_month.values, color='orange')
            plt.xticks(rotation=90)
            ax.set_xlabel("Month")
            ax.set_ylabel("Number of Messages")
            st.pyplot(fig)

        #heatmap
        st.title("Weekly Activity Map")
        user_heatmap = helper.activity_heatmap(selected_user, df)
        fig, ax = plt.subplots()
        ax = sns.heatmap(user_heatmap)
        st.pyplot(fig)

            

        #finding busiest user in group (if overall selected)
        if selected_user == 'Overall':
            st.title("Most Busy Users")
            x,percent_def =  helper.most_busy_users(df)
            fig, ax = plt.subplots()
            

            col1, col2 = st.columns(2)

            with col1:
                ax.bar(x.index, x.values, color='red')
                plt.xticks(rotation='vertical')
                st.pyplot(fig)
            with col2:
                st.dataframe(percent_def) 

        #wordcloud
        st.title("Wordcloud")
        df_wc = helper.create_wordcloud(selected_user, df)
        fig, ax = plt.subplots()
        ax.imshow(df_wc)
        st.pyplot(fig)

        #most common words
        st.title("Most common words")
        common_words = helper.most_common_words(selected_user, df)  

        fig, ax = plt.subplots()
        ax.barh(common_words[0], common_words[1])
        plt.xticks(rotation='vertical')

        st.pyplot(fig)

        
        #emoji analysis

        emoji_df = helper.emoji_helper(selected_user, df)
        st.title("Emoji Analysis")

        col1, col2 = st.columns(2)

        with col1:
            st.dataframe(emoji_df)

        with col2:
            fig, ax = plt.subplots()
            ax.pie(emoji_df['Count'], labels=emoji_df['Emoji'], autopct='%1.1f%%', startangle=90)
            ax.axis('equal')  # equal aspect ratio ensures the pie is circular
            st.pyplot(fig)

        
                





