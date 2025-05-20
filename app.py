import os
import streamlit as st
from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage
from langchain.callbacks.base import BaseCallbackHandler

# Page configuration
st.set_page_config(
    page_title="Indian Personalities Conversation Simulator",
    page_icon="🇮🇳",
    layout="wide"
)

# Define famous Indian personalities
indian_personalities = {
    "Narendra Modi": {
        "role": "Prime Minister of India",
        "brief": "Known for his leadership style, oratory skills, and development agenda.",
        "image": "https://yespunjab.com/wp-content/uploads/2024/10/PM-Narendra-Modi-decision.jpg",
        "language_preference": "Hindi"
    },
    "Shah Rukh Khan": {
        "role": "Bollywood Actor",
        "brief": "Known as the 'King of Bollywood', famous for romantic roles and charismatic personality.",
        "image": "https://pad.mymovies.it/cinemanews/2024/189011/coverlg.jpg",
        "language_preference": "Hindi"
    },
    "A.R. Rahman": {
        "role": "Music Composer",
        "brief": "Oscar-winning musician known for his fusion of Eastern and Western musical styles.",
        "image": "https://songsall.com/wp-content/uploads/2024/08/Untitled-design-6.png",
        "language_preference": "Tamil"
    },
    "Amitabh Bachchan": {
        "role": "Legendary Bollywood Actor",
        "brief": "The 'Shahenshah' of Bollywood with a deep baritone voice and powerful screen presence.",
        "image": "https://m.media-amazon.com/images/M/MV5BNTk1OTUxMzIzMV5BMl5BanBnXkFtZTcwMzMxMjI0Nw@@._V1_.jpg",
        "language_preference": "Hindi"
    },
    "Mahatma Gandhi": {
        "role": "Father of the Nation",
        "brief": "Led India's independence movement with principles of non-violence and truth.",
        "image": "https://andvijaysays.com/wp-content/uploads/2013/01/mahatma-gandhi.jpg?w=750",
        "language_preference": "Gujarati"
    },
    "Indira Gandhi": {
        "role": "Former Prime Minister",
        "brief": "First and only female Prime Minister of India known for her strong leadership.",
        "image": "https://rukminim3.flixcart.com/image/850/1000/xif0q/painting/r/i/z/indira-a-1-jog-craft-original-imagphgcccrtsx8z.jpeg?q=20&crop=false",
        "language_preference": "Hindi"
    },
    "Ratan Tata": {
        "role": "Industrialist",
        "brief": "Former chairman of Tata Group known for his business acumen and philanthropy.",
        "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR3LBa3JBPtjJ-i6gDvp0UZGKKRzzLdB-YQPw&s",
        "language_preference": "English"
    },
    "P.V. Sindhu": {
        "role": "Badminton Player",
        "brief": "Olympic medalist and one of India's top badminton players.",
        "image": "https://img.olympics.com/images/image/private/t_1-1_300/f_auto/primary/ravhqy073xqoc25izxle",
        "language_preference": "Telugu"
    },
    "Rabindranath Tagore": {
        "role": "Poet, Writer, Philosopher",
        "brief": "First non-European Nobel laureate who reshaped Bengali literature and music.",
        "image": "https://cdn.britannica.com/49/134949-050-242B08C7/Rabindranath-Tagore.jpg",
        "language_preference": "Bengali"
    },
    "Virat Kohli": {
        "role": "Cricketer",
        "brief": "One of the world's best batsmen and former captain of the Indian cricket team.",
        "image": "https://documents.bcci.tv/resizedimageskirti/164_compress.png",
        "language_preference": "Hindi"
    }
}

