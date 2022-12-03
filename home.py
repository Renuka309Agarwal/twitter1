import streamlit as st
from streamlit_option_menu import option_menu

with st.sidebar:
    selected = option_menu(
        menu_title="twitter",  # required
        options=["Home", "sentiments","sentiment", "Contact"],  # required
        icons=["house", "twitter","twitter", "envelope"],  # optional
        menu_icon="cast",  # optional
        default_index=0,  # optional
            styles={
                "container": {"padding": "10" ,"background-color": "#fafafa"},
                "icon": {"color": "orange", "font-size": "25px"},
                "nav-link": {
                    "font-size": "25px",
                    "text-align": "left",

                    "margin": "0px",
                    "--hover-color": "#eee",
                },
                "nav-link-selected": {"background-color": "green"},
            },
        )

if selected == "sentiment":
    import streamlit as st
    from textblob import TextBlob
    import requests  # pip install requests
    import streamlit as st  # pip install streamlit
    from streamlit_lottie import st_lottie  # pip install streamlit-lottie


    def header(url):
        st.markdown(f'<p style="background-color:none;color:blue;font-size:45px;width:100%;align:centre;">{url}</p>',
                    unsafe_allow_html=True)


    header('SINGLE LINE SENTIMENT ANALYSIS')


    def load_lottieurl(url: str):
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()


    lottie_hello = load_lottieurl("https://assets3.lottiefiles.com/private_files/lf30_bz1uh69q.json")

    st_lottie(
        lottie_hello,
        speed=1,
        reverse=False,
        loop=True,
        width=200,
    )
    input = st.text_input("Enter Your Tweet")
    score = TextBlob(input).sentiment.polarity
    if score == 0:
        st.write("Neutral 😐")
    elif score < 0:
        st.write("Negative 😫")
    elif score > 0:
        st.write("Positive 😀")

if selected == "Home":
    import json

    import requests  # pip install requests
    import streamlit as st  # pip install streamlit
    from streamlit_lottie import st_lottie  # pip install streamlit-lottie


    def header(url):
        st.markdown(f'<p style="background-color:none;color:green;font-size:50px;width:100%;align:centre;">{url}</p>',
                    unsafe_allow_html=True)


    header('TWITTER SENTIMENT ANALYSIS')


    # GitHub: https://github.com/andfanilo/streamlit-lottie
    # Lottie Files: https://lottiefiles.com/

    def load_lottieurl(url: str):
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()


    lottie_hello = load_lottieurl("https://assets3.lottiefiles.com/private_files/lf30_bz1uh69q.json")

    st_lottie(
        lottie_hello,
        speed=1,
        reverse=False,
        loop=True,
        width=400,
    )

