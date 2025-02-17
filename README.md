# CTD-Net-for-CBIR
Overview
This repository implements a Hybrid Image Retrieval System (CTD-Net) that combines handcrafted features (color & texture) with deep features extracted from EfficientNet-B7 to improve image retrieval accuracy. The hybrid approach significantly enhances retrieval performance on Corel-1K and Corel-10K datasets, achieving 98.85% and 92.40% precision, respectively.

This research explores various similarity distance measures to evaluate retrieval effectiveness and validate the performance of the hybrid model.

# Repository Structure
CTD-Net-for CBIR/
│── Dataset/                         # File for dataset links
│   ├── Dataset Links.txt/
│
│── Models/                        # All Handcrafted Models alongwith Pre-trained model (EfficientNet B7)
│   ├── All_Models.ipynb.
│
│── src/                           # Source code
│   ├── CTD_Net_for_CBIR.ipynb      # Handcrafted + Deep feature extraction along with Distance metrics & ranking
│
│── Results/                       # Output evaluation results
│   ├── Corel_10K.xlsx
│   ├── Corel_1K.xlsx
│
│── README.md                      # Documentation
│── requirements.txt                # Dependencies

# About Dataset
Corel-1K Dataset
Size: 1000 images
Classes: 10 categories (100 images per category)
Download: [Corel-1K](https://www.kaggle.com/datasets/elkamel/corel-images)

Corel-10K Dataset
Size: 10,000 images
Classes: Multiple categories
Download: [Corel-10K](https://www.kaggle.com/datasets/michelwilson/corel10k)

