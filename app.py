import streamlit as st

# Configuration de la page
st.set_page_config(page_title="Le Code de Cliousclat", page_icon="🏺")

# Style CSS pour forcer la lisibilité du texte
st.markdown("""
    <style>
    /* Fond de page */
    .stApp { 
        background-color: #fdfaf5; 
    }
    /* Texte des énigmes et titres en marron foncé */
    .stApp p, .stApp label, .stApp h1, .stApp h2, .stApp h3 {
        color: #5D2E17 !important;
    }
    /* Case de saisie : fond sombre et texte BLANC pour la visibilité */
    .stNumberInput input {
        background-color: #5D2E17 !important;
        color: white !important;
        -webkit-text-fill-color: white !important; /* Pour Safari/iPhone */
    }
    /* Bouton personnalisé */
    .stButton>button { 
        background-color: #8b4513; 
        color: white !important; 
        border-radius: 20px; 
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
