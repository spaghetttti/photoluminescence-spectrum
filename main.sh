#!/bin/bash

# Main script to coordinate intensite.py and recherche_plot.py

file_path="data/data.csv"  # Hardcoded file path

# Execute intensite.py to index the intensities
python3 intensite.py "$file_path"

# Ask for user input to plot intensities within a specific wavelength interval
echo "Do you want to plot intensities for a specific wavelength interval? (y/n)"
read plot_choice

if [ "$plot_choice" == "y" ]; then
    python3 recherche_plot.py "$file_path"
else
    echo "Exiting..."
    exit 0
fi
