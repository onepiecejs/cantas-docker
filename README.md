# Docker container of Cantas

Docker container based on the latest development version of Cantasn.

## Make image

    docker build -t [tag-you-prefer] .

## Accepted environment variables

- `AUTH_DEFAULT`: which authentication strategy is preferred to use. local
  would be the most proper one probably.
- `DEFAULT_USERNAME`: username of default user account used when local
  authentication strategy is enabled. Defaults to cantas.
- `DEFAULT_PASSWORD`: password of default user account used when local
  authentication strategy is enabled. Defaults to cantas.
- `REALM`: realm used for constructing user's email. This is useful when
  Kerberos authentication strategy is enabled.

## Dependencies

Both `redis` and `mongodb` should be running before Cantas container is
launched.

## Run

    docker run --name cantas-devel -p 3000:3000 \
           --link redis:redis --link mongo:mongo --rm \
           --env AUTH_DEFAULT=local cantas:devel

This runs Cantas container tagged `cantas:devel` by `local` authentication
strategy is enabled. And anyone is able to login as `cantas:cantas`.

Open your Web browser, then navigate to `http://127.0.0.1:3000/`.
