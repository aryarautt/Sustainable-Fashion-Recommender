FROM public.ecr.aws/lambda/python:3.9

# Install system packages
RUN yum install -y gcc gcc-c++ make

# Install Python dependencies
COPY requirements.txt ./
RUN pip install -r requirements.txt

# Copy Lambda function code
COPY lambda_function.py ${LAMBDA_TASK_ROOT}

CMD ["lambda_function.lambda_handler"]

