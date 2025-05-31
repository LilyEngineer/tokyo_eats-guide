# 🍣 Tokyo Eats Guide

Your ultimate curated guide to eating in Tokyo — from budget ramen joints to Michelin-star sushi.  
This interactive app helps locals, travelers, and food lovers explore 100+ of the city's best restaurants, filtered by price, location, and cuisine.


Here's a screenshot of the app:
![App Screenshot]((https://github.com/LilyEngineer/tokyo_eats_guide/blob/fb80739e49d4f95645195ffe4ffc80914c2adb16/images/Screenshot%202025-05-30%20204526.png)

---

## 🔥 Features

- 🍜 Browse 100+ top-rated Tokyo restaurants across **all budgets**
- 📍 Filter by **neighborhood**, **price level**, or **cuisine**
- 💸 Plan your food expenses with **daily and trip budget tools**
- 🌐 Built-in **currency converter** (JPY to your local currency)
- 🗺️ View restaurant locations on interactive **maps**
- 📷 See images, ratings, and must-try dishes

---

## 🛠 Tech Stack

- **Python 3.11+**
- **Streamlit** – easy, fast UI for data apps
- **Pandas** – CSV data management
- **Plotly / Folium** – optional for mapping
- **OpenStreetMap** – base for location views
- **CSV** – backend data source (`restaurants.csv`)

---

## 🚀 How to Run the App

1. **Clone the repository:**
   ```bash
   git clone https://github.com/LilyEngineer/tokyo_eats_guide.git
   cd tokyo_eats_guide

pip install -r requirements.txt

streamlit run app.py

tokyo_eats_guide/
├── app.py                # Streamlit frontend logic
├── restaurants.csv       # Main data source (100+ listings)
├── requirements.txt      # Dependencies
└── README.md             # This file

🧩 Planned Additions
🔎 Search by keyword or dish

⭐ User reviews and favorites

📆 Daily meal planner

📍 Google Maps integration

📜 License
MIT License.
Contributions welcome! Feel free to fork, improve, or submit a pull request with new restaurant data.

Bon Appétit — or as they say in Japan, いただきます! 🇯🇵
