import streamlit as st

# --- CONFIG ---
st.set_page_config(
    page_title="Le Code de Cliousclat",
    page_icon="🏺",
    layout="centered"
)

# --- CSS ROBUSTE (FIX DÉFINITIF COULEUR) ---
st.markdown("""
<style>

/* Fond général */
.stApp {
    background-color: #f8f5f0;
}

/* 🔥 Couleur de TOUT le texte (fix principal) */
html, body, .stApp {
    color: #3e2f1c !important;
}

/* Texte des widgets Streamlit */
div, p, label, span {
    color: #3e2f1c !important;
}

/* Champs de saisie */
input {
    color: #3e2f1c !important;
}

/* Titres */
h1 {
    color: #8b4513 !important;
    text-align: center;
}

/* Cartes */
.block {
    background-color: white;
    padding: 18px;
    border-radius: 12px;
    margin-bottom: 12px;
    border: 1px solid #e5e5e5;
}

/* Bouton */
.stButton>button {
    background-color: #8b4513;
    color: white;
    border-radius: 8px;
    padding: 8px 20px;
}

/* Barre de progression */
.stProgress > div > div > div {
    background-color: #8b4513;
}

</style>
""", unsafe_allow_html=True)

# --- TITRE ---
st.title("🏺 Le Code de Cliousclat")
st.write("Résous les énigmes pour trouver le code final.")

# --- QUESTIONS ---
questions = [
    {"q": "Volume total du grand four (m³) ?", "a": 20},
    {"q": "Numéro de rue de la Poterie du Fer Rouge ?", "a": 664},
    {"q": "Nombre de becs de la fontaine ?", "a": 2},
    {"q": "Nombre de cloches dans le clocher ?", "a": 1},
    {"q": "Distance Cliousclat → Privas (km) ?", "a": 24},
    {"q": "Âge de la fabrique en 2026 ?", "a": 124}
]

# --- FORMULAIRE (STABLE) ---
responses = []

with st.form("quiz_form"):
    for i, item in enumerate(questions):
        st.markdown('<div class="block">', unsafe_allow_html=True)

        res = st.number_input(
            f"{i+1}. {item['q']}",
            min_value=0,
            step=1,
            key=f"q{i}"
        )

        responses.append(res)

        st.markdown('</div>', unsafe_allow_html=True)

    submitted = st.form_submit_button("Vérifier")

# --- RÉSULTAT ---
if submitted:
    score = sum(1 for i, q in enumerate(questions) if responses[i] == q["a"])
    total_attendu = sum(q["a"] for q in questions)
    total_joueur = sum(responses)

    st.divider()

    st.progress(score / len(questions))
    st.write(f"{score} / {len(questions)} bonnes réponses")

    if total_joueur == total_attendu:
        st.success("🎉 Bravo ! Code correct")
        st.write(f"Code final : **{total_attendu}**")
    else:
        st.error("❌ Code incorrect")
