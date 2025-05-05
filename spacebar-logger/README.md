# Spacebar Logger

This project logs occurrences of spacebar key presses along with timestamps. It is designed to help users track their interactions with the spacebar for various purposes.

## Project Structure

```
spacebar-logger
├── src
│   ├── main.py        # Entry point of the application
│   └── logger.py      # Contains logging functions
├── requirements.txt    # Lists project dependencies
└── README.md           # Project documentation
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd spacebar-logger
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

To run the application, execute the following command:
```
python src/main.py
```

The application will start listening for spacebar key presses and log each occurrence with a timestamp to a log file.

## Dependencies

This project requires the following Python packages:
- `keyboard`: For capturing keyboard events.

Make sure to install the dependencies listed in `requirements.txt` before running the application.