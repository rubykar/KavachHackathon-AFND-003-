import joblib
import pickle
import streamlit as st
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
st.set_page_config(page_title = "Fake news detector",page_icon = ":tada:", layout = "wide")
tfidf_vectorizer = pickle.load(open('tfidf.pkl', 'rb'))
pickled_model = pickle.load(open('lr_model.pkl', 'rb'))
new_data = ["Abhinav Kashyap claims Salman Khan "]
new_data_tfidf = tfidf_vectorizer.transform(new_data)
predicted_label = pickled_model.predict(new_data_tfidf)
# st.markdown("""<form>
#       <label for="name">Enter the news:</label>
#       <input type="text" id="name" name="name" placeholder="Your name...">
#       <input type="submit" value="Submit">
#   </form>""", unsafe_allow_html = True)
st.title("Fake news Detector AI")
st.subheader("BEWARE OF FAKE NEWS!")
st.subheader("Hello, I am here to help you identify fake news floating around.")
st.write(" In the era of information overload, it can be challenging to distinguish between real and fake news. Our web application helps you separate fact from fiction by analyzing news articles and providing a prediction on whether they are genuine or fake.Our detector uses advanced machine learning algorithms to analyze various features of news articles, such as language, tone, and sentiment, to identify patterns that distinguish real from fake news. By leveraging these algorithms, we can provide you with a reliable and accurate prediction of the authenticity of any news article that you submit.So, whether you're curious about the authenticity of a news article you've read or want to verify a piece of news before sharing it with others, our Fake News Detector is here to help. Simply enter the news article in the text box provided, and we'll provide you with a prediction of whether it's genuine or fake.")
news = st.text_input("Enter the news you want to check:")
if news:
    news = [news]
    new_data_tfidf = tfidf_vectorizer.transform(news)
    predicted_label = pickled_model.predict(new_data_tfidf)
    #st.write(f"Hello, {name}!")
    if predicted_label[0]=="Fake":
        st.write("FAKE NEWS DETECTED!")
        true_news = "True news goes here!"
        st.write("The true version of this news might be:", true_news)
    else:
        st.write("This is a true news!.")
