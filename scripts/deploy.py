from brownie import FundMe, MockV3Aggregator, config, network

from scripts.utils import deploy_mocks, get_account


def deploy_fund_me():
    account = get_account()
    # Deploy our contract with price feed address
    # If deploy on persistent chain like Rinkeby, use the assiociated address
    # else, deploy mocks
    if network.show_active() != "development":
        price_feed_address = config["networks"][network.show_active()][
            "eth_usd_price_feed"
        ]  # Price feed address of Chain Link
    else:
        deploy_mocks()
        price_feed_address = MockV3Aggregator[-1].address
    fund_me = FundMe.deploy(
        price_feed_address,
        {"from": account},
        publish_source=config["networks"][network.show_active()].get("verify"),
    )
    print(f"Contract deployed to {fund_me.address}")


def main():
    deploy_fund_me()
