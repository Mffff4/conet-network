from typing import List, Optional
from playwright.sync_api import Page, expect, TimeoutError
import asyncio
from dataclasses import dataclass
import logging
import argparse
import random
import sys
import subprocess
from pathlib import Path
import signal
import contextlib
from fake_useragent import UserAgent
import aiohttp
from urllib.parse import urlparse
import socket

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger(__name__)

def get_random_user_agent() -> str:
    try:
        ua = UserAgent()
        return ua.random
    except Exception as e:
        logger.warning(f"Error generating user agent: {e}")
        return (
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/120.0.0.0 Safari/537.36"
        )

BROWSER_CONFIG = {
    "viewport": {"width": 800, "height": 600},
    "args": [
        "--disable-gpu",
        "--disable-software-rasterizer",
        "--disable-dev-shm-usage",
        "--disable-accelerated-2d-canvas",
        "--no-sandbox",
        "--disable-setuid-sandbox",
        "--disable-web-security",
        "--disable-features=IsolateOrigins,site-per-process",
        "--disable-site-isolation-trials",
        "--disable-extensions",
        "--disable-logging",
        "--disable-in-process-stack-traces",
        "--disable-logging-redirect",
        "--disable-component-extensions-with-background-pages",
        "--disable-background-timer-throttling",
        "--disable-backgrounding-occluded-windows",
        "--disable-renderer-backgrounding",
        "--disable-background-networking",
        "--disable-breakpad",
        "--disable-default-apps",
        "--disable-translate",
        "--disable-sync",
        "--hide-scrollbars",
        "--metrics-recording-only",
        "--mute-audio",
        "--no-first-run",
        "--safebrowsing-disable-auto-update",
        "--password-store=basic",
        "--use-mock-keychain",
        "--force-device-scale-factor=1",
        "--disable-threaded-scrolling",
        "--disable-smooth-scrolling",
        "--disable-composited-antialiasing",
    ]
}

async def random_delay(min_seconds: float = 1.0, max_seconds: float = 3.0) -> None:
    delay = random.uniform(min_seconds, max_seconds)
    await asyncio.sleep(delay)

@dataclass
class WalletCredentials:
    seed_phrase: List[str]
    password: str

    @classmethod
    def from_string(cls, seed_phrase: str, password: str) -> 'WalletCredentials':
        words = seed_phrase.strip().split()
        if len(words) != 12:
            raise ValueError(
                f"The seed phrase must contain 12 words, got: {len(words)}"
            )
        return cls(seed_phrase=words, password=password)

