\# 🌾 Cross-Regional Crop AI Lab



An interactive Streamlit dashboard for exploring \*\*cross-regional crop classification and geographic generalization in machine learning\*\*.



The project focuses on an important challenge in agricultural AI: a model may perform well on data from regions similar to its training data, but its performance can change when it is evaluated on a geographically different or unseen region.



This dashboard provides interactive tools for exploring regional data, running experiments, comparing models, analyzing errors, and understanding domain shift.



\---



\## 🎯 Project Objective



The primary objective of this project is to explore how machine learning models behave when crop data comes from different geographic regions.



Agricultural datasets can vary significantly across regions because of differences in:



\- Climate

\- Soil conditions

\- Crop varieties

\- Agricultural practices

\- Geographic characteristics

\- Environmental conditions

\- Remote-sensing observations



Understanding these differences is important for developing crop-classification systems that can generalize beyond the geographic region used for training.



\---



\## ✨ Features



The dashboard contains multiple interactive modules:



\### 01 — Overview



Provides an introduction to the project, its motivation, and the concept of cross-regional crop classification.



\### 02 — Regional Explorer



Allows users to explore crop-related information across different geographic regions.



\### 03 — Experiment Lab



Provides an environment for exploring different experimental configurations and evaluating model behavior.



\### 04 — Generalization Results



Visualizes model performance when evaluated across different geographic regions and helps analyze generalization.



\### 05 — Model Comparison



Provides comparisons between different machine-learning approaches and their performance.



\### 06 — Error Analysis



Helps investigate classification errors and understand where models may struggle.



\### 07 — Domain Shift



Explores differences between data distributions across geographic regions and demonstrates the concept of domain shift.



\### 08 — Sample Inspector



Allows users to inspect individual samples and their corresponding classification information.



\### 09 — Roadmap



Documents possible future improvements and research directions for the project.



\---



\## 🧠 Key Research Concepts



\### Geographic Generalization



Geographic generalization refers to the ability of a machine-learning model trained using data from certain geographic regions to maintain useful performance when applied to a different or previously unseen region.



```text

Training Regions

&#x20;      │

&#x20;      ▼

&#x20;  ML Model

&#x20;      │

&#x20;      ▼

&#x20;Unseen Region

&#x20;      │

&#x20;      ▼

Model Evaluation



Domain Shift



Domain shift occurs when the statistical distribution of data changes between the training and testing environments.



For crop classification, this can occur because different regions may have different environmental and agricultural characteristics.



Training Region

&#x20;      │

&#x20;      ▼

Different environmental conditions

&#x20;      │

&#x20;      ▼

Different data distribution

&#x20;      │

&#x20;      ▼

Unseen Region

&#x20;      │

&#x20;      ▼

Possible performance change

🛠️ Technology Stack



The project is built using:



Python

Streamlit — interactive web dashboard

Pandas — data manipulation

NumPy — numerical computing

Scikit-learn — machine-learning algorithms

Plotly — interactive data visualization

Folium — geographic visualization

Streamlit-Folium — Folium integration with Streamlit

📂 Project Structure

crop-classification-dashboard/

│

├── app.py

├── requirements.txt

├── .gitignore

├── README.md

│

├── pages/

│   ├── 01\_overview.py

│   ├── 02\_regional\_explorer.py

│   ├── 03\_experiment\_lab.py

│   ├── 04\_generalization\_results.py

│   ├── 05\_model\_comparison.py

│   ├── 06\_error\_analysis.py

│   ├── 07\_domain\_shift.py

│   ├── 08\_sample\_inspector.py

│   └── 09\_roadmap.py

│

└── utils/

&#x20;   ├── data\_loader.py

&#x20;   └── styling.py

⚙️ Installation

1\. Clone the repository

git clone https://github.com/AT839/crop-classification-dashboard.git

2\. Navigate to the project

cd crop-classification-dashboard

3\. Create a virtual environment



Windows:



python -m venv venv

4\. Activate the virtual environment

venv\\Scripts\\activate

5\. Install dependencies

pip install -r requirements.txt

▶️ Running the Dashboard



Start the Streamlit application:



streamlit run app.py



The application will open in your browser.



By default, Streamlit runs the application at:



http://localhost:8501

🔬 Research Workflow



A typical cross-regional experiment can be represented as:



&#x20;            Crop Dataset

&#x20;                 │

&#x20;                 ▼

&#x20;         Geographic Regions

&#x20;                 │

&#x20;         ┌───────┴───────┐

&#x20;         ▼               ▼

&#x20;  Training Regions   Unseen Region

&#x20;         │               │

&#x20;         ▼               │

&#x20;     ML Model            │

&#x20;         │               │

&#x20;         └───────┬───────┘

&#x20;                 ▼

&#x20;         Model Evaluation

&#x20;                 │

&#x20;                 ▼

&#x20;      Generalization Analysis



This workflow can be used to study how model performance changes when the geographic distribution of testing data differs from the training data.



🚀 Future Directions



Potential future extensions include:



Integration of satellite remote-sensing data

NDVI and other vegetation indices

Additional geographic regions

Deep-learning-based crop classification

CNN-based approaches

Temporal satellite-data analysis

Domain adaptation

Domain-adversarial learning

Improved GIS visualization

External regional validation

Deployment for real-world agricultural applications

🎓 Applications



The project can support research and experimentation in areas such as:



Precision agriculture

Agricultural remote sensing

Crop classification

Machine learning

Geographic AI

GIS

Domain adaptation

Cross-regional model evaluation

👥 Project



This project was developed as a collaborative project focused on understanding and visualizing cross-regional crop classification and geographic generalization using machine learning.

📄 License



This project is intended primarily for educational and research purposes.

