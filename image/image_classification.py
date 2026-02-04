from torchvision import models, transforms
from PIL import Image
import torch

model = models.resnet18(pretrained=True)
model.eval()

img = Image.open("image/sample.jpg")

transform = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor()
])

x = transform(img).unsqueeze(0)

with torch.no_grad():
    y = model(x)

print("Output shape:", y.shape)
