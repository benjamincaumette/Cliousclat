import streamlit as st

# Configuration de la page
st.set_page_config(page_title="Le Code de Cliousclat", page_icon="🏺")

# Style CSS pour forcer la lisibilité du texte
st.markdown("""
    <style>
    /* 1. CONFIGURATION GÉNÉRALE */
    .stApp {
        background-color: #FDFBF7; /* Blanc cassé / Papier */
    }

    /* 2. TITRES ET TEXTES (Marron Terre de Sienne) */
    h1, h2, h3, p, label {
        color: #5D2E46 !important; /* Marron profond */
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
    }

    /* 3. LES CHAMPS DE SAISIE (Look moderne) */
    .stNumberInput div[data-baseweb="input"] {
        background-color: #8B4513 !important; /* Fond Marron Poterie */
        border-radius: 12px !important;
        border: 2px solid #5D2E46 !important;
        padding: 5px !important;
    }

    /* Chiffres à l'intérieur des cases */
    .stNumberInput input {
        color: #FFFFFF !important; /* BLANC PUR */
        -webkit-text-fill-color: #FFFFFF !important;
        font-size: 1.2rem !important;
        font-weight: bold !important;
        text-align: center !important;
    }

    /* 4. LE BOUTON FINAL (Bouton d'action élégant) */
    .stButton > button {
        width: 100% !important;
        background-color: #5D2E46 !important; /* Couleur plus sombre pour le bouton */
        color: #FFFFFF !important; /* TEXTE BLANC */
        border: none !important;
        padding: 15px !important;
        border-radius: 50px !important; /* Arrondi complet */
        font-size: 1.1rem !important;
        font-weight: 600 !important;
        text-transform: uppercase;
        letter-spacing: 1px;
        box-shadow: 0 4px 15px rgba(93, 46, 70, 0.2);
        transition: all 0.3s ease;
    }

    .stButton > button:hover {
        background-color: #8B4513 !important; /* Change au survol */
        transform: translateY(-2px);
    }

    /* 5. FIX POUR LE TEXTE DU BOUTON (Obligatoire sur Streamlit) */
    .stButton > button div p {
        color: #FFFFFF !important;
    }
    
    /* 6. STYLE DES MESSAGES DE RÉUSSITE / ERREUR */
    .stAlert {
        border-radius: 12px !important;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🏺 Le Code de Cliousclat")
st.write("Bienvenue dans le jeu de piste ! Trouve les nombres cachés dans le village.")

# --- LES ÉNIGMES ---
questions = [
    {"q": "1. Quel est le volume total du grand four en m³ ?", "a": 20},
    {"q": "2. Quel est le numéro de rue de la Poterie du Fer Rouge ?", "a": 664},
    {"q": "3. Combien de becs verseurs possède la fontaine ?", "a": 2},
    {"q": "4. Combien de cloches vois-tu dans le clocher ?", "a": 1},
    {"q": "5. Distance Cliousclat - Privas indiquée au Belvédère (km) ?", "a": 24},
    {"q": "6. Depuis combien d'années la fabrique existe-t-elle (en 2026) ?", "a": 124}
]

responses = []
score = 0

# Génération des champs de réponse
for i, item in enumerate(questions):
    res = st.number_input(item["q"], min_value=0, key=f"q{i}", step=1)
    responses.append(res)
    if res == item["a"]:
        score += 1

st.divider()

# --- VALIDATION ---
if st.button("Vérifier le Code Final"):
    total_attendu = sum(q["a"] for q in questions)
    total_joueur = sum(responses)
    
    if total_joueur == total_attendu:
        st.balloons()
        st.success(f"Bravo ! Le code final est correct : {total_attendu}")
        st.write("Félicitations, vous êtes un expert de Cliousclat !")
    else:
        st.error(f"Le code est incorrect. Vous avez {score} bonne(s) réponse(s) sur {len(questions)}.")
        st.info("Continuez à chercher dans les ruelles !")
