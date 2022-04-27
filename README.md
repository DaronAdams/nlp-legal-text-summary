# nlp-legal-text-summary
Web application developed to summarize legal documents using Natural Language Processing.
The backend is written in Flask and the frontend uses standard html/css. 

## Installation

First run the following: 

```bash
git clone https://github.com/DaronAdams/nlp-legal-text-summary
```


Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the required packages.
You will need the following packages to successfully run the program.

```bash
pip install flask
pip install transformers
pip install torch
```

Navigate to the directory where you saved the file
Open VsCode or your IDE of choice and start the server using

```python
python server.py
```

By default flask will run on the following url

```bash
http://127.0.0.1:5000/#
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
