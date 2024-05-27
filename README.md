# Set up:

- Install docker desktop or rancher desktop
- make sure docker-cli is installed and working
- run `docker-compose build`
- run `docker-compose up`

# Running without docker:

## Back-end:
This is a basic django project set up to handle fetch and creation of getodata and shapes for the map-experiment project.

### Getting Started:

- Setup the latest python.
- Create a python virtual environment.
- Activate the virtual environment.
- in the root directory exectue: `python3 manage.py runserver`
- The url for this server needs to be configured in the FE environment variable.

### Tests:

- To run test execute: `python3 manage.py test`

## map-experiment(Front-end):

First, run the development server:

```bash
npm run dev
# or
yarn dev
# or
pnpm dev
# or
bun dev
```

To run a production build:

First make the build:
```bash
npm run build
```

Then serve the build:
```bash
npm run start
```


Open [http://localhost:3000](http://localhost:3000) with your browser to see the result.

### Running the python server:
The [https://github.com/SrikarVasta/mapbackend](geodata) project needs to be run along with this project.

- Once running set the GEO_DATA_SERVER_URI=[server url] in `.env.local`;

### Genreral info:

- There's no auth implemented so it should work right off the bat.
- Choose the shapes from the side pannel and draw the shape.
- The api calls to the server is made through the nextjs api to keep the potentian auth creds private.
