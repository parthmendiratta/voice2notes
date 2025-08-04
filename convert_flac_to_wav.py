from pydub import AudioSegment
import os

flac_folder=os.path.join("LibriSpeech","test-clean","2961","960")
output_folder="audio-samples/"
os.makedirs(output_folder,exist_ok=True)

flac_files=[f for f in os.listdir(flac_folder) if f.endswith(".flac")]

for file in flac_files[21:22]:
    flac_path=os.path.join(flac_folder,file)
    wav_path=os.path.join(output_folder,file.replace(".flac",".wav"))

    audio=AudioSegment.from_file(flac_path,format="flac")
    audio.export(wav_path,format="wav")
    print(f"Converted: {file} -> {wav_path}")