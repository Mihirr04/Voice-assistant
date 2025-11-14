import os
from dotenv import load_dotenv
from elevenlabs.client import ElevenLabs
from elevenlabs.conversational_ai.conversation import Conversation
from elevenlabs.conversational_ai.default_audio_interface import DefaultAudioInterface

# Load environment variables from .env file
load_dotenv()

# Get credentials from environment variables
agent_id = os.getenv("AGENT_ID")
api_key = os.getenv("ELEVENLABS_API_KEY")

# Check if credentials are loaded
if not agent_id or not api_key:
    print("Error: Missing AGENT_ID or ELEVENLABS_API_KEY in .env file")
    exit(1)

print("Starting voice assistant...")
print("Speak into your microphone. Press Ctrl+C to stop.")

# Initialize the ElevenLabs client
client = ElevenLabs(api_key=api_key)

# Create a conversation with your agent
conversation = Conversation(
    client=client,
    agent_id=agent_id,
    requires_auth=True,
    audio_interface=DefaultAudioInterface(),
    callback_agent_response=lambda response: print(f"Agent: {response}"),
    callback_agent_response_correction=lambda original, corrected: print(f"Corrected: {original} -> {corrected}"),
    callback_user_transcript=lambda transcript: print(f"You: {transcript}"),
)

# Start the conversation
try:
    conversation.start_session()
    print("\nConversation started! Speak now...")
    conversation.wait_for_session_end()
except KeyboardInterrupt:
    print("\n\nStopping voice assistant...")
    conversation.end_session()
except Exception as e:
    print(f"\nError: {e}")
    conversation.end_session()