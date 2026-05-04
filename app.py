import streamlit as st
import folium
from streamlit.components.v1 import html

# --- CONFIG ---
st.set_page_config(page_title="Le Code de Cliousclat", page_icon="🏺", layout="centered")

# --- STYLE ---
st.markdown("""
<style>
.stApp {
    background: linear-gradient(180deg, #fdfaf5 0%, #f4efe6 100%);
    color: #3e2f1c;
}

h1, h2, h3 {
    color: #8b4513 !important;
    text-align: center;
}

p, label, div {
    color: #3e2f1c !important;
    font-size: 16px;
}

.stButton>button {
    background-color: #8b4513;
    color: white;
    border-radius: 25px;
    padding: 10px 25px;
    font-weight: bold;
    transition: 0.3s;
}
.stButton>button:hover {
    background-color: #a0522d;
    transform: scale(1.05);
}

.block {
    background-color: white;
    padding: 20px;
    border-radius: 15px;
    margin-bottom: 15px;
    box-shadow: 0 4px 10px rgba(0,0,0,0.05);
}
</style>
""", unsafe_allow_html=True)

# --- TITRE ---
st.title("🏺 Le Code de Cliousclat")
st.markdown("### 🔍 Résous les énigmes pour découvrir le code final")

# --- AUDIO ---
st.markdown("### 🎧 Ambiance du village")

st.audio("assets/ambiance.mp3")

# --- QUESTIONS ---
questions = [
    {"q": "Volume total du grand four (m³) ?", "a": 20, "pos": [44.6526, 4.8333]},
    {"q": "Numéro de rue de la Poterie du Fer Rouge ?", "a": 664, "pos": [44.6530, 4.8325]},
    {"q": "Nombre de becs de la fontaine ?", "a": 2, "pos": [44.6528, 4.8330]},
    {"q": "Nombre de cloches dans le clocher ?", "a": 1, "pos": [44.6525, 4.8335]},
    {"q": "Distance Cliousclat → Privas (km) ?", "a": 24, "pos": [44.6529, 4.8332]},
    {"q": "Âge de la fabrique en 2026 ?", "a": 124, "pos": [44.6532, 4.8328]}
]

# --- STATE ---
if "validated" not in st.session_state:
    st.session_state.validated = False

responses = []

# --- INPUTS ---
for i, item in enumerate(questions):
    with st.container():
        st.markdown(f'<div class="block">', unsafe_allow_html=True)

        res = st.number_input(
            f"**{i+1}. {item['q']}**",
            min_value=0,
            step=1,
            key=f"q{i}"
        )

        responses.append(res)

        if st.session_state.validated:
            if res == item["a"]:
                st.success("✅ Correct")
            else:
                st.error(f"❌ Faux (réponse : {item['a']})")

        st.markdown("</div>", unsafe_allow_html=True)

# --- PROGRESSION ---
score_live = sum(1 for i, q in enumerate(questions) if responses[i] == q["a"])
progress = score_live / len(questions)

st.progress(progress)
st.caption(f"Progression : {score_live} / {len(questions)} bonnes réponses")

st.divider()

# --- VALIDATION ---
if st.button("🔐 Vérifier le Code Final"):
    st.session_state.validated = True

    total_attendu = sum(q["a"] for q in questions)
    total_joueur = sum(responses)

    if total_joueur == total_attendu:
        st.balloons()
        st.success("🎉 CODE VALIDÉ ! 🎉")
        st.markdown(f"## 🔢 Code final : **{total_attendu}**")
    else:
        st.error("❌ Code incorrect")
        st.warning(f"Tu as {score_live} bonne(s) réponse(s)")

# --- CARTE ---
st.markdown("## 🗺️ Carte interactive")

map_center = [44.6528, 4.8330]

m = folium.Map(location=map_center, zoom_start=16)

for i, q in enumerate(questions):
    folium.Marker(
        location=q["pos"],
        popup=f"Énigme {i+1}",
        tooltip=q["q"]
    ).add_to(m)

html(m._repr_html_(), height=500)
