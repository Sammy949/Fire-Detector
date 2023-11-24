# SafeTempGuard

SafeTempGuard is a Python-based temperature monitoring system designed to alert users about potential fire risks based on temperature readings. It provides information about the current temperature, humidity level, and air quality index to help users stay informed and take necessary precautions.

## Installation

Ensure you have Python installed on your system. 

## Usage

To use SafeTempGuard, simply run the main script:

```python
python firedetector.py
```

The program will display information about the current temperature, humidity, and air quality index, along with safety recommendations based on the temperature level.

**N.B: The values are randomly generated**
## Temperature States

SafeTempGuard classifies temperature into the following states:

- **Moderate (1):** Temperature range 18°C to 27°C
- **Hot (2):** Temperature range 28°C to 37°C
- **Scorching (3):** Temperature range 38°C to 61°C
- **Above Normal (4):** Temperature above 61°C

## Alerts

The system provides alerts based on the temperature level:

- If the temperature is above 300°C, it raises a fire alert, recommending users to stay safe and alerting fire services.

## Contributing

Feel free to contribute to the project by opening issues or submitting pull requests. Your feedback and suggestions are highly appreciated.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

**Built by [SamY](https://samy01.netlify.app)**

## Thank you for using SafeTempGuard! Stay safe and cool!
