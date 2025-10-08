import streamlit as st

st.set_page_config(
    page_title="Prueba de Partículas",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
    <style>
    /* Fondo negro en toda la app */
    [data-testid="stAppViewContainer"],
    [data-testid="stHeader"],
    .main {
        background-color: black !important;
        color: white !important;
    }

    /* Contenedor fijo para partículas */
    #test-particles {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        pointer-events: none; /* No bloquear clics */
        z-index: 1; /* ¡Por encima del fondo, pero debajo del banner! */
    }

    .test-particle {
        position: absolute;
        width: 20px;
        height: 20px;
        background: white;
        border-radius: 50%;
        box-shadow: 0 0 15px 5px cyan;
        animation: floatUp 8s infinite ease-in;
    }

    @keyframes floatUp {
        0% {
            transform: translateY(100vh) translateX(0);
            opacity: 0;
        }
        10% {
            opacity: 1;
        }
        90% {
            opacity: 1;
        }
        100% {
            transform: translateY(-100px) translateX(50px);
            opacity: 0;
        }
    }

    .banner {
        position: relative;
        z-index: 10; /* Por encima de las partículas */
        background: rgba(0, 0, 0, 0.7);
        padding: 40px;
        border-radius: 20px;
        text-align: center;
        margin: 20px auto;
        max-width: 800px;
        border: 1px solid #0ff;
        box-shadow: 0 0 20px #0ff;
    }

    .banner h1 {
        color: white;
        font-size: 4rem;
        text-shadow: 0 0 10px cyan;
    }
    </style>

    <div id="test-particles">
        <div class="test-particle" style="left: 10%; animation-delay: 0s;"></div>
        <div class="test-particle" style="left: 30%; animation-delay: 2s; width: 25px; height: 25px; box-shadow: 0 0 20px 8px #ff00ff;"></div>
        <div class="test-particle" style="left: 50%; animation-delay: 4s; width: 18px; height: 18px; box-shadow: 0 0 18px 6px #ff9900;"></div>
        <div class="test-particle" style="left: 70%; animation-delay: 1s; width: 22px; height: 22px; box-shadow: 0 0 22px 7px #00ff99;"></div>
        <div class="test-particle" style="left: 90%; animation-delay: 3s; width: 30px; height: 30px; box-shadow: 0 0 25px 10px white;"></div>
    </div>
""", unsafe_allow_html=True)

# Banner
st.markdown("""
<div style="display: flex; justify-content: center; align-items: center; min-height: 100vh;">
    <div class="banner">
        <h1>¡Hola mundo!!!</h1>
    </div>
</div>
""", unsafe_allow_html=True)