if selected == "sentiments":
    # -*- coding: utf-8 -*-
    import pandas as pd
    import seaborn as sns
    import matplotlib.pyplot as plt
    from textblob import TextBlob
    import tweepy
    import re
    from wordcloud import WordCloud
    import warnings

    warnings.filterwarnings("ignore", category=DeprecationWarning)
    import streamlit as st
    import requests  # pip install requests
    import streamlit as st  # pip install streamlit
    from streamlit_lottie import st_lottie  # pip install streamlit-lottie


    def header(url):
        st.markdown(f'<p style="background-color:none;color:green;font-size:50px;width:100%;align:centre;">{url}</p>',
                    unsafe_allow_html=True)


    header(' SENTIMENT ANALYSIS OF TWEETS')


    def load_lottieurl(url: str):
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()


    lottie_hello = load_lottieurl("https://assets3.lottiefiles.com/private_files/lf30_bz1uh69q.json")

    st_lottie(
        lottie_hello,
        speed=1,
        reverse=False,
        loop=True,
        width=200,
    )

    # assinging secret keys and token

    ## api removed from public code please use your own api

    consumer_key = '1AzSpfxr8RDcbNPC4HxEfTBdI'
    consumer_key_s = 'FrFm4e2P2tiYVAVRL3DEsAvNdOpsKWFYVqLAze5Fwa6bfCgStt'
    access_token = '1576445406405619712-SY7pPBG66uFCite7G0tmmm1HTHXD4o'
    access_token_s = 'WJyI1SwlSS1ZlcRdaIr5Acd5uvEE36nChNUZwLRh91ahA'
    # authenticating
    auth = tweepy.OAuthHandler(consumer_key, consumer_key_s)
    auth.set_access_token(access_token, access_token_s)
    api = tweepy.API(auth)


    def main():
        st.title("Please enter details")


    if __name__ == '__main__':
        main()

    # searchcriteria
    searchtype = st.selectbox("search with", ('Username', 'Hashtag'))
    searchvalue = st.text_input("Enter usrer name or hashtag")


    # searching the tweets
    def searchValue():
        if searchtype == 'Hashtag':
            searchv = api.search_tweets(searchvalue, count=1000, lang='en', tweet_mode='extended')
            return searchv
        elif searchtype == 'Username':
            searchv = api.user_timeline(screen_name=searchvalue, count=1000, lang='en', tweet_mode='extended')
            return searchv
        else:
            print('ok')


    searchv = searchValue()

    # creating dataframe
    if searchtype == 'Username':
        data = pd.DataFrame([tweet.full_text for tweet in searchv], columns=['tweets'])
    elif searchtype == 'Hashtag':
        data = pd.DataFrame([tweet.full_text for tweet in searchv], columns=['tweets'])
    else:
        pass


    # creating the function to clean the text
    def cleanText(text):
        text = re.sub(r'@[A-Za-z0-9_:]+', '', text)  # removin @mention
        text = re.sub(r'#', '', text)
        # removing '#' syboll
        text = re.sub(r'RT[\s]+', '', text)  # removing retweets
        text = re.sub(r'https?:\/\/\S+', '', text)  # removing links

        return text


    data['tweets'] = data['tweets'].apply(cleanText)


    # creting a funcitno to get subjectivity
    def getSubejectivity(text):
        return TextBlob(text).sentiment.subjectivity


    # creating a function to get polarity
    def getPolarity(text):
        return TextBlob(text).sentiment.polarity


    # creating a new column for subjectivity and polority
    data['Polarity'] = data['tweets'].apply(getPolarity)
    data['Subjectivity'] = data['tweets'].apply(getSubejectivity)


    # plot the wordclaud
    def PlotWordcloud():
        allwords = ''.join(twts for twts in data['tweets'])
        if len(allwords) == 0:
            allwords = 'twitter sentiment analysis'
            wrdcld = WordCloud(width=500, height=300, random_state=21, max_font_size=120).generate(allwords)
            plt.axis('off')
            fig, ax = plt.subplots()
            ax = plt.imshow(wrdcld, interpolation='bilinear')
            return fig
        else:
            wrdcld = WordCloud(width=500, height=300, random_state=21, max_font_size=120).generate(allwords)
            plt.axis('off')
            fig, ax = plt.subplots()
            ax = plt.imshow(wrdcld, interpolation='bilinear')
            return fig


    st.pyplot(PlotWordcloud())


    # plotting the subjectivity and poloarity
    def scatterPlot():
        plt.figure(figsize=(15, 7))
        plt.title('Sentimental Analysis')
        plt.xlabel('Tweets')
        plt.ylabel('Polarity & Subjectivity')
        fig, ax = plt.subplots()
        ax = sns.scatterplot(data=data.iloc[:, 1:2])
        return fig


    st.pyplot(scatterPlot())


    # creating fucntion for analysis
    def computePositivity(polarityvalue):
        if polarityvalue > 0:
            return "Positive😀"
        elif polarityvalue < 0:
            return "Negative😫"
        else:
            return "Nutral😐"


    data['Analysis'] = data['Polarity'].apply(computePositivity)

    st.write(data)
if selected == "Contact":
    import streamlit as st  # pip install streamlit
    import json

    import requests  # pip install requests
    import streamlit as st  # pip install streamlit
    from streamlit_lottie import st_lottie


    def load_lottieurl(url: str):
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()


    lottie_hello = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_lt8ter7g.json")

    st_lottie(
        lottie_hello,
        speed=1,
        reverse=False,
        loop=True,
        width=200

    )

    contact_form = """
    <form action="https://formsubmit.co/agarwalrenuka773@gmail.com" method="POST">
         <input type="hidden" name="_captcha" value="false">
         <input type="text" name="name" placeholder="Your name" required>
         <input type="email" name="email" placeholder="Your email" required>
         <textarea name="message" placeholder="Your message here"></textarea>
         <button type="submit">Send</button>
    </form>
    """

    st.markdown(contact_form, unsafe_allow_html=True)


    # Use Local CSS File
    def local_css(file_name):
        with open(file_name) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


    local_css("style.css")