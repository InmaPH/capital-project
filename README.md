# capital-project

![Capital Expenses - Dummy Data](https://github.com/user-attachments/assets/7de42583-df8f-49f6-80e8-eabfdaaaab21)

**OBJECTIVE**
This dashboard is a template for a business case focused on global capital management, making it relevant to companies worldwide. In real-world scenarios, such data is typically available for extraction and transformation within business environments but is not freely accessible for public use. To simulate this business problem, I developed a testing dataset using dummy data. This way, we can closely resemble the information companies typically handle within their FinOps operations. In addition, the use of faker can provide with a methodology to anonimize company data or create datasets for testing scenarios.

**INSTRUCTIONS**

Packages used: Faker, pandas

1) Create dataset.

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

3) The dashboard will be available to you. Enjoy! Feel free to reach out if you have any questions.
