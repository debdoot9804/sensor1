
import subprocess


# MongoDB Atlas connection string and CSV file location
atlas_connection_string = "mongodb://DEBDOOT:DEB9804@cluster0-shard-00-00.qicpj.mongodb.net:27017,cluster0-shard-00-01.qicpj.mongodb.net:27017,cluster0-shard-00-02.qicpj.mongodb.net:27017/?ssl=true&replicaSet=atlas-14iia8-shard-0&authSource=admin&retryWrites=true&w=majority&appName=Cluster0"

csv_file_path = "aps_failure_training_set1.csv"
collection_name = "sensor"

# Create the mongoimport command
command = [
    "mongoimport",
    "--uri", atlas_connection_string,
    "--collection", collection_name,
    "--type", "csv",
    "--file", csv_file_path,
    "--headerline"
]

# Run the command
subprocess.run(command, check=True)
