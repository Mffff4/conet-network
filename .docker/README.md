# Conet Network Automation

![Conet Network Automation](https://raw.githubusercontent.com/Mffff4/conet-network/main/.docker/logo.png)

**Automated wallet recovery and mining setup for Conet Network**

[![Docker Pulls](https://img.shields.io/docker/pulls/mffff4/conet-node)](https://hub.docker.com/r/mffff4/conet-node)
[![License](https://img.shields.io/badge/license-BSD%203--Clause-blue.svg)](https://github.com/Mffff4/conet-network/blob/main/LICENSE)
[![Telegram](https://img.shields.io/badge/Telegram-Join%20Chat-blue?logo=telegram)](https://t.me/+rq804XYKgjFkYjIy)

## Quick Start

```bash
docker run -it --rm \
    --name conet-miner \
    mffff4/conet-node:latest \
    --seed-phrase "your twelve word seed phrase here" \
    --password "your-secure-password" \
    --keep-open
```

## Features

- One-Click Wallet Recovery
- Automated Mining Setup
- Real-Time Balance Monitoring
- Enhanced Security
- Proxy Support (SOCKS5/HTTP)
- Random User Agent Rotation

## Command Line Options

| Option | Description | Required |
|--------|-------------|----------|
| `--seed-phrase` | Your 12-word recovery phrase | Yes |
| `--password` | Wallet password | Yes |
| `--keep-open` | Keep browser running | Yes |
| `--proxy` | SOCKS5 or HTTP proxy URL | No |
| `--debug` | Enable detailed logging | No |

## Proxy Examples

### SOCKS5 Proxy
```bash
docker run -it --rm \
    --name conet-miner \
    mffff4/conet-node:latest \
    --seed-phrase "your seed phrase" \
    --password "your-password" \
    --proxy "socks5://username:password@proxy.example.com:1080" \
    --keep-open
```

### HTTP Proxy
```bash
docker run -it --rm \
    --name conet-miner \
    mffff4/conet-node:latest \
    --seed-phrase "your seed phrase" \
    --password "your-password" \
    --proxy "http://username:password@proxy.example.com:8080" \
    --keep-open
```

## Support

Join our [Telegram community](https://t.me/+rq804XYKgjFkYjIy) for support and updates.

## License

BSD 3-Clause License

---

Made with ❤️ for Mffff4