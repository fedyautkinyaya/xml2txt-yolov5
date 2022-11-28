# yolov5 - helmet detector


Скачаем имеющийся в свободном доступе датасет https://www.v7labs.com/open-datasets/shwd-dataset  
  
Воспользуемся *voc2yolo5.py* для преобразования файлов аннотации в формат yolo:  
```
python3 voc2yolo5.py
```

Проверим получившуюся разметку используя файл *annotation_check_yolov5.py* 
```
python3 annotation_check_yolov5.py
```
Создадим виртуальную среду, скачаем репозиторий https://github.com/ultralytics/yolov5, установим *requirements.txt*:  
```
git clone https://github.com/ultralytics/yolov5  # clone
cd yolov5
pip install -r requirements.txt  # install
```

Создадим папку training_data, скопируем наши изображения и txt-файлы согласно рекомендациям по yolov5.  

Запустим обучение:
```
python3 train.py --img 640 --batch 32 --epochs 100 --data hat.yaml --weights yolov5s.pt --device 0
```
Наслаждаемся результатом :+1:




