import streamlit as st

# 1. CONFIGURATION ET DESIGN ÉPURÉ
st.set_page_config(page_title="Le Code de Cliousclat", page_icon="🏺")

st.markdown("""
    <style>
    .stApp { background-color: #FDFBF7; }
    h1, h2, h3, p, label { color: #5D2E46 !important; font-family: 'Helvetica Neue', Arial, sans-serif; }
    
    /* Style des cases de saisie */
    .stNumberInput div[data-baseweb="input"] {
        background-color: #8B4513 !important;
        border-radius: 12px !important;
        border: 2px solid #5D2E46 !important;
    }
    .stNumberInput input {
        color: #FFFFFF !important;
        -webkit-text-fill-color: #FFFFFF !important;
        font-size: 1.2rem !important;
        font-weight: bold !important;
        text-align: center !important;
    }

    /* Style du bouton */
    .stButton > button {
        width: 100% !important;
        background-color: #5D2E46 !important;
        color: #FFFFFF !important;
        border-radius: 50px !important;
        padding: 15px !important;
        font-weight: 600 !important;
        text-transform: uppercase;
        border: none !important;
    }
    .stButton > button div p { color: #FFFFFF !important; }
    </style>
""", unsafe_allow_html=True)

# 2. LOGIQUE DE NAVIGATION
if 'page' not in st.session_state:
    st.session_state.page = 'intro'

def aller_au_jeu():
    st.session_state.page = 'jeu'

def aller_a_intro():
    st.session_state.page = 'intro'

# --- PAGE 1 : INTRODUCTION NARRATIVE ---
if st.session_state.page == 'intro':
    st.title("🏺 Le Secret de l'Argile")
    
    # AJOUT DE L'IMAGE ICI
    st.image("https://i.postimg.cc/SQ8DG54J/Gemini-Generated-Image-5im20b5im20b5im2.png", 
             caption="Cliousclat, terre de potiers", 
             use_container_width=True)
    
    st.write("""
    ### Bienvenue à Cliousclat.
    
    Depuis des siècles, le feu des fours illumine ces collines et les mains des potiers façonnent la terre. Mais au-delà de l'artisanat, le village cache un secret accessible uniquement à ceux qui savent observer.
    
    Une combinaison de **six nombres** a été dissimulée à travers les ruelles, les pierres et les panoramas. Seul le cumul exact de ces chiffres vous permettra de déverrouiller le code final.
    
    *Prenez votre temps, observez les détails, et laissez le village vous raconter son histoire.*
    """)
    
    st.divider()
    st.button("Commencer l'exploration", on_click=aller_au_jeu)

# --- PAGE 2 : LES ÉNIGMES ---
elif st.session_state.page == 'jeu':
    st.title("🧩 Les Énigmes")
    
    # Liste des énigmes
    q1 = st.number_input("1. Le volume total du grand four (m³)", min_value=0, step=1)
    q2 = st.number_input("2. Le numéro de rue de la Poterie du Fer Rouge", min_value=0, step=1)
    q3 = st.number_input("3. Nombre de becs verseurs de la fontaine", min_value=0, step=1)
    q4 = st.number_input("4. Nombre de cloches dans le clocher", min_value=0, step=1)
    q5 = st.number_input("5. Distance Cliousclat-Privas au Belvédère (km)", min_value=0, step=1)
    q6 = st.number_input("6. Âge de la fabrique en 2026 (ans)", min_value=0, step=1)

    st.divider()

    if st.button("Vérifier le Code Final"):
        # Calcul des réponses
        total_joueur = q1 + q2 + q3 + q4 + q5 + q6
        total_attendu = 20 + 664 + 2 + 1 + 24 + 124 # Soit 835
        
        if total_joueur == total_attendu:
            st.balloons()
            st.success(f"Félicitations ! Le code {total_joueur} est correct.")
            st.subheader("Vous avez percé le secret de Cliousclat.")
        else:
            st.error("Le code est incorrect. Repartez à la recherche des chiffres manquants.")

    st.button("Retour au récit", on_click=aller_a_intro)
