import uvr
from uvr import models
from uvr.utils.get_models import download_all_models
import json

# Tải xuống tất cả các mô hình cần thiết
models_json = json.load(open("src/models_dir/models.json", "r"))
download_all_models(models_json)

# Đường dẫn đến tệp âm thanh đầu vào
input_audio = "path/to/your_audio_file.wav"

# Khởi tạo mô hình Demucs
demucs = models.Demucs(name="hdemucs_mmi", other_metadata={"segment": 2, "split": True}, device="cuda", logger=None)

# Tách tệp âm thanh
result = demucs(input_audio)
separated_audio = result["separated"]
vocals = separated_audio["vocals"]
bass = separated_audio["bass"]
drums = separated_audio["drums"]
other = separated_audio["other"]