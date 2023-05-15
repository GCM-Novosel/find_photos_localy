from multiprocessing import Pool, cpu_count, freeze_support
import os
import shutil
import face_recognition

# Iterate through all files and subfolders in the given folder path
def process_image(task):
    file_path, reference_encoding, save_path = task
    # Load the image file into a numpy array
    image = face_recognition.load_image_file(file_path)
    print("opening", str(file_path))

    # Find all the faces in the image
    face_locations = face_recognition.face_locations(image)


    # If any faces were found, check if your face is one of them
    for face_location in face_locations:
        # Generate the face encoding for the current face in the image
        face_encoding = face_recognition.face_encodings(image, [face_location])[0]

        # Compare the face encoding to your reference face encoding
        match = face_recognition.compare_faces([reference_encoding], face_encoding)[0]

        # If the current face in the image matches your face, copy the image to the save folder
        if match:
            shutil.copy2(file_path, save_path)
            print("found one")
        else:
            print("didn't detect the person on this photo")


if __name__ == '__main__':
    # Define the number of worker processes to use
    num_processes = cpu_count() - 1

    # Call the freeze_support() function on Windows
    freeze_support()

    # Create a Pool of worker processes
    pool = Pool(processes=num_processes)

    folder_path = ""
    save_path = ""
    reference_image_path = ""

    # Load the reference image into a numpy array and generate its face encoding
    reference_image = face_recognition.load_image_file(reference_image_path)
    reference_encoding = face_recognition.face_encodings(reference_image)[0]

    # Iterate through all files and subfolders in the given folder path
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            # Check if the file is a supported image file type
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp')):
                # Create a tuple of the file path, reference encoding, and save path to pass to the worker process
                file_path = os.path.join(root, file)
                task = (file_path, reference_encoding, save_path)

                # Submit the task to the Pool
                pool.apply_async(process_image, args=(task,))

    # Wait for all worker processes to complete
    pool.close()
    pool.join()