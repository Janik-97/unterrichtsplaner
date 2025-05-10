import streamlit as st

# Beispielhafte Lehrplandaten (Du kannst hier später echte Daten integrieren)
subjects = {
    "Biologie": {
        "Jahrgangsstufe 7": ["Thema 1: Zellen", "Thema 2: Photosynthese"],
        "Jahrgangsstufe 8": ["Thema 1: Genetik", "Thema 2: Evolution"]
    },
    "Chemie": {
        "Jahrgangsstufe 7": ["Thema 1: Atome und Moleküle", "Thema 2: Säuren und Basen"],
        "Jahrgangsstufe 8": ["Thema 1: Chemische Reaktionen", "Thema 2: Periodensystem"]
    }
}

# Sidebar für Fach und Jahrgangsstufe
st.sidebar.title("Unterrichtsplaner")
fach = st.sidebar.selectbox("Wählen Sie das Fach", list(subjects.keys()))
jahrgang = st.sidebar.selectbox("Wählen Sie die Jahrgangsstufe", list(subjects[fach].keys()))

# Anzeige der Themen in der Hauptansicht
st.title(f"{fach} - Jahrgangsstufe {jahrgang}")

# Klappbare Überkapitel für das ausgewählte Fach und die Jahrgangsstufe
with st.expander(f"{fach} - Lehrplan"):
    for thema in subjects[fach][jahrgang]:
        st.checkbox(thema)

# Optionale Anzeige von weiteren Inhalten
st.write("Hier könnte weitere interaktive Planung erfolgen.")