# Define languages supported by Sutra
languages = [
    "English", "Hindi", "Gujarati", "Bengali", "Tamil", 
    "Telugu", "Kannada", "Malayalam", "Punjabi", "Marathi", 
    "Urdu", "Assamese", "Odia", "Sanskrit", "Korean", 
    "Japanese", "Arabic", "French", "German", "Spanish", 
    "Portuguese", "Russian", "Chinese", "Vietnamese", "Thai", 
    "Indonesian", "Turkish", "Polish", "Ukrainian", "Dutch", 
    "Italian", "Greek", "Hebrew", "Persian", "Swedish", 
    "Norwegian", "Danish", "Finnish", "Czech", "Hungarian", 
    "Romanian", "Bulgarian", "Croatian", "Serbian", "Slovak", 
    "Slovenian", "Estonian", "Latvian", "Lithuanian", "Malay", 
    "Tagalog", "Swahili"
]

# Conversation topics
conversation_topics = [
    "National development", "Cultural heritage", "Indian cinema",
    "Education system", "Technology in India", "Sports achievements",
    "Environmental challenges", "Economic growth", "Politics",
    "Indian cuisine", "Art and music", "Rural development",
    "Youth empowerment", "Indian philosophy", "Historical events",
    "Future of India", "Cultural diversity", "Global role of India"
]

# Streaming callback handler
class StreamHandler(BaseCallbackHandler):
    def __init__(self, container, initial_text=""):
        self.container = container
        self.text = initial_text
        self.run_id_ignore_token = None
    
    def on_llm_new_token(self, token: str, **kwargs):
        self.text += token
        self.container.markdown(self.text)

# Initialize the ChatOpenAI model - base instance for caching
@st.cache_resource
def get_base_chat_model(api_key):
    return ChatOpenAI(
        api_key=api_key,
        base_url="https://api.two.ai/v2",
        model="sutra-v2",
        temperature=0.8,
    )

# Create a streaming version of the model with callback handler
def get_streaming_chat_model(api_key, callback_handler=None):
    return ChatOpenAI(
        api_key=api_key,
        base_url="https://api.two.ai/v2",
        model="sutra-v2",
        temperature=0.8,
        streaming=True,
        callbacks=[callback_handler] if callback_handler else None
    )

# Sidebar for settings
st.sidebar.image("https://framerusercontent.com/images/3Ca34Pogzn9I3a7uTsNSlfs9Bdk.png", use_container_width=True)
with st.sidebar:
    st.title("Personalities Simulator")
    
    # API Key section
    st.markdown("### API Key")
    st.markdown("Get your free API key from [Sutra API](https://www.two.ai/sutra/api)")
    api_key = st.text_input("Enter your Sutra API Key:", type="password")
    
    # Language selector
    output_language = st.selectbox("Select output language:", languages)
    
    # Number of conversation turns
    conversation_rounds = st.slider("Conversation rounds:", min_value=1, max_value=5, value=3)
    
    # Conversation topic selection
    selected_topic = st.selectbox("Select conversation topic:", conversation_topics)
    
    st.divider()
    
    # About section
    st.markdown("### About This App")
    st.markdown("This app simulates conversations between famous Indian personalities using the Sutra multilingual model.")
    st.markdown("Select personalities, a topic, and watch them engage in an AI-generated discussion.")

# Main layout
st.markdown('<h1><img src="https://cdn.pixabay.com/animation/2022/08/21/20/03/20-03-41-348_512.gif" width="70" height="50" style="vertical-align: middle;"> Indian Icons Chat Simulator</h1>', unsafe_allow_html=True)

# Select personalities for conversation
st.header("Select Personalities for Conversation")

col1, col2 = st.columns(2)

with col1:
    person1 = st.selectbox("Select first personality:", list(indian_personalities.keys()), index=0)
    st.image(indian_personalities[person1]["image"], width=150)
    st.write(f"**Role:** {indian_personalities[person1]['role']}")
    st.write(f"**About:** {indian_personalities[person1]['brief']}")

with col2:
    person2 = st.selectbox("Select second personality:", list(indian_personalities.keys()), index=1)
    st.image(indian_personalities[person2]["image"], width=150)
    st.write(f"**Role:** {indian_personalities[person2]['role']}")
    st.write(f"**About:** {indian_personalities[person2]['brief']}")

