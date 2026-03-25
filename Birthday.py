import streamlit as st

def show_birthday_message(friend_name):
   
    st.markdown(f"""
    <div style="text-align:center; animation: pop-up 1s;">
        <span style="font-size: 30px;">🎉🎈🎊</span><br>
        <span style="font-size: 24px; color: green;">Happy Birthday, {friend_name}!</span><br>
        <span style="font-size: 30px;">🎉🎈🎊</span>
    </div>
    <style>
        
        @keyframes pop-up {{
            0% {{ transform: scale(0); }}
            100% {{ transform: scale(1); }}
        }}
    </style>
    """, unsafe_allow_html=True)


st.title("Birthday Surprise")

friend_name = st.text_input("Enter your name to see the surprise")

if st.button("🎁 Click Me!"):
    show_birthday_message(friend_name)
    st.balloons()
