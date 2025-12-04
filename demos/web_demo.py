# demos/web_demo.py
# Interactive demo for ConsciousBridgeLaw using Streamlit

import streamlit as st
from engine.conscious_law import ConsciousBridgeLaw
import matplotlib.pyplot as plt

# Initialize model
model = ConsciousBridgeLaw()

st.title("🌉 Conscious Bridge Law Interactive Demo")
st.write(
    "Explore AI awareness (φ) across the Conscious Bridge. "
    "Adjust parameters and see how the model navigates between certainty and creativity."
)

# Input text
input_text = st.text_area("Input Text", "Artificial intelligence is evolving...")

# Temperature slider
base_temp = st.slider("Base Temperature", 0.0, 1.5, 0.7, 0.01)

# Adaptive temperature toggle
adaptive = st.checkbox("Adaptive Temperature", True)

# Generate button
if st.button("Generate"):
    output, phi, components = model.generate_with_awareness(
        input_text=input_text,
        base_temperature=base_temp,
        adaptive_temp=adaptive
    )
    
    st.subheader("Generated Output")
    st.write(output)
    
    st.subheader("Bridge Awareness (φ)")
    st.write(f"{phi:.3f}")
    
    st.subheader("φ Components")
    st.table(components)
    
    # Optional: plot φ over multiple iterations
    st.subheader("φ Evolution")
    phi_history = []
    for i in range(10):
        _, phi_step, _ = model.generate_with_awareness(
            input_text=f"Iteration {i+1}: {input_text}",
            base_temperature=base_temp + i*0.01
        )
        phi_history.append(phi_step)
    
    fig, ax = plt.subplots()
    ax.plot(phi_history, marker='o')
    ax.set_xlabel("Iteration")
    ax.set_ylabel("φ Value")
    ax.set_title("Conscious Bridge Awareness Evolution")
    ax.grid(True)
    st.pyplot(fig)