# Indian Personalities Conversation Simulator

![Banner](https://framerusercontent.com/images/3Ca34Pogzn9I3a7uTsNSlfs9Bdk.png)

## 🇮🇳 Overview

The Indian Personalities Conversation Simulator is an interactive Streamlit application that generates simulated conversations between famous Indian personalities using the Sutra multilingual AI model. This application allows users to select any two personalities from a curated list of prominent Indian figures, choose a conversation topic, and watch an AI-generated dialogue unfold in any of 14 supported Indian languages.

## ✨ Features

- **Personality Selection**: Choose from 10 famous Indian personalities including politicians, actors, sports figures, and historical leaders
- **Topic-Based Conversations**: Select from 18 India-related conversation topics
- **Multilingual Support**: Generate conversations in 14 Indian languages including Hindi, Bengali, Tamil, Telugu, etc.
- **Interactive UI**: Visual representation of personalities with images and descriptive information
- **Custom Dialogue Generation**: Suggest specific dialogue prompts for any personality
- **Configurable Conversation Length**: Set the number of conversation turns (1-5)
- **Real-time Response Streaming**: Watch responses appear in real-time using streaming capabilities

## 🚀 Installation

### Prerequisites

- Python 3.7+
- Streamlit
- LangChain
- An API key from Sutra API (https://www.two.ai/sutra/api)

### Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/indian-personalities-simulator.git
   cd indian-personalities-simulator
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file (optional):
   ```
   SUTRA_API_KEY=your_api_key_here
   ```

## 🏃‍♂️ Running the Application

1. Start the Streamlit app:
   ```bash
   streamlit run app.py
   ```

2. Open your browser and navigate to `http://localhost:8501`

3. Enter your Sutra API key in the sidebar (if not set in .env file)

4. Select personalities, topic, language, and conversation rounds

5. Click "Start Conversation" to generate the dialogue

## 👨‍💻 Usage Guide

### Basic Usage

1. **Select Personalities**: Choose two Indian personalities from the dropdown menus
2. **Choose Topic**: Select a conversation topic from the dropdown list
3. **Configure Settings**:
   - Select output language
   - Set number of conversation rounds (1-5)
4. **Start Conversation**: Click the button to generate the conversation
5. **Custom Dialogues**: Use the text area at the bottom to suggest specific dialogue prompts

### Personalities Included

- Narendra Modi (Prime Minister)
- Shah Rukh Khan (Bollywood Actor)
- A.R. Rahman (Music Composer)
- Amitabh Bachchan (Legendary Actor)
- Mahatma Gandhi (Freedom Fighter)
- Indira Gandhi (Former Prime Minister)
- Ratan Tata (Industrialist)
- P.V. Sindhu (Badminton Player)
- Rabindranath Tagore (Poet, Writer)
- Virat Kohli (Cricketer)

### Topics Included

- National development
- Cultural heritage
- Indian cinema
- Education system
- Technology in India
- Sports achievements
- Environmental challenges
- Economic growth
- Politics
- Indian cuisine
- And many more...

## 🧠 How It Works

The application uses the Sutra multilingual language model via LangChain to generate contextually appropriate, character-authentic dialogue. Each personality is assigned specific traits, speaking styles, and background information to ensure the generated conversation feels realistic.

The app uses carefully crafted prompts that instruct the AI to:
- Adopt the speaking style of the selected personality
- Address the chosen topic in a manner consistent with that personality's views
- Respond to previous dialogue turns in a conversational manner
- Output text in the selected Indian language

## 📋 Requirements

```
streamlit>=1.22.0
langchain>=0.0.267
langchain-openai>=0.0.2
python-dotenv>=1.0.0
```

## 🤝 Contributing

Contributions to improve the application are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📜 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgements

- [Sutra AI](https://www.two.ai/sutra/api) for providing the multilingual AI model
- [Streamlit](https://streamlit.io/) for the web application framework
- [LangChain](https://python.langchain.com/) for the language model integration tools

---

*Built with ❤️ for India's rich cultural heritage and diversity*
