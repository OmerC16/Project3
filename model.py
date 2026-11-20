import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
from matplotlib.patches import Ellipse

ORBIT_OBJECT_RADIUS = 0.35
CONST_X = 5
VERTICAL_DIST_MIN = 2.01 - 0.18
VERTICAL_DIST_MAX = 8.98 - 0.18
WIDTH_TO_HEIGHT_RATIO = 0.6
W = np.array([-3610782303.5985737, 1614790935.5551405, 6.93764541298151, 14.44410478323698, -154.9549529403448, 332.2918645106256, 436.8382604122162, 198.17179575562477])
b = -592.2797174702706

st.title("Predict the orbital period by the Asteroid Features")

estDiaKMMin = st.slider("Enter the minimum estimated diameter of the asteroid (km): ", 0.0, 15.6)
estDiaKMMax = st.slider("Enter the maximum estimated diameter of the asteroid (km): ", 0.0, 34.8)
missDist = st.slider("Enter the miss distance of the asteroid (AU): ", 0.0, 0.5)
minOrbitInter = st.slider("Enter the minimum orbit intersection distance (AU): ", 0.0, 0.48)
eccentricity = st.slider("Enter the oebit's eccentricity: ", 0.0, 0.48)
perihelionDist = st.slider("Enter the Perihelion distance of the asteroid (AU):", 0.18, 1.3)
aphelionDist = st.slider("Enter the Aphelion distance of the asteroid (AU):", 2.01, 8.98)
meanMotion = st.slider("Enter the asteroid's mean motion: ", 0.09, 2.04)

def CalcPrediction(params):
  return params @ W + b

st.success("Minimum estimated diameter: " + str(estDiaKMMin) + "km\nMaximum estimated diameter: " + str(estDiaKMMax) + "km\nAsteroid's miss distance: " + str(missDist) + "AU\nOrbit's minimum intersection distance: " + str(minOrbitInter) + "AU\nOrbit's eccentricity: " + str(eccentricity) + "\nPerihelion distance: " + str(perihelionDist) + "AU\n\nAphelion distance: " + str(aphelionDist) + "AU\nMean motion: " + str(meanMotion) + "\nThe Orbital period is: " + str(np.round(CalcPrediction(np.array([estDiaKMMin, estDiaKMMax, missDist, minOrbitInter, eccentricity, perihelionDist, aphelionDist, meanMotion])))) + " days")

verticalDist = aphelionDist + perihelionDist + 2 * ORBIT_OBJECT_RADIUS
maxY = verticalDist + 2
constY = maxY - verticalDist + perihelionDist
yValue = constY + (verticalDist / 2 - ORBIT_OBJECT_RADIUS - perihelionDist)

# Create figure and axes
fig, ax = plt.subplots()

# Define ellipse: center (x, y), width, height, angle in degrees
ellipse = Ellipse(
    xy=(CONST_X, yValue), width=verticalDist, height=verticalDist * WIDTH_TO_HEIGHT_RATIO, angle=90, edgecolor='gray', facecolor='white'
)
ax.add_patch(ellipse)

# 2. Add the Circle: center (x, y), radius
orbitAround = plt.Circle(
    xy=(CONST_X, constY), radius=ORBIT_OBJECT_RADIUS, edgecolor='lightblue', facecolor='lightblue', label='Orbit around'
)
ax.add_patch(orbitAround)

# Semi-axes lengths
a = verticalDist / 2  # Semi-vertical axis
b = (verticalDist * WIDTH_TO_HEIGHT_RATIO) / 2  # Semi-horizontal axis

# Configure axes
ax.set_xlim(0, CONST_X * 2)
ax.set_ylim(0, maxY)
ax.set_aspect('equal')
ax.set_title('Asteroid orbit')
ax.axis('off')
# Display in Streamlit
st.pyplot(fig)
