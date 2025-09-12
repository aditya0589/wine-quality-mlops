import sys
import os

# Add the src directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from project.utils import logger

if __name__ == "__main__":
    logger.info("welcome to the custom logging")
    print("Main script is executing successfully!")