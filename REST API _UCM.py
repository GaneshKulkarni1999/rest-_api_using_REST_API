#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
import json

# Prepare the data
data = {
    "OperationName": "uploadFileToUCM",
    "DocumentContent": "UEsDBBQAAAAIAGB6I1mmq8t32wsAAMI6AAAiAAAAUHVyY2hhc2VPcmRlclJlcXVpc2l0aW9uX1BPUkVDLmNzds2bbW/byBHH3xfodyDyqgUYZWef9+VaoiXGFKkjKV98bwwjddEA1xyQc69fvzNcPkgr5+wLGfQcJFjSsvnb4czsf2Y3eZvt70u/z9Kq3voy/8m3eVXer6tNljb1fV42rS/XWX/jeDgUeVYPP7DBYXt3yNLrvN7fHwpfltkm3Bk/2uRt/9OHY73e3Rd5md2Xx33/4zi6yuq0zm7zBh+cltmP9+E7Pxx92ebtXXq1b++vC7/FD/1wzJoWH9Hs8sP9xrf4S+tqnzdnt9a+rkfIPT75vrq+b2tfNoeqbtMmq29znFGR3WZF2v3YPmt31Sbd1NWh/z34mDCP6d76iPe63xndm2bYrHfZ5lhk0yQ3WZHfZvXd/aHGZ57MYPzG+SzObzfHq7y8zcq2wjvdE/D7Gf14Zw/ftnV+daSn73wN0TWPrkV0LaNrFV3r6NpE1za6djEPi2/EhBAjQswIMSTElBBjQswJMSjEpPyUNDgkXNzhF3fExR15cUdd3NEXd8zFHXtxx13cOTMveQtE1zy6FtG1jK5VdK2jaxNd2+jaRdeXgDEhxIgQM0IMCTElxJgQc0IMCjEpvv9tUV354v7CyPDV7/A0KzeUWbpYz8vNX4AxAGVSxXCih3XqPz49/Pbp1yT//PT45fPD06dfPj/8nBRP/0htevf4a7pv3w4fwZurFFLNOJNaujTlDoRIy1/S8MXxr5JaWWXxgoF9x+Q7fEwYmnc46enDf+wLZ/FXQpf495vRRUB3DvHAWHxL5+jWguWmRwcY0XGIr3gmOv7B547ohyJp/vvpn09J8/jlt08fH39N/rZ/+Pnp4e8BNUxg/FRvdSEkoktpYnKttWNiMLqYjO7e4Sz/PORCG/ccuvpu6BJ/yTx0UAxBhY640SbOuYEbPYSNLs9n+zlx65nchll0WnuObYyVkubD8ROduVU/1MtgazkTW2lGnoLZ7hzccW5VBw6OwGEAJ69ZAtx8M3ifV5jRBK4icg1WW3oVwT10IKdJ8EU83KBVBvJ9tsmbJNtdD5DCKaXFkLRBM8x8Mo5BDU4KOcagPSN08wmtZd9sW9XbVgJyumix0coBlycZewRHb14gYzv57U7Rm1wYBIfYmYUTGv2k52ZTFKLB7QLcZorC7apYJQfUj3ufbPdXux50W7w9/Ovhy78f3vp2SBjckXswKSNaXM+VtumEONCaJWgBOJ9pZcM0xReCxnbWCoQayGEi5wg/j5wbtLJD/9B/hBwLrL2v71Ja5FCIKXJrLgWm3jNwXFqEMgEcOm9W4xCdaRa4oOdiWH8rOGjLQNNiobiMHFsabjSETGIIVrAwBPQamMmNwpKh9h64j2Xe7rI68fs8K5seM7rZm9nSiqdcTOuE4MLYwcooOMQ45HOt7NDORtcj7pvt4+fHLyhFrynqPj7+5+nTx4c0aVZ+9WaIyazMaszf1xSsxE5anSnMwJjGY3aNoYOihIB55888sKOl2cygXAO3BgxL14fAvsn7BHJd+3KNhM2qxrTSY+etLzqPBsnR3JxywopFoQiIKThnA7AMrkFD9Y7rmcCSkh6VcnDogA+1/+DzOsGCJ/fJ4bZdJUW7GYB3d5us9ld+Q94swXHDKUlIoVaRyjPKcZhSX+/PNESVN3NlXAZacXEBjSnRGf4MtJotlS6g87L6kBD1oa42x3XbjODPcnOSWpTYdFw4GqslN3IIRhMEdb/KLGZqPsPUgsULowHuxHOG1rOXlwvkrCiy8qprGhL2scFK3xfJ1jdZc2Lu936zxgRY+N7cXBlUX6nm0QKjjKBFoLc2RqGehktZO/s2H0GDy65cBI25M3JtTDICnnft/zN259r2Ode2qFAEH1dz9U5AoEblt1jqm0sNoKOywIGVXJxEZMCGruSaqa4Xw9YuCkqHqgQ0XFKH8mBZ6m8KSvRvq7G8p15Z7N7grDWDe8vv6t7z2LmJ87fmGLbPs8+Vfsuwdz7TlbkQpRUKUMnGABULB6hgxvKRHfVp4svNrvZJc9z6GoHzfd5mA3Try+PNEQtfsjaGIOk/yeIKkjNBvzQN5a4lNdINUf7Nla4j8Y0IxO/9XbOrsyxBY+7ztS9i5ApVa9M7CGAtZoFWy3NiobUMCw6E5V30Q9Ta80XJHGAsZqgvEgNjiSNkqNE51Y7M9UOxhPQTwPGBNzoAb7Ls4G+wTM/KqsjXMe6t31QbX/duDAhG/ejLksCh/B7ydXCEYSjmR6DA2MEn9l785pBXZYaV1mDiMQ6zLnUHPTVUNrc5vhL/o99MWaTrQiprVo6+FI/92ygh3ZBN4B2343CBbIIaAl/trp9Ls8tvfJKVbVZjmYsppKdusvWxPFMmAhyDLsfFAQkSVUtXzWNZ1hlfjcO5mwcErLAkG0V3kd16snuyriJPWe/y0ie7qtwmN/hPoEZbA+UKQEOvXGRpbbEMtmLIJEPJ7rrAnA+uGMbmCF4j8o+70Sl+8gMhYJnVMZzDKWmcYUODD7NGCMJuyOe7wavgqH9hSL3pqKS1DANOjT7qeg3dDedudU1w/CU4JRRZLm59OdQSfbndNclDbyMMl4K7fgEOMMk5fZlaHcmcab3Fd8knZTm3eTHA3bz0WtHtKTJBxu9VUdU/toV42JLqh/MVJNLJic4XN3cFtatKzJtfW672x/2Vz0OoGGr74AuXNu69cTRr6FWc995C+3ABbDtht8k2uU2a2vt1xHpzrMuqKnoHEEaTJhRyZViUeABzqOYs2Dksq3oazl9hFYMTOzc71FyUFndHXxzf4kK7beifaf1aV6tJOXZ5dCihUSKIy+XWagus78B1vhGWqE4/zu3Rfgd8KVf2cgLW2j/7BIBLS4IS3AqXiSiROGZBy8GFhinwfiN5gSmoaQrvj1d54csWlc6WToL5yPMPxzIbkC1QklVo85jY4GpszEDcHzIIw7kbsBfEhf+wz5NwZG59KtBOml21z7dDUU2ChSDcBTYGq2O9TAjt29HSkrL3Atz2xZUYjOBUCaUXJzeoTy7G8w98OkQgluh4Brihfuu1+nVWt3mBahELOHTt5JC1dTUl8HVVH6q6O6b4NTcBi8YObaFIkoE00BXZ/V53V46G/Vi2lK3zpadD1ZymoDNxrYqJhoVaNbRzh+qaFv5F8szJwrTcdIA70538wLUrimGrOdfj3gtMscCX0VZYXrwUC/gRY7R7xtq0ZyFGVaqnPrpeRjK/Cg4D1bjLjW/aR1bhLETorpxKqyWEXwf3+6oUFRS6KXU8Y1kquRXKniioTtD3CmqJNPIKutF07tJ00o4ndyLTze9RBbgXBT1XBqtyluqL3oNUxg37Cee9h0VinOh2v+91tHYxag5I5aJWNmiDK0dYIGSnL1k/lEvs1AS8/MWg6A7S0bZu9GotN6ZfW1nXremNh3SL5ZMXyiHgzFg6q2Iv6NCmNjQ2eFegwTRcQqW/Ag4tpkS38MOlinUCE/XJ5srgeTRcYrF8FR9XmrYIVyyucpzh+B0zBcaJ3lugkfVqPEMJTKOwi7dLDJPUiZz4xMi3wCYP8slXLBccxVDXmI9Lce6UMUMXg7rFahwuk1a+RndaclvmNDVQdRwaSjimx/NntEqwabhITpavWDB648Up2XLthOTP2g4WCQw5ieLt8b1HPZVcF8fqVGhNFd3G77L3CNZ1f4VW1HmJWxiGOpTh5ELYyhiEL8w/iBiQzYvOSG9b0kE4FRcZuCyDPD3HuWgvUtMxsDGSX2vPqWwjtYU1vokPKndHRI0ba+STgzfzTyqvK7+vqJGDftWmCvNt19P6oyfKsHzTlGzQNViktRWo8USZHevlcM4aZmqyzbGoPjBUg4zb9Rx6fAOd2DXx+VQhQevBZVCzgQ3+TLJjZkuuQMu3jB7O5pleAB2BizdgKOexcDYu7AWwoWibvy1A/6etZRyrdjUPnXP+NbtLzcV3sXtV+PInRuhmHryQVL6BiwPWOq4ZP9lIH4W+mp1nDr5sK3IZmOk0ILtdGaNltJWuQAobsg0d+2Sn8TpXLh7yQ+ulohOdPJ9Fr+lMFBZa8XIu7bCpfv5/UfTsXPM/UEsBAhQAFAAAAAgAYHojWaary3fbCwAAwjoAACIAAAAAAAAAAQAAAAAAAAAAAFB1cmNoYXNlT3JkZXJSZXF1aXNpdGlvbl9QT1JFQy5jc3ZQSwUGAAAAAAEAAQBQAAAAGwwAAAAA",
    "DocumentAccount": "scm$/planningDataLoader$/import$",
    "ContentType": "zip",
    "FileName": "validate.zip",
    "DocumentId": None
}

