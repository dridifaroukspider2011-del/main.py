import streamlit as st
import requests
import random

# 1. Configuration
st.set_page_config(page_title="AppScanner Global", page_icon="🔎")

# 2. Style CSS
st.markdown("""
    <style>
    .stButton>button {
        width: 100%;
        border-radius: 20px;
        background-color: #2A5C9A;
        color: white;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Header
col1, col2 = st.columns([1, 3])
with col1:
    try:
        st.image("image_b35803.jpg", width=100)
    except:
        st.title("🔎")
with col2:
    st.title("AppScanner Global")

st.divider()

# 4. Recherche
idee = st.text_input("Quelle application scanner ?", placeholder="Ex: Block Blast")

if st.button("Lancer le Scanner 🚀"):
    if not idee:
        st.warning("Entre un nom d'application !")
    else:
        with st.spinner('Analyse...'):
            try:
                # Tentative réelle
                url = "https://itunes.apple.com/search"
                res = requests.get(url, params={"term": idee, "entity": "software", "limit": 4}, timeout=5)
                res.raise_for_status()
                donnees = res.json()
                results = donnees.get("results", [])
            except:
                # MODE DÉMO : Si l'API est bloquée, on simule des données
                st.info("💡 Mode Démo activé (Connexion API bloquée par l'éditeur)")
                results = [
                    {
                        "trackName": f"{idee} Pro",
                        "sellerName": "Dev Studio Inc.",
                        "averageUserRating": 4.5,
                        "formattedPrice": "Gratuit",
                        "description": f"La meilleure version de {idee} pour mobile.",
                        "artworkUrl100": "https://is1-ssl.mzstatic.com/image/thumb/Purple122/v4/7b/72/f3/7b72f37c-f38b-0881-8e50-f80e0600a944/AppIcon-0-0-1x_U007emarketing-0-0-0-7-0-0-sRGB-0-0-0-GLES2_U002c0-512MB-85-220-0-0.png/256x256bb.jpg"
                    },
                    {
                        "trackName": f"{idee} - Puzzle Game",
                        "sellerName": "Game Masters",
                        "averageUserRating": 3.2,
                        "formattedPrice": "1,99 €",
                        "description": "Un clone amusant avec des graphismes rétro.",
                        "artworkUrl100": "https://is1-ssl.mzstatic.com/image/thumb/Purple112/v4/4a/5b/4a/4a5b4a3a-3c3d-e3f4-a5b6-c7d8e9f0a1b2/AppIcon-0-0-1x_U007emarketing-0-85-220-0.png/256x256bb.jpg"
                    }
                ]

            # Affichage du Score
            count = len(results)
            if count > 2:
                st.error("🔴 Score : 3/10 - Marché Saturé")
            else:
                st.warning("🟡 Score : 7/10 - Compétition Modérée")
            
            st.divider()

            # Affichage des cartes
            cols = st.columns(2)
            for i, app in enumerate(results):
                with cols[i % 2]:
                    st.image(app["artworkUrl100"], width=60)
                    st.markdown(f"**{app['trackName']}**")
                    st.caption(f"⭐ {app['averageUserRating']} | {app['formattedPrice']}")
                    with st.expander("Détails"):
                        st.write(app["description"])

st.caption("Propulsé par AppScanner Global • 2026")
