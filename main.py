import pypff

pst = pypff.file()
pst.open("<file>.pst")

root = pst.get_root_folder()
def parse_folder(base):
    messages = []
    for folder in base.sub_folders:
        
        if folder.number_of_sub_folders:
            messages += parse_folder(folder)
        if folder.name in ["my_folder_name"]:
            for message in folder.sub_messages:
                with open(f'{message.subject.replace("/", "-")}.txt', 'w') as f:
                    f.write(message.plain_text_body.decode("utf-8") )
    return messages

messages = parse_folder(root)