class ConetWalletAutomation:
    def __init__(self, page: Page):
        self._page = page
        self._base_url = (
            "https://beta1.conet.network/"
            "?referral=0x71f2bf703645c23e07e303fa11cd6c4fb77f6919"
        )

    async def navigate_to_site(self) -> None:
        logger.info("Navigating to site")
        await self._page.goto(self._base_url)
        await random_delay()
        
    async def click_recover_wallet(self) -> None:
        logger.info("Clicking recover wallet button")
        recover_button = self._page.locator('p:text("Recover wallet")')
        await recover_button.click()
        await random_delay()
        
    async def fill_seed_phrase(self, seed_words: List[str]) -> None:
        logger.info("Filling seed phrase")
        for index, word in enumerate(seed_words, start=1):
            logger.debug("Entering word %d: %s", index, word)
            input_selector = (
                f'.MuiPaper-root:has(div[style*="top: -10px"]:text("{index}"))'
                ' input'
            )
            await self._page.fill(input_selector, word)
            await random_delay(0.2, 0.5)
            
    async def set_passwords(self, password: str) -> None:
        logger.info("Setting passwords")
        password_inputs = self._page.locator(
            '#outlined-password-input[type="password"]'
        )
        for input_field in await password_inputs.all():
            await input_field.fill(password)
            await random_delay(0.3, 0.7)

    async def click_reset_password(self) -> None:
        logger.info("Clicking Reset password button")
        reset_button = self._page.locator('button:has-text("Reset password")')
        await reset_button.click()
        await random_delay()

    async def enter_unlock_password(self, password: str) -> None:
        logger.info("Entering unlock password")
        password_input = self._page.locator(
            '#outlined-password-input[placeholder="Minimum 6 character"]'
        )
        await password_input.fill(password)
        await random_delay()

    async def click_unlock(self) -> None:
        logger.info("Clicking Unlock button")
        unlock_button = self._page.locator('button:has-text("Unlock")')
        await unlock_button.click()
        await random_delay()

    async def try_close_modal(self) -> None:
        logger.info("Trying to close modal window")
        try:
            close_button = self._page.locator('button.modal-close-button')
            await close_button.click(timeout=5000)
            logger.info("Modal window closed")
            await random_delay()
        except TimeoutError:
            logger.info("Modal window not found, skipping")

    async def accept_terms(self) -> None:
        logger.info("Accepting terms of use")
        checkbox = self._page.locator('input[type="checkbox"]')
        await checkbox.click()
        await random_delay()

    async def start_mining(self) -> None:
        logger.info("Starting mining")
        mining_button = self._page.locator(
            'p.MuiTypography-root.MuiTypography-body1:text("Click to start mining")'
        )
        await mining_button.click()
        await random_delay()

    async def monitor_balance(self) -> None:
        logger.info("Starting balance monitoring")
        balance_selector = 'p.MuiTypography-root.MuiTypography-body1.css-1bgqh7'
        
        initial_balance = await self._page.locator(balance_selector).text_content()
        logger.info("Initial balance: %s", initial_balance)
        
        while not shutdown_event.is_set():
            try:
                current_balance = await self._page.locator(balance_selector).text_content()
                if current_balance != initial_balance:
                    logger.info("Balance changed: %s", current_balance)
                    initial_balance = current_balance
                await asyncio.sleep(5)
            except Exception as e:
                if not shutdown_event.is_set():
                    logger.error("Error monitoring balance: %s", str(e))
                break

    async def recover_wallet(self, credentials: WalletCredentials) -> None:
        logger.info("Starting wallet recovery process")
        await self.navigate_to_site()
        await self.click_recover_wallet()
        await self.fill_seed_phrase(credentials.seed_phrase)
        await self.set_passwords(credentials.password)
        await self.click_reset_password()
        await self.enter_unlock_password(credentials.password)
        await self.click_unlock()
        await self.try_close_modal()
        await self.accept_terms()
        await self.start_mining()
        await self.monitor_balance()
        logger.info("Wallet recovery and setup process completed")

async def check_proxy(proxy: str) -> bool:
    try:
        proxy_parts = urlparse(proxy)
        proxy_type = proxy_parts.scheme.lower()
        
        if proxy_type not in ['socks5', 'http', 'https']:
            logger.error("Unsupported proxy type. Use socks5://, http:// or https://")
            return False
            
        host = proxy_parts.hostname
        port = proxy_parts.port
        username = proxy_parts.username
        password = proxy_parts.password
        
        if not all([host, port]):
            logger.error("Invalid proxy format. Use scheme://[user:pass@]host:port")
            return False
        
        if username and password:
            auth_str = f"{username}:{password}@"
            logger.info(f"Using proxy with authentication: {proxy_type}://{host}:{port}")
        else:
            auth_str = ""
            logger.info(f"Using proxy without authentication: {proxy_type}://{host}:{port}")
            
        proxy_url = f"{proxy_type}://{auth_str}{host}:{port}"
        
        if proxy_type == 'socks5':
            from aiohttp_socks import ProxyConnector
            connector = ProxyConnector.from_url(proxy_url)
            session_kwargs = {'connector': connector}
        else:
            session_kwargs = {'proxy': proxy_url}
        
        async with aiohttp.ClientSession(**session_kwargs) as session:
            async with session.get(
                'http://ip-api.com/json',
                timeout=aiohttp.ClientTimeout(total=10)
            ) as response:
                if response.status == 200:
                    data = await response.json()
                    logger.info(f"Proxy check successful. IP: {data.get('query')}")
                    return True
                logger.error(f"Proxy check failed. Status: {response.status}")
                return False
                
    except Exception as e:
        logger.error(f"Proxy check failed: {str(e)}")
        return False

def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Script for automating Conet wallet recovery"
    )
    parser.add_argument(
        "--seed-phrase",
        type=str,
        help="12 words of the seed phrase, separated by spaces",
        required=True
    )
    parser.add_argument(
        "--password",
        type=str,
        help="Password for the wallet",
        required=True
    )
    parser.add_argument(
        "--debug",
        action="store_true",
        help="Enable detailed logging"
    )
    parser.add_argument(
        "--keep-open",
        action="store_true",
        help="Do not automatically close the browser after execution"
    )
    parser.add_argument(
        "--proxy",
        type=str,
        help="Proxy URL (socks5://user:pass@host:port or http://host:port)",
        default=None
    )
    return parser.parse_args()

