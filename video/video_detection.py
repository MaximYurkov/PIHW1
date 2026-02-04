from ultralytics import YOLO

model = YOLO("yolov8n.pt")

results = model("video/sample.mp4")

print("Done")
