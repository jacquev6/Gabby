*Gabby* is a tool to generate digital versions of grammar exercices found in school books.
It's part of the MALIN project.

*Gabby* is still in the early days of its development.

# Hosted demo

The development version of *Gabby* is running at https://gabby.vincent-jacques.net/.

# Run locally

You only need a recent version of [Docker](https://www.docker.com/) and a not ancient version of Bash to run:

    dev-env/run.sh

And then open your browser at http://localhost:8080/.
Hit Ctrl+C to stop the development environment.

# Run shells in the development environment

    dev-env/frontend/shell.sh
    dev-env/backend/shell.sh
    dev-env/db/shell.sh

# Run tests

With the development environment running:

    dev-env/frontend/shell.sh -c 'npm run test:unit'  # Component tests
    dev-env/frontend/shell.sh -c 'npm run test:e2e'  # End-to-end tests on development server

# Build Docker images for production

    prod/build.sh

(That command will push to hub.docker.com as @jacquev6, so it will fail if ran by anyone else than Vincent Jacques)
