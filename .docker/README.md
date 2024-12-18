# 🚀 Conet Network Automation

<div align="center">
  <img src="https://raw.githubusercontent.com/Mffff4/conet-network/main/.docker/logo.png" alt="Conet Network Automation" width="200"/>
  <br>
  <strong>Automated wallet recovery and mining setup for Conet Network</strong>
  <br>
  <br>

  [![Docker Pulls](https://img.shields.io/docker/pulls/mffff4/conet-node)](https://hub.docker.com/r/mffff4/conet-node)
  [![License](https://img.shields.io/badge/license-BSD%203--Clause-blue.svg)](https://github.com/Mffff4/conet-network/blob/main/LICENSE)
  [![Telegram](https://img.shields.io/badge/Telegram-Join%20Chat-blue?logo=telegram)](https://t.me/+rq804XYKgjFkYjIy)
</div>

## 🚀 Quick Start

```bash
docker run -it --rm \
    --name conet-miner \
    mffff4/conet-node:latest \
    --seed-phrase "your twelve word seed phrase here" \
    --password "your-secure-password" \
    --keep-open
```

## 🎮 Features

- 🔐 **One-Click Wallet Recovery**
- ⚡ **Automated Mining Setup**
- 📊 **Real-Time Balance Monitoring**
- 🛡️ **Enhanced Security**
- 🌐 **Proxy Support (SOCKS5/HTTP)**
- 🤖 **Random User Agent Rotation**

## 📝 Command Line Options

| Option | Description | Required |
|--------|-------------|----------|
| `--seed-phrase` | Your 12-word recovery phrase | ✅ |
| `--password` | Wallet password | ✅ |
| `--keep-open` | Keep browser running | ✅ |
| `--proxy` | SOCKS5 or HTTP proxy URL | ❌ |
| `--debug` | Enable detailed logging | ❌ |

## 🌐 Proxy Examples

### SOCKS5
```bash
# With authentication
docker run -it --rm \
    --name conet-miner-1 \
    mffff4/conet-node:latest \
    --seed-phrase "your seed phrase" \
    --password "your-password" \
    --proxy "socks5://username:password@proxy.example.com:1080" \
    --keep-open

# Without authentication
docker run -it --rm \
    --name conet-miner-2 \
    mffff4/conet-node:latest \
    --seed-phrase "your seed phrase" \
    --password "your-password" \
    --proxy "socks5://proxy.example.com:1080" \
    --keep-open
```

### HTTP/HTTPS
```bash
# HTTP with authentication
docker run -it --rm \
    --name conet-miner-3 \
    mffff4/conet-node:latest \
    --seed-phrase "your seed phrase" \
    --password "your-password" \
    --proxy "http://username:password@proxy.example.com:8080" \
    --keep-open

# HTTPS with authentication
docker run -it --rm \
    --name conet-miner-4 \
    mffff4/conet-node:latest \
    --seed-phrase "your seed phrase" \
    --password "your-password" \
    --proxy "https://username:password@proxy.example.com:8080" \
    --keep-open

# Without authentication
docker run -it --rm \
    --name conet-miner-5 \
    mffff4/conet-node:latest \
    --seed-phrase "your seed phrase" \
    --password "your-password" \
    --proxy "http://proxy.example.com:8080" \
    --keep-open
```

### Debug Mode with Proxy
```bash
docker run -it --rm \
    --name conet-miner-debug \
    mffff4/conet-node:latest \
    --seed-phrase "your seed phrase" \
    --password "your-password" \
    --proxy "socks5://username:password@proxy.example.com:1080" \
    --debug \
    --keep-open
```

## 🔧 Troubleshooting

### Common Issues

#### Connection Problems
- Check your internet connection
- Verify proxy settings if using one
- Run with `--debug` for detailed logs
- Check container logs: `docker logs conet-miner`

#### Mining Issues
- Verify seed phrase correctness
- Ensure password meets requirements
- Check network connectivity
- View real-time logs: `docker logs -f conet-miner`

#### Container Management
```bash
# View all running miners
docker ps --filter "name=conet-miner"

# Stop specific miner
docker stop conet-miner-1

# View logs of specific miner
docker logs -f conet-miner-2

# Remove stopped containers
docker rm $(docker ps -a -q --filter "name=conet-miner" --filter "status=exited")
```

## 💬 Support

[![Telegram](https://img.shields.io/badge/Join%20Our%20Telegram-blue?style=for-the-badge&logo=telegram)](https://t.me/+rq804XYKgjFkYjIy)

Join our Telegram community for:
- 🤝 Quick support
- 📢 Latest updates
- 💡 Tips and tricks
- 👥 Community discussions

## 🔒 Security Features

- Headless browser operation
- Random user agent rotation
- Proxy support
- Automatic cleanup

## 📄 License

This project is licensed under the BSD 3-Clause License - see the [LICENSE](https://github.com/Mffff4/conet-network/blob/main/LICENSE) file for details.

---

<p align="center">
Made with ❤️ for Mffff4
</p> 