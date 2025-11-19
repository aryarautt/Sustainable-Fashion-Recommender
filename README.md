# Sustainable Fashion Recommender System 👗🤖  
An AI-powered outfit recommendation system using Machine Learning and AWS Cloud Services.

## 📌 Project Summary  
This project recommends fashion items based on **colour**, **type**, and **occasion** using ML models.  
The system analyzes garment descriptions and predicts the most similar products using **text-based similarity**.

The deployed system uses:
- **Machine Learning (TF-IDF, KMeans, Cosine Similarity)**
- **AWS Lambda** (serverless backend)
- **AWS API Gateway** (API access)
- **AWS S3** (model + dataset storage)
- **AWS ECR + Docker** (containerized Lambda)
- **HTML/CSS/JS** frontend

---

# 🚀 Key Features
- Enter **colour**, **product type**, and **occasion**
- ML model recommends best-matching outfits
- Real-time predictions using AWS Lambda
- Secure API using AWS API Gateway
- Fully cloud-hosted, scalable, cost-efficient

---

# 🧠 Machine Learning Overview  

### **1. TF-IDF Vectorizer**
Converts text (product descriptions) into number vectors.  
Helps model understand important words like *“red dress party”*.

### **2. KMeans Clustering**
Groups similar clothes into clusters.  
Makes search and comparison faster.

### **3. Cosine Similarity**
Measures similarity between user input and product descriptions.  
Example:  
- *“Red party dress”* is more similar to *“Red sequins party dress”* than *“Blue winter jacket”*.

---

# 🏗 AWS Architecture  
✔ **S3** → stores ML models (vectorizer.pkl, kmeans.pkl, metadata.csv)  
✔ **Lambda** → executes Python ML code  
✔ **Docker + ECR** → package dependencies  
✔ **API Gateway** → exposes HTTPS endpoint for frontend  
✔ **CORS enabled** → allows browser access  
✔ **Frontend** → calls API and shows results

---

Sustainable-Fashion-Recommender/
│
├── backend/
│ ├── lambda_function.py
│ ├── requirements.txt
│ └── Dockerfile
│
├── ml-models/
│ ├── vectorizer.pkl
│ ├── kmeans.pkl
│ ├── metadata.csv
│ └── articles.csv
│
└── frontend/
└── index.html


---

# 🧪 How It Works  
1. User enters: **color**, **type**, **occasion**  
2. Query is converted into numbers using **TF-IDF**  
3. System compares query with dataset using **cosine similarity**  
4. Top 10 most similar fashion items are returned  
5. Results displayed instantly in the UI

---

# 🖥 Frontend  

Simple HTML + CSS + JavaScript page.

The JS function calls:
GET https://your-api-id.execute-api.us-east-1.amazonaws.com/prod/recommend?color=red&type=dress&occasion=party


---

# 🌐 Deployment Steps (Short)
1. Upload ML models to AWS S3  
2. Package Lambda backend using Docker  
3. Push Docker image to AWS ECR  
4. Create Lambda function from container image  
5. Connect Lambda to API Gateway  
6. Enable CORS  
7. Deploy API  
8. Connect frontend with API URL  

---

# 📦 Requirements  
Python 3.9  
Libraries:  
`pandas`, `sklearn`, `boto3`, `joblib`, `numpy`

---

# 🎯 Project Outcome  
This system helps:
- Improve clothing suggestions  
- Reduce browsing time  
- Enable personalised fashion shopping  
- Support sustainable buying decisions  

---

# 🛠 Future Improvements  
- Add body-size & fit preference  
- Add image-based recommendations (CNN/Deep Learning)  
- Add trending and seasonal suggestions  
- User login + saved recommendations  

---

# 👩‍💻 Author  
**Arya Raut**  
Sustainable Fashion Recommender System using ML + Cloud.

# 📁 Project Structure  

