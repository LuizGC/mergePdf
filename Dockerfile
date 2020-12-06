FROM mcr.microsoft.com/vscode/devcontainers/python:0-3.9

RUN if [ "${INSTALL_NODE}" = "true" ]; then su vscode -c "source /usr/local/share/nvm/nvm.sh && nvm install ${NODE_VERSION} 2>&1"; fi

COPY requirements.txt .
COPY app.py .
COPY pdfmerger.py .
copy templates ./

RUN pip3 install --upgrade pip \
    && pip3 install -r requirements.txt
