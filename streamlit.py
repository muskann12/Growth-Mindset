# Importing streamlit
import streamlit as st

st.set_page_config(page_title="Muskan Growth Mindset Project", page_icon="✨")

st.title("Aspire – Your Growth Partner")
st.header("Mindset Matters: Start Growing Today ❦")

st.write("A growth mindset is the key to unlocking your full potential. Embrace challenges, learn from failures, and keep pushing forward. 🚀✨")

# Quote Section
st.header("🌟 Quote of the Day")
st.write("“Success is not the key to happiness. Happiness is the key to success. If you love what you are doing, you will be successful.” – Albert Schweitzer")

# Challenge Section
st.header("🔍 What's Holding You Back?")
st.write("Every challenge is a stepping stone to success. Take a moment to reflect and share your biggest roadblock – let's turn it into a breakthrough! 💡")

user_challenge = st.text_input("Share your challenge here...")

# Condition & Warning
if user_challenge:
    if len(user_challenge) < 10:
        st.warning("⚠️ Please provide a more detailed challenge (at least 10 characters).")
    else:
        st.success(f"💪 You acknowledged: *{user_challenge}* – Now, let's find a way to overcome it! 🚀")
else:
    st.info("ℹ️ Don't hesitate! Express your challenge and take the first step towards growth. ✨")

# Reflection Section
st.header("🤔 Self-Reflection Time")
st.write("Take a deep breath. Think about how you've handled challenges before. What did you learn? How did you grow?")

user_reflection = st.text_area("Write your reflection here...")

if user_reflection:
    st.success("🌱 Reflection is the key to improvement. Keep growing!")

# Achievements Section
st.header("🏆 Celebrate Your Wins!")
st.write("No matter how small, every achievement counts. Take a moment to acknowledge your progress! 🎉")

user_achievement = st.text_area("Share one achievement you're proud of...")

if user_achievement:
    st.balloons()
    st.success(f"🔥 Amazing! *{user_achievement}* is proof of your growth. Keep striving for more! 🚀")

# Unique Footer
st.markdown("---")  # Divider line for a clean look

st.markdown(
    """
    <div style="text-align: center;">
        <h3>✨ Keep Learning, Keep Growing ✨</h3>
        <p style="font-style: italic;">"Your mindset shapes your reality. Make it powerful, make it unstoppable!"</p>
        <p>🚀 Made with passion by <strong>Muskan Nisar</strong> | Growth Mindset App</p>
    </div>
    """,
    unsafe_allow_html=True,
)
