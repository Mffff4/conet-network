# Conet Network Automation

**Automated wallet recovery and mining setup for Conet Network**

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

For support and updates join our Telegram: https://t.me/+rq804XYKgjFkYjIy

## License

BSD 3-Clause License