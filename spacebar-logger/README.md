# Breath Timing Logger

This project is a simple Python-based logger that records the timing of spacebar presses. It is designed to help users log and analyze their breathing patterns.

## Features
- Logs the timestamp of each spacebar press.
- Calculates the time interval between consecutive presses.
- Saves the data to a dynamically named CSV file.
- Includes user metadata such as name, lamp version, and stone version.

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/judgeyrose/Breath_Timing_Logger.git
   ```
2. Navigate to the project directory:
   ```bash
   cd Breath_Timing_Logger/spacebar-logger
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. Run the main script:
   ```bash
   python src/main.py
   ```
2. Follow the prompts to enter user metadata.
3. Press the spacebar to log timestamps and intervals.
4. Press `ESC` to stop the logger.

## File Structure
- `src/main.py`: Main script for the logger.
- `src/logger.py`: Additional logging utilities (if any).
- `requirements.txt`: List of Python dependencies.

## Contributing
Feel free to fork this repository and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.

## License
This project is licensed under the MIT License. See the LICENSE file for details.