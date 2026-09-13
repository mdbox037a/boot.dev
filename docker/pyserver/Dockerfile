FROM debian:stable-slim
COPY main.py main.py
COPY books/ books/
RUN <<EOF
apt update
apt upgrade -y
apt install -y build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev libsqlite3-dev wget libbz2-dev
wget https://www.python.org/ftp/python/3.10.8/Python-3.10.8.tgz
tar -xf Python-3.10.*.tgz
cd Python-3.10.8 && ./configure --enable-optimizations && make && make altinstall
EOF
CMD ["python", "main.py"]
