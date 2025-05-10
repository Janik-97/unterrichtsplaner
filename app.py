import streamlit as st

# Beispielhafte Daten für die Unterrichtsphasen (Wiederholung, Motivation, etc.)
lesson_flow = {
    "Wiederholung": [
        "Fragen zur letzten Stunde",
        "Kurze Gruppenarbeit",
        "Quiz zur Vorstunde",
        "Visualisierung der letzten Stunde"
    ],
    "Motivation": [
        "Fragen zur Relevanz des Themas",
        "Aktuelles Beispiel aus der Praxis",
        "Bezug zur Lebenswelt der Schüler herstellen",
        "Motivierendes Video"
    ],
    "Erarbeitung": [
        "Lernstationen",
        "Kooperative Gruppenarbeit",
        "Frontalunterricht mit interaktiven Elementen",
        "Experiment durchführen"
    ],
    "Sicherung": [
        "Kurzes Quiz zur Stunde",
        "Zusammenfassung durch Schüler",
        "Individuelle Reflexion",
        "Abschlussdiskussion"
    ]
}

# Funktion zum Erstellen eines Vorschlags mit Auswahlmöglichkeiten
def show_step(step_name):
    st.subheader(f"{step_name} - Schritt")
    choices = lesson_flow.get(step_name, [])
    selected_option = st.radio(
        "Wähle eine Option für diesen Schritt",
        choices
    )
    st.write(f"Du hast gewählt: **{selected_option}**")
    return selected_option

# Titel der App
st.title("Unterrichtsplaner - Schritt für Schritt")

# Start des Flows mit Wiederholung
current_step = "Wiederholung"
selected_wiederholung = show_step(current_step)

# Nach Auswahl in "Wiederholung" folgt der nächste Schritt, z.B. "Motivation"
if selected_wiederholung:
    st.write("---")
    selected_motivation = show_step("Motivation")

# Nach Auswahl in "Motivation" folgt der nächste Schritt, z.B. "Erarbeitung"
if selected_motivation:
    st.write("---")
    selected_erarbeitung = show_step("Erarbeitung")

# Nach Auswahl in "Erarbeitung" folgt der nächste Schritt, z.B. "Sicherung"
if selected_erarbeitung:
    st.write("---")
    selected_sicherung = show_step("Sicherung")

# Optional kannst du hier eine Zusammenfassung des gesamten Flows anzeigen
if selected_sicherung:
    st.write("### Zusammenfassung der geplanten Stunde:")
    st.write(f"1. **Wiederholung:** {selected_wiederholung}")
    st.write(f"2. **Motivation:** {selected_motivation}")
    st.write(f"3. **Erarbeitung:** {selected_erarbeitung}")
    st.write(f"4. **Sicherung:** {selected_sicherung}")
