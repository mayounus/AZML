#Source your python virtual environment (python3 -m venv ~/.myrepo)
source ~/.myrepo/bin/activate

#Project scaffolding
make install

# Run prediction
./make_predict_azure_app.sh

#Use Locust testing tool 
locust -f locust.py --headless -t 3s