install:
	pip install -r requirements.txt

run:
	streamlit run app/main.py

format:
	black .

lint:
	ruff check .

test:
	pytest

docker:
	docker compose up --build