# Specify the API endpoint URL
url = "https://elbq-dev2.fa.us2.oraclecloud.com/fscmRestApi/resources/11.13.18.05/erpintegrations"

# Convert the data to JSON format
json_data = json.dumps(data)

# Set your authentication credentials (if required)
# Replace 'your_username' and 'your_password' with your actual credentials
auth = ('mfg_portal', 'Oracle@123')  # Use appropriate auth method

# Send the request
response = requests.post(url, headers={'Content-Type': 'application/json'}, data=json_data, auth=auth)

# Check the response
if response.status_code == 200:
    print("File uploaded successfully.")
else:
    print(f"Failed to upload file: {response.status_code} - {response.text}")


# ##SubmitESSJobRequest Operation

# In[3]:


import requests
import json

# Prepare the data
data = {
    "OperationName": "submitESSJobRequest",
    "JobPackageName": "/oracle/apps/ess/scm/advancedPlanning/collection/configuration/",
    "JobDefName": "CSVController",
    "ESSParameters": "OPS ,2,validate.zip,UCMFA02730766 ,2737760 ,300000000234546 ,2,2,#NULL,2,2,0,0"
}

# Specify the API endpoint URL
url = "https://elbq-dev2.fa.us2.oraclecloud.com/fscmRestApi/resources/11.13.18.05/erpintegrations"  # Adjust as needed

