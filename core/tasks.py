import os, cv2
from ultralytics import YOLO
from celery import shared_task
from django.conf import settings
from .models import Video


@shared_task
def process_video(video_id):
    video = Video.objects.get(id=video_id)
    inp = video.file.path
    out_dir = os.path.join(settings.MEDIA_ROOT, 'outputs')
    os.makedirs(out_dir, exist_ok=True)

    model = YOLO('core/weights/best.pt')
    results = model.predict(source=inp, save=True, project=out_dir,
                            name=f'vid_{video_id}', conf=0.5)

    detections = []
    for r in results:
        for box in r.boxes:
            detections.append({
                'class': model.names[int(box.cls.cpu())],
                'conf': float(box.conf.cpu()),
                'bbox': box.xyxy.cpu().tolist()
            })

    out_path = os.path.join(out_dir, f'vid_{video_id}', os.path.basename(inp))
    video.output = out_path.replace(str(settings.MEDIA_ROOT) + '/', '')
    video.result = {'detections': detections}
    video.processed = True
    video.save()
