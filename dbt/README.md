# dbt

## 개요

GroceryMate 의 DB 를 관리할 수 있도록 dbt 개발 환경을 구축

## 상세

아래의 순서로 기재

- dbt
- duckdb
- dbt project 를 작성하여, duckdb 와 연계

### dbt Install

[https://docs.getdbt.com/docs/core/pip-install](https://docs.getdbt.com/docs/core/pip-install)

기본적으로는 아래의 커맨드로 인스톨 가능

```shell
pip install dbt-core dbt-duckdb
```

#### dbt project 작성 (본 템플릿 상에선 실행하지 않아도 됨)

`dbt init` 으로 프로젝트 작성

### duckdb Install & Create DB

[https://duckdb.org/#quickinstall](https://duckdb.org/#quickinstall)

```shell
brew install duckdb
```

#### Create DB

아래의 커맨드로 간단히 DB 작성 가능

```shell
duckdb [DB 명].db
```

예시)

```shell
duckdb grocery_mate.db
```

#### DB 접속

```shell
duckdb grocery_mate.db
```

#### DB 동작 확인

```duckdb
.databases
.tables
```

#### Table 작성 및 더미 데이터 입력

```shell
cd scripts
poetry install
poetry shell
```

테이블 작성용 스크립트

```shell
python create_tables.py
```

더미 데이터 작성용 스크립트

```shell
python create_dummy_data.py
```

#### DuckDB GUI Client

아래의 GUI 클라이언트를 사용할 수도 있음
[DB Pilot](https://www.dbpilot.io/duckdb)
이용 방법에 관해선 [블로그](https://idenrai.tistory.com/296) 참조

### dbt 와 duckdb 연결

#### profile 수정

dbt project (grocery_mate) 에, 위에서 만든 DB（grocery_mate）를 연결

```shell
vi ~/.dbt/profiles.yml
```

해당하는 dbt project 에 아래의 내용을 입력

```shell
[dbt project name]:
  outputs:
   dev:
     type: duckdb
     path: [duckdb 에서 만든 DB 의 패스]
  target: dev
```

예시)

```shell
grocery_mate:
  outputs:
   dev:
     type: duckdb
     path: /Users/idenrai/project/GroceryMate/dbt/grocery_mate.db
  target: dev
```

### dbt 기동

```shell
dbt run
```
