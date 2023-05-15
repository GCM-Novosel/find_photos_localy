# Face Recognition App

This Python script utilizes the `face_recognition` library to detect photos with a specific face in a given folder and copy them to another folder. The script employs multiprocessing to speed up the face recognition process.

## Usage

1. Install the required packages by running the following command:
    ```shell
    pip install face_recognition
    ```

2. Modify the following variables in the script to match your requirements:
    - `folder_path`: The path to the folder containing the photos you want to search.
    - `save_path`: The path to the folder where the identified photos should be copied.
    - `reference_image_path`: The path to the reference image containing the face to be detected.

3. Run the script:
    ```shell
    python find_photos_multiprocessing.py
    ```

4. The script will iterate through all files and subfolders in the `folder_path`. If a photo contains the specified face, it will be copied to the `save_path` folder. The console will display messages indicating the progress and outcome of the search.

## Requirements

- Python 3.x
- face_recognition library

## Contributing

Contributions are welcome! If you find a bug or have suggestions for improvements, please feel free to open an issue or submit a pull request on GitHub.

## License

This project is licensed under the [MIT License](LICENSE).

