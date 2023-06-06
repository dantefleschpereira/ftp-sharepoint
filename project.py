from sharepoint import SharePoint

#i.e - file_dir_path = r'C:\project\report.pdf'
file_dir_path = "/home/dante/projetos/ftp-sharepoint/RREO.pdf"

# this will be the file name that it will be saved in SharePoint as 
file_name = 'RREO.pdf'

# The folder in SharePoint that it will be saved under
folder_name = 'Teste'

# upload file
SharePoint().upload_file(file_dir_path, file_name, folder_name)

# delete file
SharePoint().delete_file(file_name, folder_name)