def init_environment() -> None:
    logger.info("Checking environment...")
    
    try:
        import playwright
        logger.info("Playwright is already installed")
    except ImportError:
        logger.info("Installing playwright...")
        subprocess.run([sys.executable, "-m", "pip", "install", "playwright"], check=True)
        import playwright
        logger.info("Playwright successfully installed")
    
    browser_path = Path.home() / ".cache" / "ms-playwright"
    if not browser_path.exists():
        logger.info("Installing playwright browsers...")
        try:
            subprocess.run(["playwright", "install", "chromium"], check=True)
            logger.info("Browsers successfully installed")
        except subprocess.CalledProcessError as e:
            logger.error("Error installing browsers: %s", str(e))
            sys.exit(1)
    else:
        logger.info("Playwright browsers are already installed")

async def graceful_shutdown(sig=None):
    if sig:
        logger.info(f"Received signal {sig.name}, starting graceful shutdown...")
    
    shutdown_event.set()
    
    if current_task and not current_task.done():
        current_task.cancel()
        try:
            await current_task
        except asyncio.CancelledError:
            pass
    
    if browser:
        try:
            await browser.close()
        except Exception as e:
            logger.error(f"Error closing browser: {e}")
    
    logger.info("Script successfully completed")

def handle_exception(loop, context):
    msg = context.get("exception", context["message"])
    logger.error(f"Unhandled exception: {msg}")
    asyncio.create_task(graceful_shutdown())

async def main():
    global browser, current_task, shutdown_event
    shutdown_event = asyncio.Event()
    
    loop = asyncio.get_running_loop()
    for sig in (signal.SIGTERM, signal.SIGINT):
        loop.add_signal_handler(
            sig,
            lambda s=sig: asyncio.create_task(graceful_shutdown(s))
        )
    
    loop.set_exception_handler(handle_exception)
    
    init_environment()
    args = parse_arguments()
    
    if args.debug:
        logger.setLevel(logging.DEBUG)
    
    proxy_config = None
    if args.proxy:
        if not await check_proxy(args.proxy):
            logger.error("Proxy check failed. Exiting...")
            return
        
        proxy_parts = urlparse(args.proxy)
        proxy_config = {
            "server": f"{proxy_parts.scheme}://{proxy_parts.hostname}:{proxy_parts.port}"
        }
        if proxy_parts.username and proxy_parts.password:
            proxy_config.update({
                "username": proxy_parts.username,
                "password": proxy_parts.password
            })
    
    try:
        credentials = WalletCredentials.from_string(
            args.seed_phrase, 
            args.password
        )
    except ValueError as e:
        logger.error(str(e))
        return

    from playwright.async_api import async_playwright
    
    try:
        async with async_playwright() as playwright:
            browser_options = {
                "headless": True,
                "args": BROWSER_CONFIG["args"]
            }
            
            if proxy_config:
                browser_options["proxy"] = proxy_config
                logger.debug(f"Using proxy configuration: {proxy_config}")
            
            browser = await playwright.chromium.launch(**browser_options)
            
            user_agent = get_random_user_agent()
            logger.debug("Using user agent: %s", user_agent)
            
            context = await browser.new_context(
                user_agent=user_agent,
                viewport=BROWSER_CONFIG["viewport"],
                ignore_https_errors=True,
                java_script_enabled=True,
                bypass_csp=True
            )
            
            page = await context.new_page()
            
            wallet_automation = ConetWalletAutomation(page)
            current_task = asyncio.create_task(
                wallet_automation.recover_wallet(credentials)
            )
            
            try:
                await current_task
            except asyncio.CancelledError:
                logger.info("Operation cancelled by user")
            except Exception as e:
                logger.error(f"Error during wallet recovery: {str(e)}")
            
            if args.keep_open and not shutdown_event.is_set():
                logger.info(
                    "Browser is running in the background. "
                    "Press Ctrl+C to exit..."
                )
                await shutdown_event.wait()
    
    except Exception as e:
        logger.error(f"An error occurred: {str(e)}")
    finally:
        if not shutdown_event.is_set():
            await graceful_shutdown()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass 