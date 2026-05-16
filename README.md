# Voice Assistant

A real-time voice assistant built with a Speech-to-Text → GPT → Text-to-Speech pipeline, delivering sub-2-second end-to-end response times across 150+ test prompts. Achieves a ~97% successful response rate through async task handling and structured error recovery.

## Features

- **Real-time voice pipeline** — continuous STT → LLM → TTS loop for natural conversation
- **Low latency** — sub-2-second average response time, benchmarked across 150+ prompts
- **Robust error handling** — async task management with structured recovery for API failures
- **Configurable agent** — driven by ElevenLabs conversational AI with customizable voice and persona

## Tech Stack

**Language:** Python
**APIs:** ElevenLabs (TTS + Conversational AI), OpenAI (GPT)
**Audio:** PyAudio
**Config:** python-dotenv

## Setup

1. **Install dependencies:**
```bash
   pip install elevenlabs elevenlabs[pyaudio] python-dotenv
```

2. **Create a `.env` file in the project root:**

AGENT_ID=your_agent_id
ELEVENLABS_API_KEY=your_api_key

3. **Run the assistant:**
```bash
   python voice_assistant.py
```

## How It Works

The assistant captures audio input through PyAudio, streams it to ElevenLabs for speech-to-text conversion, routes the transcribed text through GPT for response generation, and synthesizes the reply back to speech — all asynchronously to minimize latency.

## Requirements

- Python 3.9+
- An [ElevenLabs](https://elevenlabs.io) account with an agent ID and API key
- Working microphone and speakers
