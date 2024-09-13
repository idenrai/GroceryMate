.PHONY: shell install serve test fmt lint

# Poetry 가상환경 활성화
shell:
	poetry shell

# 종속성 설치
install:
	poetry lock
	poetry install

# 실행
serve:
	poetry run uvicorn main:app --reload

# 테스트 실행
test:
	export PYTHONPATH=$(pwd):$PYTHONPATH
	python -m pytest tests

# 코드 포맷팅
fmt:
	poetry run ruff format .

# 코드 린팅
lint:
	poetry run ruff check . --fix
	poetry run mypy .
