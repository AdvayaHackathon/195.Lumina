# 🌟 Lumina: AI-Powered Mental Health Companion

> *"Bringing the warmth of your loved ones back — through the power of voice, memory, and AI."*

**Lumina** is a deeply empathetic mental health chatbot designed to comfort, connect, and converse — just like your loved ones would. With cutting-edge **voice cloning**, **relationship-based memory**, **emotion-aware responses**, and **natural speech**, Lumina offers more than just conversation — it brings healing.

---

## 🧠 Why Lumina?

Mental health support doesn't always need a therapist — sometimes, it just needs a **familiar voice**, a **gentle word**, or someone who simply **understands**. Lumina delivers this experience through:

- **Personalized chatbot personas** based on your chosen relationship.
- **Cloned voices** of loved ones for authentic emotional comfort.
- **Voice-based interaction** in both **English and Hindi**.
- A wholesome **Therapy & Mood Booster** section for quick uplift.
- Empathetic, **emotion-aware** replies for deeper connection.

---

## ✨ Key Features

| Feature | Description |
|--------|-------------|
| 💬 Relationship Chat | Choose a relationship (e.g., Mom, Dad, Friend) & how you'd like to be addressed |
| 🗣️ Voice Cloning | Upload a voice sample to clone a loved one’s voice for chatbot responses |
| 🎧 ElevenLabs TTS | Expressive voice synthesis with emotional tone using SSML |
| 🧑‍🤝‍🧑 Friend Gender Support | Choose “Boy” or “Girl” for personalized friend voices |
| 🌍 Multi-language Support | English and Hindi conversation modes |
| 🎭 Personality Selection | Choose the chatbot’s tone (e.g., Calm Mom, Fun Mom, Emotional Mom, etc.) |
| 🧘 Therapy & Mood Booster | Jokes, affirmations, music therapy, breathing exercises & motivational stories |
| 💡 Static Voice for Orphans | Natural Indian voice used when no voice sample is provided |

---

## 🛠️ Tech Stack

- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Python (Flask)
- **AI Models**: Gemma 3, OpenAI Whisper, Emotion Detection
- **Voice**: ElevenLabs (TTS + Cloning), SSML
- **Languages**: English & Hindi
- **Hosting**: [Optional - add hosting platform if deployed]

---

## 📁 Folder Structure

```
mental_health_chatbot 2/
├─ __pycache__/
│  └─ app.cpython-312.pyc
├─ chatbot/
│  ├─ __pycache__/
│  │  ├─ response_generator.cpython-312.pyc
│  │  ├─ speech_to_text.cpython-312.pyc
│  │  ├─ translation.cpython-312.pyc
│  │  ├─ voice_cloning.cpython-312.pyc
│  │  └─ voice_generator.cpython-312.pyc
│  ├─ response_generator.py
│  ├─ speech_to_text.py
│  ├─ translation.py
│  └─ voice_cloning.py
├─ models/
│  ├─ __pycache__/
│  │  └─ emotion_detector.cpython-312.pyc
│  └─ emotion_detector.py
├─ static/
├─ templates/
│  ├─ diary.html
│  ├─ fun.html
│  ├─ index.html
│  └─ therapy.html
├─ uploads/
│  ├─ voice_input.wav
│  └─ voice_sample.wav
├─ .env
├─ app.py
├─ diary_entries.txt
├─ output_speech.mp3
├─ README.md
└─ recorded_audio.wav


---

## 🚀 Getting Started

### 1. Clone the Repo

```bash
git clone https://github.com/yourusername/lumina-mental-health-chatbot.git
cd lumina-mental_health_chatbot
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Set Up Environment Variables

Create a `.env` file and add your API keys:

```
ELEVEN_API_KEY=your_key
OPENAI_API_KEY=your_key
```

### 4. Run the App

```bash
python app.py
```

Open `http://localhost:5000` in your browser 🚀

---

## 💡 Use Cases

- 💔 **For Orphans**: Provides an emotionally warm Indian voice when no sample is available.
- 🧑‍⚕️ **For Mental Health Support**: Recreates personal connections that can emotionally heal.
- 👩‍🎓 **For Students**: A kind companion to support during academic stress.


---

## 🔮 Roadmap

- 📱 Mobile App Support (React Native or Flutter)
- 🧠 Contextual Memory for deeper, ongoing conversations
- 🔐 User Login with personal history
- 🌐 Regional Language Expansion (Tamil, Telugu, etc.)
- 📊 Emotional Health Analytics

---

## 🙌 Credits

- 🗣️ [ElevenLabs](https://www.elevenlabs.io/) — for TTS and voice cloning  
- 🎤 [OpenAI Whisper](https://openai.com/) — for speech-to-text  
- 🤗 [HuggingFace Models](https://huggingface.co/) — for emotion detection  
- 💙 Family, mentors, and friends who inspired this project

---

## 📫 Contact

👨‍💻 **Developer**: Nithish,Hari  
📧 Email: naninithish988@example.com  
🔗 LinkedIn: [linkedin.com/in/nithishdaruvuri](https://linkedin.com/in/nithishdaruvuri)

---

## 🌈 Final Note

> *“Sometimes, the best therapy is a voice you miss.”*  
Let **Lumina** be that voice — always present, always healing 💙

---