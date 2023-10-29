# Face-Recognition-with-GPS-tracking

Program of Face Recognition and GPS tracking. Students Face Recognition takes 3 steps.

First, using database.py we simply create a dataset, where we will store for each id, a group of photos in gray with the portion that was used for face detecting. Besides the 3 python scripts that we will create for our project, we must have saved on it the Facial Classifier. frontface.xml

Second, by using trainning.py, we must take all user data from our dataset and "trainer" the OpenCV Recognizer. This is done directly by a specific OpenCV function. The result will be a .yml file that will be saved on a "trainer/" directory.

Third, we capture a face on our camera and if this student had his face captured and trained before, our recognizer will make a "prediction" returning its id and an index, shown how confident the recognizer is with this match.

Next is GPS tracking where we use device_location.py to get student device's current gps coordinates to get distance between teacher in the classroom and the student. 
