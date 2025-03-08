# Unit Converter

## Description
Unit Converter is a web application for converting units of **length, weight, and temperature**. It utilizes **Flask** as the backend and **JavaScript** for frontend interactions.  
project for https://roadmap.sh/projects/unit-converter

## Features
Convert **length** units (meters, miles, feet, etc.)  
Convert **weight** units (kilograms, grams, pounds, etc.)  
Convert **temperature** units (Celsius, Fahrenheit, Kelvin)  
Buttons for switching between different conversion pages  

## Project Structure

```
UnitConverter/
├── index.html         # Main page with options to select unit type
├── lenght.html        # Length conversion page
├── weight.html        # Weight conversion page
├── temprature.html    # Temperature conversion page
├── script.js          # Handles client-side logic and fetch requests
├── server.py          # Flask backend for unit conversion
├── LICENSE            # License file
├── README.md          # Documentation file
```

## Installation
### Prerequisites
- Python 3.x
- Flask

### Steps
1. Clone the repository:
   ```sh
   git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
   cd UnitConverter
   ```
2. Install dependencies:
   ```sh
   pip install flask flask-cors
   ```
3. Run the Flask server:
   ```sh
   python server.py
   ```
4. Open `index.html` in a browser or use Live Server in VS Code.

## Usage
### Conversion Process
1. Open the corresponding page (`lenght.html`, `weight.html`, or `temprature.html`).
2. Enter a value and select the units to convert from and to.
3. Click the "Convert" button.
4. The result will be displayed on the page.

### API Endpoint
- **`GET /convert`**
  - **Parameters:**
    - `value` (float) – The numeric value to convert
    - `fromun` (string) – The unit to convert from
    - `toun` (string) – The unit to convert to
    - `type` (string) – The type of conversion (`length`, `weight`, `temprature`)
  - **Example Request:**
    ```sh
    curl "http://127.0.0.1:5000/convert?fromun=m&toun=km&value=100&type=length"
    ```
  - **Example Response:**
    ```json
    { "result": "0.1" }
    ```

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author
- **Anton**  
- GitHub: [YourGitHubProfile](https://github.com/anton3029941)

