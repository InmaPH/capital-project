# capital-project

![Capital Expenses - Dummy Data](https://github.com/user-attachments/assets/7de42583-df8f-49f6-80e8-eabfdaaaab21)

Packages used: Faker, pandas

1) Create dataset.
Usually in a business setting this data is available for extraction and transformation. However, since this project is just a showcase, I'll be using dummy data that would be similar to what companies have available in their FinOps environment.

Faker is a Python library that allows us to create random data points that can be stored into a dataset. For more information on Faker, access the official documentation at https://faker.readthedocs.io/en/master/index.html.
The script to generate the data can be found in DummyData.py. **Don't edit** the script if you want to use the PowerBI template as the CSV won't work as a data source with different or new columns. 
Once the data is generated, the results should look like dummy_data.csv

2) Connect to the dataset.
When the PowerBI file is downloaded, **keep in mind to change the filepath** from "Data Source Settings" to point to the CSV location.
For this particular case, I'll be using:

       - 'First Name'
       - 'Last Name'
       - 'Email'
       - 'Phone Number'
       - 'Location'
       - 'Profession'
       - 'Company'
       - 'Date'

3) Enjoy! Feel free to reach out if you have any questions.
