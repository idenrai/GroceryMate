# GroceryMate Backend

GroceryMate의 백엔드 서비스입니다. 이 프로젝트는 FastAPI를 사용하여 쇼핑 리스트를 관리하는 API를 제공합니다.

## 프로젝트 개요

이 프로젝트는 사용자가 쇼핑 리스트를 생성, 조회, 수정, 삭제할 수 있는 기능을 제공합니다. 주요 기술 스택은 다음과 같습니다:

- Python 3.12 이상
- FastAPI
- SQLAlchemy
- Pydantic
- DuckDB

## 설치 방법

### 1. Poetry 설치

Poetry가 설치되어 있지 않다면, 다음 명령어를 사용하여 설치합니다:

```sh
curl -sSL https://install.python-poetry.org | python3 -
```

### 2. 프로젝트 클론

프로젝트를 클론합니다:

```sh
git clone https://github.com/idenrai/GroceryMate.git
cd GroceryMate/backend
```

### 3. 가상환경 생성 및 종속성 설치

Poetry를 사용하여 가상환경을 생성하고 종속성을 설치합니다:

```sh
poetry install
```

### 4. 가상환경 활성화

Poetry 가상환경을 활성화합니다:

```sh
make shell
```

## 사용 방법

### 1. 데이터베이스 설정

DuckDB를 사용하여 데이터베이스를 설정합니다. 데이터베이스 파일은 `database.db`로 설정되어 있습니다.

### 2. 서버 실행

다음 명령어를 사용하여 FastAPI 서버를 실행합니다:

```sh
make serve
```

서버가 실행되면, 브라우저에서 <http://127.0.0.1:8000>에 접속하여 API 문서를 확인할 수 있습니다.

## 주요 기능

### 1. 쇼핑 리스트 생성

쇼핑 리스트를 생성합니다. 요청 본문에는 리스트 이름과 아이템 목록이 포함됩니다.

### 2. 쇼핑 리스트 조회

특정 쇼핑 리스트를 조회합니다.

### 3. 쇼핑 리스트 수정

특정 쇼핑 리스트를 수정합니다.

### 4. 쇼핑 리스트 삭제

특정 쇼핑 리스트를 삭제합니다.

## 데이터 모델

### ShoppingList

- `list_id: UUID`
- `user_id: UUID`
- `list_name: str`
- `total_estimated_price: float`
- `items: List[ShoppingListItem]`

### ShoppingListItem

- `item_id: UUID`
- `list_id: UUID`
- `product_id: UUID`
- `quantity: int`
- `estimated_price: float`

## 기여 방법

기여를 원하시면, 이슈를 생성하거나 풀 리퀘스트를 제출해 주세요. 기여해 주셔서 감사합니다!

## 라이선스

이 프로젝트는 MIT 라이선스 하에 배포됩니다. 자세한 내용은 LICENSE 파일을 참조하세요.
