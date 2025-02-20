#  Enhanced Content-Based Image Retrieval via Hybrid Color, Texture, and Deep Learning Features 
## **CTD-Net-for-CBIR**  

---

##  Overview  
This repository implements a **Hybrid Image Retrieval System (CTD-Net)** that combines **handcrafted features (color & texture)** with **deep features extracted from EfficientNet-B7** to improve image retrieval accuracy. The hybrid approach significantly enhances retrieval performance on **Corel-1K** and **Corel-10K** datasets, achieving **98.85% and 92.40% precision**, respectively. This research explores **various similarity distance measures** to evaluate retrieval effectiveness and validate the performance of the hybrid model.  

---

##  Repository Structure  

### **Dataset/**  
Contains dataset links for **Corel-1K** and **Corel-10K**.  
 **Files Included:**  
- [`Dataset_Links.txt`](Dataset/Dataset Links.txt) → Contains URLs to download datasets  

---

### **Models/**  
Includes all handcrafted models along with the pre-trained **EfficientNet-B7** model.  
 **Files Included:**  
- [`All_Models.ipynb`](Models/All_Models.ipynb) → Contains feature extraction models  

---

### **src/**  
Contains the main source code for **feature extraction, similarity measurement, and ranking**.  
 **Files Included:**  
- [`CTD_Net_for_CBIR.ipynb`](src/CTD_Net_for_CBIR.ipynb) → Code for feature extraction, similarity metrics, and ranking  

---

### **Results/**  
Stores output evaluation results generated after running the model.  
 **Files Included:**  
- [`Corel_10K.xlsx`](Results/Corel_10K.xlsx) → Evaluation results for Corel-10K dataset  
- [`Corel_1K.xlsx`](Results/Corel_1K.xlsx) → Evaluation results for Corel-1K dataset  

---

### **Other Files**  
- [`README.md`](README.md) → Documentation and usage instructions  
- [`requirements.txt`](requirements.txt) → Dependencies for setting up the environment  


---

##  About Dataset  

### Corel-1K Dataset  
- **Size**: 1000 images  
- **Classes**: 10 categories (100 images per category)  
- **Download**: [Corel-1K](https://www.kaggle.com/datasets/elkamel/corel-images)  

### Corel-10K Dataset  
- **Size**: 10,000 images  
- **Classes**: Multiple categories  
- **Download**: [Corel-10K](https://www.kaggle.com/datasets/michelwilson/corel10k)  

---

##  How to Use the Hybrid Image Retrieval System  

###  Extract Features  
Extract both **handcrafted and deep features** for image retrieval by running:  
 **File:** `CTD_Net_for_CBIR.ipynb`  

 **This will generate:**  
- `handcrafted_features.csv` (Color histograms, texture features)  
- `deep_features.csv` (EfficientNet-B7 extracted feature vectors)  
- `final_combined_features.csv` (Fusion of handcrafted + deep features)  

---

### Evaluation Metrics Output  
 **Generated Metrics:**  
- **List of Top-K retrieved images**  
- **Similarity scores** computed using multiple distance metrics  

 **Evaluation Metrics Include:**  
- **Precision**  
- **Recall**  
- **F1-Score**  
- **Accuracy**  

---

##  Citing CTD-Net  
If you find **CTD-Net** useful in your research, please consider citing:  

```bibtex
@article{Surbhi2024HybridRetrieval,
  title={Enhanced Content-Based Image Retrieval via Hybrid Color, Texture, and Deep Learning Features},
  author={Surbhi Tyagi, Praveen Shukla, Partap Singh, Hitesh Tekchandani},
  journal={},
  year={2024}
}

