import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
from matplotlib.patches import Ellipse

st.set_page_config(layout="wide")

SUN_RADIUS = 0.25
W = np.array([6.93764541298151, 14.44410478323698, -154.9549529403448, 332.2918645106256, 436.8382604122162, 198.17179575562477])
bias = -592.2797174702706

st.title("Predict the orbital period by the Asteroid Features")

def CalcPrediction(params):
    return params @ W + bias

col_sliders, col_output = st.columns([1.1, 1], gap="large")

with col_sliders:
    st.subheader("Asteroid Parameters")
    missDist = st.slider("Enter the miss distance of the asteroid (AU): ", 0.0, 0.5)
    minOrbitInter = st.slider("Enter the minimum orbit intersection distance (AU): ", 0.0, 0.48)
    eccentricity = st.slider("Enter the orbit's eccentricity: ", 0.01, 0.96)
    perihelionDist = st.slider("Enter the Perihelion distance of the asteroid (AU):", 0.33, 1.3)
    aphelionDist = st.slider("Enter the Aphelion distance of the asteroid (AU):", 2.01, 8.98)
    meanMotion = st.slider("Enter the asteroid's mean motion: ", 0.09, 2.04)

with col_output:
    st.subheader("Summary & Prediction")
    st.info(
        f"Asteroid's miss distance: {missDist} AU\n\n"
        f"Orbit's minimum intersection distance: {minOrbitInter} AU\n\n"
        f"Orbit's eccentricity: {eccentricity}\n\n"
        f"Perihelion distance: {perihelionDist} AU\n\n"
        f"Aphelion distance: {aphelionDist} AU\n\n"
        f"Mean motion: {meanMotion}"
    )

    predicted_days = np.round(CalcPrediction(np.array([missDist, minOrbitInter, eccentricity, perihelionDist, aphelionDist, meanMotion])))
    st.success(f"The Orbital period is: {predicted_days} days")

    # --- SMALLER ORBIT GRAPH ---
    a = (aphelionDist + perihelionDist) / 2.0
    b = a * np.sqrt(1 - eccentricity**2)
    sun_x, sun_y = 0, 0
    ellipse_center_y = a - perihelionDist

    # Smaller figsize (3.5 x 3.5 inches)
    fig, ax = plt.subplots(figsize=(3.5, 3.5))

    ellipse = Ellipse(
        xy=(sun_x, ellipse_center_y),
        width=2 * a,
        height=2 * b,
        angle=90,
        edgecolor='gray',
        facecolor='none',
        linewidth=1.5,
        label='Asteroid Orbit'
    )
    ax.add_patch(ellipse)

    sun = plt.Circle(
        xy=(sun_x, sun_y),
        radius=SUN_RADIUS,
        edgecolor='orange',
        facecolor='gold',
        zorder=5,
        label='Sun'
    )
    ax.add_patch(sun)

    earth_orbit = plt.Circle((0, 0), radius=1.0, edgecolor='dodgerblue', facecolor='none', linestyle='--', alpha=0.5, label='Earth (1 AU)')
    ax.add_patch(earth_orbit)

    if missDist > 0:
        miss_circle = plt.Circle((1.0, 0), radius=missDist, edgecolor='red', facecolor='red', alpha=0.2, label='Miss Zone')
        ax.add_patch(miss_circle)

    ax.plot(0, -perihelionDist, 'go', markersize=4, label=f'Perihelion ({perihelionDist})')
    ax.plot(0, aphelionDist, 'ro', markersize=4, label=f'Aphelion ({aphelionDist})')

    max_extent = max(aphelionDist, 1.5) + 1.0
    ax.set_xlim(-max_extent, max_extent)
    ax.set_ylim(-perihelionDist - 1.5, aphelionDist + 1.0)
    ax.set_aspect('equal')
    ax.set_title('Asteroid Orbit (AU)', fontsize=10)
    ax.tick_params(labelsize=7)
    ax.legend(loc='upper right', fontsize=6.5)
    ax.grid(True, linestyle=':', alpha=0.4)
    ax.axis("off")
    
    # use_container_width=False prevents Streamlit from stretching the small figure
    st.pyplot(fig, use_container_width=False)