import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("Sigmoid Activation Function")
x = np.linspace(-10,10,100)
y = 1 / (1 + np.exp(-x))
fig, ax = plt.subplots()
ax.plot(x, y)
st.pyplot(fig)
st.write("The sigmoid function is defined as: ")
st.latex(r"\sigma(x) = \frac{1}{1 + e^{-x}}")