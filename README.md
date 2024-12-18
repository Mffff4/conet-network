# 🚀 Conet Network Automation

[![Docker Pulls](https://img.shields.io/docker/pulls/mffff4/conet-node)](https://hub.docker.com/r/mffff4/conet-node)
[![License](https://img.shields.io/badge/license-BSD%203--Clause-blue.svg)](LICENSE)
[![Python Version](https://img.shields.io/badge/python-3.11%2B-blue)](https://www.python.org/downloads/)
[![Telegram](https://img.shields.io/badge/Telegram-Join%20Chat-blue?logo=telegram)](https://t.me/+rq804XYKgjFkYjIy)

> 🔥 Streamline your Conet Network experience with automated wallet recovery and mining setup

## ✨ Features

- 🔐 **One-Click Wallet Recovery**: Restore your wallet with just your seed phrase
- ⚡ **Automated Mining Setup**: Start mining immediately after wallet recovery
- 📊 **Real-Time Balance Monitoring**: Track your mining rewards automatically
- 🛡️ **Enhanced Security**: Headless operation with random user agents
- 🎯 **Resource Optimized**: Minimal system impact
- 🐳 **Docker Support**: Run anywhere with containerization
- 🔄 **Auto-Recovery**: Graceful handling of connection issues

## 🚀 Community & Support

[![Telegram](https://img.shields.io/badge/Join%20Our%20Telegram-blue?style=for-the-badge&logo=telegram)](https://t.me/+rq804XYKgjFkYjIy)

Join our Telegram community for:
- 🤝 Quick support and troubleshooting
- 📢 Latest updates and announcements
- 💡 Tips and tricks
- 👥 Community discussions

## 🚀 Quick Start

### 🐳 Docker (Recommended)

```bash
docker run -it --rm mffff4/conet-node \
  --seed-phrase "your twelve word seed phrase here" \
  --password "your-secure-password"
  --keep-open
```

### 🐍 Python

1. **Setup Environment**
```bash
# Clone repository
git clone https://github.com/Mffff4/conet-network.git
cd conet-network

# Install dependencies
pip install -r requirements.txt

# Install browser
playwright install chromium
```

2. **Run Script**
```bash
python src/conet-node.py \
  --seed-phrase "your twelve word seed phrase here" \
  --password "your-secure-password"
```

## 🎮 Command Line Options

| Option | Description | Required |
|--------|-------------|----------|
| `--seed-phrase` | Your 12-word recovery phrase | ✅ |
| `--password` | Wallet password | ✅ |
| `--keep-open` | Keep browser running | ✅ |
| `--proxy` | SOCKS5 or HTTP proxy URL | ❌ |

## 📝 Examples

### Basic Usage
```bash
docker run -it --rm mffff4/conet-node \
    --seed-phrase "word1 word2 word3 word4 word5 word6 word7 word8 word9 word10 word11 word12" \
    --password "PASSWORD" \
    --keep-open
```

### Using Proxies

#### SOCKS5 Proxy
```bash
# With authentication
docker run -it --rm mffff4/conet-node \
    --seed-phrase "word1 word2 word3 word4 word5 word6 word7 word8 word9 word10 word11 word12" \
    --password "PASSWORD" \
    --proxy "socks5://username:password@proxy.example.com:1080" \
    --keep-open

# Without authentication
docker run -it --rm mffff4/conet-node \
    --seed-phrase "word1 word2 word3 word4 word5 word6 word7 word8 word9 word10 word11 word12" \
    --password "PASSWORD" \
    --proxy "socks5://proxy.example.com:1080" \
    --keep-open
```

#### HTTP/HTTPS Proxy
```bash
# HTTP with authentication
docker run -it --rm mffff4/conet-node \
    --seed-phrase "word1 word2 word3 word4 word5 word6 word7 word8 word9 word10 word11 word12" \
    --password "PASSWORD" \
    --proxy "http://username:password@proxy.example.com:8080" \
    --keep-open

# HTTPS with authentication
docker run -it --rm mffff4/conet-node \
    --seed-phrase "word1 word2 word3 word4 word5 word6 word7 word8 word9 word10 word11 word12" \
    --password "PASSWORD" \
    --proxy "https://username:password@proxy.example.com:8080" \
    --keep-open

# Without authentication
docker run -it --rm mffff4/conet-node \
    --seed-phrase "word1 word2 word3 word4 word5 word6 word7 word8 word9 word10 word11 word12" \
    --password "PASSWORD" \
    --proxy "http://proxy.example.com:8080" \
    --keep-open
```

### Debug Mode with Proxy
```bash
docker run -it --rm mffff4/conet-node \
    --seed-phrase "word1 word2 word3 word4 word5 word6 word7 word8 word9 word10 word11 word12" \
    --password "PASSWORD" \
    --proxy "socks5://username:password@proxy.example.com:1080" \
    --debug \
    --keep-open
```

## 🔧 Proxy Troubleshooting

#### ❌ Proxy Connection Issues
- Check if proxy server is running and accessible
- Verify proxy credentials if using authentication
- Ensure proxy supports SOCKS5/HTTP protocol
- Try running with `--debug` flag for detailed connection logs

#### ❌ Proxy Performance Issues
- Try different proxy protocols (SOCKS5 vs HTTP)
- Check proxy server location and latency
- Verify proxy server bandwidth limits

## 🔧 Troubleshooting

### Common Issues


#### ❌ Browser Issues
- Ensure you have enough system resources
- Try restarting the container
- Check Docker logs: `docker logs <container_id>`

#### ❌ Mining Not Starting
- Verify your seed phrase is correct
- Ensure password meets minimum requirements
- Check network connectivity

## 📚 Additional Information

- The script runs in headless mode by default for better performance
- Uses random user agents for enhanced privacy
- Automatically monitors and logs balance changes
- Gracefully handles interruptions and shutdowns

## 🛡️ Security Features

- 🔒 Headless browser operation
- 🎭 Random user agent rotation
- ⚡ Optimized browser configuration
- 🛑 Automatic cleanup on exit

## 📄 License

This project is licensed under the BSD 3-Clause License - see the [LICENSE](LICENSE) file for details.

## 💬 Support

Having issues? We're here to help!

- 📝 [Join our Telegram community](https://t.me/+rq804XYKgjFkYjIy)
- 📝 Open an issue in the GitHub repository
- 💡 Check the troubleshooting section

---

<p align="center">
Made with ❤️ for Mffff4
</p>