# Initialize session state for conversation
if "conversation" not in st.session_state:
    st.session_state.conversation = []

# Start conversation button
start_button = st.button("Start Conversation")

# Display conversation header
if start_button or st.session_state.conversation:
    st.header(f"Conversation between {person1} and {person2} on {selected_topic}")
    
    if not api_key:
        st.error("Please enter your Sutra API key in the sidebar.")
    else:
        # Clear previous conversation if starting new
        if start_button:
            st.session_state.conversation = []
            
            try:
                # Set up the conversation
                chat = get_streaming_chat_model(api_key)
                
                # Generate conversation turns
                for i in range(conversation_rounds):
                    # First person's turn
                    with st.chat_message(person1, avatar=indian_personalities[person1]["image"]):
                        response_placeholder1 = st.empty()
                        stream_handler1 = StreamHandler(response_placeholder1)
                        chat1 = get_streaming_chat_model(api_key, stream_handler1)
                        
                        # Create context for the first person
                        if i == 0:
                            # First message in conversation
                            prompt = f"""You are simulating a conversation between famous Indian personalities. 
                            You are roleplaying as {person1}, the {indian_personalities[person1]['role']}. 
                            Start a conversation about "{selected_topic}" with {person2}. 
                            Keep your response authentic to {person1}'s speaking style, views, and personality.
                            Respond in {output_language} language.
                            Respond in 2-3 sentences only as {person1}."""
                        else:
                            # Responding to previous message
                            prompt = f"""Continue this conversation as {person1}. 
                            You are responding to {person2}'s previous statement about "{selected_topic}". 
                            Keep your response authentic to {person1}'s speaking style, views, and personality.
                            Respond in {output_language} language.
                            Previous exchange: {st.session_state.conversation[-1]['content']}
                            Respond in 2-3 sentences only as {person1}."""
                        
                        messages = [HumanMessage(content=prompt)]
                        response1 = chat1.invoke(messages)
                        answer1 = response1.content
                        
                        # Add to conversation history
                        st.session_state.conversation.append({
                            "role": person1,
                            "content": answer1,
                            "avatar": indian_personalities[person1]["image"]
                        })
                    
                    # Second person's turn
                    with st.chat_message(person2, avatar=indian_personalities[person2]["image"]):
                        response_placeholder2 = st.empty()
                        stream_handler2 = StreamHandler(response_placeholder2)
                        chat2 = get_streaming_chat_model(api_key, stream_handler2)
                        
                        # Create context for the second person
                        prompt = f"""Continue this conversation as {person2}, the {indian_personalities[person2]['role']}. 
                        You are responding to {person1}'s statement about "{selected_topic}": "{answer1}"
                        Keep your response authentic to {person2}'s speaking style, views, and personality.
                        Respond in {output_language} language.
                        Respond in 2-3 sentences only as {person2}."""
                        
                        messages = [HumanMessage(content=prompt)]
                        response2 = chat2.invoke(messages)
                        answer2 = response2.content
                        
                        # Add to conversation history
                        st.session_state.conversation.append({
                            "role": person2,
                            "content": answer2,
                            "avatar": indian_personalities[person2]["image"]
                        })
                
                st.success("Conversation completed!")
                        
            except Exception as e:
                st.error(f"Error: {str(e)}")
                if "API key" in str(e):
                    st.error("Please check your Sutra API key in the sidebar.")
        
        # Display saved conversation
        else:
            for message in st.session_state.conversation:
                with st.chat_message(message["role"], avatar=message["avatar"]):
                    st.write(message["content"])

# Custom CSS for better appearance
st.markdown("""
<style>
    .block-container {
        padding-top: 2rem;
    }
    .stButton>button {
        width: 100%;
        background-color: #FF9933;
        color: white;
        font-weight: bold;
    }
    .stButton>button:hover {
        background-color: #138808;
        color: white;
    }
    h1 {
        color: #000080;
    }
    h2 {
        color: #138808;
    }
</style>
""", unsafe_allow_html=True)
