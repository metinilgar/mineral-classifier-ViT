# 🔬 Mineral Classifier - Vision Transformer (ViT)

This project is a comprehensive machine learning system that automatically classifies mineral images using the **Vision Transformer (ViT)** model. The project includes both a research-oriented Jupyter notebook and a user-friendly web interface.

## 🎯 Project Overview

### Supported Mineral Types
- **Biotite** - Dark-colored mica mineral
- **Bornite** - Copper sulfide mineral
- **Chrysocolla** - Copper silicate mineral
- **Malachite** - Green copper carbonate mineral
- **Muscovite** - Light-colored mica mineral
- **Pyrite** - Gold-colored iron sulfide mineral
- **Quartz** - Crystal silicon oxide mineral

### Key Features
- 🤖 **Modern AI Technology:** Vision Transformer (ViT) architecture
- 📊 **High Accuracy:** Reliable predictions with a trained model
- 🖥️ **Web Interface:** User-friendly interface with Gradio
- 📝 **Jupyter Notebook:** Detailed research and development environment
- 📈 **Visual Results:** Interactive charts with Plotly
- 🔄 **Multiple Model Versions:** Different model iterations

## 📁 Project Structure

```
mineral-classifier-ViT/
├── 📂 app/                          # Web Application
│   ├── app.py                       # Gradio web interface
│   ├── model_loader.py              # Model loading module
│   ├── requirements.txt             # Python dependencies
│   ├── README.md                    # Web app documentation
│   └── 📂 model/                    # Active model files
│       ├── config.json              # Model configuration
│       ├── model.safetensors        # Trained model weights
│       └── preprocessor_config.json # Image preprocessing settings
├── 📂 models/                       # Model Versions
│   ├── 📂 v1/                      # Model Version 1
│   ├── 📂 v2/                      # Model Version 2
│   └── 📂 v3/                      # Model Version 3
├── 📂 notebooks/                    # Jupyter Notebooks
│   └── Mineral_ViT.ipynb           # Main development notebook
└── README.md                        # This file
```

## 🚀 Quick Start

### 1. Requirements
- Python 3.8+
- CUDA support (optional, for GPU acceleration)
- Minimum 4GB RAM
- 2GB free disk space

### 2. Installation

```bash
# Clone the project
git clone https://github.com/yourusername/mineral-classifier-ViT.git
cd mineral-classifier-ViT

# Create a virtual environment (recommended)
python -m venv mineral_env
source mineral_env/bin/activate  # Linux/Mac
# or
mineral_env\Scripts\activate     # Windows

# Install required packages
cd app
pip install -r requirements.txt
```

### 3. Run the Web Application

```bash
# Go to the app directory
cd app

# Start the web interface
python app.py
```

The application will automatically open in your browser: `http://127.0.0.1:7860`

## 📚 User Guide

### 🖥️ Using the Web Interface

1. **Model Loading:** The model loads automatically when the app starts
2. **Image Upload:** Select or drag-and-drop a mineral image from the left panel
3. **Classification:** Click the "🔍 Classify Image" button
4. **Review Results:**
   - Main prediction and confidence score
   - Detailed scores for all classes
   - Interactive chart view

### 📓 Using the Jupyter Notebook

```bash
# Go to the notebooks directory
cd notebooks

# Start Jupyter
jupyter lab Mineral_ViT.ipynb
```

In the notebook, you will find:
- Downloading and preparing the dataset
- Model training and evaluation
- Visualization and analysis
- Model comparisons

## 🔧 Technical Details

### Model Architecture
- **Type:** Vision Transformer (ViT-Base)
- **Input Size:** 224x224x3 RGB
- **Output:** 7 classes (mineral types)
- **Framework:** PyTorch + Transformers (Hugging Face)
- **Model Size:** ~300MB

## 📸 Image Requirements

### Quality Standards
- **Resolution:** At least 224x224 pixels
- **Format:** JPEG, PNG
- **Lighting:** Good and even lighting
- **Sharpness:** Not blurry, sharp images
- **Background:** Clean, non-distracting background

### Tips
✅ **Good Examples:**
- Mineral framed alone
- Natural colors preserved
- Sufficient detail visible

❌ **To Avoid:**
- Mixed minerals
- Too close or too far shots
- Poor lighting
- Blurry or noisy images

## 🔄 Model Versions

### v1 - Basic Training
- First training iteration
- Low number of epochs
- Basic ViT architecture

### v2 - Intermediate Training
- Increased number of epochs
- Longer training duration
- Improved model performance

### v3 - Full Training
- Highest number of epochs
- Maximum training iteration
- Best model performance


## 📊 Dataset

### Source
- **Dataset:** [Minerals Identification Classification](https://www.kaggle.com/datasets/youcefattallah97/minerals-identification-classification)
- **Platform:** Kaggle
- **Size:** ~800MB
- **Number of Images:** Thousands of mineral photos

### Data Structure
```
data/
├── biotite/
├── bornite/
├── chrysocolla/
├── malachite/
├── muscovite/
├── pyrite/
└── quartz/
```

## 📝 License

This project is distributed under the MIT license. For details, please see the `LICENSE` file.

---

**⭐ If you like this project, don't forget to give it a star!** 