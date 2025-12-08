                Project Title: Organoid-Inspired Bio-Computer State Classification
      Course: Final Project — Data Science Methods (INFO6105)
      Student Name: Jiadong Liu
  1. Project Overview
This project simulates a monitoring system for a Biological Computer (Brain Organoid). Since real-time organoid wet-lab data is scarce, we utilize public EEG data as a "Biological Signal Proxy" to train a machine learning model. The goal is to classify the organoid's computational state as:Active (Processing / Computing)，
Inactive (Resting / Standby)
  The project follows the complete Data Science Pipeline:
  EXTRACT:Data extraction, cleaning, and feature engineering.LEARN: Model training and evaluation.PREDICT: Deployment for real-time state prediction.

  2. Data Description
  2.1 Data Source
Source: Public Kaggle Dataset (mental-state.csv).
Processing: The data was randomly sampled and processed to create a curated dataset of 150 rows.
Bonus Requirement Met: 100 < rows < 200.
  2.2 Data Structure
The dataset contains 12 input features mapped to organoid-inspired metrics, plus the target label:
Neural Inputs: Neuron_Input_AF7, TP9, AF8, TP10
Synapse Activity: Alpha, Beta, Delta
Metabolic Rates: Metabolic_Rate_1, Metabolic_Rate_2
Ion Channels: Ion_Channel_Flux_1, Ion_Channel_Flux_2
Membrane Potential: Membrane_Potential
  2.3 Feature Engineering (Bonus Met)
To satisfy the course requirement ("Engineer at least 2 features"), the following composite features were created:
（1）Total_Input_Power: Sum of the 4 neural input channels (representing total energy).
（2）Synapse_Ratio: Ratio of Alpha/Beta activity (representing synaptic balance).
Final Dimensions: 150 Rows × 15 Columns (Meets Bonus: 10 < columns < 20).
  2.4 Target Label
Target: Bio_Computer_State
Values: 1 (Active) vs 0 (Inactive).

  3. Methodology
  3.1 Split
Training Set: 80% (120 samples)
Testing Set: 20% (30 samples)
  3.2 Models
（1）. Decision Tree: Used as a baseline model for interpretability.
（2）. Random Forest: Selected as the Final Model due to its robustness against biological signal noise and higher stability.
 (3). We additionally implemented a Gradient Boosting Classifier, a model not covered in the course curriculum. This model utilizes Boosting techniques to enhance overall performance by sequentially stacking multiple weak learners, serving as a robust comparative baseline against the Random Forest model.
  3.3 Evaluation Metrics：Accuracy,Confusion Matrix,Precision / Recall / F1-score
  Result: The Random Forest model achieved an accuracy of approx. 67%, which is consistent with the high noise floor of non-invasive biological signals.

  5. Results
(1)The model successfully classifies Active / Inactive states.
(2)Some misclassifications are observed, which is expected due to the overlap in proxy biological signals.
(3)Confusion Matrix and Scores are visualized in the Notebook.

  6. Prediction Demo
A live prediction pipeline was built to simulate a real-world scenario. The system loads the saved model (my_best_model.pkl), accepts new signal arrays, and outputs the status.
Example Output:
==============================
 >>> Biological Computer Status Analysis Report <<<
==============================
Current Forecast Status: 🔴 INACTIVE 
Model Confidence  : 82.00%
==============================

  6. Repository Structure
README.md: Project documentation
mental-state.csv: Original Raw Data
organoid_data_cleaned.csv: Processed Data
code.ipynb: Main Notebook
my_best_model.pkl: Saved Model
Summary.pdf: Executive Summary
Slides.pdf: Presentation Slides

  7. How to Run
  1. Install Dependencies:
pip install pandas numpy seaborn matplotlib scikit-learn joblib
  2. Run the Notebook:
Open code.ipynb and run all cells. The script will automatically perform data cleaning, training, and the prediction demo.

  8. Limitations
(1)Proxy Data: EEG is used as a proxy; it is not direct Micro-Electrode Array (MEA) data from wet-lab organoids.
(2)Sample Size: Small dataset (N=150) limits generalization.
(3)Dynamics: Lacks temporal sequence features (Time-Series).

  9. Future Work
(1)Integrate real wet-lab organoid data when available.
(2)Implement Deep Learning (LSTM / 1D-CNN) for signal dynamics.
(3)Build a real-time dashboard using Streamlit.
