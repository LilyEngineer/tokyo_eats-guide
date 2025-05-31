import streamlit as st
import pandas as pd
import pydeck as pdk

# --- Page config ---
st.set_page_config(page_title="Tokyo Eats Guide", layout="wide")
st.title("🍣 Tokyo Eats Guide")
st.markdown("Filter and discover the best places to eat in Tokyo — from budget to luxury.")

# --- Load data ---
df = pd.read_csv("tokyo_restaurants.csv")
restaurants = df.to_dict(orient="records")

# --- Currency conversion rates ---
currency_rates = {
    "JPY": 1,
    "USD": 0.0064,
    "EUR": 0.0059,
    "GBP": 0.0051
}

# --- Sidebar filters ---
st.sidebar.header("🔍 Filters")
currency = st.sidebar.selectbox("Currency", options=list(currency_rates.keys()))
trip_budget = st.sidebar.number_input("Total Trip Budget (in selected currency)", min_value=0.0, value=1000.0, step=10.0)
days = st.sidebar.number_input("Number of Days in Tokyo", min_value=1, value=5)
max_daily_budget = (trip_budget / days) / currency_rates[currency]
st.sidebar.markdown(f"💴 Max daily budget in yen: ¥{int(max_daily_budget):,}")

selected_neighborhoods = st.sidebar.multiselect("Neighborhoods", options=sorted(df['neighborhood'].unique()), default=df['neighborhood'].unique())
selected_types = st.sidebar.multiselect("Food Type", options=sorted(df['type'].unique()), default=df['type'].unique())
sort_option = st.sidebar.radio("Sort by", options=["Rating", "Price"], horizontal=True)

# --- Initialize favorites ---
if "favorites" not in st.session_state:
    st.session_state.favorites = []

def toggle_favorite(name):
    if name in st.session_state.favorites:
        st.session_state.favorites.remove(name)
    else:
        st.session_state.favorites.append(name)

# --- Filter data ---
filtered_restaurants = [r for r in restaurants if
    r['price'] <= max_daily_budget and
    r['neighborhood'] in selected_neighborhoods and
    r['type'] in selected_types
]

if sort_option == "Rating":
    filtered_restaurants.sort(key=lambda x: x['rating'], reverse=True)
elif sort_option == "Price":
    filtered_restaurants.sort(key=lambda x: x['price'])

# --- Display Restaurants ---
st.subheader(f"🎯 Showing {len(filtered_restaurants)} results")
for r in filtered_restaurants:
    with st.container(border=True):
        st.image(r['photo_url'], width=300)
        cols = st.columns([3, 1])
        with cols[0]:
            st.subheader(r['name'])
            st.markdown(f"🍽️ *{r['type'].title()}*  | 📍 {r['neighborhood']}")
            st.markdown(f"💴 ¥{r['price']:,}  | ⭐ {r['rating']}")
            st.markdown(f"📍 {r['address']}")
            st.markdown(f"💬 _{r['review']}_")
        with cols[1]:
            if r['name'] in st.session_state.favorites:
                if st.button("★ Unfavorite", key=f"fav_{r['name']}"):
                    toggle_favorite(r['name'])
            else:
                if st.button("☆ Favorite", key=f"fav_{r['name']}"):
                    toggle_favorite(r['name'])

# --- Show favorites ---
with st.sidebar:
    st.markdown("---")
    st.header("⭐ Your Favorites")
    for fav in st.session_state.favorites:
        st.write(f"- {fav}")

# --- Map ---
st.subheader("🗺️ Map View")
map_df = pd.DataFrame(filtered_restaurants)
if not map_df.empty:
    st.pydeck_chart(pdk.Deck(
        map_style='mapbox://styles/mapbox/light-v9',
        initial_view_state=pdk.ViewState(
            latitude=map_df['lat'].mean(),
            longitude=map_df['lon'].mean(),
            zoom=12,
            pitch=50,
        ),
        layers=[
            pdk.Layer(
                'ScatterplotLayer',
                data=map_df,
                get_position='[lon, lat]',
                get_color='[200, 30, 0, 160]',
                get_radius=150,
            ),
        ],
    ))
else:
    st.info("No restaurants match your filters.")
