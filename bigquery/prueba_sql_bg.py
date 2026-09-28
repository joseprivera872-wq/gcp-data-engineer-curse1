import os
from google.cloud import bigquery

def query_public_dataset():
    # 1. Definimos la ruta al archivo JSON que descargaste de GCP
    # Si lo pusiste en la misma carpeta que este script, solo pon su nombre:
    nombre_archivo_json = "sa-test-bq01.json" 
    
    # Conseguimos la ruta absoluta de forma segura
    ruta_credenciales = os.path.join(os.path.dirname(__file__), nombre_archivo_json)
    
    # 2. Inicializamos el cliente cargando directamente el archivo de credenciales
    client = bigquery.Client.from_service_account_json(ruta_credenciales)

    query = """
    SELECT order_items.id, order_id, product_id, products.name
    FROM `bigquery-public-data.thelook_ecommerce.order_items` AS order_items
    JOIN `bigquery-public-data.thelook_ecommerce.products` AS products
    ON order_items.product_id = products.id
    LIMIT 5
    """

    print("Enviando consulta a BigQuery usando cuenta de servicio...")
    results = client.query(query).result()
    
    print("\n--- RESULTADOS ---")
    for row in results:
        print(f"ID: {row.id} | Order ID: {row.order_id} | Product ID: {row.product_id} | Name: {row.name}")

if __name__ == "__main__":
    query_public_dataset()
