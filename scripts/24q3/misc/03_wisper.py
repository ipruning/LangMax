import mlx_whisper


def transcribe_audio(audio_file, model_path):
    result = mlx_whisper.transcribe(audio_file, path_or_hf_repo=model_path)

    print(f"Detected language: {result['language']}")
    print(f"Transcription length: {len(result['text'])}")

    print("Transcription preview:")
    print(result["text"][:1000])


if __name__ == "__main__":
    audio_file = ""
    model_path = "mlx-community/distil-whisper-large-v3"

    transcribe_audio(audio_file, model_path)
