*Gabby* is a tool to generate digital versions of grammar exercices found in school books.
It's part of the MALIN project.

*Gabby* is still in the early days of its development.

# Hosted demo

The development version of *Gabby* is running at https://gabby.vincent-jacques.net/.

# Run locally

You only need a recent version of [Docker](https://www.docker.com/) and a not ancient version of Bash to run:

    dev-env/run.sh

And then open your browser at http://localhost:8080/.

# Run tests

With the development environment running:

    dev-env/frontend/shell.sh -c 'npm run test:unit'  # Component tests
    dev-env/frontend/shell.sh -c 'npm run test:e2e'  # End-to-end tests on development server
