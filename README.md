# Assignment4

## Technical stack
![Codelabs](https://img.shields.io/badge/Codelabs-violet?style=for-the-badge)
![GCP provider](https://img.shields.io/badge/GCP-orange?style=for-the-badge&logo=google-cloud&color=orange)
[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/)
[![Python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)](https://streamlit.io/)

## Link to the Live Applications
* [Streamlit](http://34.136.31.176:8090/)
* [Codelabs](https://codelabs-preview.appspot.com/?file_id=1lap9Vb67gt5LqbizQqg99aGZz84vDvcE3179fATSm3M#0)


## Running the application
### Pre-requisites
- [Docker Engine](https://docs.docker.com/engine/install/)
- [Docker compose](https://docs.docker.com/compose/install/)

### Steps to run application locally
1. Clone the repository
    ```bash
        git clone https://github.com/BigDataIA-Summer2023-Team2/Assignment3.git
    ```
2. Create an .streamlit/secrets.toml file in streamlit folder with following variables defined
    ```bash
        [connections.snowpark]
        account="xxx"
        user="xxx"
        password="xxx"
        role = "xxx"
        warehouse = "xxx"
        database = "xxx"
        schema = "xxx"
        client_session_keep_alive = true
    ```
3. Create a credentials.yaml file in streamlit folder with following information for predefined users to access your application
    ```yaml
        credentials:
        usernames:
            jsmith:
                email: jsmith@gmail.com
                name: John Smith
                password: xxx # hash_password
            rbriggs:
                email: rbriggs@gmail.com
                name: Rebecca Briggs
                password: xxx # hash_password
        cookie:
            expiry_days: 30
            key: random_signature_key # Must be string
            name: random_cookie_name
        preauthorized:
            emails:
            - melsby@gmail.com

    ```
4. Run the make command to build and deploy the application
    ```bash
        make build-up
    ```
5. Applciation would be accessible on localhost at following URLs \
    **Streamlit:** http://localhost:8090/ \
6. Destroying the deployed environment
    ```bash
        make down
    ```
## Project Tree

```
.
├── Makefile
├── README.md
├── docker-compose-local.yml
├── streamlit
│   ├── Dockerfile
│   ├── Home.py
│   ├── pages
│   │   ├── 1_Query_7.py
│   │   └── 2_Query_8.py
│   ├── requirements.txt
│   └── utils
│       ├── generic.py
│       ├── query_7.py
│       └── query_8.py
└── terraform
    ├── main.tf
    ├── resources.tf
    ├── startup.sh
    ├── terraform.tfvars.example
    └── variables.tf
```

## References
- [Streamlit](https://streamlit.io/)
- [Snowflake](https://docs.snowflake.com/en/learn-quickstarts)
- [Snowflake SQLAlchemy](https://docs.snowflake.com/en/user-guide/sqlalchemy)
- [TPC-DS](https://www.tpc.org/tpc_documents_current_versions/pdf/tpc-ds_v2.5.0.pdf)
- [TPC-DSQuery-Github](https://github.com/gregrahn/tpcds-kit/tree/master)


## Team
| Contributor    | Contibutions |
| -------- | ------- |
| Ashritha Goramane  | Query7, Query8, IaC  |
| Parvati Sohani     | Query9, Query10		|
| Rishabh Indoria    | Query11, Query12		|

Guided by: Prof. Srikanth Krishnamurthy
Supported by: [Piyush](https://github.com/piyush-an)
