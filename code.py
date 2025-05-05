import tkinter as tk
from tkinter import messagebox
import speech_recognition as sr


def start_speech_to_text():
    """Function to handle speech-to-text conversion."""
    recognizer = sr.Recognizer()  # Create a Recognizer object
    with sr.Microphone() as source:  # Use the microphone as the audio source
        try:
            # Inform the user that recording is starting
            messagebox.showinfo("Listening", "Speak now...")
            audio = recognizer.listen(source)  # Listen to the audio input
            # Convert speech to text using Google's Web Speech API
            text = recognizer.recognize_google(audio)
            # Display the recognized text in the output field
            output_text.delete(1.0, tk.END)
            output_text.insert(tk.END, text)
        except sr.UnknownValueError:
            # Handle cases where speech could not be understood
            messagebox.showerror("Error", "Sorry, could not understand the audio.")
        except sr.RequestError:
            # Handle cases where the API is unavailable
            messagebox.showerror("Error", "Could not request results; check your internet connection.")


# Create the main Tkinter application window
root = tk.Tk()
root.title("Speech-to-Text Application")
root.geometry("400x300")  # Set the window size

# Add a label to guide the user
label = tk.Label(root, text="Click the button and speak something:", font=("Arial", 14))
label.pack(pady=20)

# Add a button to start the speech-to-text process
start_button = tk.Button(root, text="Start Speech-to-Text", command=start_speech_to_text, font=("Arial", 12), bg="lightblue")
start_button.pack(pady=10)

# Add a text widget to display the output
output_text = tk.Text(root, height=10, width=40, font=("Arial", 12))
output_text.pack(pady=10)

# Run the Tkinter main event loop
root.mainloop()
