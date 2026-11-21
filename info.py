import streamlit as st

st.title("Information")
st.warning("Notes\n\n"
           "Miss distance (AU) - The distance from earth during close approach.\n\n"
           "Minimum Orbit Intersection Distance (MOID, AU) - The closest distance between earth's orbit and the asteroid's orbit.\n\n"
           "Eccentricity - The shape of the orbit - 0 = circular, 0 < e < 1 = elliptical.\n\n"
           "Perihelion distance (AU) - The distance of the sattelite from the parental object it orbits, at its closest point to it.\n\n"
           "Aphelion distance (AU) - The distance of the sattelite from the parental object it orbits, at its farthest point from it.\n\n"
           "Mean motion (Degrees per day) - The average angular speed of the asteroid along its orbit."
           "Orbital period (days) - The time it takes for a sattelite to complete one full orbit."
        )

st.header("Model information")
st.write(
    "The AI model is a Linear Regression model that uses six features to predict a output.\n\n"
    "In this case, the model takes as input the Miss distance of the asteroid, its MOID, the orbit's eccentricity, the Perihelion distance and the Aphelion distance of the sattelite's orbit, and the asteroid's mean motion - it predicts the Orbital period of the sattelite."
)

st.header("Game explanation")
st.write(
    "The game includes six sliders that are used to supply the AI model with information, so it will be able to predict the orbital period.\n\n"
    "The features that the user has provided are then displayed, along with the orbital period prediction, in the blue and green text boxes that are to the right of the sliders.\n\n"
    "In order to visualize the orbit that the user has created (with the information they provided), there is a graph under the information text boxes that shows sattelite's orbit (this visualization is not accurate).\n\n"
)