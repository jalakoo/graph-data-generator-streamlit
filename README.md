# Graph Data Generator Streamlit
Applet with UI interface to conveniently use and test the graph-data-generator package.

## Install Poetry
This applet uses Poetry for dependency management as the `dev` branch uses it to reference any local copy of the graph-data-generator for development and testing.

Update SSL certs
`/Applications/Python\ 3.11/Install\ Certificates.command`

Install
`curl -sSL https://install.python-poetry.org | python3 -`

## Testing Local
If referencing the graph-data-generator locally, with Poetry:
`poetry add --editable /path/to/package`

Point to the project root folder, for example:
`poetry add --editable /Users/jasonkoo/jason/repos/graph-data-generator`

## Running
`poetry update`
`poetry run streamlit run graph_data_generator_streamlit/app.py`