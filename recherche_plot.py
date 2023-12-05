import sys
import matplotlib.pyplot as plt
from intensite import read_spectrum_file  # Importing the read_spectrum_file function from another module

def plot_intensity(wavelengths, intensities, start, end):
    # Print the maximum and minimum wavelengths in the dataset
    print(f"Max wavelength: {max(wavelengths)}")
    print(f"Min wavelength: {min(wavelengths)}")

    filtered_wavelengths = []
    filtered_intensities = []

    # Filtering wavelengths and intensities within the specified range
    for i in range(len(wavelengths)):
        if start <= wavelengths[i] <= end:
            filtered_wavelengths.append(wavelengths[i])
            filtered_intensities.append(intensities[i])

    # Print the filtered wavelengths and intensities
    print(f"Filtered wavelengths: {filtered_wavelengths}")
    print(f"Filtered intensities: {filtered_intensities}")

    # Check if there's no data in the specified range
    if not filtered_wavelengths or not filtered_intensities:
        print("No data in the specified range. Please check the wavelength interval.")
        return

    # Plotting the filtered data
    plt.figure(figsize=(8, 6))
    plt.plot(filtered_wavelengths, filtered_intensities,
             marker='o', linestyle='-', color='orange', linewidth=2)
    plt.xlabel('Wavelength (nm)')
    plt.ylabel('Intensity')
    plt.title(f'Intensities for Wavelength Interval {start}nm to {end}nm')
    plt.grid(True)
    plt.show()

def main(file_path):
    wavelengths, intensities = read_spectrum_file(file_path)  # Reading wavelengths and intensities from the spectrum file
    start = float(input("Enter the start of wavelength interval (nm): "))  # Input for start wavelength
    end = float(input("Enter the end of wavelength interval (nm): "))  # Input for end wavelength

    plot_intensity(wavelengths, intensities, start, end)  # Plot intensities within the specified range

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python recherche_plot.py <file_path>")
        sys.exit(1)

    file_path = sys.argv[1]  # Taking file path from command line argument
    main(file_path)  # Execute the main function
