# Download-Steaming-Videos

## This program is made for educational purposes only


Azure Media Services is a cloud-based platform that allows encoding, storing, streaming, and managing video content. When videos are uploaded to Azure Media Services, each video asset generates a unique URL called an Azure Media link. This link points to the video file hosted on Azure and can be used for streaming or downloading the video.

So in this project, the first step is to programmatically retrieve the Azure Media links for all the videos hosted on a particular website. This involves extracting the links from the website code. Once the Azure Media links have been collected, the next step is to iterate through the list and use each link to download the associated video file to a local drive. This can be done using HTTP download libraries/methods.

This project automates the process of gathering Azure Media links from a website and then downloading all the videos to a local machine. The downloaded videos can then be used for local viewing, processing, archival etc. This avoids having to manually scrape for links and download each video individually.

In summary, the project uses programmatic methods like pyautogui to extract Azure Media links from a website and leverages these links to automate the process of downloading all the videos to a local drive using another set of libraries/methods like subprocess/ffmpeg. 


## Note: This programs' click coordinates may have to be tweaked according to where each button is. 

