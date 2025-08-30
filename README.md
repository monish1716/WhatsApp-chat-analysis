# 💬 WhatsApp Chat Analyzer (Python + Streamlit)
[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)]((https://monish-whatsapp-chat-analysis.streamlit.app/))




![Python](https://img.shields.io/badge/Language-Python-blue)
![ML](https://img.shields.io/badge/Domain-Machine_Learning-green)
![Matplotlib](https://img.shields.io/badge/Library-Matplotlib-yellow)
![Seaborn](https://img.shields.io/badge/Library-Seaborn-orange)  
An interactive WhatsApp Chat Analyzer built with Python and Streamlit that provides insights into your chats including message trends, user activity, emoji usage, and most common words.

---

## 🚀 Features
- 📊 Data preprocessing and cleaning of raw dataset.  
- 🧮 Content-based filtering using **cosine similarity**.  
- 🎥 Movie recommendations with titles and posters.  
- 🌐 Interactive **Streamlit web app** for easy use.  

---

## 🛠️ Tech Stack
- **Python**
- **Pandas, NumPy**
- **Scikit-learn**
- **Streamlit**
- **Pickle** (for saving the model)

---

## ⚙️ Installation & Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/monish1716/Movies-Recommend-System.git
   cd Movies-Recommend-System

2. Install dependencies:

pip install -r requirements.txt

3. Download similarity.pkl:
   ```bash
   pip install gdown
   python download_similarity.py
   
4. Run the Streamlit app:

streamlit run app.py

---

## Dataset
This project uses the TMDB 5000 Movies Dataset from Kaggle, which contains two files:
1. `movies.csv` – movie details (title, genres, keywords, etc.)
2. `credits.csv` – cast and crew information  

Download them from [Kaggle](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata) and place them in the `data/` folder.

---

## 🎯 How It Works
 
1️⃣ Extract features (genres, cast, crew, keywords)  
2️⃣ Preprocess data (clean, remove nulls/duplicates)  
3️⃣ Convert text → vectors (CountVectorizer)  
4️⃣ Compute **cosine similarity** between movies  
5️⃣ Recommend **Top 5 similar movies** 🎥  


---

## 🌐 Demo

After running the Streamlit app:
Enter a movie title in the input box.
Get top 5 recommended movies with posters.

---

## 📌 Example  
Here’s how the app looks in action:  

![Movie Recommender Screenshot](images/mrs.png)  

---

## 🔮 Future Improvements  
- [ ] Add hybrid recommendation system (content + collaborative)  
- [ ] Deploy on HuggingFace Spaces / Render  
- [ ] Integrate with real-time movie APIs  

---

## 🤝 Contributing

Pull requests are welcome.
For major changes, please open an issue first to discuss what you’d like to change

