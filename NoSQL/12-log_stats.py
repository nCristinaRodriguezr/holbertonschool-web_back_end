#!/usr/bin/env python3
"""
a Python script that provides some stats about Nginx logs stored in MongoDB
"""


from pymongo import MongoClient


def nginx_stats():
    # Conexión a la base de datos logs y la colección nginx
    client = MongoClient('mongodb://127.0.0.1:27017')
    db = client.logs
    collection = db.nginx

    # Contar el número total de documentos en la colección
    total_logs = collection.count_documents({})
    print(f"{total_logs} logs")

    # Contar el número de documentos para cada método HTTP
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for method in methods:
        count = collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    # Contar el número de documentos con el método GET y path /status
    status_check = collection.count_documents(
        {"method": "GET",
         "path": "/status"}
    )
    print(f"{status_check} status check")


if __name__ == "__main__":
    nginx_stats()