# Convert the data to JSON format
json_data = json.dumps(data)

# Set your authentication credentials (if required)
# Replace 'your_username' and 'your_password' with your actual credentials
auth = ('mfg_portal', 'Oracle@123')  # Use appropriate auth method

# Send the request
response = requests.post(url, headers={'Content-Type': 'application/json'}, data=json_data, auth=auth)

# Check the response
if response.status_code == 200:
    print("ESS job submitted successfully.")
    print("Response:", response.json())  # Print the response from the API
else:
    print(f"Failed to submit ESS job: {response.status_code} - {response.text}")


# In[ ]:


##ImportBulkData Operation


# In[9]:


import requests
import json

# Prepare the data
data = {
    "OperationName": "importBulkData",
    "DocumentContent": "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",
    "ContentType": "zip",
    "FileName": "validate.zip",
    "DocumentAccount": "scm$/planningDataLoader$/import$",
    "JobName": "/oracle/apps/ess/scm/advancedPlanning/collection/configuration/",
    "ParameterList": "OPS, 2, validate.zip, UCMFA02729990, 2736984, 300000000234546, 2",
    "JobDefName": "CSVController",
    "CallbackURL": "#NULL",
    "NotificationCode": "10",
    "JobOptions": "#NULL"
}

# Specify the API endpoint URL
url = "https://elbq-dev2.fa.us2.oraclecloud.com/fscmRestApi/resources/11.13.18.05/erpintegrations"  # Adjust as needed

# Convert the data to JSON format
json_data = json.dumps(data)

# Set your authentication credentials (if required)
# Replace 'your_username' and 'your_password' with your actual credentials
auth = ('mfg_portal', 'Oracle@123')  # Use appropriate auth method

# Send the request
response = requests.post(url, headers={'Content-Type': 'application/json'}, data=json_data, auth=auth)

# Check the response
if response.status_code == 200:
    print("Bulk data import submitted successfully.")
    print("Response:", response.json())  # Print the response from the API
else:
    print(f"Failed to import bulk data: {response.status_code} - {response.text}")


# In[ ]:




