def upload_txt_file(filename):
    print(f"uploading file :{filename}")

def list_files_in_directory():
    print("Listing files in directory")

def print_llm_response(response):
        print(f"LLM Response: {response}")

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    print(f"{fahrenheit}°F is equivalent to {celsius:.2f}°C")

def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9 / 5) + 32
    print(f"{celsius}°C is equivalent to {fahrenheit:.2f}°F")