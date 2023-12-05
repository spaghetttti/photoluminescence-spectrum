import sys

# Function to read the photoluminescence spectrum file and return lists of wavelengths and intensities
def read_spectrum_file(file_path):
    wavelengths = []
    intensities = []
    try:
        with open(file_path, 'r') as file:
            # Read line by line
            for line in file:
                # Skip lines starting with '#' or empty lines
                if line.startswith('#') or not line.strip():
                    continue
                # Extract and convert wavelength and intensity, then append to respective lists
                wavelength, intensity = map(float, line.strip().split())
                wavelengths.append(wavelength)
                intensities.append(intensity)
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        sys.exit(1)  # Exit the program if file not found
    return wavelengths, intensities

# Function to organize data into windows based on a window size
def organize_data(wavelengths, intensities, window_size=10):
    windows = {}
    min_wavelength = min(wavelengths)
    max_wavelength = max(wavelengths)
    
    current_window_start = min_wavelength
    while current_window_start <= max_wavelength:
        current_window_end = current_window_start + window_size
        
        window_data = []
        for i in range(len(wavelengths)):
            # Check intensities within the current window range
            if current_window_start <= wavelengths[i] < current_window_end:
                window_data.append(intensities[i])
        
        if window_data:
            windows[(current_window_start, current_window_end)] = sorted(window_data)
        
        current_window_start += window_size

    return windows

# Function to calculate statistics (number of data points, min, max, and average intensity) for each window
def calculate_statistics(intensity_data):
    statistics = {}
    
    for window, intensities in intensity_data.items():
        num_data = len(intensities)
        min_intensity = min(intensities)
        max_intensity = max(intensities)
        avg_intensity = sum(intensities) / num_data if num_data > 0 else 0
        
        statistics[window] = {
            'num_data': num_data,
            'min_intensity': min_intensity,
            'max_intensity': max_intensity,
            'avg_intensity': avg_intensity
        }
    
    return statistics

# Main function to execute the program
def main(file_path, window_size=10):
    wavelengths, intensities = read_spectrum_file(file_path)  # Read data from file
    windows = organize_data(wavelengths, intensities, window_size)  # Organize data into windows
    statistics = calculate_statistics(windows)  # Calculate statistics for each window
    
    # # Display statistics for each window COMMENTED OUT BY DEFAULT BECAUSE OUTPUT CAN BE A LARGE DATA SET
    # for window, stats in statistics.items():
    #     print(f"Window: {window}, Statistics: {stats}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python intensite.py <file_path>")
        sys.exit(1)  # Exit if no file path provided
    file_path = sys.argv[1]  # Get file path from command line argument
    main(file_path)  # Execute the main function