# GitHub Repos Statistics

## Overview

GitHub Repos Statistics is a Flask-based web application based on Github-Ranking repo that provides insightful data and statistics from GitHub repositories. The application allows users to explore various metrics through interactive visualizations and an intuitive interface. While at first the website was made with being updated dynamically in mind, due to the time-contraints that came with extended long loading times and severe server loads, it has been converted to the static implementation. The original dynamic code is still contained within files. 

**The website is in polish**  

## Github Ranking - Source Repo

https://github.com/EvanLi/Github-Ranking

## Features

- **Homepage**: An overview of GitHub repository statistics presented in a user-friendly way.
- **Interactive menu**: A side menu with categories and subcategories, allowing easy navigation and exploration of various GitHub data points.
  
### Main sections:

1. **Data scraping**:
   - Displays data retrieved through web scraping, including comparisons of commits, contributors, and usage statistics for GitHub repositories.
   
2. **Free Code Camp analysis**:
   - Tracks the growth of stars, issues, and forks over time for Free Code Camp repositories.

3. **General statistics analysis**:
   - Provides general statistics, such as:
     - Sum of stars by programming language.
     - Top 20 repositories by the number of stars.
     - Top 20 repositories by the number of forks.

4. **Interactive add-ons**:
   - Offers interactive visualizations such as:
     - Popularity trends of repositories over time (2018-2023).
     - Summaries of star counts for different programming languages.

## Tech stack

- **Flask**: The core framework used for developing the backend.
- **Python**: The main programming language used for data processing and backend logic.
- **Bootstrap**: For styling and responsive design.
- **JavaScript Libraries**: Includes libraries like Shopify Draggable and Bokeh for enhanced interactivity and data visualization.

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Coktoco/Github-Repos-Statistics.git
   cd Github-Repos-Statistics

2. **Set up a virtual enviornment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate # On Windows use `venv\Scripts\activate`

3. **Install dependences**:
   ```bash
   pip install -r requirments.txt

4. **Run the application**
   ```bash
   python3.11 app.py

The application will start and be accessible at http://127.0.0.1:5000.

## Usage 

- Navigate through the interactive menu on the right side of the application to explore different data categories.
- View detailed comparisons of commits, contributors, and repository usage.
- Explore the growth and trends of Free Code Camp repositories.
- Analyze general statistics such as star counts and forks for various programming languages.

## Contributing

Contributions are welcome! If you have ideas for improvements or new features, please feel free to open an issue or submit a pull request. For major changes, it’s best to discuss them first via an issue.

## License

This project is licensed under the MIT License.

## Contact

For questions or further information, feel free to contact me via email or on LinkedIn.

## Links

Google colab workspace with original code that was used for creating the diagrams, files and general content used on the website. 
- https://colab.research.google.com/drive/19WtFMykiO_ZMpf1csPICVpQg3pvGFNx1#scrollTo=9OdvRHmlE87V

# Photos of working project:

<img width="1512" alt="Zrzut ekranu 2024-08-29 o 19 15 26" src="https://github.com/user-attachments/assets/a9a24036-3340-4fee-af24-f48e551538de">
<img width="1512" alt="Zrzut ekranu 2024-08-29 o 19 16 56" src="https://github.com/user-attachments/assets/eb909da2-2693-4eed-8ba9-47c8137c9fe4">

