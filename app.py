import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

ést.set_page_config(layout="wide")

def generate_hemicycle(n_deputes, n_rows, initial_radius, radius_increment, point_size):
    radii = [initial_radius + i * radius_increment for i in range(n_rows)]

    arc_lengths = [r * np.pi for r in radii]
    total_arc_length = sum(arc_lengths)

    deputies_per_row = [int(n_deputes * (arc_length / total_arc_length)) for arc_length in arc_lengths]

    diff = n_deputes - sum(deputies_per_row)
    deputies_per_row[-1] += diff  # Add the remainder to the last row

    points = []

    plt.figure(figsize=(12, 6))
    for row in range(n_rows):
        radius = radii[row]

        n_deputies_row = deputies_per_row[row]

        angles = np.linspace(0, np.pi, n_deputies_row)

        x = radius * np.cos(angles)
        y = radius * np.sin(angles)

        for i in range(n_deputies_row):
            points.append((radius, angles[i], x[i], y[i]))

        plt.scatter(x, y, s=point_size, alpha=1, color='grey')

    plt.gca().set_aspect('equal')
    plt.axis('off')

    st.pyplot(plt)

st.title('Hemicycle Visualization')

# Create two columns with adjusted proportions
col1, col2 = st.columns([3, 1])

# the sliders in the second column
with col2:
    n_deputes = st.slider('Number of Deputies', min_value=100, max_value=1200, value=577)
    n_rows = st.slider('Number of Rows', min_value=5, max_value=20, value=15)
    initial_radius = st.slider('Initial Radius', min_value=10, max_value=50, value=30)
    radius_increment = st.slider('Radius Increment', min_value=1, max_value=10, value=5)
    point_size = st.slider('Point Size', min_value=20, max_value=200, value=50)

# the figure in the first column
with col1:
    generate_hemicycle(n_deputes, n_rows, initial_radius, radius_increment, point_size)