from helper_functions import upload_txt_file,list_files_in_directory,print_llm_response,fahrenheit_to_celsius,celsius_to_fahrenheit
import pandas as pd
import matplotlib.pyplot as plt


upload_txt_file("example.txt")
list_files_in_directory()
print_llm_response("Hello AI")


f = open("file.txt","r")
txt = f.read()
f.close()


temp_fahrenheit_to_celsius = fahrenheit_to_celsius(68)
print(temp_fahrenheit_to_celsius)

temp_celsius_to_fahrenheit = celsius_to_fahrenheit(68)
print(temp_celsius_to_fahrenheit)



df = pd.read_csv('cars.csv')
filter = df[df["Invoice"]>=10000]
print(filter['Invoice'].median())


# Sample data
data = {
    'Model': ['Honda Amaze 1.2 VX i-VTEC', 'Honda Brio V MT', 'Honda WR-V VX MT Petrol', 
              'Honda CR-V 2.4 AT', 'Honda Brio S MT', 'Honda Accord 2.4 iVtec AT', 
              'Honda City SV Diesel', 'Honda City V', 'Honda City SV CVT', 'Honda City V'],
    'Price': [5050.00, 3510.00, 8199.99, 8600.00, 4400.00, 1950.00, 7500.00, 7300.00, 5900.00, 4800.00],
    'Year': [2017, 2014, 2018, 2013, 2016, 2008, 2018, 2016, 2015, 2015],
    'Kilometer': [87150, 39276, 27963, 67000, 50374, 57885, 75000, 51834, 116592, 49000]
}

# Create DataFrame
df = pd.DataFrame(data)

# Count cars sold each year
year_counts = df['Year'].value_counts()

# Plot pie chart
plt.figure(figsize=(8, 8))
plt.pie(year_counts, labels=year_counts.index, autopct='%1.1f%%', startangle=140)
plt.title('Car Sales Distribution by Year')
plt.axis('equal')  # Equal aspect ratio ensures that pie chart is circular.
plt.show()