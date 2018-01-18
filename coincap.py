import requests


def get_data(start=0, limit=5000):
    api_url = 'https://api.coinmarketcap.com/v1/ticker/?start=' + str(start) + '&limit=' + str(limit) + ''
    data_result = requests.get(api_url)

    if data_result.status_code == 200:
        return data_result.json()

    else:
        print("Error: " + str(data_result.status_code))
        print(data_result.json())
        return


def rough_filter(_data):
    clean_data = []
    for currency in _data:
        market_cap_usd = currency['market_cap_usd']
        if market_cap_usd is not None and is_number(market_cap_usd):
            clean_data.append(currency)
    return clean_data


def filter(_data):
    filtered_data = []
    for currency in _data:
        id = currency["id"]
        name = currency["name"]
        symbol = currency["symbol"]
        rank = currency["rank"]
        price_usd = currency["price_usd"]
        price_btc = currency["price_btc"]
        s24h_volume_usd = currency["24h_volume_usd"]
        market_cap_usd = currency['market_cap_usd']
        available_supply = currency["available_supply"]
        total_supply = currency["total_supply"]
        percent_change_1h = currency["percent_change_1h"]
        percent_change_24h = currency["percent_change_24h"]
        percent_change_7d = currency["percent_change_7d"]

        if float(market_cap_usd) > 195000021388:
            filtered_data.append(currency)

    return filtered_data


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass


if __name__ == "__main__":
    data = get_data()
    print(len(data))
    data = rough_filter(data)
    print(len(data))
    data = filter(data)
    print(len(data))

    #for currency in data:
        #print(currency['id'])

