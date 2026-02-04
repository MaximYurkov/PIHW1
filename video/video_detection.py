from ultralytics import YOLO

model = YOLO("yolov8n.pt")
model.predict(
    source="video/sample.mp4",
    save=True,
    project="video",
    name="result",
)
print("Done. Saved to: video/result/")


# Цель:
# детекция объектов на видео.

# Выход:
# видео или кадры с размеченными объектами.

# python video/video_detection.py