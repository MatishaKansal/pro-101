import dropbox;
import os;
from dropbox.files import WriteMode

class TransferData:

    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, files_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)
        # local_path = os.getcwd()
        for root, dirs, files in os.walk(files_from):
            for name in files:
                local_path = os.path.join(root, name)
                relative_path = os.path.relpath(local_path, files_from)
                dropbox_path = os.path.join(file_to, relative_path)
        
                with open(local_path, 'rb') as f:
                    dbx.files_upload(f.read(), dropbox_path, mode=WriteMode('overwrite'))

def main() :
        access_token = "sl.AzfvW3oFYYtZj5L72zCzhq-rp6pWQAyzpbALI5F98BbVzHnYbIWBejZxaINh0_QJG_5DCRs9Tdo5-JG_1LBvIXYhsz22uQfuxZhfsUUbUFtA8kZCFZq-ArF1ARIFiSkHM9Zk45o"
        transferData = TransferData(access_token)
        files_from = str(input("Location of the file  "))
        # file_name =  input("Name of the file  ")
        file_to = input("Enter the full path to upload to dropbox")
        transferData.upload_file(files_from, file_to)
        print("File has been moved")
    
main()

# data = TransferData("sl.AzfvW3oFYYtZj5L72zCzhq-rp6pWQAyzpbALI5F98BbVzHnYbIWBejZxaINh0_QJG_5DCRs9Tdo5-JG_1LBvIXYhsz22uQfuxZhfsUUbUFtA8kZCFZq-ArF1ARIFiSkHM9Zk45o")
# data.main()
