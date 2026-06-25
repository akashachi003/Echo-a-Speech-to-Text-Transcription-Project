import speech_recognition as sr
import os

def transcribe_audio_file(file_path):
    """Transcribes an audio file (WAV format preferred)."""
    # Initialize the recognizer
    recognizer = sr.Recognizer()
    
    if not os.path.exists(file_path):
        print(f"❌ Error: File '{file_path}' not found.")
        return

    print("⏳ Processing audio file...")
    
    # Load the audio file
    with sr.AudioFile(file_path) as source:
        # Record the audio data from the file
        audio_data = recognizer.record(source)
        
        try:
            # Recognize speech using Google's free Web Speech API
            text = recognizer.recognize_google(audio_data)
            print("\n📝 Transcription Result:")
            print("-" * 30)
            print(text)
            print("-" * 30)
            return text
        except sr.UnknownValueError:
            print("❌ Google Speech Recognition could not understand the audio.")
        except sr.RequestError as e:
            print(f"❌ Could not request results from Google service; {e}")

def transcribe_from_mic():
    """Transcribes live audio from your microphone."""
    recognizer = sr.Recognizer()
    
    with sr.Microphone() as source:
        print("\n🎤 Adjusting for ambient noise... Please wait.")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        print("🗣️ Speak now! I am listening...")
        
        # Listen for the user's input
        audio_data = recognizer.listen(source)
        print("⏳ Analyzing speech...")
        
        try:
            text = recognizer.recognize_google(audio_data)
            print("\n📝 You said:")
            print("-" * 30)
            print(text)
            print("-" * 30)
            return text
        except sr.UnknownValueError:
            print("❌ Oops! I couldn't understand what you said.")
        except sr.RequestError as e:
            print(f"❌ API connection issue; {e}")

# --- Execution Example ---
if __name__ == "__main__":
    # Choose your flavor:
    
    # Option A: Transcribe an existing file (uncomment to use)
    # transcribe_audio_file("my_recording.wav")
    
    # Option B: Transcribe live microphone input
    transcribe_from_mic()