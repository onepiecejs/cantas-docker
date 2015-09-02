# Docker container of Cantas

Docker container based on the latest development version of Cantas.

## Make image

    docker build -t [tag-you-prefer] .

## Environment Variables

- `AUTH_DEFAULT`: Preferred authentication strategy. The best default
  choice is probably `local`.
- `DEFAULT_USERNAME`: The username to use with the local authentication
  strategy. Defaults to `cantas`.
- `DEFAULT_PASSWORD`: The password to use with the local authentication
  strategy. Defaults to cantas.
- `REALM`: The realm used for constructing the user's email. This is useful
  when the Kerberos authentication strategy is selected.

## Dependencies

Both `redis` and `mongodb` should be running before the Cantas container is
launched.

## Run

You can use the `run` script in this directory to start the Cantas container.
The script expects the tag for your cantas container as its only argument.

    ./run <tag>

Alternately, you can manually execute the docker command as follows:

    docker run --name cantas-devel -p 3000:3000 \
           --link redis:redis --link mongo:mongo --rm \
           --env AUTH_DEFAULT=local cantas:devel

In both cases, this runs Cantas container tagged `cantas-devel` with the `local`
authentication strategy enabled. Anyone is able to login as `cantas` with the
password `cantas`.

Access it in your Web browser at `http://127.0.0.1:3000/`.
