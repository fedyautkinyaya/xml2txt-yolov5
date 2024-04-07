# yolov5 - helmet detectorr


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
Проверка полученных результатов:  

```
python3 detect.py --weights ./runs/train/exp/weights/best.pt --source ./val_img/ --conf-thres 0.5
```

 
Наслаждаемся результатом :+1:  


![ezgif-1-96b2fe6805](https://user-images.githubusercontent.com/56885818/204822080-33217f48-c67e-48a4-b99d-c1959e453707.gif)  

![7c1ba4fe5df8b041806a9c4048f3bf44_XL](https://user-images.githubusercontent.com/56885818/204825375-7c40a83c-f449-4348-a1ba-7dd043024518.jpg)  

![original-16d](https://user-images.githubusercontent.com/56885818/204825013-4ee33185-a760-4610-9036-c569a61b72b4.jpg)  




