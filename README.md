# Xalen Python SDK (legacy snapshot)

This repository is retained as historical source for an early Xalen API client. It is not the current Xalen Python SDK and should not be used for new integrations.

## Package-name warning

Do **not** install `xalen` expecting the API client shown in this repository. The `xalen` name on PyPI now publishes **XALEN Ephemeris**, the shared astronomical calculation engine. The examples and package metadata in this snapshot predate that change and are not valid installation guidance.

The current Xalen client is maintained from Xalen's private product monorepo under the distinct `xalen-sdk` package identity. Public release documentation will be published at [xalen.io/docs](https://xalen.io/docs) when that distribution is available.

## Product boundary

- **Xalen** is the parent company's AI platform.
- **Vedika** is Xalen Technology's astrology intelligence product and has its own API and SDK namespace.
- **XALEN Ephemeris** is a shared calculation engine. It is not the Xalen API client.

For Vedika integrations, use the official packages listed on the [Vedika GitHub profile](https://github.com/vedika-io).

## Status

Historical and unsupported. Issues and pull requests are not accepted here.

## License

MIT
