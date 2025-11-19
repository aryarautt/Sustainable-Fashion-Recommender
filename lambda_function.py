import boto3
import json
import joblib
import pandas as pd
from io import BytesIO
from sklearn.metrics.pairwise import cosine_similarity

# S3 bucket where your model files are stored
bucket_name = "sustainable-fashion-models"

s3 = boto3.client("s3")

def load_pickle_from_s3(key):
    obj = s3.get_object(Bucket=bucket_name, Key=key)
    return joblib.load(BytesIO(obj['Body'].read()))

# Load vectorizer + kmeans
vectorizer = load_pickle_from_s3("vectorizer.pkl")
kmeans = load_pickle_from_s3("kmeans.pkl")

# Load metadata
obj = s3.get_object(Bucket=bucket_name, Key="metadata.csv")
df = pd.read_csv(obj['Body'])

# Build text column
df['text'] = (
    df['prod_name'].astype(str) + " " +
    df['detail_desc'].astype(str) + " " +
    df['product_type_name'].astype(str) + " " +
    df['colour_group_name'].astype(str) + " " +
    df['garment_group_name'].astype(str)
)

def lambda_handler(event, context):

    # ---- CORS Preflight (OPTIONS) ----
    if event.get("httpMethod") == "OPTIONS":
        return {
            "statusCode": 200,
            "headers": {
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Headers": "*",
                "Access-Control-Allow-Methods": "GET,POST,OPTIONS"
            },
            "body": ""
        }

    # ---- GET Request Processing ----
    params = event.get("queryStringParameters", {}) or {}

    color = params.get("color", "")
    item_type = params.get("type", "")
    occasion = params.get("occasion", "")

    query = f"{color} {item_type} {occasion}"
    
    q_vec = vectorizer.transform([query])
    product_vectors = vectorizer.transform(df['text'])

    similarities = cosine_similarity(q_vec, product_vectors).flatten()
    df['similarity'] = similarities

    top = df.sort_values("similarity", ascending=False).head(10)

    results = top[[
        'prod_name',
        'product_type_name',
        'colour_group_name',
        'garment_group_name',
        'detail_desc',
        'similarity'
    ]].to_dict(orient="records")

    # ---- RETURN SUCCESS RESPONSE WITH CORS ----
    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Headers": "*",
            "Access-Control-Allow-Methods": "GET,POST,OPTIONS"
        },
        "body": json.dumps(results)
    }

