# Metallica Songs Dataset

The purpose of this repository is to maintain Metallica datasets and notebooks on Kaggle.

The `song-data` folder contains an up-to-date compliation of Metallica songs from the Spotify API. A scheduled workflow runs on the 1st of every month to check for updates. If updates are made, Kaggle is updated via the Kaggle API. The 'popularity' feature is really the only column that will change over time unless new songs are added.

## Table of Contents
1. [Project Structure](#project-structure)
2. [Getting Started](#getting-started)
3. [Automation with GitHub Actions](#automation-with-github-actions)
4. [Licenses](#licenses)
5. [Disclaimer](#disclaimer)
6. [Acknowledgements](#acknowledgements)

## Project Structure

- 📂 `song-data`: This folder contains the dataset and metadata required for the Kaggle upload. The dataset comprises attributes of Metallica songs, and the metadata file provides information about the dataset and the data fields.

- 📂 `utils`: This folder contains helper functions that are used in the generator script. These functions facilitate data processing and interactions with APIs.

- 📜 `met_spotify_generator.py`: This is the main script that generates the dataset. It utilizes the helper functions in the `utils` folder, interacts with the Spotify API to fetch song attributes, and compiles the data into the format stored in the `song-data` folder.

- 📓 `met_spotify_data.ipynb`: This Jupyter notebook allows for testing and visualization of the code used in the generator script. It provides a step-by-step execution of the code blocks for better understanding and debugging.

- 📓 `metallica-visualize-em-all.ipynb`: This Jupyter notebook contains an EDA of the dataset and a simple XGBoost regressor to predict popularity. This is connected to a Kaggle notebook.

- 📂 `.github/workflows`: This folder contains the GitHub Actions workflows that run the `met_spotify_generator.py` script on a schedule. The workflows automate the process of dataset generation and updating the Kaggle dataset.

- 📜 `README.md`: The file you are currently viewing, provides an overview of the project.

## Getting Started

Before diving into the project, there are several prerequisites that need to be fulfilled:

### 1. Spotify Account and API Credentials

This project fetches data from the Spotify Web API. Hence, you will need to have a Spotify account and register an application to get the necessary API credentials (Client ID and Client Secret). 

1. Visit the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/login) and log in with your Spotify account. 
2. Create a new application and obtain your Client ID and Client Secret.

The credentials are stored in a `config.py` file which is not included in the repository due to privacy concerns. This file should be created locally in your project directory. The file should contain:

```python
spotify_credentials = {
    "CLIENT_ID": "your_spotify_client_id",
    "CLIENT_SECRET": "your_spotify_client_secret"
}
```

The `config.py` file is used in the notebook to interact with the Spotify API.

### 2. Kaggle Account and API Credentials

To upload datasets to Kaggle, you will need a Kaggle account and API token.

1. Sign up for a Kaggle account at Kaggle.
2. Obtain your API Token by clicking on your profile picture on the top right corner, and then navigate to 'My Account' from the dropdown menu. Scroll down to the 'API' section and click on 'Create New API Token'. This will download a kaggle.json file containing your API credentials.
Store the kaggle.json file in the location `~/.kaggle/kaggle.json` on your machine. For more information, refer to the [Kaggle API documentation](https://www.kaggle.com/docs/api).
3. Update the dataset-metadata.json file to direct the data at your dataset. You will not be able to use my same filepath because it is tied to my Kaggle credentials.

### 3. Cloning the Repository
Once you have set up your API credentials, clone this repository to your local machine to get started:

```bash
git clone https://github.com/your-github-username/your-repo-name.git
```

Now you can navigate into the cloned project directory and install the required Python packages.

```bash
cd your-repo-name
pip install -r requirements.txt
```
With these steps, you're ready to explore the project!

## Automation with GitHub Actions
Under `.github/workflows` there is a `scheduled_update.yml` file. This file tells the repository to run generator.py file on the first of every month. Can be easily modified to run on push.

## Licenses

This project is not officially associated with Metallica, Spotify, or Kaggle and doesn't represent these companies or entities in any way. It serves as an open-source tool developed by the community to aid in the analysis of publically available data.

### Spotify Data

The data utilized in this project is fetched from the Spotify Web API. According to Spotify's [Developer Terms of Service](https://developer.spotify.com/terms/#iii-user-generated-applications), data fetched through the API can be used for non-commercial purposes.

### Kaggle

The project and its datasets are shared on Kaggle, an open platform for data science projects. All users are expected to respect the Kaggle [Terms of Service](https://www.kaggle.com/terms). 

## Disclaimer

The developer of this project is not responsible for misuse or violation of any terms of service caused by users of the project or the datasets generated by it.


## Acknowledgements

- **Spotify**: For providing the comprehensive and accessible Web API that makes projects like this possible.
- **Kaggle**: For being an exceptional platform for data scientists around the world, fostering an environment of learning and collaboration.
- **OpenAI**: For developing GPT-4, which aided in generating parts of this document that I don't have much experience with.
- **Python open-source community**: For providing an extensive range of libraries that have made the data analysis and visualization so much more efficient.
- **Spotipy**: For creating a simple way to work with the Spotify API in python.

And lastly, a huge thank you to all those on Kaggle who came before me with Metallica datasets that inspired me to create a more refined, up-to-date version.



