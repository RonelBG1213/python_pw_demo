pip install pytest-playwright
pip install -r requirement.tx
playwright install

Sample cli command
pytest -v tests/regression/homepage/test_dashboard.py --enable-trace --headed