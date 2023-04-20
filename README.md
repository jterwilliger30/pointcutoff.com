<h1>www.pointcutoff.com</h1>

# Summary
This project was done as a favor to a friend. Apparently, the US Army uses a point system when considering enlisted soldiers for promotion to E-5/Sergeant and E-6/Staff Sergeant. In order to be eligible for promotion, you must meet a minimum point threshold specific to your MOS. These thresholds change monthly, and are published in PDF memorandums by U.S. ARMY HUMAN RESOURCES COMMAND.

# Setup
Download the prerequisites: python3 (flask, pdfminer.six), npm, yarn, and react. Run npm install to download the required node_modules. Then run 'yarn start' in the root directory, which will begin serving the frontend on port 3000. With another daemon run 'python3 -m flask run -p 5001' in the /api directory, which will begin serving the backend on port 5000. The frontend will automatically proxy api requests to port 5000.
Proxy nginx requests from port 80 to port 3000.

N.B.: Make sure the 'proxy' attribute in package.json is pointing to port 5000. If you are on a Mac, you may need to change this and the port flask runs on, since some versions of MacOS reserve port 5000 for some OS-specific function. (UPDATE: I have changed the frontend to proxy requests to 5001, not 5000. Configure flask accordingly)

# Current Version
A Flask backend that web scrapes the PDFs, organizes them by month, and parses the needed data from them. React front end. Nginx proxy server redirecting to Flask and React on localhost.

# V2.0
Flask backend, hand-written html.

# V1.0
Eel webserver, hand-written html.
