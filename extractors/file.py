def save_to_file(file_name, jobs):
    
    file = open(f"{file_name}.csv", "w")
    file.write("title,company,kind,region\n")

    for job in jobs:
        print(job)
        file.write(f"{job['title']},{job['company']},{job['kind']},{job['region']}\n")
    file.close()
