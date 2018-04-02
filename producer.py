import time
import cv2
from kafka import SimpleProducer, KafkaClient

kafka = KafkaClient('localhost:9092')
producer = SimpleProducer(kafka)

topic = 'my-topic'


def vide_emitter(video):
	video = cv2.VideoCapture(video)
	print('emitting...')

	while (video.isOpened):
		success, image = video.read()

		if not success:
			break

		ret, jpeg = cv2.imencode('.png', image)

		producer.send_messages(topic, jpeg.tobytes())
		time.sleep(0.2)

	video.release()
	print('done emitting')



if __name__ == '__main__':
	vide_emitter('video.mp4')