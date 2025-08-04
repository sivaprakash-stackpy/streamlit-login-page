import streamlit as st

# --- User credentials (you can expand this or move to a secure file/db) ---
USER_CREDENTIALS = {
    "admin": "admin123",
    "user1": "welcome1",
    "guest": "guest123"
}

# --- Streamlit App ---
def main():
    st.set_page_config(page_title="Login Page", page_icon="🔐")
    st.title("🔐 Secure Login Page")
    st.markdown("Enter your credentials below:")

    # --- Login Form ---
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username in USER_CREDENTIALS and USER_CREDENTIALS[username] == password:
            st.success(f"Welcome, {username} 👋")
            st.session_state["authenticated"] = True
            st.session_state["username"] = username
        else:
            st.error("Invalid username or password")

    # Optional: Protected content
    if st.session_state.get("authenticated"):
        st.markdown("---")
        st.subheader("🧠 Protected Content")
        st.success("You now have access to secured content!")

if __name__ == "__main__":
    main()
