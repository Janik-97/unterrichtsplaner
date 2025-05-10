import streamlit as st

st.title("📚 Unterrichtsplaner")

fach = st.selectbox("Fach wählen", ["Biologie", "Chemie"])
thema = st.text_input("Stundenthema eingeben")
schema = st.selectbox("Unterrichtsschema", [
    "Einstieg–Erarbeitung–Sicherung",
    "Gruppenarbeit",
    "Stationenlernen"
])

if st.button("Stunde generieren"):
    st.subheader("🧩 Strukturvorschlag")
    st.write(f"**Fach:** {fach}")
    st.write(f"**Thema:** {thema}")
    st.write(f"**Schema:** {schema}")
    st.write("### 🧠 Vorschläge")
    st.write("**Einstieg:** Zeige ein Phänomen oder stelle eine provozierende Frage.")
    st.write("**Erarbeitung:** Schüler*innen analysieren Material in Partnerarbeit.")
    st.write("**Sicherung:** Gemeinsames Mindmap oder Quiz.")
