# EngageVision - YouTube Thumbnail Engager
A simple AI-powered Streamlit web application that analyzes YouTube thumbnails and provides feedback to make them more engaging and viewer-friendly.

## Features
- Upload a thumbnail image to get an analysis of its engagement potential.
- Feedback includes strengths, weaknesses, and tips for improvement.
- Clean, modern sidebar design with developer details and social media links.
- Easy-to-use interface built with Streamlit.

## Folder Structure

The directory structure of the project is as follows:
```
project-folder/
├── data/
│   ├── engaging/
│   │   ├── thumbnail1.jpg
│   │   ├── thumbnail2.jpg
│   ├── not_engaging/
│   │   ├── thumbnail3.jpg
│   │   ├── thumbnail4.jpg
├── app.py
├── fetch_data.py
├── train_model.py
```

## Installation

Follow these steps to install the required dependencies for the project.

1. Clone the repository:

    ```
    git clone https://github.com/your-username/your-repository.git
    cd your-repository
    ```

2. Set up a virtual environment:

    ```
    python -m venv venv
    source venv/bin/activate  # For Linux/Mac
    venv\Scripts\activate     # For Windows
    ```

3. Install dependencies:

    ```
    pip install -r requirements.txt
    ```
    
## Fetching Data

To fetch the data, follow these steps:

1. The script `fetch_data.py` is used to download and preprocess the data.
2. Run the script as follows:

    ```
    python src/fetch_data.py
    ```
3. Thumbnails will be downloaded at `/data` folder.    

## Training the Model

1. Once the data has been fetched, the next step is to train the model.
2. The script `train_model.py` is used to train the model and save it as `thumbnail_model.h5`.
3. Run the script as follows:

    ```
    python src/train_model.py
    ```

4. This will train the model using the preprocessed data and save the trained model as `thumbnail_model.h5` in the `models/` folder.

## Running the Streamlit App

1. Now that the model has been trained, you can run the Streamlit app to use the model in a web interface.
2. Navigate to the `app/` folder and run the Streamlit app using the following command:

    ```
    streamlit run app.py
    ```

3. This will start the Streamlit app, and you can interact with it through your web browser. The app will allow you to upload images and generate thumbnails using the trained model (`thumbnail_model.h5`).

## Usage

### Example: Using the Streamlit App

Once the Streamlit app is running, follow these steps to interact with it:

1. Open the web interface (usually available at `http://localhost:8501`).
2. Upload an image for processing.
3. The app will tell how engaging is the uploaded image using the trained model and display it on the page.

## Technologies Used

- **Python:** Core programming language.
- **Streamlit:** Front-end for building the web app.
- **TensorFlow/Keras:** For AI model integration.
- **YouTube Data API:** Fetches video metadata (if applicable).

## Contributing
Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a feature branch:
```git checkout -b feature-name```
3. Commit your changes:
```git commit -m "Description of changes"```
4. Push to your forked repository:
```git push origin feature-name```
5. Submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/VortexV7/EngageVision/blob/main/LICENSE) file for details.

## Preview

![screenshot1](https://github.com/user-attachments/assets/bae32cb7-54a4-4836-9bcc-4f2ab4a7655a)
![screenshot2](https://github.com/user-attachments/assets/2a5b4b86-686f-446b-832d-9923483d1fa3)
