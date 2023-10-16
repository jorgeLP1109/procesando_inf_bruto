import requests

def descargar_csv_desde_url(url, nombre_archivo):
    try:
        
        response = requests.get(url)
       
        if response.status_code == 200:
            
            with open(nombre_archivo, 'wb') as archivo:
                archivo.write(response.content)
            print(f'Los datos se han descargado con éxito en "{nombre_archivo}"')
        else:
            print(f'Error al descargar los datos. Código de respuesta: {response.status_code}')
    except Exception as e:
        print(f'Error: {str(e)}')

descargar_csv_desde_url("https://huggingface.co/datasets/mstz/heart_failure/raw/main/heart_failure_clinical_records_dataset.csv", "heart_failure_dataset.csv")
