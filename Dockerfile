FROM public.ecr.aws/lambda/python:3.9

ENV AWS_CLI_VERSION=2.0.30

COPY app.py ${LAMBDA_TASK_ROOT}
COPY .env ${LAMBDA_TASK_ROOT}
COPY requirements.txt ${LAMBDA_TASK_ROOT}
# COPY tmp/ ${LAMBDA_TASK_ROOT}/tmp/

RUN set -ex \
  && yum update -y && yum install -y \
    unzip \
    tar \
    gzip

RUN curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64-${AWS_CLI_VERSION}.zip" -o "/tmp/awscliv2.zip" \
  && unzip /tmp/awscliv2.zip -d /tmp/ \
  && /tmp/aws/install \
  && rm -rf /tmp/aws*

RUN curl -o kubectl -sL "https://amazon-eks.s3.us-west-2.amazonaws.com/1.21.2/2021-07-05/bin/linux/amd64/kubectl" \
  && chmod +x ./kubectl \
  && mv ./kubectl /usr/local/bin/kubectl

RUN curl -sL "https://github.com/weaveworks/eksctl/releases/latest/download/eksctl_$(uname -s)_amd64.tar.gz" | tar xz -C /tmp \
  && mv /tmp/eksctl /usr/local/bin

RUN pip3 install -r requirements.txt

CMD ["app.handler"]
