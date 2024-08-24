# Movie Recommender System 🍿

Welcome to the **Movie Recommender System**! This app helps you discover your next favorite movie by suggesting the top 5 movies based on your selected preference. Whether you're in the mood for action, romance, or comedy, this app has you covered! 🎬

## Features 🌟

- **Personalized Recommendations**: Select a movie you like, and the system will recommend 5 similar movies just for you.
- **Movie Posters**: Get a visual preview of each recommended movie with its poster.
- **Interactive UI**: Easy-to-use interface with a clean and modern design.

## How It Works ⚙️

### 1. Movie Selection 🎥
Start by selecting a movie from the dropdown menu. The app includes a vast database of movies, so you're sure to find one you know and love.

### 2. Fetching Recommendations 🔄
Once you've selected a movie, the app calculates similarity scores using a pre-trained model stored in `similarity.pkl`. It finds the top 5 movies most similar to your selection.

### 3. Displaying Results 📊
The app displays the recommended movies along with their posters, so you can easily see what each movie looks like.

## How to Use the App 🖥️

1. **Select a Movie**: Use the dropdown menu to choose a movie you like.
2. **Show Recommendations**: Click the "Show Recommendation" button to see your top 5 recommended movies.
3. **View Details**: Each recommended movie is shown with its title and poster for easy browsing.

## Installation and Setup 🛠️

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/machinelearningprodigy/movie-recommender-system.git
    ```
2. **Navigate to the Project Directory**:
    ```bash
    cd movie-recommender-system
    ```
3. **Install the Required Packages**:
    ```bash
    pip install -r requirements.txt
    ```
4. **Run the Streamlit App**:
    ```bash
    streamlit run app.py
    ```

## Live Demo 🚀

Check out the live demo of this app here: [Movie Recommender System](https://movie-recommendation-system24.streamlit.app/)

## Technical Details 🔧

- **Data Source**: The movie data is stored in a dictionary format, loaded using `movies_dict.pkl`, and converted into a DataFrame for easy manipulation.
- **Model**: The similarity scores are precomputed and stored in `similarity.pkl`, which is used to find the top 5 most similar movies.
- **Poster Fetching**: Movie posters are fetched from the TMDB (The Movie Database) API, ensuring that you get up-to-date and high-quality images.

## Visual Output 🎨

The recommended movies are displayed in a visually appealing layout:
- **Movie Titles**: Each movie title is displayed in a stylish heading with a unique color.
- **Movie Posters**: The posters are displayed below each title, giving you a glimpse of what the movie is about.

## Acknowledgments 🙌

- **TMDB API**: For providing the movie data and posters.
- **Streamlit**: For making it easy to build beautiful web apps with minimal code.

Enjoy your movie recommendations! 🎉
