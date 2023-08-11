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
2. Create a gcs_key.json{} file in airflow and streamlit folder with following variables defined
{
    "type": "service_account",
    "project_id": "projectid",
    "private_key_id": "xxx",
    "private_key": "\n---- PRIVATE KEY-----\n",
    "client_email": "clientname@projectid.iam.gserviceaccount.com",
    "client_id": "000",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/client_email",
    "universe_domain": "googleapis.com"
  }
  
3. Create a kaggle.json{} file in airflow folder with following variables defined
    {"username":"xxx","key":"000"}
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


## References
- [Streamlit](https://streamlit.io/)
- [Snowflake SQLAlchemy](https://docs.snowflake.com/en/user-guide/sqlalchemy)


## Team
| Contributor    | Contibutions |
| -------- | ------- |
| Ashritha Goramane  |  |
| Parvati Sohani     |	|
| Rishabh Indoria    | 	|

Guided by: Prof. Srikanth Krishnamurthy
Supported by: [Piyush](https://github.com/piyush-an)
