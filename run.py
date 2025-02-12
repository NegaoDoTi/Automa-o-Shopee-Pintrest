from robot.start_robot import Robot
from config.config import robot_name
import logging

logging.basicConfig(filename=f"{robot_name}.log", filemode="a", format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO)

print("Executando o robô...")

robo = Robot()

robo.start()