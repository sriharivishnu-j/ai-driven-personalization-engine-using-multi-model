from kafka import KafkaConsumer
import logging

logging.basicConfig(level=logging.INFO)

consumer = KafkaConsumer(
    'user_events',
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='ai_personalization_group'
)

for message in consumer:
    logging.info(f"Consumed message: {message.value}")
    # Process the message
