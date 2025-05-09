<h1>Fetch Weather Data From <a href="https://openweathermap.org/">OpenWeatherMapAPI</a>, Automate it to Run Daily With Github Actions, and uploads them as a CSV file to a specified Google Drive folder — using a service account</h1>

<h2>Description</h2>
This project automates the process of collecting 5-day weather forecasts in London, schedule the script to run at 6am UTC every day, and storing weather data into csv in Google Drive.
<br />

<h2>Languages and Utilities Used</h2>

- <b>python</b>
- <b>web scrapping</b>
- <b>requests</b>
- <b><a href="https://openweathermap.org/">openweathermapAPI</a></b>
- <b>ETL</b>
- <b>pandas</b>
- <b>Google Drive API</b>

<h2>How to obtain openweathermap API Key:</h2>

<p align="center">
<br />
You have to sign in to <a href="https://openweathermap.org/">openweathermapAPI</a>, then navigate to My API Keys<br/>
<img src="https://i.imgur.com/WGDsGwV.jpeg" height="70%" width="70%" alt="MyAPIKeys"/>
<br />
<br />
Copy the API Key<br/>
<img src="https://i.imgur.com/b0ullLH.jpeg" height="70%" width="70%" alt="CopytheAPIKey"/>
<br />
<br />
Then paste the API KEY into repository secret in Settings > Secrets and Variables > Actions > Click on New Repository Secret<br/>
<br />
 
<h2>Setting up Service Account API</h2>

<br />1. Go to <a href="https://console.cloud.google.com/">Google Cloud Console</a><br/>
<br />2. Select your project (or create a new one)<br/>
<br />3. In the left sidebar:<br/>
   - <b>Go to IAM & Admin → Service Accounts<br/>
   
<br />4. Click Create Service Account<br/>
   - <b>Name it gdrive-uploader or similar</b>
   - <b>Click Create and Continue</b>
   - <b>Skip permissions → Done<br/>
   
<br />5. In the service account list:<br/>
   - <b>Click your new service account</b>
   - <b>Go to the “Keys” tab</b>
   - <b>Click “Add Key” → “Create new key” → JSON<br/>

<br />Then, Copy the entire JSON file content.<br/>

<br />1. Go to GitHub repo → Settings → Secrets → Actions<br/>
<br />2. Add a new secret:<br/>
   - <b>Name: GDRIVE_CREDS_JSON</b>
   - <b>Value: paste the full JSON (no formatting or quotes)<br/>
   
<br />4. Click Save<br/>

<h2>Setting Google Drive</h2>

<br />1. Open <a href="https://drive.google.com/">Google Drive</a><br/>
   - <b>Create a new folder (or use an existing one)</b>
   
<br />2. Find the Service Account Email<br/>
   - <b>Open the service_account.json file you downloaded earlier<br/>
   - <b>Look for the line:<br/>
   <p align="center">
   <b>"client_email": "something@your-project.iam.gserviceaccount.com"<br/>

   - <b>Copy that email address (this is your service account’s identity)<br/>
   
<br />3. Share the Folder<br/>
   - <b>In Google Drive, right-click the folder → Click Share</b>
   - <b>In the “Add people and groups” box</b>
   - <b>Paste the service account’s email</b>
   - <b>Set Editor as the permission<br/>
   - <b>Click Send</b>

<h2>Output:</h2>

<p align="center">
<br />
The CSV file will be in a folder created in Google Drive<br/>
<br />
<img src="https://i.imgur.com/r6YtGdH.png" height="90%" width="90%" alt="ActionsTabs">
<br />
<br />
Here is the Example of the output in csv format<br/>
<br />
<img src="https://i.imgur.com/IaUPrPB.png" height="80%" width="80%" alt="CSVOutput">
<br />


<!--
 ```diff
- text in red
+ text in green
! text in orange
# text in gray
@@ text in purple (and bold)@@
```
--!>
