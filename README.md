# Image Captioner

This repository provides an implementation of an **Image Captioning** model, utilizing deep learning techniques to generate captions for images. The project is implemented in Python and uses Jupyter notebooks for experimentation and demonstration.

---

## Table of Contents
- [Features](#features)
- [Setup Instructions](#setup-instructions)
  - [Cloning the Repository](#cloning-the-repository)
  - [Creating a Python Virtual Environment](#creating-a-python-virtual-environment)
  - [Installing Dependencies](#installing-dependencies)
  - [Downloading the Dataset](#downloading-the-dataset)
- [Running the Notebook](#running-the-notebook)
- [Contributing](#contributing)


---

## Features
- Uses deep learning models to generate captions for images.
- Pre-trained models can be used for inference.
- Clear and well-documented Jupyter notebook for step-by-step understanding.
- Planning to integrate model into self hosted web application.

---

## Setup Instructions
Follow these steps to set up the project locally on your machine:

### 1. Cloning the Repository
First, clone the repository to your local machine:

```bash
git clone https://github.com/Eshaan416/Image_Captioner.git
cd Image_Captioner
```

---

### 2. Creating a Python Virtual Environment
It is recommended to use a virtual environment to isolate project dependencies.

For **Windows**:
```bash
python -m venv venv
venv\Scripts\activate
```

For **Linux/macOS**:
```bash
python3 -m venv venv
source venv/bin/activate
```

Once activated, your terminal prompt will show the virtual environment name.

---

### 3. Installing Dependencies
Install the required Python libraries using the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

This will install all dependencies, including TensorFlow, NumPy, Matplotlib, and other required packages.

---

### 4. Downloading the Dataset
This project works with the **Flickr8k** dataset. Follow these steps to download it:

1. **Flickr8k Dataset**: Download the dataset from [this link](https://www.kaggle.com/datasets/adityajn105/flickr8k).
2. Extract the dataset and ensure the following structure:
   ```
   Image_Captioner/
   |-- model/
   |   |-- Flickr8k/
   |       |-- captions.txt    # Annotations
   |       |-- Images/  # Images
   |-- captioner.ipynb
   ```
3. Place the extracted `captions.txt` and `Images` directories inside the `Flickr8k/` folder as shown above.

---

## Running the Notebook
Once the dependencies are installed and the dataset is in place, you can run the Jupyter notebook:

1. Launch Jupyter Notebook:
   ```bash
   jupyter notebook
   ```
2. Navigate to the `model` folder and open `captioner.ipynb`.
3. Run the cells step-by-step to train the model and generate captions for sample images.

---

## Contributing
Contributions are welcome! Feel free to fork the repository and submit a pull request with improvements or fixes.

---

